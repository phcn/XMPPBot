'''
Last Commit: 01.02.2014

@author: freak_out@phcn.de
'''

from features.feature import Feature

class BotFeature(Feature):
    
    def __init__(self):
        self.__minibar = {}
        self.__minibar_file = open('features/minibar.txt','r', encoding='utf-8')
        
        for line in self.__minibar_file:
            drink = line.split(',')
            self.__minibar[drink[0].lower()] = drink[1]
    
    def process(self, parameters):
        if len(parameters) == 2:
            drinks = 'Inhalt der Bar: \n'
            for key in self.__minibar:
                drinks += key + '\n'
            return drinks[:-1]

        if len(parameters) == 3:
            baritem = parameters[0].lower()
            if baritem in self.__minibar:
                return  '*** ' + parameters[1] + ' ' + self.__minibar[baritem][:-1] + ' ' + parameters[2]
            else:
                return 'Ham wa nit'     
        else:
            return self.help()
                        
    
    def help(self):
        return 'bar <drink> - get a drink, type bar only for list of available drinks\n'
    
    def keyword(self):
        return 'bar'
