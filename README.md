This Project has not been released yet, still work in progress!  However, comments are welcome!

# Summary

This project is a fully documented (for basic user easy install) installation for controlling a UK SkyHD box with simple and friendly Voice Commands using Google Home/Mini/Assistant via a Raspberry Pi3 hosting this project software.  You can also add an optional Broadlink BlackBean RM3 IR device (for the IR commands), its supported too.  If you do not have the optional BlackBean RM3 device then dont worry, all of the SkyHD box functions will still work ok (they work over WiFi/Ethernet), you just will not have the functionality to control the IR commands (TV Power, Mute, vol Up/Down) via Google Home/Mini/Assistant.

The project contains all the steps and files necessary to complete the project from end to end, including the optional RM3 functionality.  In order to complete this project you will need the following: A Google Home/Mini device (or Google Assistant on your phone will do) and a Raspberry Pi with a Blank 8 Gb Micro SD card, and of course, a SkyHD Box.  If you want to control your TV power and audio functions (which are IR based) then you will also need the optional Broadlink BlackBean RM3.  

# How does it work?

The project uses the Google Home/Mini/Assistant to capture your voice commands, this converts your voice commands to text and then automatically sends them in a string directly to your IFTTT account (I'll show you how to set up a free account for this).  Your IFTTT then detects simple and friendly keyword triggers within the text it recieves and then sends commands back to your Raspberry Pi.  The Raspberry Pi then captures those commands, filters them through a series of logical steps and compiles commands into a SkyHD friendly format that can then be sent directly over your WiFi/Ethernet to your SkyHD box.  The Raspberry Pi will also detect and output the commands that need to be sent to your TV for contolling the Power and Audio functions via IR (through the optional BlackBean RM3) if you decide to include this capability. 

Right, lets get started!

You will probaly need to set up Port Forwarding on your Router to allow the IFTTT commands to get through to your Raspberry Pi.  I'll show you how I did it on my own BT Hub Router, but you may need to look elsewhere for specific instructions if yours is not a BT Router.

You will also probably need to set up a free Dynamic IP addressing service as well, this will save you the trouble of always having to change your external IP address in IFTTT every couple of days/weeks.  Most ISPs have a Dynamic external IP address set up on your Router for security; that means to the outside world you internet address they can see is not static and it often changes.  I use a free service from NO-IP.com, but there are other free services out there too.  I'll show you how to set this up for a NO-IP.com free account.



# No-IP.com

Text here

# IFTTT

Text here

# Raspberry Pi

I used a Raspberry Pi 3 for development and testing, other versions should also work fine but I've not tested them.  The Raspberry Pi can be used via SSH if you know how to do this, but if your unsure then just connect the HDMI port to a TV or suitable monitor and plug in a USB keyboard and mouse.  Dont forget to plug in an ethernet cable for internet connectivity or use a WiFi dongle. Of course, you will also need a 5v Power Supply with a micro USB connector for powering the Raspberry Pi.

Use your Windows PC or Mac to write the latest Raspian image available from https://www.raspberrypi.org/downloads/raspbian/ to the 8Gb Micro SD card.  I use a programme called Etcher to write to the SD card on my Windows PC.

Put the SD card into your Raspberry Pi and boot it up!

Once you are at the Desktop on the Raspberry Pi, then open a terminal screen  by clicking on the black box with a right arrow in it on the top left of yor Raspberry Pi screen.  In the Terminal screen (just after the Raspberrypi:~$) type the following lines, one line at a time, pressing enter after each line:

```
git clone https://github.com/VinceW31/SkyHD.git
```
```
sudo chmod +x /home/pi/SkyHD/installer.sh
```
```
sudo /home/pi/SkyHD/installer.sh
```

The installation script will now install everything for you over the next 10 to 15 min.  
The installation script will ask you for your SkyHD box IP address, this can be found from your Sky Box menu as follows:

At the end it will wait for you to get your SKY Remote ready so that it can learn your TV's IR commands for TV Power On/Off, Mute, TV Vol Up and TV Vol Down.  
When prompted you must point your SKY Remote directly downwards at the top of the BlackBean RM3 and press the appropriate button.  You will have 30 seconds to do this per command.




#### Remote control commands supported

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

