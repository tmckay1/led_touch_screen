from .Animation import Animation
import asyncio

# Animation to fade the leds out over time once drawn on screen
class FadeTouchAnimation(Animation):

  # color used to show on each led
  _color = (0, 0, 0)

  # points that have been drawn
  _points_drawn = []

  def __init__(self, led_matrix, cursor, cursor_config, color):
    super().__init__(led_matrix, cursor, cursor_config)
    self._color = color
  
  def run(self):
    print("Running PersistTouchAnimation with color: " + str(self._color))
    self._points_drawn = []
    self._led_matrix.fillScreen()
    self._led_matrix.push_to_driver()

    while True:
      raw_position = self._cursor.get_current_position()
      print("Retrieved raw_position: " + str(raw_position))
      (x, y) = self._cursor_config.get_x_y_position_from_raw_position(raw_position)
      print("x: " + str(x) + ", y: " + str(y))

      # check if we had this point before
      pair_not_chosen = True
      for index, pair in enumerate(self._points_drawn):
        if x == pair[0] and y == pair[1]:
          pair_not_chosen = False

      # draw led if valid point and the point was not yet chosen
      if x != -1 and y != -1 and pair_not_chosen:
        print("Setting color " + str(self._color) + " for position " + str((x, y)))
        self._points_drawn.append((x, y))
        self._led_matrix.set(x, y, self._color)
        self._led_matrix.push_to_driver()