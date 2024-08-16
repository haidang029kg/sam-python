import json

import requests


def lambda_handler(event, context):

    try:
        ip = requests.get("http://checkip.amazonaws.com/")
        print(ip.text)
        print(ip.text)
        print(ip.text)
        print(ip.text)
        print(ip.text)
    except requests.RequestException as e:
        # Send some context about this error to Lambda Logs
        print(e)
        raise e

