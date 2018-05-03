import time
import os

anykey = input("Press Enter on keyboard when you are ready to proceed")
time.sleep(1)
print("\n","Waiting for POWER button to be pressed")

time.sleep(20)
os.system ("python BlackBeanControl.py -c power")

#time.sleep(1)
print("\n","Waiting for MUTE button to be pressed")
os.system ("python BlackBeanControl.py -c mute")

#time.sleep(1)
print("\n","Waiting for VOL UP button to be pressed")
os.system ("python BlackBeanControl.py -c volup")

#time.sleep(1)
print("\n","Waiting for VOL DOWN button to be pressed")
os.system ("python BlackBeanControl.py -c voldown")
