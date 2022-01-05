from djitellopy import tello
import pygame
from time import sleep

'x' == False


def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))


def getkey(keyName):
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update

    return ans


def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if kp.getkey("LEFT"):
        lr = -speed
    elif kp.getkey("RIGHT"):
        lr = speed

    if kp.getkey("UP"):
        fb = speed
    elif kp.getkey("DOWN"):
        fb = -speed

    if kp.getkey("w"):
        ud = speed
    elif kp.getkey("s"):
        ud = -speed

    if kp.getkey("a"):
        yv = speed
    elif kp.getkey("d"):
        yv = -speed

        if kp.getkey("PgUp"): me.takeoff()
        if kp.getkey("PgDn"): me.land()

    return [lr, fb, ud, yv]




def main():
    print(getkey("a"))
