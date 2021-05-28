from cursors.TouchCursor import TouchCursor
from configs.TouchCursorConfig import TouchCursorConfig
from animations.PersistTouchAnimation import PersistTouchAnimation

from bibliopixel.layout import Matrix
from bibliopixel.layout.geometry import Rotation
from bibliopixel.drivers.PiWS281X import *

# create biblio pixel driver and led
vert_flip  = False   # flip across x-axis
y_flip     = False   # flip across y-axis
serpentine = True    # serpentine pattern
thread     = False   # display updates to run in background thread
width      = 9       # width of board
height     = 5       # height of board
brightness = 100     # brightness 0-255
driver     = PiWS281X(height*width)
led_matrix = Matrix(driver, width, height, Rotation.ROTATE_0, vert_flip, y_flip, serpentine, thread, brightness)

# create cursor object to get position of finger/mouse
device_path = "/dev/input/event0"
cursor = TouchCursor(device_path)

# create the cursor config that will be used to determine
# the position of the leds in relation to the screen
config = {
  "x": [],
  "y": []
}
cursor_config = TouchCursorConfig(config) 

color = (0, 255, 0)
anim = PersistTouchAnimation(led_matrix, cursor, cursor_config, color)
anim.run()
