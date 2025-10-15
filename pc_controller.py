# pc_controller.py

import serial
from pynput import keyboard
import time

# --- CONFIGURATION ---
PICO_PORT = 'COM7' 

# --- SETUP SERIAL CONNECTION ---
try:
    pico = serial.Serial(PICO_PORT, 115200, timeout=0.1)
    print(f"Successfully connected to {PICO_PORT}")
    print("Use WASD to control the arm. Press 'ESC' to quit.")
except serial.SerialException as e:
    print(f"Error: Could not connect to Pico on {PICO_PORT}.")
    exit()

# --- GLOBAL VARIABLES for tracking state ---
input_count = 0
last_action_time = time.time()
last_known_position = "Waiting for first update..."

def on_press(key):
    """This function runs in a separate thread and listens for key presses."""
    global input_count, last_action_time
    try:
        if key.char in ['w', 'a', 's', 'd', 'c']:
            pico.write(key.char.encode())
            input_count += 1
            last_action_time = time.time()
    except AttributeError:
        if key == keyboard.Key.esc:
            return False # This will stop the listener

def report_position():
    """A helper function to print the status and reset counters."""
    global input_count, last_action_time
    print(f"Position Check -> {last_known_position}")
    input_count = 0 # Reset the input counter
    last_action_time = time.time() # Reset the timer

# --- MAIN PROGRAM ---
listener = keyboard.Listener(on_press=on_press)
listener.start() # Start listening to the keyboard in the background

# This loop runs on the main thread.
while listener.is_alive():
    # Check if the Pico has sent us any data
    if pico.in_waiting > 0:
        response = pico.readline().decode().strip()
        if response: # Make sure the line is not empty
            last_known_position = response

    # Condition 1: Have we made 5 or more moves?
    if input_count >= 5:
        report_position()

    # Condition 2: Has it been 5 seconds since the last move?
    elif time.time() - last_action_time > 5:
        # Only report if there were moves to report on (input_count > 0)
        if input_count > 0:
            report_position()
        else:
            # If there was no activity, just reset the timer to prevent spamming
            last_action_time = time.time()

    time.sleep(0.05) # A short pause to prevent the loop from using 100% CPU

# --- CLEANUP ---
pico.close()
print("Connection closed.")