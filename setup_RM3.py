#!/usr/bin/python
import broadlink
import time
import os
import re
import binascii

print("You can now setup the Optional BlackBean RM3 IR device, ")
print("or you can choose to do it at a later time or date ")
print("by running the setup_RM3.py script in the SkyHD folder.")
print("\n")
print("If you decide to install the RM3 now then make sure its powered ")
print("and is correctly set up first through its own App so its visible ")
print("on your Wifi network (see the BlackBean instructions).")
print("\n")
reply = raw_input("Do you want to setup a BlackBean RM3 IR device now? Y/N ")
      
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

    # Write settings to RM3settings.py file
    data = ["[General]","RM3_IPAddress = " + ipadd,"RM3_Port = " + port,"RM3_MACAddress = " + macadd,"RM3_Timeout = 5","[Commands]"]
    with open("RM3settings.py", "w") as f:
        f.write('\n'.join(data))
    print("BlackBean RM3 found and details stored sucessfully in RM3settings.py file")
    print("\n")
    reply2 = raw_input("Do you want to teach the BlackBean your TV IR codes now? Y/N ")
    if reply2 == "y":
            
      # Learn IR commands
      print("\n")
      print("Now its time to Learn the IR commands for your TV")
      print("\n")
      print("You must point your TV Remote towards the top of the BlackBean RM3 and ")
      print("press the appropriate button to allow it to learn each command in turn.")
      print("\n")
      print("Once you press the Enter key the script will wait 30 sec for you to ")
      print("get your TV/SKY remote ready next to the BlackBean RM3.")
      print("The WHITE light on the BlackBean RM3 will come on after the 30 sec is up, ")
      print("this shows its in learning mode and waiting for you to press a Remote button.")
      print("At the first white light press the TV POWER button, ")
      print("at the next white light a few seconds later press the MUTE button, ")
      print("at the third white light its the VOL UP button (hold for 1 sec),")
      print("and finally on the 4th its the VOL DOWN button (again, hold for 1 sec)")
      print("\n")
      print("So, the button sequence is: TV POWER, MUTE, VOL UP, VOL DOWN.")
      print("\n")

      anykey = raw_input("Press Enter on keyboard when you are ready to proceed  ")
      time.sleep(1)
      print("Waiting for TV POWER button to be pressed on the SKY Remote")
      time.sleep(20)
      os.system ("python BlackBeanControl.py -c power")
      #os.system ("python3 RM3control.py -c power")
      print("Waiting for MUTE button to be pressed")
      os.system ("python BlackBeanControl.py -c mute")
      #os.system ("python3 RM3control.py -c mute")
      print("Waiting for VOL UP button to be pressed")
      os.system ("python BlackBeanControl.py -c volup")
      #os.system ("python3 RM3control.py -c volup")
      print("Waiting for VOL DOWN button to be pressed")
      os.system ("python BlackBeanControl.py -c voldown")
      #os.system ("python3 RM3control.py -c voldown")
      
else:
    print("OK, proceeding without setting up BlackBean RM3 device. ")
    print("\n")

