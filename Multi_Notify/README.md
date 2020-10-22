# Multi Notify

An upgrade, from the Slack notification action.
The idea here, is to have one action, that support notifications in as many different platforms, as possible.

Currently it's working for the following platforms.

- Slack
- Email
- Telegram
- Ms Teams

Currently it's working, by manualily defining whick kind of notification you want. 
on my todo list is
- Input from blueprint, to chose notification method
- Error handling
- change to apprise plugin

Let me know if more are needed, and if you are able to help. 

## Pre-requisites

## Blueprint
In my blueprints, i have a input that looks like this : 

```
notify:
    type: boolean
    description: Notify when deployment is finished
    default: true
    title: Notify
```

And in each VM, where i wan't notification i have the following :
```
notify: '${input.notify}'
```

Note this can be a static value, if you want to be notified everytime, without allowing the user to select it. 

## Inputs
Required inputs (for the message type you want to use).
- slack_webhook
- telegram_token
- telegram_chatid
- smtp_port
- smtp_sender_email
- smtp_server
- smtp_username
- smtp_password
- teams_webhook

## Dependency
- requests

### Telegram
- Create bot (type /newbot @BotFather) and save token.
- Create group
- Add bot to group as admin.
- Get group id (https://api.telegram.org/bot<YourBOTToken>/getUpdates) and save it. 
More info can be found here : https://core.telegram.org/api

### Email
Email have been tested with AWS Simple Email service, but should work with 
all smtp servers. 
Guide on how to setup will come later.

### MS Teams
Add an incoming webhook to a Teams channel:

- Navigate to the channel where you want to add the webhook and select (•••) More Options from the top navigation bar.
- Choose Connectors from the drop-down menu and search for Incoming Webhook.
- Select the Configure button, provide a name, and, optionally, upload an image avatar for your webhook.
- The dialog window will present a unique URL that will map to the channel. Make sure that you copy and save the URL—you will need to provide it to the outside service.
- Select the Done button. The webhook will be available in the team channel.

### Slack
- Create Slack webhook. 
link etc will come later. 