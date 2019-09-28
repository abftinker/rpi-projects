import RPi.GPIO as GPIO
from time import sleep
import signal
import sys

RED, YLW, GRN = 7, 11, 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(YLW, GPIO.OUT)
GPIO.setup(GRN, GPIO.OUT)


def close(signal, frame):
    print("\nTurning OFF PIR Sensor\n")
    GPIO.cleanup()
    sys.exit(0)


signal.signal(signal.SIGINT, close)

for i in range(3):
    GPIO.output(RED, True)
    sleep(0.5)
    GPIO.output(RED, False)
    sleep(0.5)
    GPIO.output(YLW, True)
    sleep(0.5)
    GPIO.output(YLW, False)
    sleep(0.5)
    GPIO.output(GRN, True)
    sleep(0.5)
    GPIO.output(GRN, False)


GPIO.cleanup()
