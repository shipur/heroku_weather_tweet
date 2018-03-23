# Dependencies
import tweepy
import time
import json
import random
import requests as req
import datetime

# Twitter API Keys
consumer_key = "moQ8rwGs3XB6AyKuwDEQYza2P"
consumer_secret = "bx2R3HMrs2NIRozTHIjqdy73PfSSdrQUzW6fPnKsDXWXMscybP"
access_token = "975007577712091136-4i58ew8yLqbmIbFdARMyzwyDmulaPyv"
access_token_secret = "EBRzbimyzUaSOlTVbcWYrdl3nluVfeJ4TwkRObX0UEAcG"

# Weather API
api_key = "25bc90a1196e6f153eece0bc0b0fc9eb"
city_list=["London", "Mumbai"]
# Create a function that gets the weather in London and Tweets it
def WeatherTweet(city):
   # Construct a Query URL for the OpenWeatherMap
    url = "http://api.openweathermap.org/data/2.5/weather?"
    #city = "London"
    units = "imperial"
    query_url = url + "appid=" + api_key + "&q=" + city + "&units=" + units
    weather_response = req.get(query_url)
    weather_json =  weather_response.json()
    #print(json.dumps(weather_json, indent=4))
    consumer_key = "moQ8rwGs3XB6AyKuwDEQYza2P"
    consumer_secret = "bx2R3HMrs2NIRozTHIjqdy73PfSSdrQUzW6fPnKsDXWXMscybP"
    access_token = "975007577712091136-4i58ew8yLqbmIbFdARMyzwyDmulaPyv"
    access_token_secret = "EBRzbimyzUaSOlTVbcWYrdl3nluVfeJ4TwkRObX0UEAcG"

    # Setup Tweepy API Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    # @TODO: Tweet the weather
    api.update_status(city + " weather as of %s: %s F" %
                  (datetime.datetime.now().strftime("%I:%M %p"), weather_json["main"]["temp"]))
    # @TODO: Construct a Query URL for the OpenWeatherMap

    # @TODO: Perform the API call to get the weather
for x in city_list:
    WeatherTweet(x)
    # @TODO: Twitter credentials
# Twitter API Keys

    # @TODO: Print success message
print("Tweeted Successfully")