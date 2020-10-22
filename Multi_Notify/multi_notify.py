import requests
import json
import smtplib
import ssl

#Global Variables
notify              = "false"                                       #Default Notify true/false
telegram_token      = ""                                            #Telegram Token
telegram_chatid     = ""                                            #Telegram gorup id
slack_webhook       = ""                                            #Slack Webhook
telegram_token      = ""                                            #Telegram Token
ipadress            = ""                                            #Cleaned up IP
hostname            = ""                                            #Cleaned up Hostname
owner               = ""                                            #The requester of the ressource
notificationtype    = ""                                            #The Type of notification  
image               = ""                                            #Image deployed
smtp_port           = ""                                            #smtp port 465 for SSL
smtp_sender_email   = ""                                            #The senders email
smtp_server         = ""                                            #The smtp server
smtp_username       = ""                                            #Username
smtp_password       = ""                                            #Password
teams_webhook       = ""                                            #MS Teams Webhook

#Get inputs from deployment
def get_vm_input(context, inputs):
    global notify
    global slack_webhook
    global ipadress
    global hostname
    global owner
    global notificationtype
    global image
    global telegram_token
    global telegram_chatid
    global smtp_port
    global smtp_sender_email
    global smtp_server
    global smtp_username
    global smtp_password
    global teams_webhook
    
    if 'notify' in inputs["customProperties"]:
      notify            = inputs["customProperties"]["notify"]
    slack_webhook       = inputs["slack_webhook"]    
    telegram_token      = str(inputs["telegram_token"])
    telegram_chatid     = str(inputs["telegram_chatid"]) 
    smtp_port           = inputs["smtp_port"]
    smtp_sender_email   = str(inputs["smtp_sender_email"]) 
    smtp_server         = str(inputs["smtp_server"]) 
    smtp_username       = str(inputs["smtp_username"]) 
    smtp_password       = str(inputs["smtp_password"]) 
    teams_webhook       = str(inputs["teams_webhook"]) 
    ip_raw              = inputs["addresses"]                         #Raw IP input
    ipadress            = str(ip_raw[0])[2:-2]                        #Cleaned up IP
    hostname_raw        = inputs["resourceNames"]                     #Raw Hostname
    hostname            = str(hostname_raw)[2:-2]                     #Cleaned up Hostname
    owner               = str(inputs["__metadata"]["userName"])       #The requester of the ressource
    notificationtype    = inputs["notificationtype"]                  #default notificationtype
    image               = str(inputs ["customProperties"]["image"])   #Needs error handling


def notify_email():
    #Generate message
    subject = "VRA Deployment Notification"
    text = owner + " your " + image + " image is ready with name : " + hostname + " and Ipadress : " + ipadress
    message = 'Subject: {}\n\n{}'.format(subject, text)
    #Send Message
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        server.login(smtp_username, smtp_password)    
        server.sendmail(smtp_sender_email, owner, message)
        server.quit()


def notify_slack():
    #Build the message
    text = "#VRA : " + owner + " your " + image + " image is ready with name : " + hostname + " and Ipadress : " + ipadress
    slack_data = {'text': text}
    #Post message
    response = requests.post(
    slack_webhook, data=json.dumps(slack_data),
    headers={'Content-Type': 'application/json'}
    )


def notify_teams():
    payload = "{\n\t\"text\" : \""+owner+" your "+image+" is ready with Name : "+hostname+" and Ipadress : "+ipadress+" \"\n}"
    headers = {
      'Content-Type': 'text/plain'
    }
    response = requests.request("POST", teams_webhook, headers=headers, data = payload)


def notify_telegram():
    url = "https://api.telegram.org/bot"+telegram_token+"/sendMessage?chat_id="+telegram_chatid+"&text="+owner+"\nyour "+image+" image is ready\nName : "+hostname+"\nIpadress : "+ipadress
    payload = {}
    headers= {}
    response = requests.request("GET", url, headers=headers, data = payload)


#Main Function
def handler(context, inputs):
    get_vm_input(context, inputs)
    if notify == "true":
      if notificationtype == "email" :                                             
        notify_email()
      if notificationtype == "slack" :                                             
        notify_slack()
      if notificationtype == "teams" :                                             
        notify_teams()
      if notificationtype == "telegram" :                                             
        notify_telegram()
    else:
      print ("No Notification since Notify = ",notify)