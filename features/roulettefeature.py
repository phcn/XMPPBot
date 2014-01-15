'''
Last Commit: 15.01.2014

@author: freak_out@phcn.de
'''

from features.feature import Feature
from random import randint
from array import *

class BotFeature(Feature):
    
    def __init__(self):
        self.__drum = array('i',[0,0,0,0,0,0])
        self.__chamber_counter = 0
        self.fillDrum()
        
    def process(self, parameters):
        returnstr=""
        
        if len(parameters) == 2:
            if self.__drum[self.__chamber_counter] == 0:
                returnstr = parameters[1]+" haelt sich den Revolver an sein Kopf und drueckt ab. +KLICK+ "+str(self.__chamber_counter)+"/5"
                self.__chamber_counter = self.__chamber_counter + 1
            else:
                returnstr = parameters[1]+" haelt sich den Revolver an sein Kopf und drueckt ab. +BOOOM+ HEADSHOT! "+str(self.__chamber_counter)+"/5"
                self.__drum[self.__chamber_counter]=0 # leere die Kammer
                self.fillDrum()
                self.__chamber_counter = 0
    

            return returnstr
        else:
            return self.help()
        
    def help(self):
        return 'roulette\n'
    
    def keyword(self):
        return 'roulette'
    
    def fillDrum(self):
        chamber = randint(0,5)
        self.__drum[chamber] = 1
