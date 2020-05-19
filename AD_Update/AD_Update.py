import winrm

#Global Variables
event         = ""                                          #Provision or remove.
hostname      = ""                                          #Cleaned up Hostname

#Get inputs from deployment
def get_vm_input(context, inputs):
    global event
    global hostname
        
    event         = str(inputs["__metadata"]["eventTopicId"])   #Provision or remove - Not used yet. 
    hostname_raw  = inputs["resourceNames"]                     #Raw Hostname
    hostname      = str(hostname_raw)[2:-2]                     #Cleaned up Hostname


def handler(context, inputs):
    get_vm_input(context, inputs)
    #Open session
    session = winrm.Session('hostname', auth=('username','password'))
    
    #Check for provision
    result = event.startswith('compute.provision')
    if result == True :
      dns_command = "dsadd computer cn="+hostname+",CN=Computers,DC=cmplab,DC=dk"
      result = session.run_ps(dns_command)
      print(result.std_out)

    #Check for removal
    result = event.startswith('compute.removal')
    if result == True :
      dns_command = "dsrm cn="+hostname+",CN=Computers,DC=cmplab,DC=dk -noprompt"
      result = session.run_ps(dns_command)
      print(result.std_out)