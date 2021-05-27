class Animation(object):

  # cursor object
  _cursor = None

  # cursor configuration
  _cursor_config = None

  # bibliopixel Matrix object for the leds
  _led_matrix = None

  def __init__(self, led_matrix, cursor, cursor_config):
    super(object, self).__init__()
    self._cursor = cursor
    self._cursor_config = cursor_config
    self._led_matrix = led_matrix

  def run(self):
    pass