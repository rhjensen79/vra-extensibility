"""
The purpose of this script, is to take VM input, and using WinRM connect to a Windows DNS server, 
and update/remove the DNS record, using the dnscmd.exe command.
"""

import winrm

#Global Variables
event         = ""                                          #Provision or remove.
ipadress      = ""                                          #Cleaned up IP
hostname      = ""                                          #Cleaned up Hostname
DNS_Server    = ""                                          #DNS server where the command will be executed
DNS_Domain    = ""                                          #The DNS Domain to be updated
Username      = ""                                          #Username with right to do the operation
Password      = ""                                          #Password for the account" 

#Get inputs from deployment
def get_vm_input(context, inputs):
    global event
    global ipadress
    global hostname
        
    event         = str(inputs["__metadata"]["eventTopicId"])   #Provision or remove. 
    ip_raw        = inputs["addresses"]                         #Raw IP input
    ipadress      = str(ip_raw[0])[2:-2]                        #Cleaned up IP
    hostname_raw  = inputs["resourceNames"]                     #Raw Hostname
    hostname      = str(hostname_raw)[2:-2]                     #Cleaned up Hostname


def handler(context, inputs):
    get_vm_input(context, inputs)
    #Open session
    session = winrm.Session(DNS_Server, auth=(Username,Password))
    
    #Check for provision
    result = event.startswith('compute.provision')
    if result == True :
      dns_command = "dnscmd.exe "+DNS_Server+" /RecordAdd "+DNS_Domain+" "+hostname+" 10 A "+ipadress+""
      result = session.run_ps(dns_command)
      print(result.std_out)

    #Check for removal
    result = event.startswith('compute.removal')
    if result == True :
      dns_command = "dnscmd /RecordDelete "+DNS_Domain+" "+hostname+" a /f"
      result = session.run_ps(dns_command)
      print(result.std_out)
