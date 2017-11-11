import os
import subprocess
import time
import keyboard

def getListVideo(pach = "/home/pi/Documents/video/"):
    list = os.listdir(pach)
    return " /home/pi/Documents/video/".join(list)

def stop():
    print ("STOP Video")
    keyboard.press_and_release("p")

def left():
    print ("Left Video")
    keyboard.press_and_release("shift + <")

def right():
    print("Right Video")
    keyboard.press_and_release("shift + >")
def play():
    print("play Video")
    keyboard.press_and_release("a")


def start(date):
    p = subprocess.call("mplayer -fs -zoom %s " % date, shell=True)
    #p = subprocess.Popen("mplayer /home/pi/Documents/video/%s& " %date, shell=True, stdout=subprocess.PIPE)
    #out = p.stdout.read()
    #print out
    return p

def test():
    print("playr star")
    list = getListVideo()
    p = start(list)
    return p



def destroy(p):
    print("close playr")



if __name__ == '__main__':  # Program start from here
    print "Playr"
    try:
        #loop()
        test()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()