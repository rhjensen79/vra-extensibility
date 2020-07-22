# Active Directory Update

Creates a Computer account at deployment, and removes it again, when the VM gets removed. 

Note that Winrm, neeeds to be enabled on the target VM, and pywinrm needs to be set, in the dependencicy on the ABX action container. 

![Dependency](https://github.com/rhjensen79/vra-extensibility/blob/master/AD_Update/Screenshoots/dependency.png)

Remember to change username and password in the script. 