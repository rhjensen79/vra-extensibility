---
runtime: "python3"
code: |
  import winrm

  # context.py is automatically added.
  from context import getInput, setOutput
  

  #Open session
  session = winrm.Session(getInput('DNS_Server'), auth=(getInput('Username'),getInput('Password')))
    
  #Create command
  dns_command = "dnscmd.exe "+getInput('DNS_Server')+" /RecordAdd "+getInput('DNS_Domain')+" "+getInput('hostname')+" 10 A "+getInput('ipadress')+""
  result = session.run_ps(dns_command)
  print(result.std_out)
  
inputProperties:      # Enter fields for input section of a task
  - name: ipadress
    type: text
    title: ipadress

  - name: hostname
    type: text
    title: hostname
    
  - name: DNS_Server
    type: text
    title: DNS Server
    defaultValue: 
    
  - name: DNS_Domain
    type: text
    title: DNS Domain
    defaultValue: 
    
  - name: Username
    type: text
    title: Username
    defaultValue: 
    
  - name: Password
    type: password
    title: Password 
    placeHolder: 'secret/password field'
    

outputProperties:     # Enter fields that would display in output section
  - name: statusCode
    type: label
    title: Status Code
