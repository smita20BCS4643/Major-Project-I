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
  
   1.  <img width="280" alt="Raspberry pi" src="https://github.com/smita20BCS4643/Major-Project-I/assets/101444257/10ce1cc3-feff-497e-a370-6e1442e57aa2">
 
- PIR (Passive Infrared) Sensor: Detects motion in the room.

   2.  <img width="281" alt="pir" src="https://github.com/smita20BCS4643/Major-Project-I/assets/101444257/0cf62bb2-057d-4805-9d4f-1cd2d3713a66">

- DHT11 Sensor: Measures temperature and humidity in the room.
  
   3.  <img width="239" alt="dht11" src="https://github.com/smita20BCS4643/Major-Project-I/assets/101444257/bc7e3f08-d964-4a57-9082-104d0932df74">

- MQ2 Gas Sensor: Monitors gas levels in the environment.
  
   4.  <img width="368" alt="mq2" src="https://github.com/smita20BCS4643/Major-Project-I/assets/101444257/5cd4a115-bfdb-40cf-9987-73dbe1d274f3">

- LED (Light-Emitting Diode): The LED is employed as a visual indicator, controlled by the PIR sensor. When motion is detected, the LED illuminates to signify the activation of the lighting system.
  
   5.  <img width="171" alt="led" src="https://github.com/smita20BCS4643/Major-Project-I/assets/101444257/ca93ed6d-7ace-4cf5-a0e7-6db0472815a1">

- Breadboard: The breadboard serves as a platform for connecting and prototyping electronic components. It facilitates the organized arrangement of jumper wires and other circuit elements.
  
   6.  <img width="369" alt="bread" src="https://github.com/smita20BCS4643/Major-Project-I/assets/101444257/e58020d9-1f7f-4db0-8c61-afc8b50667a5">

- Buzzer: The buzzer is integrated with the MQ2 gas sensor. In the event of a gas leak, the buzzer alerts users audibly, enhancing safety measures.
  
   7.  <img width="161" alt="buzzer" src="https://github.com/smita20BCS4643/Major-Project-I/assets/101444257/5c23f7b9-5f06-4f58-bc05-7b806a202490">

- Jumper Wires: Jumper wires establish connections between the components on the breadboard, creating a seamless electrical pathway.
  
   8.  <img width="261" alt="jumper wire" src="https://github.com/smita20BCS4643/Major-Project-I/assets/101444257/3738546d-87e9-4169-b728-c1876a1d31dd">
   
- Resistor: A resistor is included in the LED circuit to control the current flow, preventing damage to the LED. The specific resistor value is chosen based on the LED's specifications.

  9.  <img width="262" alt="resistors" src="https://github.com/smita20BCS4643/Major-Project-I/assets/101444257/4cba1253-7e8f-4a99-b13a-589ce42f4748">


### Software:

- Raspbian: Raspbian is the official operating system for Raspberry Pi, based on the Debian Linux distribution, optimized for Raspberry Pi's ARM architecture.

  <img width="213" alt="raspbian" src="https://github.com/smita20BCS4643/Major-Project-I/assets/101444257/e3925a39-2f9b-4fba-86d7-762eda66c447">


- MQTT (Message Queuing Telemetry Transport) Protocol: Used for communication between Raspberry Pi and the MQTT Dashboard, ensuring secure data exchange.

  <img width="156" alt="mqtt dashboard" src="https://github.com/smita20BCS4643/Major-Project-I/assets/101444257/717f192a-9a30-4ab4-bdf0-7522dd4cb2b6">

  
- ThinkSpeak: Platform for centralized storage and analysis of sensor data.

 ![download](https://github.com/smita20BCS4643/Major-Project-I/assets/101444257/409e90f1-27c8-4ef5-8853-024b946d9002)



### User Interfaces:

- MQTT Dashboard Interface: User-friendly dashboard for manual control of lights, fan, and buzzer.
- Mobile Application: Allows remote control and monitoring of the system through a mobile app.

### Programming Languages:

- Python: Commonly used for programming Raspberry Pi devices.

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
