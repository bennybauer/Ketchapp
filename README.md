# Ketchapp ![](./assets/food.png | width=70)
Your [Pomodoro](http://pomodorotechnique.com/) mentor! 


Ketchapp helps your focus to catch up with your work.

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

	git clone https://git.autodesk.com/bauerb/monitor-test

Add .env file to root folder:

```
SERVERLESS_STAGE=dev
SERVERLESS_DATA_MODEL_STAGE=dev
SERVERLESS_PROJECT_NAME=monitor-test
```

Add admin.env file to root folder (get staging credentials from 1Password):

```
SERVERLESS_ADMIN_AWS_ACCESS_KEY_ID=
SERVERLESS_ADMIN_AWS_SECRET_ACCESS_KEY=
```


Create the dependencies packages:

```
cd functions
pip install -t vendored/ -r requirements.txt
```

Deploy it!

	sls dash deploy





*Ketcup icon was made by freepik from [www.flaticon.com](http://www.flaticon.com/free-icon/ketchup-bottle_34603)*
