import json
import os
import uuid
import boto
import time
import logging

from boto.sqs.message import RawMessage

__author__ = 'bauerb'

log = logging.getLogger()
log.setLevel(logging.DEBUG)


class QueueHandler(object):
    @staticmethod
    def push_message(queue, message):
        data = {
            'submitdate': time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime()),
            'key': str(uuid.uuid1()),
            'message': str(message)
        }

        # Connect to SQS and open the queue
        conn = boto.sqs.connect_to_region(os.getenv('SERVERLESS_REGION'), aws_access_key_id=os.getenv('AWS_KEY'),
                                          aws_secret_access_key=os.getenv('AWS_SECRET'))
        q = conn.get_queue(queue)

        # Put the message in the queue
        m = RawMessage()
        m.set_body(json.dumps(data))
        log.debug("Pushing message {} to queue {}".format(data['key'], queue))
        status = q.write(m)

        return status
