#!/usr/bin/env python
from  urllib2 import urlopen
from re       import search,compile

RFIURL  = 'http://telechargement.rfi.fr.edgesuite.net/rfi/francais/audio/journaux/derniers/journal_francais_facile.mp3.asx'
PREFIX  = 'http://telechargement.rfi.fr.edgesuite.net/rfi/francais/audio/jff/'
RE      = compile(r'jff/(.+?)/(.+?).wsx')

# 'fetchme' is the URL for today's actualite
asx     = urlopen(RFIURL).read()
yearmo  = search(RE, asx).group(1)
mp3     = search(RE, asx).group(2)
fetchme = PREFIX + yearmo + '/' + mp3

# ...and download it - save as a file called 'mp3'
print fetchme
req = urlopen(fetchme)
fp  = open(mp3, 'wb')     
for line in req:          
    fp.write(line)        
fp.close() 
