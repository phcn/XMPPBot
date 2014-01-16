'''
Last Commit: 16.01.2014

@author: freak_out@phcn.de
'''

from features.feature import Feature

class BotFeature(Feature):    

    def __init__(self):
        self.__imbiss = {}
        self.__imbiss_file = open("features/imbiss.txt","r")
        
        for line in self.__imbiss_file:
            food = line.split(',')
            self.__imbiss[food[0].lower()] = food[1]
        
    def process(self, parameters):
        if len(parameters) == 2:
            food = "Imbiss Speisekarte: \n"
            for key in self.__imbiss:
                food += key + "\n"
            return food[:-1]

        if len(parameters) == 3:
            imbissitem = parameters[0].lower().encode('utf-8')

            if imbissitem in self.__imbiss:
                return  '*** ' + parameters[1] + ' ' + self.__imbiss[imbissitem][:-1] + ' ' + parameters[2]
            else:
                return 'Ham wa nit'
        else:
            return self.help()
                        
    
    def help(self):
        return 'imbiss <food> - get food, type imbiss only for list of available food\n'

    def keyword(self):
        return 'imbiss'