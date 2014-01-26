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
            endpoint = 'http://5.gp/api/short?longurl=' + parameters[0]
            response = requests.get(endpoint, verify=False)

            data = json.loads(response.content)
        
            feature_response = 'v.ly URL => ' + data['url']
        else:
            feature_response = 'Sorry bro, URL is not valid :/'
              
        return feature_response

    def help(self):
        return 'vly <url> - v.ly url shortener\n'

    def keyword(self):
        return 'vly'