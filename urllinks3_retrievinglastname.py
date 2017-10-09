# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
"""
URL = input("Enter the URL:") #Enter main URL
link_line = int(input("Enter position:")) - 1 #The position of link relative to first link
count = int(input("Enter count:")) #The number of times to be repeated

while count >= 0:
    html = urllib.request.urlopen(URL).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    print (URL)
    URL = tags[link_line].get("href", None)
    count = count - 1
"""
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input ('Enter count: '))
position = int(input ('Enter position: '))


while count >=0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    print(url)
    url = tags[position-1].get("href",None)
    count -= 1
