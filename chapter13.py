'''
import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)

counts = tree.findall('.//count')
nums = list()
for result in counts:
    nums.append(int(result.text))

print('Count:', len(nums))
print('Sum:', sum(nums))

'''
#################


'''
import json
from urllib.request import urlopen
url = "https://py4e-data.dr-chuck.net/comments_2433813.json"

data = urlopen(url).read()

info = json.loads(data)
nums = list()
print('User count:', len(info['comments']))

for i in range(len(info['comments'])):
    nums.append(int(info['comments'][i]["count"]))

print('Sum:', sum(nums))


'''


import urllib.request, urllib.parse
import json, ssl

# Heavily rate limited proxy of https://www.geoapify.com/ api
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    address = address.strip()
    parms = dict()
    parms['q'] = address

    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'features' not in js:
        print('==== Download error ===')
        print(data)
        break

    if len(js['features']) == 0:
        print('==== Object not found ====')
        print(data)
        break

    # print(json.dumps(js, indent=4))

    lat = js['features'][0]['properties']['lat']
    lon = js['features'][0]['properties']['lon']
    plus_code = js['features'][0]['properties']['plus_code']
    print('lat', lat, 'lon', lon, 'plus_code', plus_code)
    location = js['features'][0]['properties']['formatted']
    print(location)



