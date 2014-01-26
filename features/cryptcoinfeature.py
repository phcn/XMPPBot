'''
Last Commit: 26.01.2014

@author: puddy@phcn.de
'''

from features.feature import Feature
import json
import urllib2

class BotFeature(Feature):
     
    def process(self, parameters):
        rates = {}
        content = urllib2.urlopen("https://localbitcoins.com/bitcoinaverage/ticker-all-currencies/").read()
        data = json.loads(content)
        
        rates['USD/BTC'] = data['USD']['avg_3h']
        rates['mBTC/USD'] = round(data['USD']['avg_3h'] / 1000, 2)
        rates['EUR/BTC'] = data['EUR']['avg_3h']
        rates['mBTC/EUR'] = round(data['EUR']['avg_3h'] / 1000, 2)
        content = urllib2.urlopen("https://btc-e.com/api/2/ppc_usd/ticker").read()
        data = json.loads(content)
        
        rates['USD/PPC'] = data['ticker']['avg']
        returnstring = "\nUSD/BTC: %.2f\tmBTC/USD: %.2f" % (rates['USD/BTC'], rates['mBTC/USD'])
        returnstring += "\nEUR/BTC: %.2f\tmBTC/EUR: %.2f" % (rates['EUR/BTC'], rates['mBTC/EUR'])
        returnstring += "\nUSD/PPC: %.2f " % rates['USD/PPC']
        
        return ("Current rates:" + returnstring)

    # a short feature description.
    def help(self):
        return 'coinrates - get various rates.\n'

    # the keyword this feature is triggerd by.
    def keyword(self):
        return 'coinrates'