# CS350
Emerging Systems Architecture and Technologies
Smart Thermostat (Embedded Systems Project)
Overview

This project is a smart thermostat prototype built using a Raspberry Pi and multiple hardware interfaces. The system reads real-time temperature data, allows user interaction through buttons, displays system information on an LCD screen, and simulates communication with an external system. The goal of this project was to demonstrate how embedded systems integrate hardware and software to create a responsive, state-driven application.

Features
State machine with three modes: Off, Heat, Cool
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

The system is built using a finite state machine with three states: Off, Heat, and Cool. Transitions occur through user interaction using the mode button, and internal behavior is driven by temperature comparisons relative to the set point.

Reflection

This project focused on building a fully functional thermostat system that integrates both hardware and software. The main problem it solved was creating a responsive embedded system that could monitor environmental conditions and react based on user input and system logic. By combining sensors, buttons, LEDs, and a display, the project demonstrated how real-time data can be used to control system behavior through a structured state machine.

One area I felt I did particularly well in was debugging and problem solving. Throughout the project, I encountered issues that required me to carefully analyze both the hardware and the code. For example, I had to troubleshoot wiring issues that affected button input and also fix logic errors such as incorrect placement of display updates in the code. These experiences helped me improve my ability to isolate problems and work through them methodically. If I were to improve anything, it would be planning more of the system design up front, especially around how different components interact, which would have reduced some of the trial and error during development.

This project also helped me build a stronger support network of tools and resources. I relied on documentation, previous lab work, and structured debugging approaches to move forward when I was stuck. The skills I developed in this project are very transferable, especially working with GPIO, understanding communication protocols like I2C and UART, and structuring programs using a state machine. I also focused on keeping the code readable and maintainable by following a clear structure, using descriptive naming, and separating functionality into logical sections. Overall, this project strengthened my understanding of embedded systems and gave me a solid foundation to build on in future courses and projects.

How to Run
Connect all hardware components as specified
Ensure required Python libraries are installed
Run the main script:
sudo python3 Thermostat.py

Author

Matt Biletnikoff

