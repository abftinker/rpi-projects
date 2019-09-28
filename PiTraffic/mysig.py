import RPi.GPIO as GPIO
import signal
import sys
from time import sleep


GPIO.setmode(GPIO.BOARD)
pins = [11, 12, 13, 15, 16, 18, 22, 29, 31, 33, 36, 38, 40]
GPIO.setup(pins, GPIO.OUT)


#  RED, YELLOW, GREEN
Directions = {"SOUTH": [11, 13, 15],
              "WEST": [16, 18, 22],
              "NORTH": [29, 31, 33],
              "EAST": [36, 38, 40]}


for i in Directions:
    print("Direction: {}".format(i))
    for s in Directions[i]:
        sleep(1)
        print("{0} is True".format(s))
        GPIO.output(s, True)
        sleep(2)
        print("{0} is False".format(s))
        GPIO.output(s, False)


print("Cleaning GPIO pins")
GPIO.cleanup()


def close(signal, frame):
    print("\nExiting PiTraffic\n")
    GPIO.cleanup()
    sys.exit(0)


signal.signal(signal.SIGINT, close)
