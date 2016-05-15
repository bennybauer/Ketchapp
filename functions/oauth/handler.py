import json
import logging
import os
import sys

log = logging.getLogger()
log.setLevel(logging.DEBUG)

here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "../lib"))
sys.path.append(os.path.join(here, "../vendored"))

from lib.slack_oauth import SlackOAuth, SlackOAuthResponse
import requests


def handle_auth_response(response):
    if response.successful:
        try:
            slack_oauth_response = SlackOAuthResponse(response.body)
        except KeyError as key_error:
            log.debug("Invalid OAuth response, missing {}".format(key_error.message))
            raise key_error

        log.debug("OAuth succeeded for user_id {} from team {} (id {})".format(slack_oauth_response.user_id,
                                                                               slack_oauth_response.team_name,
                                                                               slack_oauth_response.team_id))

        # Send welcome message to user
        welcome_message = {"text": "Thanks for adding Ketchapp!"}
        requests.post(slack_oauth_response.incoming_webhook_url, json=welcome_message)

        # Get user data
        # slack.users.

        # store user's token

        return True

    else:
        log.debug("OAuth failed {}".format(response.error))
        return False


def handler(event, context):
    log.debug("Received event {}".format(json.dumps(event)))

    slack_oauth = SlackOAuth(os.getenv('SLACK_VERIFICATION_TOKEN'), os.getenv('SLACK_CLIENT_ID'),
                             os.getenv('SLACK_CLIENT_SECRET'), os.getenv('SLACK_CLIENT_REDIRECT_URI'))
    response = slack_oauth.authorize(event['code'])

    if handle_auth_response(response):
        # TODO: redirect to a nice app page - not possible yet in python lambda
        return "Success"
    else:
        return "Failure"
