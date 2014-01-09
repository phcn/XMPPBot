'''
Last Commit: 09.01.2014

@author: board.phcn.net
'''

import sleekxmpp
from features.feedfeature import FeedFeature

class MUCBot(sleekxmpp.ClientXMPP):
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
        if msg['mucnick'] != self.nick and self.nick in msg['body']:
            feature_parameters = msg['body'].split()
            feature_parameters.pop(0)
            feature_command = feature_parameters.pop(0)
            
            if feature_command in features:
                if feature_command in msg['body']:
                    feature_response = features[feature_command].process(feature_parameters)
            else:
                feature_response = 'Unknown Feature "' + feature_command + '"\n'
                feature_response += help_messages
        
            self.send_message(mto=msg['from'].bare, mbody=feature_response, mtype='groupchat')


if __name__ == '__main__':
    jid = "bot@phcn.de"
    password = "botpassword"
    room = "chatroom@conference.phcn.de"
    nick = "roomnick"
    
    features = {'feed' : FeedFeature() }
    
    help_messages = 'XMPP-ChatBot Features: \n'
    
    for feature in features:
        help_messages += features[feature].help(); 

    xmpp = MUCBot(jid, password, room, nick)
    xmpp.register_plugin('xep_0030') # Service Discovery
    xmpp.register_plugin('xep_0045') # Multi-User Chat
    xmpp.register_plugin('xep_0199') # XMPP Ping


    if xmpp.connect():
        xmpp.process(block=True)
        print("Done")
    else:
        print("Unable to connect.")