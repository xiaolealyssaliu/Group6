#!/usr/bin/env python

from textblob import TextBlob

def mood(data):

	m = TextBlob(data).sentiment[0]		# this function returns the polarity as value nearer to 1 means a positive
						# and values nearer to -1 means a negative sentiment.
	m = round((m - (-1))/(1 - (-1)), 1) # normalize the scores
	return m

