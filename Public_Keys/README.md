# Public Keys

Get public keys, from Github, based on the requester.
All deployments, with this subscription, will get a Github property attached, but it will not be used, 
unless you specify it in the blueprint. 

## Pre Req

### Add your public keys to your Github Account.

1. Go to Github.com and login
2. Select your profile
3. Select SSH and GPG keys
4. Add new SSH key.
5. Give it a title and paste your public key
6. Verify your key is avaliable, by going to https://github.com/username.keys

### Image

1. Image must be cloud-init enabled, running Linux (Don't know if/how this is possible with Windows)

### Extensibility

1. Create a action, with the content from public_key.py
2. Add the requesters email and github username, to the users list, to match requester, with github username. 
3. Create a subscription, for projects you want to use, with 
Event Topic : Compute Alloation
Blocking : Enabled

### Bleuprint

Must contain the runcmd: bash code, from the blueprint.yaml file.