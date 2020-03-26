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

For the case of the MagicMirror installed into the home directory ´´´~/MagicMirror/´´, go there and clone the repository.

´´´
cd ~/MagicMirror/
git clone https://github.com/maximiliangall/rpi0-pir-MotionScreenToggle.git
´´´

Further, we need to add the script to the crontab to be executed upon boot.

´´´
crontab -e
´´´
Then, add the following line. It will execute the python script upon boot as a background task.
´´´
@reboot python /home/MagicMirror/rpi0-pir-MotionScreenToggle/pirhandler.py &
´´´

Done.  
Simple as that, the Raspberry now toggels the screen based on the input data from the motion sensor.
