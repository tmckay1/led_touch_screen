from cursors.TouchCursor import TouchCursor
from configs.TouchCursorConfig import TouchCursorConfig
from animations.PersistTouchAnimation import PersistTouchAnimation
from animations.FadeTouchAnimation import FadeTouchAnimation
from animations.SingleTouchAnimation import SingleTouchAnimation

from bibliopixel.layout import Matrix
from bibliopixel.layout.geometry import Rotation
from bibliopixel.drivers.PiWS281X import *

# create biblio pixel driver and led
vert_flip  = True   # flip across x-axis
y_flip     = False   # flip across y-axis
serpentine = True    # serpentine pattern
thread     = False   # display updates to run in background thread
width      = 9       # width of board
height     = 5       # height of board
brightness = 100     # brightness 0-255
rotation   = Rotation.ROTATE_0
driver     = PiWS281X(height*width)
led_matrix = Matrix(driver, width, height, rotation, vert_flip, y_flip, serpentine, thread, brightness)

# create cursor object to get position of finger/mouse
device_path = "/dev/input/event0"
cursor = TouchCursor(device_path)

# create the cursor config that will be used to determine
# the position of the leds in relation to the screen
config = {
  "x": [(0,3600), (3600, 6900), (6900, 10300), (10300, 14250), (14250, 17750), (17750, 21250), (21250, 25000), (25000, 28500), (28500, 40000)],
  "y": [(0, 5250), (5250, 11000), (11000, 18500), (18500, 24900), (24900, 40000)]
}
cursor_config = TouchCursorConfig(config) 

# color = (0, 255, 0)
# anim = PersistTouchAnimation(led_matrix, cursor, cursor_config, color)
# anim.run()

# fade_time_to_black = 1
# anim = FadeTouchAnimation(led_matrix, cursor, cursor_config, fade_time_to_black)
# anim.run()

color = (0, 255, 0)
anim = SingleTouchAnimation(led_matrix, cursor, cursor_config, color)
anim.run()