import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

serviceurl = 'http://py4e-data.dr-chuck.net/comments_30869.xml'



#if len(address) < 1: break

#url = serviceurl + urllib.parse.urlencode({'address': address})
print('Retrieving from ', serviceurl)
uh = urllib.request.urlopen(serviceurl)
data = uh.read()
print('Retrieved from', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)

sum = 0
counts = tree.findall('.//count')
#print (counts)
for count in counts:
    sum += int(count.text)

print('Count:', len(counts))
print('Sum:', sum)

#print(lst)
#print('Count:', len(lst))


#while counts >0 :
#num = results[0].find('comment').find('count').text
#total += int(num)
    #counts -= 1

#lat = results[0].find('geometry').find('location').find('lat').text
#lng = results[0].find('geometry').find('location').find('lng').text
#location = results[0].find('formatted_address').text

#print('lat', lat, 'lng', lng)
#print(location)
