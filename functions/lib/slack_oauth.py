from slacker import Slacker


class SlackOAuth(object):
    def __init__(self, verification_token, app_id, app_secret, redirect_uri=None):
        self.slack = Slacker(verification_token)
        self.app_id = app_id
        self.app_secret = app_secret
        self.redirect_uri = redirect_uri

    def authorize(self, code):
        return self.slack.oauth.access(self.app_id, self.app_secret, code, self.redirect_uri)
