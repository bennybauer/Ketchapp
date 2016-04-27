from __future__ import print_function
from urlparse import parse_qs

import os
import sys
import json
import logging

log = logging.getLogger()
log.setLevel(logging.DEBUG)

here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "../lib"))
sys.path.append(os.path.join(here, "../vendored"))

from lib.model.slack import SlackResponseMessage


def handler(event, context):
    log.debug("Received event {}".format(json.dumps(event)))

    body = parse_qs(event['body'], 1)

    if body['token'][0] != os.getenv('SLACK_VERIFICATION_TOKEN'):
        error = "Error: {}. Message: {}".format('Access denied', 'Invalid token')
        log.debug(error)
        return error

    if not body['text']:
        error = "Error: {}. Message: {}".format('Bad Request', 'Command is missing')
        log.debug(error)
        return SlackResponseMessage(error).build()

    return handle_command(body['text'][0])


def handle_command(command):
    default_work_time = 10
    default_rest_time = 5

    if command is None or command == '':
        text = 'command is missing'
    elif command == 'start':
        text = 'Focus time, make the best of your next {} minutes.'.format(default_work_time)
    elif command == 'pause':
        text = 'Sorry, no pausing for now :smirk:'
    elif command == 'stop':
        text = "Ok, let's take a brake"
    elif command == 'rest':
        text = 'Rest time, you have {} minutes to do anything else but work!'.format(default_rest_time)
    else:
        text = '{} is invalid command'.format(command)

    return SlackResponseMessage(text).build()
