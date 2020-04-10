# set up all imports
from gpiozero import MotionSensor
from subprocess import call
import time
import os

# parse config
import json
with open(os.path.join(os.path.dirname(__file__), 'config.json')) as config_file:
    data = json.load(config_file)

ON_CYCLE = data["time_screenon"]
REFRESH_CYCLE = data["refresh_cycle"]
GPIO_PIN = data["gpio_pin"]
DEBUG = data["debug"]
BOOT_TIME = data["boot_time"]

# instanciate motion sensor
print("Initializing PIR Motion Sensor...")
mMotionSensor = MotionSensor(GPIO_PIN)
time.sleep(1)

# define ScreenOn routine for callback
def screen_on():
        s_pir = mMotionSensor.value
        if DEBUG:
                print("Screen on", s_pir)
        call(["/usr/bin/vcgencmd", "display_power", "1"], stdout=open(os.devnull, 'wb'))
        time.sleep(ON_CYCLE)

# define ScreenOff routine for callback
def screen_off():
        s_pir = mMotionSensor.value
        if DEBUG:
                print("Screen off", s_pir)
        call(["/usr/bin/vcgencmd", "display_power", "0"], stdout=open(os.devnull, 'wb'))
        time.sleep(REFRESH_CYCLE)

# Setup callbacks
mMotionSensor.when_motion = screen_on
mMotionSensor.when_no_motion = screen_off

# Wait for MagicMirror Boot
# approx. 13min for a RaspberryPi Zero W
print("Waiting for MagicMirror boot to finish...")
time.sleep(BOOT_TIME/2)
print("Waiting for MagicMirror boot to finish (2/2) ...")
time.sleep(BOOT_TIME/2)

# Set initial state
print("Fetching initial state...")
if mMotionSensor.value == 0:
    call(["/usr/bin/vcgencmd", "display_power", "0"], stdout=open(os.devnull, 'wb'))
else:
    call(["/usr/bin/vcgencmd", "display_power", "1"], stdout=open(os.devnull, 'wb'))

print("Setup done, ready2go.")
#Contiuous loop to run
while True:
        # setup callbacks
        time.sleep(REFRESH_CYCLE)
