import json
from botocore.vendored import requests

#Variables
auth_token  = ""                #Your VRA Token
pipeline    = ""                #Your Pipeline ID

def lambda_handler(event, context):
    # Autorize
    url = "https://api.mgmt.cloud.vmware.com/iaas/api/login"
    payload = "{\n\t\"refreshToken\": \""+auth_token+"\"\n}"
    headers = {
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data = payload)
    data = response.json()
    token = (data['token'])
    #print ("Token : "+token)
    
    #Request 
    url = "https://api.mgmt.cloud.vmware.com/pipeline/api/pipelines/"+pipeline+"/executions"
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer '+token
    }
    response = requests.request("POST", url, headers=headers, data = payload)
    #print(response)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Demo Env comming up!')
    }