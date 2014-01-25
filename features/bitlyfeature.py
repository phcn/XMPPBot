'''
Last Commit: 25.01.2014

@author: fraggle@phcn.de
'''

from features.feature import Feature
from lepl.apps.rfc3696 import HttpUrl
import requests
import json

class BotFeature(Feature):
    def __init__(self):
        self.__url_validator = HttpUrl()
        
    def process(self, parameters):
        feature_response = ''
        
        if self.__url_validator(parameters[0]):
            query_params = {'access_token' : 'your-access-token',
                            'longUrl': parameters[0]} 

            endpoint = 'https://api-ssl.bitly.com/v3/shorten'
            response = requests.get(endpoint, params=query_params, verify=False)

            data = json.loads(response.content)
        
            feature_response = 'bit.ly URL => ' + data['data']['url']
        else:
            feature_response = 'Sorry bro, URL is not valid :/'
              
        return feature_response

    def help(self):
        return 'bitly <url> - bit.ly url shortener\n'

    def keyword(self):
        return 'bitly'
