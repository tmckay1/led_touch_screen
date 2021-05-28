from .Animation import Animation
import time

# Animation to keep the drawn values on screen and to not clear them
class RectFillTouchAnimation(Animation):

  # time in seconds to reset the animation if an event doesn't occur in this time
  _reset_time = 3

  # color used to show on each led
  _color = (0, 0, 0)

  def __init__(self, led_matrix, cursor, cursor_config, color, reset_time):
    super().__init__(led_matrix, cursor, cursor_config)
    self._color = color
    self._reset_time = reset_time
  
  def run(self):
    print("Running PersistTouchAnimation with color: " + str(self._color))
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
        (top_x, top_y) = self.top_left_coordinates(initial_position, current_position)
        rect_width = 1 + abs(current_position[0] - initial_position[0])
        rect_height = 1 + abs(current_position[1] - initial_position[1])
        self._led_matrix.fillScreen()
        self._led_matrix.fillRect(top_x, top_y, rect_width, rect_height, self._color)
        self._led_matrix.push_to_driver()

  def has_point_changed(self, x, y, current_position):
    print("has_point_changed x: " + str(x) + ", y: " + str(y) + "current_position: " + str(current_position))
    return current_position[0] != x and current_position[1] != y

  def top_left_coordinates(self, initial_position, current_position):
    # initial position is top left of current position
    if initial_position[0] <= current_position[0] and initial_position[1] <= current_position[1]:
      return initial_position
    # initial position is top right of current position
    elif initial_position[0] >= current_position[0] and initial_position[1] <= current_position[1]:
      return (current_position[0], initial_position[1])
    # initial position is bottom left of current position
    elif initial_position[0] <= current_position[0] and initial_position[1] >= current_position[1]:
      return (initial_position[0], current_position[1])
    # initial position is bottom right of current position
    else:
      return current_position