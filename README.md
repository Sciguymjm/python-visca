# visca
A Python library for controlling Sony VISCA cameras.

# Installation

Run `pip install git+git://github.com/Sciguymjm/python-visca.git`.

# Usage

```
from visca import camera

cam = camera.D100(output='COM7') # set serial port
cam.init() # initialize camera object and connect to serial port

# Now you can run commands
cam.home() # send camera to home position
cam.left() # move camera to left
cam.right(5) # even adjust speed
cam.right_up(6, 3)

# you can change picture effects
cam.picture_effect_pastel()

# or autofocus
cam.autofocus_sens_high()



```
