import RPi.GPIO as GPIO
import signal
import sys
from time import sleep


GPIO.setmode(GPIO.BOARD)
pins = [11, 12, 13, 15, 16, 18, 22, 29, 31, 33, 36, 38, 40]
GPIO.setup(pins, GPIO.OUT)


Directions = {"SOUTH": {'RED': 11, 'YELLOW': 13, "GREEN": 15},
              "WEST": {'RED': 16, 'YELLOW': 18, "GREEN": 22},
              "NORTH": {'RED': 29, 'YELLOW': 31, "GREEN": 33},
              "EAST": {'RED': 36, 'YELLOW': 38, "GREEN": 40}}


def close(signal, frame):
    print("\nTurning off ...\n")
    GPIO.cleanup()
    sys.exit(0)


signal.signal(signal.SIGINT, close)


def Rockit(d):
    for k, v in d.items():
        if isinstance(v, dict):
            print(k)
            Rockit(v)
        else:
            sleep(1)
            print("{0} is True".format(v))
            GPIO.output(v, True)
            sleep(2)
            print("{0} is False".format(v))
            GPIO.output(v, False)


Rockit(Directions)
print("Cleaning GPIO pins")
GPIO.cleanup()
