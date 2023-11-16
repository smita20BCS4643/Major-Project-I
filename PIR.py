
import time
from time import sleep
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import requests

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LED_PIN = 12  # Define LED pin
PIR_PIN = 4  # PIR sensor input pin

# Setup GPIO pins
GPIO.setup(LED_PIN, GPIO.OUT)  # Set LED pin as output
GPIO.setup(PIR_PIN, GPIO.IN)   # Set PIR sensor pin as input

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("led")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    if msg.payload.decode("utf-8") == "on":
        print("LED on")
        GPIO.output(LED_PIN, GPIO.HIGH)  # LED ON
    elif msg.payload.decode("utf-8") == "off":
        print("LED off")
        GPIO.output(LED_PIN, GPIO.LOW)   # LED OFF

# ThingSpeak Configuration
url = "https://api.thingspeak.com/update"
api_key = "O9EUVLGHIRB19SY2"
field_number = 1  # The field number you want to update on ThingSpeak

# MQTT Configuration
broker_url = "broker.emqx.io"
broker_port = 1883
led_topic = "led"

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect(broker_url, broker_port, 60)


try:
    print("PIR Motion Sensor Test (CTRL+C to exit)")
    time.sleep(2)  # Allow sensor to settle

    while True:
        mqtt_client.loop()
        sleep(1)
        if GPIO.input(PIR_PIN):  # PIR sensor detects motion
        
            print("Motion detected!")
            mqtt_client.publish(led_topic, "on")  # Publish MQTT message to turn on LED
            GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on LED
            sleep(5)  # LED stays on for 5 seconds
            params = {
                "api_key": api_key,
                f"field{field_number}": 1  # You can customize the field and value according to your ThingSpeak channel fields
            }
            response = requests.post(url, params=params)
            if response.status_code == 200:
                print("Data sent to ThingSpeak successfully.")
            else:
                print("Failed to send data to ThingSpeak.")
            time.sleep(5)  # Wait for 5 seconds to avoid multiple detections for the same motion
        else: 
            mqtt_client.publish(led_topic, "off")  # Publish MQTT message to turn off LED
            GPIO.output(LED_PIN, GPIO.LOW)   # Turn off LED when no motion
            time.sleep(1)  # Pause for a second before checking again
            print("No motion detected.")
            params = {
                "api_key": api_key,
                f"field{field_number}": 0  # You can customize the field and value according to your ThingSpeak channel fields
            }
            response = requests.post(url, params=params)
            if response.status_code == 200:
                print("Data sent to ThingSpeak successfully.")
            else:
                print("Failed to send data to ThingSpeak.")
                time.sleep(1)  # Pause for a second before checking again

except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()


