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
cd /home/pi/

echo ""
echo "Installing Raspbian updates....."
echo ""
sudo apt-get update -y

echo ""
echo "Installing nodejs npm.......approx 5 mins"
echo ""
sudo apt-get install nodejs npm node-semver -y

echo ""
echo "Installing sky-remote-cli.....approx 1 min"
echo ""
sudo npm install -g sky-remote-cli -y

#cd /home/pi/SkyHD
echo ""
echo "Installing BlackBean requirements.....approx 5 mins"
echo ""
#pip3 install -r blackbean_requirements.txt
#pip install -r blackbean_requirements.txt
pip3 install configparser
#pip3 install netaddr
pip3 install pycryptodome



cd /home/pi/SkyHD
python3 path.py

echo ""
echo "Detecting and setting up BlackBean RM3....."
echo ""
python3 setup_RM3.py

# setup noip DUC
echo ""
echo "You must have already created a FREE Dynamic IP account at noip.com "
echo "before proceeding, because you will need to enter the username and "
echo "password for the noip account in the next steps."
echo "If you have not already done this, then do it now on your PC/Mac etc"
echo "or use the Raspberry Pi Browser (noip.com); this script will wait."
echo ""
echo "if you want to skip this step then just press Enter at the Username "
echo "and Password prompts."

#sudo cp -R /home/pi/Downloads/noip-duc-linux.tar.gz /usr/local/src
#sudo cp -R /home/pi/Downloads/noip-duc-linux.tar.gz /home/pi/SkyHD

sudo cp -R /home/pi/SkyHD/noip-duc-linux.tar.gz /usr/local/src
cd /usr/local/src
sudo tar xzf noip-duc-linux.tar.gz
cd /usr/local/src/noip-2.1.9-1/
echo ""
echo "Insatlling No-IP DUC"
sudo make
sudo make install
sudo /usr/local/bin/noip2
cd /home/pi/SkyHD

echo ""
python3 GetSkyIP.py

echo ""
echo "This is the end of the installation script."
echo ""
echo "*******************************************************************************"
echo "To make your Raspberry Pi automatically start the SkyHD service after boot-up"
echo "please see the README file in the SkyHD folder. "
echo "*******************************************************************************"

echo ""
echo "The SkyHD service is now running....."
echo ""
python3 SkyHD.py
