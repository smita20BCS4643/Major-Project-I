import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import requests

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 17  # GPIO pin connected to the DHT11 sensor
LED_PIN = 13  # GPIO pin connected to the LED
THINGSPEAK_API_KEY = 'O9EUVLGHIRB19SY2'

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

def send_to_thingspeak(temperature, humidity):
    url = f'https://api.thingspeak.com/update?api_key={THINGSPEAK_API_KEY}&field2={temperature}&field5={humidity}'
    response = requests.get(url)
    if response.status_code == 200:
        print("Data sent to ThingSpeak successfully.")
    else:
        print("Failed to send data to ThingSpeak.")

try:
    while True:
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            print("Temperature={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
            if temperature > 20:
                GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on LED
            else:
                GPIO.output(LED_PIN, GPIO.LOW)  # Turn off LED
            # Send data to ThingSpeak
            send_to_thingspeak(temperature, humidity)
        else:
            print("Failed to retrieve data from DHT sensor")
        time.sleep(2)  # Read temperature every 2 seconds

except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()

