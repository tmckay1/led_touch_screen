from .CursorConfig import CursorConfig

# The config object structure is a dict with "x" and "y" as keys and the values are
# array of tuples that represent the distribution of values for a particular led.
# For example:
#
# {
#   x: [(0, 20), (20, 40), (40, 60), (60, 80), (80, 100)],
#   y: [(0, 25), (25, 50), (50, 75), (75, 100)]
# }
#
# The above dict would trigger led x = 3, y = 1 for a cursor with
# a reading raw_x = 60, raw_y = 26. Note the touple is (inclusive, exclusive)
# format. To get the config you'll have to manually calibrate your cursor and get these values
class TouchCursorConfig(CursorConfig):

  def get_x_y_position_from_raw_position(self, raw_position):
    (raw_x, raw_y) = raw_position

    # x y indexes of leds
    x = -1
    y = -1

    # if we find our raw x in the range, set the index
    x_ranges = self._config["x"]
    for index, x_range in enumerate(x_ranges):
      if raw_x >= x_range[0] and raw_x < x_range[1]:
        x = index
        break

    # if we find our raw y in the range, set the index
    y_ranges = self._config["y"]
    for index, y_range in enumerate(y_ranges):
      if raw_y >= y_range[0] and raw_y < y_range[1]:
        y = index
        break

    return (x, y)

    