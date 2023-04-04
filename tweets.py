import requests
from requests.api import request
import os
import json
import streamlit as st
import streamlit.components.v1 as components
import random
from datetime import datetime, timedelta
import sys

bearer_token = st.secrets["bearer_token"]
               
def bearer_oauth(r):

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def theTweets(tweets_url):
    api =f'https://publish.twitter.com/oembed?url={tweets_url}&theme=dark'
    response_tweets = requests.get(api)
    res = response_tweets.json()["html"]
    return res

def tweets(input):
    search_url = "https://api.twitter.com/2/tweets/search/recent"
    query_params_tweets = {'query': f'{input}','tweet.fields': 'author_id', 'max_results': 50}
    json_response = connect_to_endpoint(search_url, query_params_tweets)
    
    for i in range(0,10):
        try:
            author_id = json_response["data"][i]["author_id"]
            tweet_id = json_response["data"][i]["id"]
            url = f'https://twitter.com/{author_id}/status/{tweet_id}'
            res = theTweets(url)
            components.html(res, height = 500)
        except:
            st.error(f"oops! Error logged! {sys.exc_info()[0]}")
            st.info("Try searching different Hashtags")
            break      