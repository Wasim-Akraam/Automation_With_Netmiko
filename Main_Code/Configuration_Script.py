from netmiko import ConnectHandler
import getpass
import os

""" Open Device host file to read host name and pass device name for connecting and executing command"""
with open("C:\\Users\\wasim\\OneDrive\\Desktop\\Automation\\Devices\\host.txt","r") as do:
    " Return list of device "
    host=do.read().splitlines()

co=open("C:\\Users\\wasim\\OneDrive\\Desktop\\Automation\\Command\\list_command.txt","r")
cmd=co.readlines()

""" For connecting with multiple device we need to iterate list of host one by one by for loop"""

for device in host:

    try:
        device_connect=ConnectHandler(device_type="cisco_xe",host=device,username="developer",password="C1sco12345")
        print("Connection established  to device {}....".format(device))

    except Exception as err:
        execption_type=type(err).__name__
        print(execption_type)
        continue


    print("Executing Command....")
    #device_connect.enable()
    #device_connect.send_config_set(cmd)
    device_connect.send_config_from_file(config_file='C:\\Users\\wasim\\OneDrive\\Desktop\\Automation\\Command\\list_command.txt')
    device_connect.save_config()
    device_connect.disconnect()
    print("Disconnected from Device")
    co.close()


