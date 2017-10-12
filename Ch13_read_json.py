import json
import urllib.request, urllib.parse, urllib.error


serviceurl = 'http://py4e-data.dr-chuck.net/comments_30870.json'

print ('Enter location:', serviceurl )
print('Retrieving', serviceurl)
uh = urllib.request.urlopen(serviceurl)
data = uh.read().decode()

print('Retrieved', len(data), 'characters')

#print(data)
js = json.loads(data)
total = 0

truedata = js["comments"]
print("Count:", len(truedata))

for item in truedata:
    total += int(item['count'])

print("Sum:", total)
"""
print(info)


for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
"""
