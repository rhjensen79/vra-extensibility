# Repo Update

Code Stream pipeline, to auto sync Gitub repositories, in vRealize Automation Cloud, when a comit is made to that repo, instead of waiting 15 minutes for a schelduled sync to happen.
![ID](https://github.com/rhjensen79/vra-extensibility/blob/master/Repo_Update/Screenshoots/pipeline.png)

## Pre-requisites

## Variables

The following variables must be setup in code Stream

- vra_api_token #Containing the VRA Api token to get the barer token
- Github_Token #Containing your github token, for the Git trigger to work.


## Pipeline Installation

- Create the variables in Code Stream
- Import the repo update.yml into codestream
- Change tasks, so they matches your projects.
- Find the ID for your sync tasks (Infrastructure -> Github -> Projects -> Your project)
![ID](https://github.com/rhjensen79/vra-extensibility/blob/master/Repo_Update/Screenshoots/id.png)

## Git trigger

- Make sure you have setup a git Endpoint first, for the Repo you want to use.

- Go to Git -> Webhooks for Git
- Select New
- Mine looks like this. The Secret token is gerated, from the UI. And for API token, i'm using my previus setup secret variable like this : ${var.Github_Token}
- I have also setup a REGEX, containing .yaml, to only trigger whe i make changed to .yaml files. But it's up to you, if you want to do the same.
- Pipeline is the importet Repo Update pipeline, from earlier.  
![ID](https://github.com/rhjensen79/vra-extensibility/blob/master/Repo_Update/Screenshoots/git_trigger.png)

If everyting is setup correct, then you will see, that everytime you do a comit, to your Github repo, and change .yaml files, then the sync will happen automaticly, and you won't have to wait for it to happen, like before.