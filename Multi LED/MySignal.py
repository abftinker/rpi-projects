# testing git
import RPi.GPIO as GPIO
from time import sleep


RED = 7
YLW = 11
GRN = 12


GPIO.setmode(GPIO.BOARD)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(YLW, GPIO.OUT)
GPIO.setup(GRN, GPIO.OUT)

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
