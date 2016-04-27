import json

__author__ = 'bauerb'

import logging

log = logging.getLogger()
log.setLevel(logging.DEBUG)


class Slack(object):
    def __init__(self):
        return

        # def send_error(self, error, message):
        #     log.debug("Error: {}. Message: {}".format(error, message);
        #       return context.done(null, {
        #         response_type: in_channel ? 'in_channel' : 'ephemeral',
        #         text: message
        #       });


class SlackResponseMessage(object):
    def __init__(self, text):
        self.text = text

    def build(self):
        return {'text': self.text}
