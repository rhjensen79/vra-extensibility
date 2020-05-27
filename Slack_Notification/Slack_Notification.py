import json
from botocore.vendored import requests

def handler(context, inputs):
    #Get webhook url from inputs
    webhook_url = inputs["webhook_url"]
    
    #Get values from deployment and clen it up, if needed.
    image = str(inputs["customProperties"]["image"])
    ip = inputs["addresses"]
    ip_clean = str(ip[0])[2:-2]
    deploymentname = inputs["resourceNames"]
    deploymentname_clean = str(deploymentname)[2:-2]
    requester = str(inputs["__metadata"]["userName"])
    
    #Build the message
    text = "#VRA : " + requester + " your " + image + " image is ready with name : " + deploymentname_clean + " and Ipadress : " + ip_clean
    
    slack_data = {'text': text}
    
    #Post message
    response = requests.post(
    webhook_url, data=json.dumps(slack_data),
    headers={'Content-Type': 'application/json'}
    )