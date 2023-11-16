# Major-Project-I
Smart Home Electric System

## INTRODUCTION 

### Problem Statement 
The need for an efficient, user-friendly, and automated home electrical system that can be remotely controlled, optimizes energy consumption and enhances safety.

### Proposed Solution
This project is designed to design and implement a smart home automation system using Raspberry Pi Module 3 as the central controller. Integrated PIR sensors increase energy efficiency by automatically turning on the light when people see it. Similarly, the MQ2 gas sensor and buzzer combination increases security measures by instantly activating the alarm in case of gas leakage. Additionally, the DHT11 temperature sensor provides a feeling of comfort by enabling the fan to operate when the room temperature is higher than the preset threshold. Users have the flexibility to manage these functions through the MQTT dashboard-based interface accessible from the mobile application.
## Technologies Used
### Hardware:

- Raspberry Pi 3 Module: Central processing unit for the system.
-  <img width="280" alt="Raspberry pi" src="https://github.com/smita20BCS4643/Major-Project-I/assets/101444257/10ce1cc3-feff-497e-a370-6e1442e57aa2">

  
- PIR (Passive Infrared) Sensor: Detects motion in the room.

- <img width="281" alt="pir" src="https://github.com/smita20BCS4643/Major-Project-I/assets/101444257/0cf62bb2-057d-4805-9d4f-1cd2d3713a66">

- DHT11 Sensor: Measures temperature and humidity in the room.
- <img width="239" alt="dht11" src="https://github.com/smita20BCS4643/Major-Project-I/assets/101444257/bc7e3f08-d964-4a57-9082-104d0932df74">

- MQ2 Gas Sensor: Monitors gas levels in the environment.
- <img width="368" alt="mq2" src="https://github.com/smita20BCS4643/Major-Project-I/assets/101444257/5cd4a115-bfdb-40cf-9987-73dbe1d274f3">

### Software:

- MQTT (Message Queuing Telemetry Transport) Protocol: Used for communication between Raspberry Pi and the MQTT Dashboard, ensuring secure data exchange.
- ThinkSpeak: Platform for centralized storage and analysis of sensor data.

### User Interfaces:

- MQTT Dashboard Interface: User-friendly dashboard for manual control of lights, fan, and buzzer.
- Mobile Application: Allows remote control and monitoring of the system through a mobile app.

### Programming Languages:

- Possibly Python: Commonly used for programming Raspberry Pi devices.

### Communication:

- Secure MQTT Communication: Ensures data security during communication between the Raspberry Pi and the MQTT Dashboard.
- Remote Access through the Internet: Allows users to interact with the system from anywhere.

### Integration Protocols:

- RESTful Services: Used in the Sensor Web node prototype for fast critical event signalling and remote access through the internet.
Wireless Communication:


### Database:

- Possibly a Database for ThinkSpeak: Used for centralized storage of historical sensor data.

### Automation Logic:

- Fuzzy Logic: Mentioned in the context of critical event signalling in the Sensor Web node prototype.

### Environmental Monitoring:

- Environmental Sensors: Used for monitoring temperature, humidity, motion, and gas levels in the smart home environment.
