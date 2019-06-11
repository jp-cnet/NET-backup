#!/bin/usr/local/python3

from netmiko import ConnectHandler

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '10.10.10.10',
    'username': 'admin',
    'password': 'password'
}

net_connect = ConnectHandler(**iosv_l2)
output = net_connect.send_command('show run')
print (output, file=open("output.txt", "w"))
