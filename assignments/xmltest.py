import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
address = input('Enter location: ')

print('Retrieving', address)
data = urllib.request.urlopen(address).read()
print('Retrieved', len(data))
tree = ET.fromstring(data)
counts = tree.findall('.//count')
print('Count: ', len(counts))
sumitems = 0
for item in counts:
    sumitems = sumitems +float(item.text)
print('Sum: ', sumitems)
