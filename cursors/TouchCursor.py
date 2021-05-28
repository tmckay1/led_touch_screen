from .Cursor import Cursor
from evdev import InputDevice, ecodes
from select import select

class TouchCursor(Cursor):

  X_POSITION_CODE = ecodes.ABS_MT_POSITION_X
  Y_POSITION_CODE = ecodes.ABS_MT_POSITION_Y

  # the device that represents the cursor
  _device = None

  def __init__(self, device_path):
    super(object, self).__init__()
    self._device = InputDevice(device_path)
  
  # Note: This is a blocking function that waits until data is received from the cursor
  def get_current_position(self):
    # signify we are waiting to read from the device
    select([self._device], [], [])

    x_pos = -1
    y_pos = -1

    # this is a synchronous operation that waits for events
    # from the device
    events = self._device.read()
    for event in events:
      if event.code == self.X_POSITION_CODE:
        x_pos = event.value
      elif event.code == self.Y_POSITION_CODE:
        y_pos = event.value

    return (x_pos, y_pos)

  async def get_current_position_async(self, position_array):
    x_pos = -1
    y_pos = -1

    while True:
      async for event in device.async_read_loop():
        if event.code == self.X_POSITION_CODE:
          x_pos = event.value
        elif event.code == self.Y_POSITION_CODE:
          y_pos = event.value

    position_array.append((x_pos, y_pos))