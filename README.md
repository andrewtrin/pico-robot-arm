# 🦾 Pico Robotic Arm Controller

![Language](https://img.shields.io/badge/Language-Python%20%26%20MicroPython-blue)
![Hardware](https://img.shields.io/badge/Hardware-Raspberry%20Pi%20Pico%20W-purple)
![Control](https://img.shields.io/badge/Control-Real--Time%20Serial-green)

> A 2-axis robotic arm built with a Raspberry Pi Pico and controlled in real-time from a host computer.

This project serves as a foundational project in embedded systems, demonstrating a professional host-client architecture, object-oriented programming for hardware control, and a stateful, non-blocking control loop. The chassis is also built around LEGO bricks, a choice that highlights creative prototyping by leveraging common materials to overcome equipment constraints.

  <img width="480" alt="v2 of arm with lego bricks" src="https://github.com/user-attachments/assets/d5ecc350-9d05-4f98-a597-7fe082105e34" />

---

## ✅ Features

-   **Real-Time Control:** A non-blocking input loop allows for instant, responsive control by sending single-keystroke commands from the host PC.
-   **Object-Oriented Design:** A reusable `Servo` class provides a high-level API to control the motors, abstracting away low-level PWM signal generation.
-   **Host-Client Architecture:** A Python script on a PC acts as the host, sending commands over a serial interface to the Pico client, which runs the firmware.
-   **Stateful Control:** The firmware tracks the current angle of each joint, enabling both incremental movement and an automated homing sequence on startup.

---

## ⚙️ Hardware

* Raspberry Pi Pico W
* 2x SG90 Micro Servo Motors
* LEGO Classic Creative Brick Box (for chassis)
* Solderless Breadboard
* Jumper Wires

---

## 💻 Software & Architecture

The system is split into three main files, representing a clean separation of concerns.

-   `servo.py`: A MicroPython library that defines the `Servo` class. This blueprint handles all the low-level PWM signal generation and angle-to-duty-cycle calculations.
-   `main.py`: The firmware that runs on the Raspberry Pi Pico. It initializes the servos, runs an auto-homing sequence on boot, and enters
