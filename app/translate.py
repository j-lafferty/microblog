import json
import requests
import uuid
import os
from flask_babel import _
from app import app

def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in app.config or \
            not app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    subscription_key = app.config['MS_TRANSLATOR_KEY']
    endpoint = 'https://api.cognitive.microsofttranslator.com'
    path = '/translate?api-version=3.0'
    param = f'&from={source_language}&to={dest_language}'
    constructed_url = endpoint + path + param
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': 'westus2',
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
        }
    body = [{'text': text}]
    r = requests.post(constructed_url, headers=headers, json=body)
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    response = r.json()
    return response[0]['translations'][0]['text']
