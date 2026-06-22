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
