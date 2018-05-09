#!/usr/bin/python
import broadlink
import time
import os
import re
import binascii

print("At this point you can now setup the Optional BlackBean RM3 IR device, ")
print("however, this can also be done at a later time or date ")
print("by running the setup_RM3.py script in the SkyHD folder.")
print("If you decide to proceed then make sure your RM3 is powered ")
print("and is correctly set up through its own App to be visible ")
print("on your Wifi network (see the BlackBean instructions).")
print("\n")
reply = input("Do you want to setup a BlackBean RM3 IR device now? Y/N ")
      
if reply == "y":
    print("\n")
    # Search for RM3
    print('Scanning network for Broadlink devices (5s timeout) ... ')
    devices = broadlink.discover(timeout=5)
    print(('Found ' + str(len(devices )) + ' broadlink device(s)'))
    time.sleep(1)
    for index, item in enumerate(devices):
        devices[index].auth()
    m = re.match(r"\('([0-9.]+)', ([0-9]+)", str(devices[index].host))
    ipadd = m.group(1)
    port = m.group(2)
    macadd = str(''.join(format(x, '02x') for x in devices[index].mac[::-1]))
    macadd = macadd[:2] + ":" + macadd[2:4] + ":" + macadd[4:6] + ":" + macadd[6:8] + ":" + macadd[8:10] + ":" + macadd[10:12]
    print(('Device ' + str(index + 1) +':\nIPAddress = ' + ipadd + '\nPort = ' + port + '\nMACAddress = ' + macadd))

    # Write settings to BlackBeanControl.ini file
    data = ["[General]","IPAddress = " + ipadd,"Port = " + port,"MACAddress = " + macadd,"Timeout = 5","[Commands]"]
    with open("BlackBeanControl.ini", "w") as f:
        f.write('\n'.join(data))
    print("BlackBean RM3 found and details stored sucessfully in BlackBeanControl.ini file")

    # Learn IR commands
    print("\n","Now its time to Learn the IR commands for your TV")
    print("\n")
    print("\n","You must point your TV Remote towards the top of the BlackBean RM3 and ")
    print("\n","press the appropriate button to allow it to learn each command in turn.")
    print("\n")
    print("\n","Once you press the Enter key below the script will wait 30 sec for you to ")
    print("\n","get your TV/SKY remote ready next to the BlackBean RM3.")
    print("\n","The White light on the BlackBean RM3 will come on after the 30 sec is up, ")
    print("\n","this indicates its in learning mode and waiting for you to press a Remote button.")
    print("\n","At the first White light press the TV POWER button, ")
    print("\n","at the next White light a few seconds later press the MUTE button, ")
    print("\n","at the htird its the VOL UP button (hold for 1 sec),")
    print("\n","and finally on the 4th its the VOL DOWN button (again, hold for 1 sec)")

    anykey = input("Press Enter on keyboard when you are ready to proceed")
    time.sleep(1)
    print("\n","Waiting for POWER button to be pressed")
    time.sleep(20)
    os.system ("python BlackBeanControl.py -c power")
    print("\n","Waiting for MUTE button to be pressed")
    os.system ("python BlackBeanControl.py -c mute")
    print("\n","Waiting for VOL UP button to be pressed")
    os.system ("python BlackBeanControl.py -c volup")
    print("\n","Waiting for VOL DOWN button to be pressed")
    os.system ("python BlackBeanControl.py -c voldown")
else:
    print("\n","OK, proceeding without setting up (or changing current setup for) ")
    print("\n","BlackBean RM3 device")
    print("\n")

