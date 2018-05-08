global ip1
global ip2
global ip3
global ip4


#get_input()
#check_valid()
#Print_IP()
#Write_to_file()


def retry():
   get_input()
   check_valid()
   Print_IP()
   Write_to_file()
   
def check_valid():
   try:
      ip_split()
   except:
      check_reply = ("Invalid format, do you want to try again? (Y/N)")
      if check_reply == "y":
         retry()
      else:
         print("You must have a vaild IP address for your SkyHD Box to proceed")
   
def get_input():
   sky = input ("Please enter your SkyHD Box IP address (format 192.168.xxx.xxx): ")

def ip_split(): 
   ip1 = sky.split('.',3)[0]
   ip2 = sky.split('.',3)[1]
   ip3 = sky.split('.',3)[2]
   ip4 = sky.split('.',3)[3]
   
def Print_IP():
   print(ip1,ip2,ip3,ip4)
   print(ip1)
   print(ip2)
   print(ip3)
   print(ip4)
   
def write_to_file():
   with open("skybox_ip.py", "w") as f:
      f.write("ip1 = " + ip1)
      f.write("\n")
      f.write("ip2 = " + ip2)
      f.write("\n")
      f.write("ip3 = " + ip3)
      f.write("\n")
      f.write("ip4 = " + ip4)

get_input()
check_valid()
Print_IP()
Write_to_file()
