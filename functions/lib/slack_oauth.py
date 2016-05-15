from slacker import Slacker


class SlackOAuth(object):
    def __init__(self, verification_token, client_id, client_secret, redirect_uri=None):
        self.slack = Slacker(verification_token)
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

    def authorize(self, code):
        return self.slack.oauth.access(self.client_id, self.client_secret, code, self.redirect_uri)


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
