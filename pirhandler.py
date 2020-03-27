# set up all imports
import RPi.GPIO as GPIO
import time
from subprocess import call

# parse config
import json
with open('config.json') as config_file:
    data = json.load(config_file)

ON_CYCLE = data["time_screenon"]
REFRESH_CYCLE = data["refresh_cycle"]
GPIO_PIN = data["gpio_pin"]
DEBUG = data["debug"]

# disable warnings
GPIO.setwarnings(False)

# setup GPIO pin setups
GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIO_PIN, GPIO.IN)

# define a previous signal
s_pir_prev = GPIO.input(GPIO_PIN)
time.sleep(1)

# Contiuous loop
while True:
        # check input
        s_pir = GPIO.input(GPIO_PIN)
        
        # Set HDMI output
        if s_pir == 0:
                if DEBUG:
                        print("Screen off", s_pir)
               	if s_pir_prev == 1:
			call(["/usr/bin/vcgencmd", "display_power", "0"])
                time.sleep(REFRESH_CYCLE)
        elif s_pir == 1:
                if DEBUG:
                        print("Screen on", s_pir)
                if s_pir_prev == 0:
			call(["/usr/bin/vcgencmd", "display_power", "0"])
                time.sleep(ON_CYCLE)
