SKY = input ("Please enter your Sky Box IP address (format 192.168.xxx.xxx): ")
data = ["[General]","skyboxip = " + str(SKY)]
with open("skybox_ip.py", "w") as f:
    f.write("\n".join(data))
