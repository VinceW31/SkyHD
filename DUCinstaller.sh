
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

#sudo cp -R /home/pi/Downloads/noip-duc-linux.tar.gz /usr/local/src
#sudo cp -R /home/pi/Downloads/noip-duc-linux.tar.gz /home/pi/SkyHD
sudo cp -R /home/pi/SkyHD/noip-duc-linux.tar.gz /usr/local/src
cd /usr/local/src
sudo tar xzf noip-duc-linux.tar.gz
cd /usr/local/src/noip-2.1.9-1/
sudo make
sudo make install
sudo /usr/local/bin/noip2 -C
sudo /usr/local/bin/noip2
sudo /usr/local/bin/noip2 -S
