# PHPipam
This repo contains PHPipam integration to vRealize Automation (VRA), using ABX Python actions
Note that I am in now way a programmer, so please use this for demo purpose only, and/or
reuse it in your own enviroment, for inspiration.

This i currently working with PHPipam 1.5. Earlier and future versions, might not work. 

The idea behind this, is to update PHPipam with data, from the deployment, after the VM is deployed,
and delete it again, when  the deployment get's removed.
So it acts more like a CMDB.

I know the real way to do this, is probably to request an ip from PHPipam, and the polulate the deployment, 
but it was not my usecase for this.
This should be easely done, by chaging the script, and api call, and make it a blocking task in VRA.

Here is an example of the end resoult, if everything is working as it should :-) 
![End Result](https://github.com/rhjensen79/vra-extensibility/blob/master/PHPipam/Screenshoots/End_Result.png)

## Links
[PHPipam offical site](https://phpipam.net)

[PHPipam official docker image](https://hub.docker.com/r/phpipam/phpipam-www)

[vRealize Automation](https://www.vmware.com/products/vrealize-automation.html)

## Postman 
Contains some Postman examples, to test the API.
There is both a Postman enviroment file, and a collection.

## ABX 
Contains the code, required to do the integration.
Zip the files, and import them into VRA, to use them, or just copy the code, into your own action.

## Screenshoots 
Contains screenshoots of different configurations.

## Docker
Docker Compose file, to run PHPipam.
Change all Passwords, hosts and path. All mentioned with !!!value!!!
Note this is the same as the public PHPipam Containers, just modified, to get access to the config
files in www container, to allow for HTTPconnections. 
The original can be found here : https://hub.docker.com/r/phpipam/phpipam-www
I use an external NFS server, to save all data from the containers. I recommend you do the same. 

The PHPipam container image, consist of 3 containers.
Web
Mariadb 
Cron

The Cron container, is set to  scan the subnets (if you turn it on) every 15 minutes. 
Note that the script is created, so if the ip is already  in use, it will be deleted, and a new entry will
be created, with the same ipadress, with the info from the deployment. 


## Custom
I have created a cusom field, that i polulate, from the VM deployment. 
It's required today, or else the script will fail. 
The idea behind this, is to have an app id input, for every request, so all applications can 
be easely tracket. This is created, with inspiration from a real customer usecase. 
![Custom Settings](https://github.com/rhjensen79/vra-extensibility/blob/master/PHPipam/Screenshoots/Custom_Field.png)


## Quick Guide

1. Deploy PHPipam and make sure API over http is allowed. (Guide will follow later)
   This can be done, by adding $api_allow_unsafe = true; to the end of config.docker.php in the 
   /phpipam-wwww data directory.
   Note this is only if you are using the docker-compose file, since the compose file don't allow port 443.
   For production use, please don't use this!

2. Create a PHPipam app and key

3. Update the ABX script, and import it into a new action og copy the code.

4. Create a subscription, and make sure the phpipam.py matches the event in the PHPipa function.

5. Make sure there is a tag in the VM deployment, with requestid (or else the script will fail)

I uses thee following in the input section :

```
requestid:
    type: string
    description: Request ID for approval
    title: Request ID
    default: 123456
```

With a tag in the VM section :

```
tags:
    - key: requestid
      value: '${input.requestid}'
```

6. Deploy a VM and test it. 


Hope you find it usefull. 
Please create an issue, if you find one, or/and reach out on [Twitter](https://twitter.com/rhjensen)

/Robert
