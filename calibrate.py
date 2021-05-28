from cursors.TouchCursor import TouchCursor
import time

device_path = "/dev/input/event0"
cursor = TouchCursor(device_path)

# script that will print out the x, y values of the current touch screen while a finger is on it
while True:
  (raw_x, raw_y) = cursor.get_current_position()
  print("x: " + str(raw_x) + ", y: " + str(raw_y))
  time.sleep(3)
