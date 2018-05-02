SKY = input ("Please enter your Sky Box IP address (format 192.168.xxx.xxx): ")
data = ["skyboxip = " + SKY]
with open("skybox_ip.ini", "w") as f:
    f.write("[General]",'/n'.join(data))
