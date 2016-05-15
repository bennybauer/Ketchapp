#!/usr/bin/python
import json
import os
import unittest

from lib.slack_oauth import SlackOAuth

__author__ = 'bauerb'


class TestSlackOAuthIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        here = os.path.dirname(os.path.realpath(__file__))
        vars_file_path = os.path.join(here, "../../../_meta/variables/s-variables-common.json")
        cls.load_env_vars_from_json(vars_file_path)

    def test_invalid_client_id(self):
        slack_oauth = SlackOAuth('token', 'app_id', 'app_secret')
        with self.assertRaises(Exception) as e:
            slack_oauth.authorize('123123')

        self.assertEquals('invalid_client_id', e.exception.message)

    def test_invalid_client_secret(self):
        slack_oauth = SlackOAuth('token', os.environ['SLACK_APP_ID'], 'app_secret')
        with self.assertRaises(Exception) as e:
            slack_oauth.authorize('123123')

        self.assertEquals('bad_client_secret', e.exception.message)

    def test_invalid_code(self):
        slack_oauth = SlackOAuth('token', os.environ['SLACK_APP_ID'], os.environ['SLACK_APP_SECRET'])
        with self.assertRaises(Exception) as e:
            slack_oauth.authorize('123123')

        self.assertEquals('invalid_code', e.exception.message)

    @staticmethod
    def load_env_vars_from_json(path):
        if not os.path.isfile(path):
            print "Warning: %s doesn't exist" % path
            return

        with open(path) as vars_file:
            vars_data = json.load(vars_file)

        os.environ['SLACK_VERIFICATION_TOKEN'] = vars_data['slackVerificationToken']
        os.environ['SLACK_APP_ID'] = vars_data['slackAppId']
        os.environ['SLACK_APP_SECRET'] = vars_data['slackAppSecret']
        os.environ['SLACK_APP_REDIRECT_URI'] = vars_data['slackAppRedirectUri']
