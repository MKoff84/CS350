# CS350
Emerging Sys Arch and Tech
Smart Thermostat (Embedded Systems Project)
Overview

This project is a smart thermostat prototype built using a Raspberry Pi and multiple hardware interfaces. The system reads real-time temperature data, allows user interaction through buttons, displays system information on an LCD screen, and simulates communication with an external system. The goal of this project was to demonstrate how embedded systems integrate hardware and software to create a responsive, state-driven application.

Features
State machine with three modes:
Off
Heat
Cool
Real-time temperature monitoring using an AHT20 sensor (I2C)
User input via three buttons:
Mode cycle (Off → Heat → Cool)
Increase temperature set point
Decrease temperature set point
Visual feedback using LEDs:
Red LED indicates heating
Blue LED indicates cooling
LCD display:
Line 1: Current date and time
Line 2: Alternates between temperature and system state/set point
UART output every 30 seconds:
Sends system state, temperature, and set point
Hardware Components
Raspberry Pi
AHT20 Temperature and Humidity Sensor (I2C)
16x2 LCD Display
Breadboard and jumper wires
3 Push buttons
2 LEDs (Red and Blue)
Resistors
Potentiometer (for LCD contrast)
Software and Technologies
Python
gpiozero (button and LED control)
adafruit_ahtx0 (temperature sensor)
digitalio and adafruit_character_lcd (LCD display)
statemachine (state machine logic)
serial (UART communication)
System Behavior
Modes
Off
All LEDs are off
Heat
If temperature < set point → Red LED fades (heating active)
If temperature ≥ set point → Red LED stays solid
Cool
If temperature > set point → Blue LED fades (cooling active)
If temperature ≤ set point → Blue LED stays solid
Inputs
Green button cycles system mode
Red button increases set point
Blue button decreases set point
Outputs
LCD displays system status and temperature
LEDs provide visual indication of system behavior
UART sends periodic system updates
State Machine Design

The system is built using a finite state machine with three states:

Off
Heat
Cool

Transitions occur through user interaction (mode button), and internal behavior is driven by temperature comparisons relative to the set point.

Challenges and Lessons Learned
Debugging hardware wiring versus software logic
Ensuring correct GPIO mapping for buttons and LEDs
Managing concurrency using threads for display updates
Structuring code using a state machine for clarity and maintainability
Handling real-time data and system responsiveness
Future Improvements
Add WiFi connectivity for cloud-based monitoring
Implement a mobile or web interface
Improve display formatting and user interaction
Add data logging and analytics
How to Run
Connect all hardware components as specified
Ensure required Python libraries are installed

Run the main script:
sudo python3 Thermostat.py

Author

Matt Biletnikoff
