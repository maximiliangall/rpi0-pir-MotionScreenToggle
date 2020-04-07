# set up all imports
from gpiozero import MotionSensor
from subprocess import call
import time

# parse config
import json
with open('config.json') as config_file:
    data = json.load(config_file)

ON_CYCLE = data["time_screenon"]
REFRESH_CYCLE = data["refresh_cycle"]
GPIO_PIN = data["gpio_pin"]
DEBUG = data["debug"]

# instanciate motion sensor
mMotionSensor = MotionSensor(GPIO_PIN)
time.sleep(1)

# define ScreenOn routine for callback
def screen_on():
        s_pir = mMotionSensor.value
        if DEBUG:
                print("Screen on", s_pir)
        call(["/usr/bin/vcgencmd", "display_power", "1"])
        time.sleep(ON_CYCLE)

# define ScreenOff routine for callback
def screen_off():
        s_pir = mMotionSensor.value
        if DEBUG:
                print("Screen off", s_pir)
        call(["/usr/bin/vcgencmd", "display_power", "0"])
        time.sleep(REFRESH_CYCLE)

# Setup callbacks
mMotionSensor.when_motion = screen_on
mMotionSensor.when_no_motion = screen_off

#Contiuous loop to run
while True:
        # setup callbacks
        time.sleep(REFRESH_CYCLE)
