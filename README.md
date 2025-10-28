# Pico Robotic Arm Controller

This project is a 2-axis robotic arm built with a Raspberry Pi Pico and controlled in real-time from a host computer. It serves as a foundational project in embedded systems, demonstrating a professional host-client architecture, object-oriented programming for hardware control, and a stateful, non-blocking control loop. The chassis is also built around Lego bricks, a choice that highlights creative prototyping by leveraging common materials to overcome equipment constraints.

<img width="2610" height="1958" alt="v2 of arm with lego bricks" src="https://github.com/user-attachments/assets/d5ecc350-9d05-4f98-a597-7fe082105e34" />

---

## Features

* **Real-Time Control:** Non-blocking input loop allows for instant, responsive control by sending single-keystroke commands from the host PC.
* **Object-Oriented Design:** A reusable `Servo` class provides a high-level API to control the motors, abstracting away low-level PWM signal generation.
* **Host-Client Architecture:** A Python script on a PC acts as the host, sending commands over a serial interface to the Pico client, which runs the firmware.
* **Stateful Control:** The firmware tracks the current angle of each joint, enabling both incremental movement and an automated homing sequence on startup.

---

## Hardware

* Raspberry Pi Pico W
* 2x SG90 Micro Servo Motors
* Solderless Breadboard
* Jumper Wires
* DIY Cardboard Arm Structure

---

## Software & Architecture

The system is split into three main files, representing a clean separation of concerns.

* `servo.py`: A MicroPython library that defines the `Servo` class. This blueprint handles all the low-level PWM signal generation and angle-to-duty-cycle calculations.
* `main.py`: The firmware that runs on the Raspberry Pi Pico. It initializes the servos, runs an auto-homing sequence on boot, and enters a main loop to listen for single-character commands from the serial port.
* `pc_controller.py`: The host application that runs on a computer. It captures single-key presses without requiring 'Enter' and sends them directly to the Pico over the serial port.

---

## Setup & Usage

### 1. Hardware Setup

Assemble the cardboard arm and wire the components according to the diagram. The system is powered entirely by the Pico's USB connection.

### 2. Pico Setup

1.  Flash the latest MicroPython firmware to your Raspberry Pi Pico.
2.  Connect to the Pico using Thonny IDE.
3.  Copy the `servo.py` and `main.py` files to the Pico's filesystem. The `main.py` script will run automatically on boot.

### 3. PC Setup

1.  Ensure you have Python 3 installed on your computer.
2.  Install the required libraries from your terminal:
    ```bash
    pip install pyserial pynput
    ```
3.  Edit the `pc_controller.py` file and update the `PICO_PORT` variable to match the COM port of your Pico (e.g., `'COM7'`).

### 4. Running the System

1.  Plug the Raspberry Pi Pico into your computer. The arm will automatically run its homing sequence and then wait for commands.
2.  From your computer's terminal, navigate to the project folder and run the host controller:
    ```bash
    python pc_controller.py
    ```
3.  The terminal window will confirm the connection. Click on this window and use the `W`, `A`, `S`, `D`, and `C` keys to control the arm.
4.  Press the `ESC` key to quit the controller.

---

## Future Development/WIP

* **Level Up From Cardboard:** 3D print proper limbs for the robotic arm.
* **Inverse Kinematics (IK):** Implement a function to calculate the required joint angles to reach a specific (x, y) coordinate.
* **Sensor Integration:** Add an HC-SR04 ultrasonic sensor to enable object detection and automated tracking.
