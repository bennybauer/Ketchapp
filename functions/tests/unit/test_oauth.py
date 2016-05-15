from unittest import TestCase

from lib.model.slack import SlackOAuthResponse

__author__ = 'bauerb'


class TestHandler(TestCase):
    def create_valid_response(self):
        return {
            "body": {
                "access_token": "xoxp-XXXXXXXX-XXXXXXXX-XXXXX",
                "user_id": "usXX-XXXXXXXX-XXXXXXXX-XXXXX",
                "team_name": "Team Installing Your Hook",
                "team_id": "XXXXXXXXXX",
                "incoming_webhook": {
                    "url": "https://hooks.slack.com/TXXXXX/BXXXXX/XXXXXXXXXX",
                    "channel": "#channel-it-will-post-to",
                    "channel_id": "XXX-YYY",
                    "configuration_url": "https://teamname.slack.com/services/BXXXXX"
                }
            }
        }

    def create_invalid_response(self):
        return {
            "body": {
                "user_id": "usXX-XXXXXXXX-XXXXXXXX-XXXXX",
                "team_name": "Team Installing Your Hook",
                "team_id": "XXXXXXXXXX",
                "incoming_webhook": {
                    "channel": "#channel-it-will-post-to",
                    "channel_id": "XXX-YYY",
                    "configuration_url": "https://teamname.slack.com/services/BXXXXX"
                }
            }
        }

    def test_handle_valid_auth_response_body(self):
        response = self.create_valid_response()
        SlackOAuthResponse(response['body'])

    def test_handle_invalid_auth_response_body(self):
        response = self.create_invalid_response()
        with self.assertRaises(KeyError):
            SlackOAuthResponse(response['body'])
