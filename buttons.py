import RPi.GPIO as GPIO
import time
import sys

gpio = int(sys.argv[1])



GPIO.setmode(GPIO.BCM)

GPIO.setup(gpio, GPIO.OUT)


GPIO.output(gpio, GPIO.LOW)

start = time.time()

GPIO.output(gpio, GPIO.HIGH)

while time.time() - start < 20: # Run forever
    if GPIO.input(gpio) == GPIO.HIGH:
        print("Button was pushed!")