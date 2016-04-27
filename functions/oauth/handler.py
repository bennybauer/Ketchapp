import json
import logging
import os
import sys

log = logging.getLogger()
log.setLevel(logging.DEBUG)

here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "../lib"))
sys.path.append(os.path.join(here, "../vendored"))

from lib.slack_oauth import SlackOAuth
import requests


def handler(event, context):
    log.debug("Received event {}".format(json.dumps(event)))

    slack_oauth = SlackOAuth(os.getenv('SLACK_VERIFICATION_TOKEN'), os.getenv('SLACK_CLIENT_ID'),
                             os.getenv('SLACK_CLIENT_SECRET'), os.getenv('SLACK_CLIENT_REDIRECT_URI'))
    response = slack_oauth.oauth_access(event['code'])

    if response.body['ok']:
        access_token = response.body['access_token']
        user_id = response.body['user_id']
        incoming_webhook = response.body['incoming_webhook']
        incoming_webhook_url = incoming_webhook['url']
        channel_id = incoming_webhook['channel_id']
        channel_name = incoming_webhook['channel']
        configuration_url = incoming_webhook['configuration_url']
        team_id = response.body['team_id']
        team_name = response.body['team_name']

        log.debug("OAuth succeeded")

        # Send welcome message to user
        welcome_message = {"text": "Thanks for adding Ketchapp!"}
        requests.post(incoming_webhook_url, json=welcome_message)


        # Get user data
        # slack.users.

        # store user's token


    else:
        log.debug("OAuth failed {}".format(response.body['error']))

    # TODO: redirect to a nice app page - not possible yet in python lambda
    return "Success"
