'''
Last Commit: 09.01.2014

@author: fraggle@phcn.de
'''

from features.botfeature import BotFeature
import feedparser
 
news_feeds = { 'prog' : 'http://www.reddit.com/r/programming/.rss',
               'comp' : 'http://www.reddit.com/r/compsci/.rss',
               'sec' : 'http://www.reddit.com/r/netsec/.rss' }

class FeedFeature(BotFeature):

    def process(self, parameters):
        if parameters[0] == 'info':
            supported_feeds = 'Supported Feeds:\n'
            for feed in news_feeds:
                supported_feeds += '"' + feed + '" - ' + news_feeds[feed] + '\n'
                
            return supported_feeds
        if parameters[0] in news_feeds:
            news_feed = feedparser.parse(news_feeds[parameters[0]])
            news_titles = 'News: \n'
             
            for item in news_feed['items']:
                news_titles += item['title'] + '\n';
            
            return news_titles         
        else:
            return self.help()
        
    def help(self):
        help_message =  'feed <newssite> - Use "info" to receive supported Feeds\n'
            
        return help_message