from __future__ import print_function

import uuid
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

from lib.queue_handler import QueueHandler
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

    text = body['text'][0]
    user_id = body['user_id'][0]
    user_name = body['user_name'][0]
    return handle_command(text, user_id, user_name)


def handle_command(command, user_id, user_name):
    default_work_time = 10
    default_rest_time = 5

    if command is None or command == '':
        text = 'command is missing'
    elif command == 'start':
        text = 'Focus time, make the best of your next {} minutes.'.format(default_work_time)
        push_to_work_queue(command, user_id, user_name)
    elif command == 'pause':
        text = 'Sorry, no pausing for now :smirk:'
    elif command == 'stop':
        text = "Ok, let's take a brake"
        # TODO: implement deleting from queue
    elif command == 'rest':
        text = 'Rest time, you have {} minutes to do anything else but work!'.format(default_rest_time)
        push_to_rest_queue(command, user_id, user_name)
    else:
        text = '{} is invalid command'.format(command)

    return SlackResponseMessage(text).build()


def push_to_work_queue(command, user_id, user_name):
    return push_to_delayed_queue(os.getenv('WORK_QUEUE_NAME'), command, user_id, user_name)


def push_to_rest_queue(command, user_id, user_name):
    return push_to_delayed_queue(os.getenv('REST_QUEUE_NAME'), command, user_id, user_name)


def push_to_delayed_queue(queue_name, command, user_id, user_name):
    message = {'task_id': uuid.uuid4(), 'user_id': user_id, 'user_name': user_name, 'command': command}
    return QueueHandler.push_message(queue_name, message)
