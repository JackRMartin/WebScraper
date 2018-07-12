#!usr/bin/python
import urllib.request
from bs4 import BeautifulSoup
import os

#create url
base_url = "https://www.youtube.com/results?search_query="
url_file = open("url.txt","r")
url = base_url + url_file.readline();

#create soup object
page = urllib.request.urlopen(url)
html = page.read()
soup = BeautifulSoup(html, 'html.parser')


#parse
print(soup.title.string)
#print ("\nTitle of the page is " + soup.title.string)
os.system("pause")


#output to text file






























#
