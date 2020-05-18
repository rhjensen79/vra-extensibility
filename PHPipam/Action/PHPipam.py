import requests
import json

#Global Variables
phpipamhost   = "FQDN of PHPipam host"                      #PHPIpam Host
event         = ""                                          #Provision or remove.
ipadress      = ""                                          #Cleaned up IP
subnetid      = ""                                          #Subnetid Calculated later from IPadress
hostname      = ""                                          #Cleaned up Hostname
description   = "App description etc. "                     #Application Description - Used for Project name
requestid     = ""                                          #Custom input value, containing Request id. Being  set in custom field later
project       = ""                                          #The project the deployment belongs to.
owner         = ""                                          #The requester of the ressource
note          = "Created by VRA"                            #Note text
app           = "PHPipam app name"                          #PHPmyipam API App Name
app_token     = "PHPipam app token"                         #PHPmyipam API App Token
token         = ""                                          #Generated auth token
response      = ""                                          #Response - not used yet.
Authorization = "Basic auth for PHPipam"                    #Username and Pass for PHPipam. Can be generated here https://www.blitter.se/utils/basic-authentication-header-generator/           

#Get inputs from deployment
def get_vm_input(context, inputs):
    global event
    global ipadress
    global hostname
    global requestid
    global project
    global owner
        
    event         = str(inputs["__metadata"]["eventTopicId"])   #Provision or remove - Not used yet. 
    ip_raw        = inputs["addresses"]                         #Raw IP input
    ipadress      = str(ip_raw[0])[2:-2]                        #Cleaned up IP
    hostname_raw  = inputs["resourceNames"]                     #Raw Hostname
    hostname      = str(hostname_raw)[2:-2]                     #Cleaned up Hostname
    requestid     = str(inputs["tags"]["requestid"])            #Custom input value, containing Request id. 
    project       = str(inputs["tags"]["project"])              #The project the deployment belongs to.
    owner         = str(inputs["__metadata"]["userName"])       #The requester of the ressource

#Get subnet identifier
def get_subnetid():
    global ipadress
    global subnetid

    result = ipadress.startswith('192.168.100')
    if result == True :
      subnetid = "10"
    result = ipadress.startswith('192.168.101')
    if result == True :
      subnetid = "11"
    result = ipadress.startswith('192.168.50')
    if result == True :
      subnetid = "12"
    result = ipadress.startswith('10.164')
    if result == True :
      subnetid = "16"
    result = ipadress.startswith('172.17.16')
    if result == True :
      subnetid = "13"
    result = ipadress.startswith('172.17.17')
    if result == True :
      subnetid = "14"
    result = ipadress.startswith('172.17.22')
    if result == True :
      subnetid = "15"
    
    print ("SubnetID : " + subnetid)

#Get token
def get_token():
    global token   
    url = "http://"+phpipamhost+"/api/"+app+"/user"
    payload  = {}
    headers = {
      'Content-Type': 'application/json',
      'token': ''+app_token+'',
      'Authorization': ''+Authorization+'',
    }
    response = requests.request("POST", url, headers=headers, data = payload)
    #Get response as json
    data = response.json()
    #Set token Variable
    token = (data['data']['token'])

#Delete VM info
def delete_vm():
    url = "http://"+phpipamhost+"/api/"+app+"/addresses/"+ipadress+"/"+subnetid+""
    payload = "{}"
    headers = {
     'Content-Type': 'application/json',
     'token': ''+token+'',
    }
    response = requests.request("DELETE", url, headers=headers, data = payload)
    
#Create VM info
def create_vm():
    #Create Custom Description
    description = "Project : "+project
    #Set IP
    url = "http://"+phpipamhost+"/api/"+app+"/addresses/"
    payload = "{\"ip\":\""+ipadress+"\",\"subnetId\":\""+subnetid+"\",\"hostname\":\""+hostname+"\",\"description\":\""+description+"\",\"owner\":\""+owner+"\",\"note\":\""+note+"\",\"custom_request\":\""+requestid+"\"}"
    headers = {
     'Content-Type': 'application/json',
     'token': ''+token+'',
    }
    response = requests.request("POST", url, headers=headers, data = payload)
   
#Main Function
def phpipam(context, inputs):
    print ("Running PHPipam function")
    get_vm_input(context, inputs)
    get_subnetid()
    get_token()
    result = event.startswith('compute.provision')
    if result == True :                                             #Update to match your subscription item if required.
      delete_vm()
      create_vm()
    result = event.startswith('compute.removal')                    #Update to match your subscription item if required.
    if result == True :
      delete_vm()
