import time
import os

anykey = input("Press Enter on keyboard when you are ready to proceed")
time.sleep(1)
print("\n","Waiting for POWER button to be pressed")

time.sleep(20)
os.system ("python BlackBeanControl.py -c POWER")

#time.sleep(1)
print("\n","Waiting for MUTE button to be pressed")
os.system ("python BlackBeanControl.py -c MUTE")

#time.sleep(1)
print("\n","Waiting for VOL UP button to be pressed")
os.system ("python BlackBeanControl.py -c VOLUP")

#time.sleep(1)
print("\n","Waiting for VOL DOWN button to be pressed")
os.system ("python BlackBeanControl.py -c VOLDOWN")
