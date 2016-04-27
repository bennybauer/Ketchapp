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


def handler(event, context):
    log.debug("Received event {}".format(json.dumps(event)))
    code = event.get('code')
    log.debug("Code: {}".format(code))

    slack_oauth = SlackOAuth(os.getenv('SLACK_VERIFICATION_TOKEN'), os.getenv('SLACK_CLIENT_ID'),
                             os.getenv('SLACK_CLIENT_SECRET'), os.getenv('SLACK_CLIENT_REDIRECT_URI'))
    response = slack_oauth.oauth_access(code)

    if response.body['ok']:
        access_token = response.body['access_token']
        log.debug("OAuth succeeded")

        # Get user data
        # slack.users.

        # store user's token
    else:
        log.debug("OAuth failed {}".format(response.body['error']))

    return response.body
