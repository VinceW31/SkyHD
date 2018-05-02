import configparser
from os import path

ApplicationDir = path.dirname(path.abspath(__file__))
BlackBeanControlSettings = path.join(ApplicationDir, 'BlackBeanControl.ini')
#SkyIPsettings =path.join(ApplicationDir, 'skybox_ip.ini')

Settings = configparser.ConfigParser()
Settings.read(BlackBeanControlSettings)
#SkySettings = configparser.ConfigParser()
#Settings2.read(SkySettings)


IPAddress = Settings.get('General', 'IPAddress')
Port = Settings.get('General', 'Port')
MACAddress = Settings.get('General', 'MACAddress')
Timeout = Settings.get('General', 'Timeout')
#SkyIP = Settings2.get('General', 'skyboxip')
