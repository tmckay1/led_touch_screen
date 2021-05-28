from .Animation import Animation
import time
import math

# Animation to draw a circle to the screen
class CircleTouchAnimation(Animation):

  # time in seconds to reset the animation if an event doesn't occur in this time
  _reset_time = 3

  # color used to show on each led
  _color = (0, 0, 0)

  def __init__(self, led_matrix, cursor, cursor_config, color, reset_time):
    super().__init__(led_matrix, cursor, cursor_config)
    self._color = color
    self._reset_time = reset_time
  
  def run(self):
    print("Running CircleTouchAnimation with color: " + str(self._color))
    self._points_drawn = []
    self._led_matrix.fillScreen()
    self._led_matrix.push_to_driver()
    initial_time = 0
    initial_position = (-2, -2)
    current_position = (-1, -1)

    while True:
      raw_position = self._cursor.get_current_position()
      print("Retrieved raw_position: " + str(raw_position))
      (x, y) = self._cursor_config.get_x_y_position_from_raw_position(raw_position)
      print("x: " + str(x) + ", y: " + str(y))

      # draw led if valid point and the point was not yet chosen
      if x != -1 and y != -1 and self.has_point_changed(x, y, current_position):
        current_time_in_seconds = time.time()
        current_position = (x, y)

        # reset the positions for the square if enough time passes
        if current_time_in_seconds - initial_time > self._reset_time:
          print("Resetting initial position to current position: " + str(current_position))
          initial_position = current_position
        initial_time = current_time_in_seconds

        print("Drawing rect for initial position " + str(initial_position) + " and current_position " + str(current_position))
        radius = self.calculate_radius(initial_position, current_position)
        self._led_matrix.fillScreen()
        self._led_matrix.drawCircle(x, y, radius, self._color)
        self._led_matrix.push_to_driver()

  def has_point_changed(self, x, y, current_position):
    return current_position[0] != x or current_position[1] != y

  def calculate_radius(self, initial_position, current_position):
    return int(math.sqrt((initial_position[0] - current_position[0])**2 + (initial_position[1] - current_position[1])**2))