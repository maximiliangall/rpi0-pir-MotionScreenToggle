# rpi0-pir-MotionScreenToggle
Toggle the HDMI signal to the screen based on motion detection.

___

## Objective

This repository provides an easy to-use framework to enable motion based screen powering.
It uses the *HC-SR501* passive infrared sensor wired to a Raspberry Pi Zero W.  
Main purpose was to add a power save mode for a MagicMirror in order to reduce overall energy consumption.

## Features

Whereas the sensor itself provides basic capabilities to change the distance and sensitvity, this framework implements additional parameters.
It features a configuration file to adapt cycle times and adapt on custom schematic layouts.

## Quick Start Guide

For the case of the MagicMirror installed into the home directory ```~/MagicMirror/```, go there and clone the repository.

```
cd ~/MagicMirror/
git clone https://github.com/maximiliangall/rpi0-pir-MotionScreenToggle.git
```

Further, we need to add the script to the crontab to be executed upon boot.
Therefore, open the crontab.  
Note: If opened for the first time, it will ask you for your editor if choice.

```
crontab -e
```
Then, add the following line. It will execute the python script upon boot as a background task.  
'Note': If you changed the install location you need to adapt your path here too.  Also, if your default user is not *pi* change the path accordingly.

```
@reboot python /home/pi/MagicMirror/rpi0-pir-MotionScreenToggle/pirhandler.py &
```

Done.  
Simple as that, the Raspberry now toggles the screen based on the input data from the motion sensor.

## Troubleshooting and fine tuning

#### Adjusting Delays

The sensor itself features two potentiometers to control sensitivity and time delay.  

As this repo uses custom timings adjustable in the configuration file, there is no need for the hardware-controlled delays. Hence, we set it to the lowest possible level. This should be all the way to the left.  
Sensitvity can be adjusted as desired.

#### Monitor not powering on

If your monitor doesn't power on from its power save mode, try to increase the HDMI output signal strength of the RPi Zero by opening the config
```
sudo nano /boot/config.txt
```
and increasing the ```config_hdmi_boost``` value. It supports values from 0 to 11, where 0 is the lowest signal power.
```
config_hdmi_boost = 7
```

#### Script not running on boot

The likeliest error is either a wrong path or wrong config setting.
Adjust the cronjob by routing the error message to a seperate file for further inspection.  

Therefore, open the crontab by ```crontab -e``` and adjust the ```@reboot ...``` line by appending the routing statement.
```
@reboot python /home/pi/MagicMirror/rpi0-pir-MotionScreenToggle/pirhandler.py >> /home/pi/cronlog.txt 2>&1
```
