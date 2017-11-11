#! /usr/bin/env python
# -*- coding: utf-8 -*-

import button
import Playr

#keyboard.press_and_release("ctrl+alt+del")

def start():
    button.setup()
    #Playr.start(Playr.getListVideo())

def loop():
    while True:
        buttonClik = button.ButtonClick()
        # (VGo,VStop,VLeft,VRight)

        if buttonClik[0] == False:
            Playr.play()
        elif buttonClik[1] == False:
            Playr.stop()
        elif buttonClik[2] == False:
            Playr.left()
        elif buttonClik[3] ==False:
            Playr.right()

def destroy():
    print ("close")


if __name__ == '__main__':  # Program start from here
    start()
    try:
        loop()

    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()