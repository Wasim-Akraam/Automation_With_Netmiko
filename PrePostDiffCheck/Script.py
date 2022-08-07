from netmiko import ConnectHandler
import getpass
import os

""" Open Device host file to read host name and pass device name for connecting and executing command"""

with open("C:\\Users\\wasim\\OneDrive\\Desktop\\Automation\\Devices\\host.txt","r") as do:
    " Return list of device "
    host=do.read().splitlines()
""" Open Command file for reading command """
with open("C:\\Users\\wasim\\OneDrive\\Desktop\\Automation\\Command\\command.txt","r") as co:
    cmd=co.read().splitlines()

""" Creating Pre-Check and Post-Check directory"""
#if not os.path.exists("Pre-Check"):
  #  os.makedirs("Pre-Check")
#if not os.path.exists("Post-Check"):
  #  os.makedirs("Post-Check")

""" Ask user to make choice to 1 for Pre-check and 2 for post check"""

Choice=input("Enter 1 for Pre-check and 2 for post check : ")


""" For connecting with multiple device we need to iterate list of host one by one by for loop"""

for device in host:
    print("Connecting to device {}".format(device))
    device_connect=ConnectHandler(device_type="autodetect",
                              host=device,username="developer",password="C1sco12345")

    "Once connected with Device we need to run required command"
    out=""
    for command in cmd:
        out+=command+"\n"
        print(command)
        out+="*"*100+"\n"
        out+=device_connect.send_command(command)

    device_connect.disconnect()

    if Choice=="1":
        with open("C:\\Users\\wasim\\OneDrive\\Desktop\\Automation\\Pre-Check\\"+device+".txt","w") as pre:
            pre.write(out)

    if Choice=="2":
        with open("C:\\Users\\wasim\\OneDrive\\Desktop\\Automation\\Post-Check\\"+device+".txt","w") as post:
            post.write(out)







