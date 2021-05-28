from .Animation import Animation

# Animation to keep the drawn values on screen and to not clear them
class SingleTouchAnimation(Animation):

  # color used to show on each led
  _color = (0, 0, 0)

  # current point to draw
  _current_point = (-1, -1)

  def __init__(self, led_matrix, cursor, cursor_config, color):
    super().__init__(led_matrix, cursor, cursor_config)
    self._color = color
  
  def run(self):
    print("Running SingleTouchAnimation with color: " + str(self._color))
    self._current_point = (-1, -1)
    self._led_matrix.fillScreen()
    self._led_matrix.push_to_driver()

    while True:
      raw_position = self._cursor.get_current_position()
      print("Retrieved raw_position: " + str(raw_position))
      (x, y) = self._cursor_config.get_x_y_position_from_raw_position(raw_position)
      print("x: " + str(x) + ", y: " + str(y))

      # check if it's not the current point
      is_current_point = self._current_point[0] == x and self._current_point[1] == y

      # draw led if valid point and the point was not yet chosen
      if x != -1 and y != -1 and not is_current_point:
        print("Setting color " + str(self._color) + " for position " + str((x, y)))
        self._current_point = (x, y)
        self._led_matrix.fillScreen()
        self._led_matrix.set(x, y, self._color)
        self._led_matrix.push_to_driver()