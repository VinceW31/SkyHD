This Project has not been released yet, still work in progress!  However, comments are welcome!

# Summary

This project is a fully documented (for basic user easy install) installation for controlling a UK SkyHD box with Google home/Mini via a Raspberry Pi.  

It contains all the steps and files necessary to complete the project from end to end.  In order to complete this project you will need the following: Google Home/Mini device (or Google Assistant on your phone will do), Raspberry Pi, Blank 8 Gb Micro SD card (for Raspberry Pi 3) and of course, a SkyHD Box.

The project uses the Google Home/Mini assistant to capture your voice command, this is then sent automatically by Google Home/Mini to IFTTT (you will need to set up a free account) which detects certain keyword triggers and then sends commands back to your Raspberry Pi to compile into a macro thats sent directly to your SkyHD box.  

# What it doesnt do

It does not control your TV functions like on/off and volume/mute, these are IR TV functions that your Sky Remote can control, but they are not Sky box functions.  You will need an IR blaster device like a Harmony Hub or a Broadlink RM3 to perform these functions directly from Google Assistant.  This is possible to do but is not covered in this project.

# No-IP.com

Text here

# IFTTT

Text here

# Raspberry Pi

I used a Raspberry Pi 3 for development and testing, other versions should also work fine but I've not tested them.  The Raspberry Pi can be used via SSH if you know how to do this, but if your unsure then just connect the HDMI port to a TV or suitable monitor and plug in a USB keyboard and mouse.  Dont forget to plug in an ethernet cable for internet connectivity or use a WiFi dongle. Of course, you will also need a 5v Power Supply with a micro USB connector for powering the Raspberry Pi.

Use your Windows PC or Mac to write the latest Raspian image available from https://www.raspberrypi.org/downloads/raspbian/ to the 8Gb Micro SD card.  I use a programme called Etcher to write to the SD card on my Windows PC.

Put the SD card into your Raspberry Pi and boot it up. Then open a terminal screen and type the following lines, one line at a time, pressing enter after each line:

When you get to the desktop open a terminal screen and type the following line by line (pressing ENTER after each line):
```
git clone https://github.com/VinceW31/SkyHD.git
```
```
sudo chmod +x /home/pi/SkyHD/installer.sh
```
```
sudo /home/pi/SkyHD/installer.sh
```
When the installation script has finished then enter the following lines:

```
cd /home/pi/SkyHD
```
```
sudo python SkyHD.py
```

At the moment you will need to correct the IP address in SkyHD.py to your own Sky Box IP address.


#### Remote control commands

`sky` `power`

`tvguide` or `home` `boxoffice` `services` or `search` `interactive` or `sidebar`

`up` `down` `left` `right` `select`

`channelup` `channeldown` `i`

`backup` or `dismiss` `text` `help`

`play` `pause` `rewind` `fastforward` `stop` `record`

`red` `green` `yellow` `blue`

`0` `1` `2` `3` `4` `5` `6` `7` `8` `9`


## See also

- http://github.com/dalhundal/sky-remote - The underlying Node module used by this tool
- http://github.com/dalhundal/sky-q - A Node module for interacting with Sky Q boxes
