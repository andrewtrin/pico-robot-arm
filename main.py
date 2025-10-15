# main.py

from servo import Servo
import sys
import time

# --- SETUP ---
waist_servo = Servo(pin=15)
elbow_servo = Servo(pin=16)
current_waist_angle = 90
current_elbow_angle = 90
STEP_AMOUNT = 5 # Changes movement increments, smaller = smoother

# Send status back to the computer
def report_status():
    print(f"W:{current_waist_angle},E:{current_elbow_angle}\n")

# --- HOMING and INITIAL REPORT ---
# Move to the starting position and report it once.
waist_servo.move_to_angle(current_waist_angle)
elbow_servo.move_to_angle(current_elbow_angle)
time.sleep(0.1) # A tiny delay to make sure the Pico is ready to send
report_status()

# --- MAIN LOOP ---
while True:
    command = sys.stdin.read(1)
    moved = False # Flag to track if a move actually happened

    if command == 'a':
        current_waist_angle += STEP_AMOUNT
        if current_waist_angle > 160: current_waist_angle = 160
        waist_servo.move_to_angle(current_waist_angle)
        moved = True
    elif command == 'd':
        current_waist_angle -= STEP_AMOUNT
        if current_waist_angle < 20: current_waist_angle = 20
        waist_servo.move_to_angle(current_waist_angle)
        moved = True
    elif command == 'w':
        current_elbow_angle -= STEP_AMOUNT
        #if current_elbow_angle < 45: current_elbow_angle = 45
        elbow_servo.move_to_angle(current_elbow_angle)
        moved = True
    elif command == 's':
        current_elbow_angle += STEP_AMOUNT
        #if current_elbow_angle > 135: current_elbow_angle = 135
        elbow_servo.move_to_angle(current_elbow_angle)
        moved = True
    elif command == 'c': # Center/home the arm
        current_elbow_angle = 90
        current_waist_angle = 90
        elbow_servo.move_to_angle(current_elbow_angle)
        waist_servo.move_to_angle(current_waist_angle)
        moved = True
    # After processing the command, if a move occurred, report the new status.
    if moved:
        report_status()