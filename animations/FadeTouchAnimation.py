from .Animation import Animation
import time

# Animation to fade the leds out over time once drawn on screen
class FadeTouchAnimation(Animation):

  MAX_BRIGHTNESS = 255

  # time after which we want to fully fade an led to black after it has been touched
  FADE_TIME_TO_BLACK = 3

  # an array of arrays representing the led matrix where the index of the array represents the
  # index of the led. This array is filled with timestamps of the last time the user was hovering
  # over that led
  _led_last_touched = []

  def run(self):
    print("Running FadeTouchAnimation")
    self._led_matrix.fillScreen()
    self._led_matrix.push_to_driver()
    self.reset_points_last_touched()

    while True:
      raw_position = self._cursor.get_current_position()
      print("Retrieved raw_position: " + str(raw_position))
      (x, y) = self._cursor_config.get_x_y_position_from_raw_position(raw_position)
      print("x: " + str(x) + ", y: " + str(y))

      current_time_in_seconds = time.time()

      # reset timestamp of led if valid point
      if x != -1 and y != -1:
        print("Setting time " + str(current_time_in_seconds) + " for position " + str((x, y)))
        self._led_last_touched[x][y] = current_time_in_seconds

      # loop through the timestamps last touched for the matrix and set the brightness appropriately
      for x in range(len(self._led_last_touched)):
        for y in range(len(self._led_last_touched[x])):
          time_last_touched = current_time_in_seconds - self._led_last_touched[x][y]
          brightness = 0
          if time_last_touched < FADE_TIME_TO_BLACK:
            brightness = int((time_last_touched / FADE_TIME_TO_BLACK) * MAX_BRIGHTNESS)
          self._led_matrix.set(x, y, (0, brightness, 0))

      self._led_matrix.push_to_driver()

  def reset_points_last_touched(self):
    self._led_last_touched = [[0 for x in range(self._led_matrix.width)] for y in range(self._led_matrix.height)]