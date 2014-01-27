'''
Last Commit: 27.01.2014

@author: fraggle@phcn.de
'''

from features.feature import Feature
import urllib.request
from bs4 import BeautifulSoup

class BotFeature(Feature):
    def process(self, parameters):
        reverse_md5_url = 'http://md5.noisette.ch/md5.php?hash=' + parameters[0]
        reverse_md5_request = urllib.request.urlopen(reverse_md5_url)
        reverse_md5_response = reverse_md5_request.read()
        reverse_md5_request.close()

        xml_response = BeautifulSoup(reverse_md5_response.decode('utf-8'))
        hash_list = xml_response.find_all('string')

        if len(hash_list) > 0:
            feature_response = parameters[0] + ' == ' + hash_list[0].text
        else:
            error = xml_response.find_all('error')
            feature_response = error[0].text
        
        return feature_response

    def help(self):
        return 'rmd5 - reverse md5 lookup (powered by md5.noisette.ch)\n'

    def keyword(self):
        return 'rmd5'