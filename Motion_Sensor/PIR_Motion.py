import RPi.GPIO as GPIO
import time
import signal
import sys


LED = 7
PIR = 11
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIR, GPIO.IN)  # Read output from PIR motion sensor
GPIO.setup(LED, GPIO.OUT)  # LED output pin


def close(signal, frame):
    print("\nTurning OFF PIR Sensor\n")
    GPIO.cleanup()
    sys.exit(0)


signal.signal(signal.SIGINT, close)

while True:
    i = GPIO.input(PIR)
    if i == 0:  # When output from motion sensor is LOW
        print "No intruders", i
        GPIO.output(LED, False)  # Turn OFF LED
        time.sleep(0.1)
    elif i == 1:  # When output from motion sensor is HIGH
        print "Intruder detected", i
        GPIO.output(LED, True)  # Turn ON LED
        time.sleep(0.1)
