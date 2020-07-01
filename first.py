'''
print('hello world')

#max number
lst=[1,66,44,90,233,66,678,2456,89007655,2333,5675,]
maxxx=None
for i in lst:
	if  maxxx is None:
		maxxx=i
	elif maxxx<i:
		maxxx=i

print(maxxx)

#select only number using findall function
import re
handle=open('assI.txt')
x=list()
for i in handle:
	y=re.findall('[0-9]+',i)
	x=x+y
sum=0
for z in x:
	sum=sum+int(z)
print(sum)


#web server connection
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()


#beutifulsoap

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Enter - ')

html = urlopen(url).read()
soup = BeautifulSoup(html)
tag = soup("span")
count=0
sum=0
for i in tag:
	x=int(i.text)
	count+=1
	sum = sum + x
print (count)
print (sum)
'''

#
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# Ignore SSL certificate errors
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/known_by_Yousif.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# get user input for how many times to search
count = int(input('Enter count:'))

# get user input for which url to click on
position = int(input('Enter position:'))-1

while count >= 0:
    # re-reads the current url
    html = urllib.request.urlopen(url, context=ctx).read()
    # creates a new soup object
    soup = BeautifulSoup(html, 'html.parser')
    # searches the page for all <a> tags
    tags = soup('a')
    print("Retrieving: ", url)
    # upates the current url
    url = tags[position].get("href", None)
    count = count - 1
