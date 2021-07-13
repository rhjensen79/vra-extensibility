# DNS Update

A ABX script, that connects to a DNS server, using WinRM, and updates/Deletes a DNS a record, based on lifecycle of the VM.

Note that Winrm, neeeds to be enable on the target VM, and pywinrm needs to be set, in the dependencicy on the ABX action container. 

![Dependency](https://github.com/rhjensen79/vra-extensibility/blob/master/DNS_Update/Screenshoots/dependency.png)

Remember to change username and password in the script. 

# Update 13.7.2021
@PaulDavey_79 has updated this script quite a lot. So please take a look at his work as well : https://automationpro.co.uk/abx-dns-management-with-python
