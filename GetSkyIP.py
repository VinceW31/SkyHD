import sys

def retry():
   get_input()
   check_valid()
   write_to_file()
   
def check_valid():
   try:
      ip_split()
   except:
      error_message()

def error_message():
   check_reply = raw_input ("Invalid format, do you want to try again? (Y/N) ")
   if check_reply == "y":
      retry()
   else:
      print("\n","You must have a vaild IP address for your SkyHD Box to proceed.")
      sys.exit()
         
def get_input():
   global sky
   sky = raw_input("Please enter your SkyHD Box IP address (format 192.168.xxx.xxx): ")

def ip_split(): 
   global sky
   global ip1
   global ip2
   global ip3
   global ip4
   ip1 = sky.split('.',3)[0]
   ip2 = sky.split('.',3)[1]
   ip3 = sky.split('.',3)[2]
   ip4 = sky.split('.',3)[3]

def write_to_file():
   global ip1
   global ip2
   global ip3
   global ip4
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
write_to_file()

