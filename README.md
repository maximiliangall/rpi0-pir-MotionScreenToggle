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
'Note': If you changed the install location you need to adapt your path here too.

```
@reboot python /home/MagicMirror/rpi0-pir-MotionScreenToggle/pirhandler.py &
```

Done.  
Simple as that, the Raspberry now toggles the screen based on the input data from the motion sensor.

## Troubleshooting

The sensor itself features two potentiometers to control sensitivity and time delay.  

As this repo uses custom timings implemented in the configuration file, there is no need for time delays. Hence, we set it to the lowest possible level. This should be all the way to the left.

If your monitor doesn't power on from its power save mode, try to increase the HDMI output signal strength of the RPi Zero by opening the config
```
sudo nano /boot/config.txt
```
and increasing the appropriate var. It supports values from 0 to 11, where 0 is the lowest signal power.
```
config_hdmi_boost = 7
```
