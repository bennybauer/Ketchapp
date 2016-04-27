from slacker import Slacker


class SlackOAuth(object):
    def __init__(self, verification_token, client_id, client_secret, redirect_uri=None):
        self.slack = Slacker(verification_token)
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

    def oauth_access(self, code):
        return self.slack.oauth.access(self.client_id, self.client_secret, code, self.redirect_uri)
