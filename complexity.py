#!/usr/bin/env python

import textstat

def complexity(data):
	
	comp = textstat.flesch_reading_ease(data)
	comp = round(1-(comp-(-806.84))/(125.32-(-806.84)), 1) # normalize the score, the original score range for all lyrics is [-806.84, 125.32]
	return comp


