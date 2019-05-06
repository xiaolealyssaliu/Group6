#!/usr/bin/env python

import textstat

def complexity(data):
	
	comp = textstat.flesch_reading_ease(data)	# get the Flesch reading-ease test. In the Flesch reading-ease test, 
							# higher scores indicate material that is easier to read; 
							# lower numbers mark passages that are more difficult to read. 
	comp = round(1-(comp-(-806.84))/(125.32-(-806.84)), 1)	# normalize the score, 
								# the original score range for all lyrics is [-806.84, 125.32]
	return comp


