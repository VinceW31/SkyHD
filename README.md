# Summary

This project is still under development.

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

Use your Windows PC or Mac to write a Raspian image to the 8Gb Micro SD card by following these steps:



# Install sky-remote-cli & Python program

Text here

A command line app to send remote control commands to a Sky TV box. Compatible with Sky+HD and Sky Q.

## Usage

#### Installation

You'll need to install this globally with the `-g` flag.

```
npm install -g sky-remote-cli
```

#### Controlling a Sky TV box

The first argument must be the IP address of the Sky box you want to control. All arguments after that are commands to send to the box - you can send just one command or many at once (they will be sent in sequence). If connecting to a Sky Q box running formware older than v0.60, pass the `--sky_q_legacy` flag. The previously used `--sky_q` flag now has no impact (but is still accepted for compatability).

###### Turn the box on / off
```
sky-remote-cli 192.168.0.40 power
```

*or, for Sky Q (with older firmware <0.60):*

```
sky-remote-cli --sky_q_legacy 192.168.0.40 power
```

###### Channel up, pause, show info
```
sky-remote-cli 192.168.0.40 channelup pause i
```

###### Change channel to 101
```
sky-remote-cli 192.168.0.40 1 0 1
```

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
