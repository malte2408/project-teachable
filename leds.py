import RPi.GPIO as GPIO
import time
import sys

gpio = int(sys.argv[1])

GPIO.setmode(GPIO.BCM)

GPIO.setup(gpio, GPIO.OUT)

time.sleep(2)

for i in range(0, 30):
    GPIO.setup(i, GPIO.OUT)

    GPIO.output(i, GPIO.LOW)

    print(i)

    time.sleep(3)

    GPIO.output(i, GPIO.HIGH)