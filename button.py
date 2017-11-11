#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
from settings import BUTTON_PIN_LEFT,BUTTON_PIN_PLAY,BUTTON_PIN_RIGHT,BUTTON_PIN_STOP

def setup():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(BUTTON_PIN_PLAY, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUTTON_PIN_STOP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUTTON_PIN_LEFT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUTTON_PIN_RIGHT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def test():
    while True:
        VGo = GPIO.input(BUTTON_PIN_PLAY)
        VStop = GPIO.input(BUTTON_PIN_STOP)
        VLeft = GPIO.input(BUTTON_PIN_LEFT)
        VRight = GPIO.input(BUTTON_PIN_RIGHT)

        if (VGo == False):
            print("Button Play ")
        elif (VStop == False):
            print ("Button Stop")
        elif (VLeft == False):
            print ("Button Left")
        elif (VRight == False):
            print ("Button Right")
        time.sleep(0.3)

def ButtonClick():
    VGo = GPIO.input(BUTTON_PIN_PLAY)
    VStop = GPIO.input(BUTTON_PIN_STOP)
    VLeft = GPIO.input(BUTTON_PIN_LEFT)
    VRight = GPIO.input(BUTTON_PIN_RIGHT)
    return (VGo,VStop,VLeft,VRight)

def destroy():
    print("close")

if __name__ == '__main__':  # Program start from here
    setup()
    try:
        #loop()
        test()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()