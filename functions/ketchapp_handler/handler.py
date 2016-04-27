from __future__ import print_function

import json
import logging
import os

log = logging.getLogger()
log.setLevel(logging.DEBUG)


def handler(event, context):
    log.debug("Received event {}".format(json.dumps(event)))
    slack_token = os.getenv('SLACK_VERIFICATION_TOKEN')

    response = """{
        "text": "Thanks for using Ketchapp",
        "attachments": [
            {
                "text":"We're still working on it"
            }
        ]
    }"""
    return response
