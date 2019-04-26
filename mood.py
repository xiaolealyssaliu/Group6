#!/usr/bin/env python

from textblob import TextBlob

def mood(data):

	m = TextBlob(data).sentiment[0]
	m = round((m - (-1))/(1 - (-1)), 1) # normalize the scores
	return m

