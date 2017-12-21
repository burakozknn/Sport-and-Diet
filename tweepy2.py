import urllib, json
import sys
import tweepy
from tweepy import OAuthHandler
import codecs
from django.utils.encoding import smart_str, smart_unicode

consumer_key = 'Kw5RsPW9V3XZULbq5ZiNQoCtI'
consumer_secret = 'Yd635P1NX0Fa1UOPJINz3I3eJSLjDJSG2OVq8dWDtSOjukVh5H'
access_token = "1580441372-XrRJC4OSFVHExG3R53LmtjAYXyOaTTGKEWUkEhp"
access_token_secret = "1gAlPUqyQzrZuX8sMCU0rx2B9Pq7zYQTvqDVZNZMEKZPp"
    
	
def twitter_fetch(screen_name = "sporsalbilgiler",maxnumtweets=2500):
    #'Fetch tweets from @BBCNews'
    # API described at https://dev.twitter.com/docs/api/1.1/get/statuses/user_timeline

    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
	
    api  = tweepy.API(auth)
    #print api.me().name
    #api.update_status('Hello -tweepy + oauth!')
	
	#a = u'\xa1'
	#print smart_str(a)
		
	
     	
    for status in tweepy.Cursor(api.user_timeline,id=screen_name).items(2500): 
		print json.dumps(status.text.encode('utf-8'))
		#print smart_str(status.text) + "\n"
		
		
		#fp = codecs.open("Tweets3.json", "w", "utf-8")
		#fp.write(status.text) 
		
		#print json.dumps(status.text.encode('unicode-escape'))
		
		
   

if __name__ == '__main__':
    twitter_fetch("sporsalbilgiler",2500)