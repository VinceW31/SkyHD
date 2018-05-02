import configparser
from os import path

ApplicationDir = path.dirname(path.abspath(__file__))
SkyIPSettings =path.join(ApplicationDir, 'skybox_ip.ini')

Settings = configparser.ConfigParser()
Settings.read(SkyIPSettings)

skyboxip = Settings.get('General', 'skyboxip')
