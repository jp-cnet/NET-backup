#!/usr/bin/env python3

import requests
import datetime

#Firewall IP address
fwip = "10.10.10.10"         

#Palo API key
key = "YOUR API KEY GOES HERE"

#build URI with previously provided IP and key
uri = "https://"+fwip+"/api/?type=export&category=configuration&key="+key

mypath = "/home/jeremy/backup/pa"
filename = "sobitnet-pa"

#filename to write
myfile = mypath+"/"+datetime.datetime.now().strftime("%y-%m-%d-%H-%M")+"-"+filename+".xml"

#output to verify requested resource
print("Requesting the following resource:")
print(uri)
print("File to be written:")
print(myfile)

#http request config from management IP and API key provided
r = requests.get(uri, verify=False)

#write results to file
f = open(myfile, "w")

f.write(r.text)
