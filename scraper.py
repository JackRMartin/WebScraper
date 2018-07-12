#!usr/bin/python
import urllib.request
from bs4 import BeautifulSoup
import os

url = "https://www.youtube.com/results?search_query="
url_file = open("url.txt","r")
url = url_file.readline()

page = urllib.request.urlopen(url)
html = page.read()
soup = BeautifulSoup(html, 'html.parser')

print ("\nTitle of the page is " + soup.title.string)
os.system("pause")































#
