from djitellopy import tello
import MovementFunction as kp
from time import sleep


kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery)

while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0],vals[1],vals[2],vals[3])
    sleep(0.05)

