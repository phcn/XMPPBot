'''
Last Commit: 10.01.2014

@author: fraggle@phcn.de
'''

from features.botfeature import BotFeature

class BeerFeature(BotFeature):
    
    def process(self, parameters):
        if len(parameters) == 2:
            return '*** ' + parameters[0] + ' geht zum Kuehlschrank und holt eine kalte Flasche Bier heraus und ueberreicht sie ' + parameters[1]
        else:
            return self.help()
        
    def help(self):
        return 'beer - Have no fear of ice cold Beer!\n'