from djitellopy import tello
import MovementFunction as kp
from time import sleep


kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery)

while True:
    me.send_rc_control(0,0,0,0)

