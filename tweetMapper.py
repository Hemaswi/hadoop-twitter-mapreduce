#!/usr/bin/env python3

import json
import sys
import string

# Mapper - filters tweets by user screen_name and generates key-value pairs of the format <hour_of_creation, 1>


for line in sys.stdin:
    tweet_data = json.loads(line)
    tweet = tweet_data.get('text')
    if 'RT @' not in tweet:
       keys = tweet.split()
       for key in keys:
            for p in string.punctuation:
                key = key.replace(p, "")
                value = 1

            if (key):
                print( "%s\t%d" % (key, value) )
