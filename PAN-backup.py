import requests

#Firewall IP address
fwip = "10.10.10.10"         

#Palo API key
key = "YOUR API KEY GOES HERE"

#build URI with previously provided IP and key
uri = "https://"+fwip+"/api/?type=export&category=configuration&key="+key

#filename to write
myfile = "jpbackup.xml"

#output to verify requested resource
print("Requesting the following resource:")
print(uri)

#http request config from management IP and API key provided
r = requests.get(uri, verify=False)

#write results to file
f = open(myfile, "w")

f.write(r.text)
