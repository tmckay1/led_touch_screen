from cursors.TouchCursor import TouchCursor
import asyncio

device_path = "/dev/input/event0"
cursor = TouchCursor(device_path)
position_array = []

asyncio.async(cursor.get_current_position_async(position_array))
# last_size = len(position_array)
loop = asyncio.get_event_loop()
loop.run_forever()

while True:
  print(position_array)
  # if last_size != len(position_array):
  #   last_size = len(position_array)
  #   asyncio.ensure_future(cursor.get_current_position_async(position_array))
