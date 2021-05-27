class CursorConfig(object):

  # config object, structure will depend on subclass
  _config = None

  def __init__(self, config):
    super(object, self).__init__()
    self._config = config

    