'''
Last Commit: 15.01.2014

@author: fraggle@phcn.de
'''

from abc import ABCMeta, abstractmethod

class Feature:
    __metaclass__ = ABCMeta
    
    @abstractmethod    
    def process(self, parameters):
        pass
    
    @abstractmethod
    def help(self):
        pass
    
    @abstractmethod
    def keyword(self):
        pass