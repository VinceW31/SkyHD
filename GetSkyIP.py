
sky = input ("Please enter your Sky Box IP address (format 192.168.xxx.xxx): ")
   
ip1 = sky.split('.',3)[0]
ip2 = sky.split('.',3)[1]
ip3 = sky.split('.',3)[2]
ip4 = sky.split('.',3)[3]

#print(ip1,ip2,ip3,ip4)
#print(ip1)
#print(ip2)
#print(ip3)
#print(ip4)

with open("skybox_ip.py", "w") as f:
    f.write("ip1 = " + ip1)
    f.write("\n")
    f.write("ip2 = " + ip2)
    f.write("\n")
    f.write("ip3 = " + ip3)
    f.write("\n")
    f.write("ip4 = " + ip4)
