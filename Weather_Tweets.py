#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
import tweepy
import time
import json
import random
import requests
import datetime
import sys
sys.path.insert(0, '..\..')
#from config import consumer_key, consumer_secret, access_token, access_token_secret, weather_api_key


# In[2]:


# Twitter API Keys

consumer_key = os.environ.get("consumer_key")
consumer_secret = os.environ.get("consumer_secret")
access_token = os.environ.get("access_token")
access_token_secret = os.environ.get("access_token_secret")
api_key = os.environ.get("weather_api_key")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# In[3]:




# In[4]:


# Create a function that gets the weather in London and Tweets it
def WeatherTweet(num):

    # Construct a Query URL for the OpenWeatherMap
    url = "http://api.openweathermap.org/data/2.5/weather?"
    city = "Washington, DC."
    units = "imperial"
    query_url = url + "appid=" + api_key + "&q=" + city + "&units=" + units

    # Perform the API call to get the weather
    response = requests.get(query_url).json()

    # Twitter credentials
    temp = response['main']['temp']

    # Tweet the weather
    api.update_status(f"Hour {num}: The current weather in {city} is {temp}F.")

    # Print success message
    print(f"The current weather in {city} is {temp}F.")


# In[5]:


# Set timer to run every 1 hour
counter = 1

while(True): 
    WeatherTweet(counter)
    time.sleep(3600)
    counter += 1
    


# In[ ]:




