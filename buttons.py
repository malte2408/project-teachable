import RPi.GPIO as GPIO
import time
import sys

gpio = int(sys.argv[1])



GPIO.setmode(GPIO.BCM)

GPIO.setup(gpio, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

start = time.time()

while time.time() - start < 20: # Run forever
    #if GPIO.input(gpio) == GPIO.LOW:
    print(GPIO.input(gpio))