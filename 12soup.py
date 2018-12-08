# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

cntentry = input('Enter count: ')
intcount = int(cntentry)
posentry = input('Enter position: ')
intpos = int(posentry)

url = input('Enter url: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags

count = 0
newcount = 0
atpos = 0
while atpos < intpos:
    tags = soup('a')
    taglist = list()
    for tag in tags:
        taglist.append(tag.get('href', None))
    url = taglist[intcount - 1]
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    print(url)
    atpos = atpos + 1
        #count = count +1
        #if count == intcount:
        #    newurl = taglist[intcount - 1]
        #    html = urllib.request.urlopen(newurl, context=ctx).read()
        #    soup = BeautifulSoup(html, 'html.parser')
        #    newtags = soup('a')
        #    newtaglist = list()
        #    for newtag in newtags:
        #        newtaglist.append(newtag.get('href', None))
        #        newcount = newcount + 1
        #        if newcount != intcount: continue
        #           newerurl = newtaglist[intcount - 1]
        #           print(newerurl)
            #atpos = atpos + 1



        #print(taglist[intcount-1])
        #    atpos = atpos +1
        #    print(atpos)
            #newhtml = urllib.reqest.urlopen(taglist[intcount-1], context=ctx).read()
            #newsoup = BeautifulSoup.(newhtml), 'html.parser')
            #    newtags = soup('a')
            #    newtaglist = list()



            #atpos = atpos + 1


#newurl = taglist[intcount - 1]
#print(newurl)



#itemofinterest = intcount-1
#tagofinterest = taglist[itemofinterest]


#print(tagofinterest)
