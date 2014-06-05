'''
Last Commit: 01.02.2014

@author: freak_out@phcn.ws
'''

from features.feature import Feature
from random import randint
from array import *

class BotFeature(Feature):
  
    def rotateDrum(self):
        self.__chamber = randint(0,4)
        print(self.__chamber)
        
  
    def __init__(self):
        self.__drum = array('i',[0,0,0,0,0])
        self.fillDrum()
        
    def process(self, parameters):
        returnstr=''
        
        if len(parameters) == 2:
            self.rotateDrum()
            if self.__drum[self.__chamber] == 0:
                returnstr = parameters[1]+' dreht die Trommel und haelt sich den Revolver an sein Kopf und drueckt ab. +KLICK+ '
            else:
                returnstr = parameters[1]+' dreht die Trommel und haelt sich den Revolver an sein Kopf und drueckt ab. +BOOOM+ HEADSHOT! '
                self.__drum[self.__chamber]=0
                self.fillDrum()
                self.__chamber = 0
    

            return returnstr
        else:
            return self.help()

  
        
    def help(self):
        return 'roulette - play russian roulette! :)\n'
    
    def keyword(self):
        return 'roulette'
    
    def fillDrum(self):
        chamber = randint(0,4)
        self.__drum[chamber] = 1
