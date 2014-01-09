'''
Last Commit: 09.01.2014

@author: fraggle@phcn.de
'''

from abc import ABCMeta, abstractmethod

class BotFeature:
    __metaclass__ = ABCMeta
    
    @abstractmethod    
    def process(self, parameters):
        pass
    
    @abstractmethod
    def help(self):
        pass