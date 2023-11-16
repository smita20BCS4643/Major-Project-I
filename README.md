# Major-Project-I
Smart Home Electric System

## INTRODUCTION 

### Problem Statement 
The need for an efficient, user-friendly, and automated home electrical system that can be remotely controlled, optimizes energy consumption and enhances safety.

### Proposed Solution
This project is designed to design and implement a smart home automation system using Raspberry Pi Module 3 as the central controller. Integrated PIR sensors increase energy efficiency by automatically turning on the light when people see it. Similarly, the MQ2 gas sensor and buzzer combination increases security measures by instantly activating the alarm in case of gas leakage. Additionally, the DHT11 temperature sensor provides a feeling of comfort by enabling the fan to operate when the room temperature is higher than the preset threshold. Users have the flexibility to manage these functions through the MQTT dashboard-based interface accessible from the mobile application.
## Technologies Used
# Hardware:

- Raspberry Pi 3 Module: Central processing unit for the system.
- PIR (Passive Infrared) Sensor: Detects motion in the room.
- DHT11 Sensor: Measures temperature and humidity in the room.
- MQ2 Gas Sensor: Monitors gas levels in the environment.
# Software:

- MQTT (Message Queuing Telemetry Transport) Protocol: Used for communication between Raspberry Pi and the MQTT Dashboard, ensuring secure data exchange.
- ThinkSpeak: Platform for centralized storage and analysis of sensor data.

# User Interfaces:

- MQTT Dashboard Interface: User-friendly dashboard for manual control of lights, fan, and buzzer.
- Mobile Application: Allows remote control and monitoring of the system through a mobile app.

# Programming Languages:

- Possibly Python: Commonly used for programming Raspberry Pi devices.

# Communication:

- Secure MQTT Communication: Ensures data security during communication between the Raspberry Pi and the MQTT Dashboard.
- Remote Access through the Internet: Allows users to interact with the system from anywhere.

# Integration Protocols:

- RESTful Services: Used in the Sensor Web node prototype for fast critical event signalling and remote access through the internet.
Wireless Communication:


# Database:

- Possibly a Database for ThinkSpeak: Used for centralized storage of historical sensor data.

# Automation Logic:

- Fuzzy Logic: Mentioned in the context of critical event signalling in the Sensor Web node prototype.

# Environmental Monitoring:

- Environmental Sensors: Used for monitoring temperature, humidity, motion, and gas levels in the smart home environment.
