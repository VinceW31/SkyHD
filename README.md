This Project has not been released yet, still work in progress!  However, comments are welcome!

# Summary

This project is a fully documented (for basic user easy install) installation for controlling a UK SkyHD box with simple and friendly Voice Commands using Google Home/Mini/Assistant via a Raspberry Pi3 hosting this project software.  You can also add an optional Broadlink BlackBean RM3 IR device (for the IR commands), its supported too.  If you do not have the optional BlackBean RM3 device then dont worry, all of the SkyHD box functions will still work ok (they work over WiFi/Ethernet), you just will not have the functionality to control your TV IR commands (TV Power, Mute, Vol Up/Down) via Google Home/Mini/Assistant.

The project contains all the steps and files necessary to complete the project from end to end, including the optional RM3 functionality.  In order to complete this project you will need the following: A Google Home/Mini device (or Google Assistant on your phone will do) and a Raspberry Pi with a Blank 8 Gb Micro SD card, and of course, a SkyHD Box.  If you want to control your TV power and audio functions (which are IR based) then you will also need the optional Broadlink BlackBean RM3.  

# How does it work?

The project uses the Google Home/Mini/Assistant to capture your voice commands, this converts your voice commands to text strings which  your IFTTT account (I'll show you how to set up a free account for this) can read.  IFTTT then detects simple and friendly keyword triggers within the text it recieves and then sends commands back to your Raspberry Pi.  The Raspberry Pi then captures those commands, filters them through a series of logical steps and compiles commands into a SkyHD friendly format that can then be sent directly over your WiFi/Ethernet to your SkyHD box.  The Raspberry Pi will also detect and output the commands that need to be sent to your TV for contolling the Power and Audio functions via IR (through the optional BlackBean RM3) if you decide to include this capability. 

Right, lets get started!

# Port Forwarding on your Router.

First you will probaly need to set up Port Forwarding on your Router to allow the IFTTT commands to get through to your Raspberry Pi.  I'll show you how I did it on my own BT Hub Router, but you may need to look elsewhere for specific instructions if yours is not a BT Router.

# Manage your External IP address with No-IP.com.

Next, you will also probably need to set up a free Dynamic IP addressing service as well, this will save you the trouble of always having to change your external IP address in IFTTT every couple of days/weeks.  Most ISPs have a Dynamic external IP address set up on your Router for security; that means to the outside world you internet address is not static, it changes quite often.  I use a free service from NO-IP.com, but there are other free services out there too.  The following procedure shows you how to set up a NO-IP.com free account.

Search for "noip" in Google and click on the link. Hit the Sign Up button, enter a Username and Password, then create a memorable hostname ( write your chosen hostname down as you will need it later), agree the Terms of service and hit the Free Sign Up button to create your account. Your Free Hostname will time expire every 30 days unless you renew it in the email reminder they send you, to avoid this you can sign up for the Enhanced service if you like.

# IFTTT

Now you need to create your IFTTT account (if you dont already have one), its all free and easy to setup.  Once your account is created then go to My Applets and click on New Applet, then click on the big blue THIS text to start creating your applet.  In the search box type "Google" and then click on the Google Assistant box, now it will ask to link to your Google account so IFTTT can capture your voice commands automatically.  Once youve done this it will move on to Step 2 and ask you to choose a trigger, we will always use the "Say a phrase with a Text ingredient" selection.  Now lets create several applets to capture our commands as follows:

The first applet will capture your requests to change channel, so where it asks "What do you want to say?" type the following: "switch to $", in the second box: "change to $", in the third box: "tune to $", or use a phrase that better suits you to capture the Change Channel request. Put something suitable in the fourth box like "ok, switching tv to $" so it will repeat back to you the channel name or number you requested. Now hit the Create Trigger button at the bottom of the applet.

Now click on the big blue THAT text to create the action to send to your Raspberry Pi for changing channel on youe Sky box. In the search box type "web", select webhooks, then click on the make a web request option. In the first box (URL) you must type the hostname you created in your no-ip.com account (for example: joebloggs.ddns.net) followed exactly by the text as show here: http://joebloggs.ddns.net:5000/channels then click on the Add Ingredient button and choose Text Field (so that it adds it to the end of your URL).  For the Method box choose "POST". For the content type choose "text/plain", then click on the Save button.

# Raspberry Pi

I used a Raspberry Pi 3 for development and testing, other versions should also work fine but I've not tested them.  The Raspberry Pi can be used via SSH if you know how to do this, but if your unsure then just connect the HDMI port to a TV or suitable monitor and plug in a USB keyboard and mouse.  Dont forget to plug in an ethernet cable for internet connectivity or use a WiFi dongle. Of course, you will also need a 5v Power Supply with a micro USB connector for powering the Raspberry Pi.

Use your Windows PC or Mac to write the latest Raspian image available from https://www.raspberrypi.org/downloads/raspbian/ to the 8Gb Micro SD card.  I use a programme called Etcher to write to the SD card on my Windows PC.

Put the SD card into your Raspberry Pi and boot it up!

Once you are at the Desktop on the Raspberry Pi, then open a terminal screen  by clicking on the black box with a right arrow in it on the top left of yor Raspberry Pi screen.  In the Terminal screen (just after the Raspberrypi:~$) type the following lines, one line at a time, pressing enter after each line:

```
git clone https://github.com/VinceW31/SkyHD.git
```
```
sudo chmod +x /home/pi/SkyHD/install.sh
```
```
sudo /home/pi/SkyHD/install.sh
```

The installation script will now switch the default Python version to Python3 and install everything for you over the next 10 to 15 min. 

The script will ask you if you want to install the optional BlackBean RM3 device, this  will allow you to control your TV IR commands like TV Power On/Off, Mute, Volume Up and Volume down.  If you select NO then it will skip this section, if you choose YES then it will continue and try to detect the BlackBean RM3 assuming its already active on your WiFi network. You MUST have already setup your BlackBean RM3 beforehand to be visible on your own WiFi network by following its own instructions.

If the script successfully detects the BlackBean RM3 then it will automatically update the relevant files and continue. The script will  now wait 30 sec for you to get your SKY Remote ready so it can learn your TV's IR commands for TV Power On/Off, Mute, TV Vol Up and TV Vol Down. When prompted, you must point your TV/SKY Remote directly downwards towards the top of the BlackBean RM3 and then press the appropriate button on the TV/SKY Remote. 

A white light will come on at the bottom of the BlackBean RM3 after the 30 sec is up, this shows its in learning mode and waiting for you to press a button on your TV/Sky Remote.
When you see the first white light press the TV POWER button, then the light will go off.
About 10 seconds later, at the second white light, press the MUTE button, at the third white light its the VOL UP button (hold for 1 sec) and finally on the 4th its the VOL DOWN button (again, hold for 1 sec). So, the button sequence to remember is: TV POWER, MUTE, VOL UP, VOL DOWN.

If you want, you can always try again or go back and add a BlackBean RM3 device at a later date by just running the Setup_RM3.py script again.

Next, the installation script will setup the "noip" Dynamic Update Client (DUC) software for you.  Their installation software will ask you for your noip.com username & password, then at the next two questions just press the Enter key for the default response. 

Finally, the main installation script will ask you for your SkyHD box IP address, this can be found from your Sky Box Network settings menu, this must be entered in the correct format (eg 192.168.xxx.xxx)

Once this is done your system should be up and running on your Raspberry Pi and listening for commands from IFTTT.

### Auto Start on Reboot
To make this program Auto-start on Raspberry Pi Boot up or Reboot then all you need to do is the following:

Type the next line in a new terminal window:
```
sudo nano /etc/rc.local
```
Then, in the file that opens up, click in the file window and scroll the cursor down with the cursor keys.  Just before the last line (exit 0), correctly add the following line:
```
/bin/sleep 15 && cd /home/pi/SkyHD/ && python3 SkyHD.py &
```
Then save the file with Ctrl X, press Y, and press Enter. This will automatically start the SkyHD service for you 15 seconds after Pi boot-up. So, Reboot your Raspberry Pi and try it!

#### SkyHD Remote control commands supported

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

