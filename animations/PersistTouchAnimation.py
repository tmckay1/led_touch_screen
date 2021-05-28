from .Animation import Animation

class PersistTouchAnimation(Animation):

  # color used to show on each led
  _color = (0, 0, 0)

  def __init__(self, led_matrix, cursor, cursor_config, color):
    super().__init__(led_matrix, cursor, cursor_config)
    self._color = color
  
  def run(self):
    print("Running PersistTouchAnimation")
    while True:
      raw_position = self._cursor.get_current_position()
      print("Retrieved raw_position: " + str(raw_position))
      (x, y) = self._cursor_config.get_x_y_position_from_raw_position(raw_position)
      print("x: " + str(x) + ", y: " + str(y))
      if x != -1 and y != -1:
        self._led_matrix.set(x, y, self._color)