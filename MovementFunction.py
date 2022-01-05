from djitellopy import tello
import pygame
from time import sleep

me = tello.Tello
me.connect()
print(me.getbattery())

def init():
    pygame.init()
    win=pygame.display.set_mode((400,400))

def getkey(keyName):
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update

    return ans


def main():
    print(getkey("a"))

if __name__ == '__main__':
    init()
    while True:
        main()




