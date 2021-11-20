'''
This python script can be used to scrape tweets from Twitter by specifying the time period and the required set of keywords. 
It is using snscrape to scrape the tweets and it can be installed using - !pip install git+https://github.com/JustAnotherArchivist/snscrape.git
Further the number of tweets that can be scraped in one run is limited so one does not get connection error 

'''

import snscrape.modules.twitter as sntwitter
import numpy as np
import pandas as pd


def extract_tweets(keywords, start_time_period, end_time_period, periods = 240, max_tweets = 5000) :
    ''' The function extracts tweets using snscrape and the two inputs from the user
    keywords - list of keywords for which the tweets needs to be extracted
    start_time_period - start of the time period from which the tweets to be extracted. Should be in yyyy-mm-dd format
    end_time_period - end of the time period from which the tweets to be extracted. Should be in yyyy-mm-dd format

    It returns list of tweets that are extracted
    '''

    #save tweets
    tweets_data = []

    #split the time period into smaller periods
    time_period_list = list(pd.date_range(start= start_time_period, end = end_time_period, periods= periods))
    time_period_list = [str(x)[:10] for x in time_periods]


    for keyword in keywords :

        for time in range(len(time_period) -1) :

            for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{keyword} since:{time_period[time]} until:{time_period[time +1]}').get_items()) :
                if i > max_tweets :
                    break
                else :
                    tweets_data.append([keyword, tweet.date, tweet.id, tweet.content])

  return tweets_data
