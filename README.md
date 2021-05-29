# led_touch_screen
This library is a template for controlling a matrix of ws281x leds with a raspberry pi and an infrared touch screen

### Installation
You will need to install two dependencies for this project to work `BiblioPixel` and `rpi_ws281x`. Both can be installed with `pip3` as shown:
```
$ sudo pip3 install bibliopixel
$ sudo pip3 install rpi_ws281x
```
Once the dependencies are installed go ahead and clone this repo onto your machine.

### Calibration and Configuration
You will need to calibrate your touch screen so you know where your leds are in relation to the values you get back from the touch screen device. You can run `calibrate.py` to see the values that come back when hovering over an led. Create the config for this screen in `main.py` as described in `TouchCursorConfig`

### Running
After the calibration, installation, and configuration is finished, you can run the animations with:
```
$ sudo python3 main.py
```
