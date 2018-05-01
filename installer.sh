#!/bin/bash
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
set -o errexit

scripts_dir="$(dirname "${BASH_SOURCE[0]}")"

# make sure we're running as the owner of the checkout directory
RUN_AS="$(ls -ld "$scripts_dir" | awk 'NR==1 {print $3}')"
if [ "$USER" != "$RUN_AS" ]
then
    echo "This script must run as $RUN_AS, trying to change user..."
    exec sudo -u $RUN_AS $0
fi
clear
echo ""
read -r -p "Enter your SkyHD box IP address (format = 192.168.xxx.xxx): " skyboxip
echo ""

cd /home/pi/

echo ""
echo "Installing Raspbian updates....."
echo ""
sudo apt-get update -y

echo ""
echo "Installing nodejs npm.......(approx 5 mins)"
echo ""
sudo apt-get install nodejs npm node-semver -y

echo ""
echo "Installing sky-remote-cli....."
echo ""
sudo npm install -g sky-remote-cli -y

cd /home/pi/SkyHD
echo ""
echo "Installing Broadlink BlackBean requirements.....(approx 5 mins)"
#echo "Installing configparser.....(approx 2 mins)"
echo ""
pip install -r blackbean_requirements.txt
#pip3 install ConfigParser

python path.py

echo ""
echo "Detecting and setting up BlackBean RM3....."
echo ""
python setup_RM3.py

echo ""
echo "Now its time to Learn the IR commands for TV Power, Mute, TV Vol Up and TV Vol Down.....
echo ""
echo "You must point the SKY Remote at the top of the BlackBean RM3 and"
echo "press the appropriate button on the Remote to allow it to learn each command."
echo "You will get 30 seconds learning time per command, so no rush!"
echo ""
echo "press Y on your keyboard when you are ready to continue with the SKY Remote" anykey
echo ""
echo "Learning command for TV Power, you have 30 sec..... to  Mute, TV Vol Up and TV Vol Down....."
echo ""
python BlackBeanControl.py -c POWER
press POWER button on remote
Code displayed in terminal window and copied to ini file

echo "Waiting for you to press the SKY Remote button for TV Power....."
python BlackBeanControl.py -c MUTE
press MUTEbutton on remote
Code displayed in terminal window and copied to ini file

echo "Learning command for TV Power, you have 30 sec..... to  Mute, TV Vol Up and TV Vol Down....."
python BlackBeanControl.py -c VOLUP
press VOLUME UP button once on remote
Code displayed in terminal window and copied to ini file

echo "Learning command for TV Power, you have 30 sec..... to  Mute, TV Vol Up and TV Vol Down....."
python BlackBeanControl.py -c VOLDOWN
press VOLUME DOWN button once on remote
Code displayed in terminal window and copied to ini file

python SkyHD.py

echo ""
echo "This is the end of the installation script."
echo ""
echo "To make your Raspberry Pi automatically start the SkyHD service after boot-up"
echo "then all you need to do is type the following in this, or a new terminal window:"
echo ""
echo "sudo nano /etc/rc.local"
Echo ""
echo "Then, in the file that opens up, click in the file window"
echo "and scroll the cursor down with the cursor keys."
echo "Just before the last line (exit 0), correctly add the following line:" 
echo ""
echo "/bin/sleep 15 && cd /home/pi/SkyHD/ && python SkyHD.py &"
echo""
echo "Then save the file with Ctrl X, press Y, and press Enter"
echo "This will automatically start the SkyHD service for you 15 seconds after Pi boot-up."
echo ""
