'''
Last Commit: 01.02.2014

@author: board.phcn.net
'''

import os
import imp 
import sys
import sleekxmpp
import configparser
import megahal
    

def log_debug(message):
    print('DEBUG: ' + message)
    pass
def log_error(message):
    print('ERROR: ' + message)
    pass
    
def feature_import(feature_sections):
    features = {}
    help_messages = 'XMPP-ChatBot Features: \n'
     
    for feature in feature_sections:        
        try:
            uri = os.path.normpath(os.path.join(os.path.dirname(__file__), feature.strip()))
            module_name = os.path.splitext(os.path.split(uri)[1])[0]     
            feature_module = imp.load_source(module_name, uri)
            feature_instance = feature_module.BotFeature()
            features[feature_instance.keyword()] = feature_instance
            help_messages += feature_instance.help(); 
        except:
            e = sys.exc_info()[0]
            log_error('Could not load module ' + module_name)
            log_debug(str(e))
    
    return features, help_messages


class XMPPBot(sleekxmpp.ClientXMPP):
    def __init__(self, jid, password, room, nick):
        sleekxmpp.ClientXMPP.__init__(self, jid, password)

        self.room = room
        self.nick = nick
        self.add_event_handler('session_start', self.start)
        self.add_event_handler('groupchat_message', self.muc_message)



    def start(self, event):
        self.plugin['xep_0045'].joinMUC(self.room,
                                        self.nick,
                                        # If a room password is needed, use:
                                        # password=the_room_password,
                                        wait=True)

    def muc_message(self, msg):        
        mega_hal.learn(msg['body'])

        if msg['mucnick'] != self.nick and \
           (self.nick in msg['body'].split(' ')[0][:-1] or\
           self.nick in msg['body'].split(' ')[0]):

            feature_parameters = msg['body'].split()
            feature_parameters.pop(0)
			
            feature_command = ''
            # check for empty parameters (otherwise -> IndexError: pop from empty list)
            if feature_parameters:
                feature_command = feature_parameters.pop(0)
            
            if feature_command in features:
                if feature_command in msg['body']:
                    feature_parameters.append(self.nick)
                    feature_parameters.append(msg['mucnick'])
                    feature_response = features[feature_command].process(feature_parameters)
            elif feature_command == 'help':
                feature_response = help_messages
			# this needs to be processed in a separate function/class
            elif feature_command == 'quit' and msg['from'] in administrators:
                feature_response = 'bye!'
                self.disconnect(wait=True)
            else:
                feature_response = mega_hal.get_reply(msg['body']).replace(self.nick,msg['mucnick'])

            self.send_message(mto=msg['from'].bare, mbody=feature_response, mtype='groupchat')


if __name__ == '__main__':     
    config = configparser.ConfigParser()
    config.read('bot.cfg')

    features, help_messages = feature_import(config.get('Features','featurepaths').split(';'))
    administrators = config.get('Administrators','jabberids').replace('\n','').split(';')

    jabber_id = config.get('XMPP', 'jabberid')
    password = config.get('XMPP', 'password')
    room = config.get('XMPP', 'room')
    nick_name = config.get('XMPP', 'nickname')
    
    xmpp = XMPPBot(jabber_id, password, room, nick_name)
    xmpp.register_plugin('xep_0030') # Service Discovery
    xmpp.register_plugin('xep_0045') # Multi-User Chat
    xmpp.register_plugin('xep_0199') # XMPP Ping
    
    mega_hal = megahal.MegaHAL()

    if xmpp.connect():
        xmpp.process(block=True)
        print('Done')
    else:
        print('Unable to connect.')
        
    print('bye!')
    
    mega_hal.sync()
    mega_hal.close()