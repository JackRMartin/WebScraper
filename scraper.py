#!usr/bin/python
import tweepy
from tweepy import OAuthHandler
import credentials

consumer_key = credentials.consumer_key
consumer_secret = credentials.consumer_secret
access_token = credentials.access_token
access_secret = credentials.access_secret
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
 #open file and get twitter name to use
twitter_name_file = open("url.txt","r")
twitter_name = twitter_name_file.readline();

api = tweepy.API(auth)
user = api.get_user(twitter_name)

print (user.screen_name)
print (user.followers_count)

statuses = api.user_timeline('thundawolf')


outputfile = open("output.txt", "a")
for status in statuses:
	this_status = status.text
	print (this_status)
	outputfile.write(this_status)








#
