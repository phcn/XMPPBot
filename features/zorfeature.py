'''
Last Commit: 27.01.2014

@author: fraggle@phcn.de
'''

from features.feature import Feature
import urllib.request
from bs4 import BeautifulSoup

class BotFeature(Feature):
    def process(self, parameters):
        zor_url = 'http://z0r.de/'
        flashloop_request = urllib.request.urlopen(zor_url)
        flashloop_response = flashloop_request.read()
        flashloop_request.close()

        soup = BeautifulSoup(flashloop_response)
        flashloop = soup.title.text.split('#')[0] + ' ' + zor_url + soup.title.text.split('#')[1]
        
        return flashloop

    def help(self):
        return 'z0r - zomg zufall!\n'

    def keyword(self):
        return 'z0r'