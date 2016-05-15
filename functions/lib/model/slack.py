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


class SlackOAuthResponse(object):
    def __init__(self, body):
        self.access_token = body['access_token']
        self.user_id = body['user_id']
        incoming_webhook = body['incoming_webhook']
        self.incoming_webhook_url = incoming_webhook['url']
        self.channel_id = incoming_webhook['channel_id']
        self.channel_name = incoming_webhook['channel']
        self.configuration_url = incoming_webhook['configuration_url']
        self.team_id = body['team_id']
        self.team_name = body['team_name']
