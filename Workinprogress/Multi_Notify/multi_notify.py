import requests
import json

#Global Variables
slack_webhook       = ""                                            #Slack Webhook
ipadress            = ""                                            #Cleaned up IP
hostname            = ""                                            #Cleaned up Hostname
owner               = ""                                            #The requester of the ressource
notificationtype    = ""                                            #The Type of notification  
image               = ""                                            #Image deployed

#Get inputs from deployment
def get_vm_input(context, inputs):
    global slack_webhook
    global ipadress
    global hostname
    global owner
    global notificationtype
    global image
    
    slack_webhook       = inputs["slack_webhook"]    
    ip_raw              = inputs["addresses"]                         #Raw IP input
    ipadress            = str(ip_raw[0])[2:-2]                        #Cleaned up IP
    hostname_raw        = inputs["resourceNames"]                     #Raw Hostname
    hostname            = str(hostname_raw)[2:-2]                     #Cleaned up Hostname
    owner               = str(inputs["__metadata"]["userName"])       #The requester of the ressource
    notificationtype    = inputs["notificationtype"]                  #default notificationtype
    image               = str(inputs ["customProperties"]["image"])   #Needs error handling


#def notify_email():

def notify_slack():
    #Build the message
    text = "#VRA : " + owner + " your " + image + " image is ready with name : " + hostname + " and Ipadress : " + ipadress
    
    slack_data = {'text': text}
    
    #Post message
    response = requests.post(
    slack_webhook, data=json.dumps(slack_data),
    headers={'Content-Type': 'application/json'}
    )


#def notify_teams():

#def notify_telegram():

   
#Main Function
def handler(context, inputs):
    get_vm_input(context, inputs)
    if notificationtype == "email" :                                             
      notify_email()
    if notificationtype == "slack" :                                             
      notify_slack()
    if notificationtype == "teams" :                                             
      notify_teams()
    if notificationtype == "telegram" :                                             
      notify_telegram()
