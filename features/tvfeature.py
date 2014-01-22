'''
Last Commit: 22.01.2014

@author: fraggle@phcn.de
'''

from features.feature import Feature
import urllib2
from bs4 import BeautifulSoup

class BotFeature(Feature):
    def process(self, parameters):
        klack_connection = urllib2.urlopen('http://www.klack.de/fernsehprogramm/was-laeuft-gerade/0/-1/free.html')
        html_file = klack_connection.read()
        klack_connection.close()

        soup = BeautifulSoup(html_file)
        broadcast_table = soup.find("table", attrs={"class":"broadcasts"})

        tv_program = self.parse_broadcast_table(broadcast_table, 'evenRow')
        tv_program.update(self.parse_broadcast_table(broadcast_table, 'oddRow'))
            
        program_response = '\nRTL:     Seit ' + tv_program['rtl'][2] + ' \"' + tv_program['rtl'][0] + '\" => \"' + tv_program['rtl'][1] + '\" ab ' + tv_program['rtl'][3] + '\n'   
        program_response += 'Sat1:    Seit ' + tv_program['sat.1'][2] + ' \"' + tv_program['sat.1'][0] + '\" => \"' + tv_program['sat.1'][1] + '\" ab ' + tv_program['sat.1'][3] + '\n'  
        program_response += 'Pro7:    Seit ' + tv_program['pro7'][2] + ' \"' + tv_program['pro7'][0] + '\" => \"' + tv_program['pro7'][1] + '\" ab ' + tv_program['pro7'][3] + '\n'
        program_response += 'ARD:     Seit ' + tv_program['ard'][2] + ' \"' + tv_program['ard'][0] + '\" => \"' + tv_program['ard'][1] + '\" ab ' + tv_program['ard'][3] + '\n'
        program_response += 'VOX:     Seit ' + tv_program['vox'][2] + ' \"' + tv_program['vox'][0] + '\" => \"' + tv_program['vox'][1] + '\" ab ' + tv_program['vox'][3] + '\n'
        program_response += 'N24:     Seit ' + tv_program['n24'][2] + ' \"' + tv_program['n24'][0] + '\" => \"' + tv_program['n24'][1] + '\" ab ' + tv_program['n24'][3] + '\n'
        program_response += 'N-TV:    Seit ' + tv_program['n-tv'][2] + ' \"' + tv_program['n-tv'][0] + '\" => \"' + tv_program['n-tv'][1] + '\" ab ' + tv_program['n-tv'][3] + '\n'
        program_response += 'Phoenix: Seit ' + tv_program['phoenix'][2] + ' \"' + tv_program['phoenix'][0] + '\" => \"' + tv_program['phoenix'][1] + '\" ab ' + tv_program['phoenix'][3] + '\n'
        program_response += 'Kabel1:  Seit ' + tv_program['kabeleins'][2] + ' \"' +tv_program['kabeleins'][0] + '\" => \"' + tv_program['kabeleins'][1] + '\" ab ' + tv_program['kabeleins'][3] + '\n'
        program_response += 'Orf1:    Seit ' + tv_program['orf1'][2] + ' \"' + tv_program['orf1'][0] + '\" => \"' + tv_program['orf1'][1] + '\" ab ' + tv_program['orf1'][3] + '\n'
        program_response += 'RTL2:    Seit ' + tv_program['rtlii'][2] + ' \"' + tv_program['rtlii'][0] + '\" => \"' + tv_program['rtlii'][1] + '\" ab ' + tv_program['rtlii'][3] + '\n' 
        program_response += 'Viva:    Seit ' + tv_program['viva'][2] + ' \"' + tv_program['viva'][0] + '\" => \"' + tv_program['viva'][1] + '\" ab ' + tv_program['viva'][3] + '\n' 
        program_response += 'ComedyCentral:  Seit ' + tv_program['comedycentral'][2] + ' \"' + tv_program['comedycentral'][0] + '\" => \"' + tv_program['comedycentral'][1] + '\" ab ' + tv_program['comedycentral'][3] + '\n' 
        program_response += 'ZDF:     Seit ' + tv_program['zdf'][2] + ' \"' + tv_program[u'zdf'][0] + '\" => \"' + tv_program['zdf'][1] + '\" ab ' + tv_program['zdf'][3]
        
        return program_response
              

    def help(self):
        return 'tv - get the latest tv program\n'

    def keyword(self):
        return 'tv'
    
    def parse_broadcast_table(self, broadcast_table, row_type):
        tv_program = {}
    
        for program_list in broadcast_table.find_all('tr', attrs={'class':row_type}):
            program_titles = []
            time_list = []
    
            for program in program_list.find_all('td', attrs={"class":'details'}):
                for program_title in program.find('a'):
                    program_titles.append(program_title)
         
            for times in program_list.find_all('td', attrs={'class':'time'}):
                time_list.append(times.text.strip())
         
            for station in program_list.find_all('span', attrs={'class':'stationName'}):
                program_titles += time_list
                tv_program[station.string.lower().replace(" ","")] = program_titles
            
        return tv_program