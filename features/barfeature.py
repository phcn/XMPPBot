'''
Last Commit: 15.01.2014

@author: freak_out@phcn.de
'''

from features.feature import Feature

class BotFeature(Feature):
    global minibar
    minibar = {}

    minibar_file = open("features/minibar.txt","r")
        
    for line in minibar_file:
        drink = line.split(',')
        minibar[drink[0].lower()] = drink[1]
    

    def process(self, parameters):
            
        if len(parameters) == 2:
            drinks = "Inhalt der Bar: \n"
            for key in minibar:
                drinks += key + "\n"
            return drinks[:-1]

        if len(parameters) == 3:
            baritem = parameters[0].lower()
            if baritem in minibar:
                return  '*** ' + parameters[1] + ' ' + minibar[baritem][:-1] + ' ' + parameters[2]
            else:
                return 'Ham wa nit'
                    
                    
        else:
            return self.help()
                        
    
    def help(self):
        return 'bar <drink> - get a drink\nbar - list of drinks\n'
    
    def keyword(self):
        return 'bar'
