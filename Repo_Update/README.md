# Repo Update

Code Stream pipeline, to auto sync Gitub repositories, when a comit is made to that repo, instead of waiting 15 minutes for a achelduled sync.
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

Guide will follow soon.