'''
Last Commit: 01.02.2014

@author: fraggle@phcn.de
'''

from features.feature import Feature
import feedparser
 
news_feeds = { 'prog' : 'http://www.reddit.com/r/programming/.rss',
               'comp' : 'http://www.reddit.com/r/compsci/.rss',
               'sec' : 'http://www.reddit.com/r/netsec/.rss',
               'heise' : 'http://heise.de.feedsportal.com/c/35207/f/653902/index.rss',
               'golem' : 'http://rss.golem.de/rss.php?feed=ATOM1.0',
               'sploitdb' : 'http://www.exploit-db.com/rss.xml',
               'netzpol' : 'https://netzpolitik.org/feed/',
               'fefe' : 'http://blog.fefe.de/rss.xml?html',
               'phcn' : 'https://board.phcn.net/index.php?action=.xml;type=rss', 
               'ntv' : 'http://www.n-tv.de/rss',
               'spon' : 'http://www.spiegel.de/schlagzeilen/tops/index.rss',
               'zeit' : 'http://newsfeed.zeit.de/index'}

class BotFeature(Feature):

    def process(self, parameters):
        if parameters[0] == 'info':
            supported_feeds = 'Supported Feeds:\n'
            for feed in news_feeds:
                supported_feeds += '"' + feed + '" - ' + news_feeds[feed] + '\n'
                
            return supported_feeds
        if parameters[0] in news_feeds:
            news_feed = feedparser.parse(news_feeds[parameters[0]])
            news_titles = 'News: \n'
             
            for item in news_feed.entries[:5]:
                news_titles += item['title'] + ": " + item['link'] + '\n';
            
            return news_titles         
        else:
            return self.help()
        
    def help(self):
        return 'feed <newssite> - use "info" to receive supported Feeds\n'

        
    def keyword(self):
        return 'feed'