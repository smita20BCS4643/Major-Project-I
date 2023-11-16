import RPi.GPIO as GPIO
import time
import requests

GPIO.setwarnings(False)

# Set GPIO pin numbers
MQ2_AO_PIN = 20  # Analog Output (AO) pin
MQ2_D0_PIN = 21  # Digital Output (D0) pin
BUZZER_PIN = 26

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(MQ2_AO_PIN, GPIO.IN)  # AO pin as input for analog readings
GPIO.setup(MQ2_D0_PIN, GPIO.IN)  # D0 pin as input for digital readings
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# ThingSpeak Configuration
api_key = "O9EUVLGHIRB19SY2"
field_number = 3  # The field number you want to update on ThingSpeak

def send_to_thingspeak(data):
    url = f"https://api.thingspeak.com/update?api_key={api_key}&field{field_number}={data}"
    response = requests.get(url)
    if response.status_code == 200:
        print("Data sent to ThingSpeak successfully.")
    else:
        print("Failed to send data to ThingSpeak.")

try:
    while True:
        gas_detected_digital = GPIO.input(MQ2_D0_PIN)
        if gas_detected_digital:
            gas_analog_value = GPIO.input(MQ2_AO_PIN)
            print("Gas Detected! Analog Value:", gas_analog_value)
            
            # Send data to ThingSpeak
            send_to_thingspeak(gas_analog_value)
            
            # Buzzer control logic can go here
            
        else:
            print("No Gas Detected")
        
        time.sleep(15)  # Wait for 15 seconds before reading again (ThingSpeak allows 15-second updates)

except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()

