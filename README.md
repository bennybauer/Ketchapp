# Ketchapp <img src="./assets/food.png" width="70"/>
[![](https://travis-ci.org/bennybauer/Ketchapp.svg?branch=master)](https://travis-ci.org/bennybauer/Ketchapp)


Your [Pomodoro](http://pomodorotechnique.com/) mentor! Ketchapp is a Slack app that helps your focus to catch up with your work.

<a href="https://slack.com/oauth/authorize?scope=incoming-webhook,commands&client_id=2778138625.38014984439"><img alt="Add to Slack" height="40" width="139" src="https://platform.slack-edge.com/img/add_to_slack.png" srcset="https://platform.slack-edge.com/img/add_to_slack.png 1x, https://platform.slack-edge.com/img/add_to_slack@2x.png 2x" /></a>

## Development
Install Node.js

	brew install node

Install Serverless

	npm install -g serverless
	
Create serverless project
	
	sls project create
	
![](./assets/ketchapp1.jpg)

Create serverless function
	
	sls function create functions/ketchapp_handler
![](./assets/ketchapp2.jpg)

Implement it and deploy

	sls dash deploy
![](./assets/ketchapp3.jpg)



## Usage
Install Node.js

	brew install node

Install Serverless

	npm install -g serverless

Clone this repository

	git clone https://github.com/bennybauer/Ketchapp.git
	
[Set up](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html#cli-config-files) your AWS credentials

Add admin.env file to root folder with:

```
AWS_DEV_PROFILE=<your aws profile>
```

Add `s-variables-common.json` file to `_meta/variables` folder:

```
{
  "project": "ketchapp",
  "slackAppName": "Ketchapp",
  "slackVerificationToken": "<your_verification_token>",
  "slackAppId": "<your_app_id>",
  "slackAppSecret": "<your_secret>",
  "slackAppRedirectUri": "</slack-oauth lambda url>"
  "slackAppWelcomePage": "<app_welcome_page>"
}
```


Create the dependencies packages:

```
pip install -t functions/vendored/ -r requirements.txt
```

Deploy it!

	sls dash deploy


###Credits###
*Ketchup icon was made by freepik from [www.flaticon.com](http://www.flaticon.com/free-icon/ketchup-bottle_34603)*
