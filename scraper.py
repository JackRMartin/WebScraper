#!usr/bin/python
import urllib.request
from bs4 import BeautifulSoup
import os
import sys
import ctypes

#create url
base_url = "http://twitter.com/"
url_file = open("url.txt","r")
url = base_url + url_file.readline();

#create soup object
try:
	page = urllib.request.urlopen("")
except urllib.error.HTTPError as err:
	if err.code == 404:
		#python will stop execution here and return to the c++ program if 404 error encountered
		err_format = "\n\n                                       "
		ctypes.windll.user32.MessageBoxW(0, url + err_format + "NOT FOUND"," 404 ERROR!", 1)
		sys.exit(0)

html = page.read()
soup = BeautifulSoup(html, 'html.parser')


#parse (gather information about tweets on the page)
#tweet div = <div class="js-tweet-text-container"> use to identify individual tweets

#print ("\nTitle of the page is: " + soup.title.string)
print(soup)

os.system("pause")


#output to text file













#
