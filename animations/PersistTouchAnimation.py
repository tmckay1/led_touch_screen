from .Animation import Animation

# Animation to keep the drawn values on screen and to not clear them
class PersistTouchAnimation(Animation):

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

      # draw led if valid point and the point was not yet chosen
      if x != -1 and y != -1 and is_pair_already_chosen(x, y):
        print("Setting color " + str(self._color) + " for position " + str((x, y)))
        self._points_drawn.append((x, y))
        self._led_matrix.set(x, y, self._color)
        self._led_matrix.push_to_driver()

  # check if we had this point before
  def is_pair_already_chosen(self, x, y):
    for index, pair in enumerate(self._points_drawn):
      if x == pair[0] and y == pair[1]:
        return True

    return False
