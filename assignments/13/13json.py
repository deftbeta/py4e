import urllib.request, urllib.parse, urllib.error
import json


address = input('Enter location: ')
print('Retrieving', address)
#data = urllib.request.urlopen(address).read()
uh = urllib.request.urlopen(address)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
parsedjs = json.loads(data)
count = 0
sumcounts = 0
for item in parsedjs['comments']:
    #print('count: ', parsedjs['comments'][count]['count'])
    sumcounts = sumcounts + parsedjs['comments'][count]['count']
    count = count + 1
print('Count: ', count)
print('Sum: ', sumcounts)
