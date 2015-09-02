#!/usr/bin/env python
from  urllib2 import urlopen
from re       import search,compile

RFIURL  = 'http://telechargement.rfi.fr.edgesuite.net/rfi/francais/audio/journaux/derniers/journal_francais_facile.mp3.asx'
PREFIX  = 'http://telechargement.rfi.fr.edgesuite.net/rfi/francais/audio/journaux/r001/'
RE      = compile(r'r001/(.+?).wsx')

# 'fetchme' is the URL for today's actualite
asx     = urlopen(RFIURL).read()
mp3     = search(RE, asx).group(1)
fetchme = PREFIX + mp3

# ...and download it
print fetchme
req     = urlopen(fetchme)
fp  = open(mp3, 'wb')     
for line in req:          
    fp.write(line)        
fp.close() 
