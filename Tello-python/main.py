from djitellopy import Tello
import time

t = Tello()
t.connect()
t.takeoff()
time.sleep(3)
response = t.get_battery()
print(response)
time.sleep(3)
t.move_forward(100)
t.land()
