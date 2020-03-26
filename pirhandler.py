# set up all imports
import RPi.GPIO as GPIO
import time
from subprocess import call

# parse config
import json
with open('config.json') as config_file:
    data = json.load(config_file)

ON_CYCLE = data[time_screenon]
REFRESH_CYCLE = data[refresh_cylce]
GPIO_PIN = data[gpio_pin]

# disable warnings
GPIO.setwarnings(False)

# setup GPIO pin setups
GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIO_PIN, GPIO.IN)


# Contiuous loop
while true:
	# check input
	s_pir = GPIO.input(GPIO_PIN)
	
	# Set HDMI output
	if s_pir == 0:
		print("Screen off", s_pir)
		run('vcgencmd display_power 0', shell=True)        	
		#call("vcgencmd display_power 0")
		time.sleep(REFRESH_CYCLE)
	elif s_pir == 1:
        	print("Screen on", s_pir)
        	run('vcgencmd display_power 0', shell=True)
		#call("vcgencmd display_power 1")
        	time.sleep(ON_CYCLE)
