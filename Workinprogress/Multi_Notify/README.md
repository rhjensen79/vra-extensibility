# Multi Notify

A development, from the Slack notification action.
The idea here, is to have one action, that support notifications in as many different platforms, as possible.

Currently it's planned for the following platforms.

- Slack
- Email
- Telegram
- Ms Teams

Let me know if more are needed, and if you are able to help. 

## Pre-requisites

## Inputs
Required inputs
- slack_webhook
- telegram_token
- telegram_chatid
- smtp_port
- smtp_sender_email
- smtp_server
- smtp_username
- smtp_password

### Telegram
- Create bot (type /newbot @BotFather) and save token.
- Create group
- Add bot to group as admin.
- Get group id (https://api.telegram.org/bot<YourBOTToken>/getUpdates) and save it. 
More info can be found here : https://core.telegram.org/api

### Email
Email have been tested with AWS Simple Email service, but should work with 
all smtp servers. 

