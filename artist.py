#!/usr/bin/env python

import re

def artist(lyric):
	pattern = r'~([^~]*)~'			# get the artist name from file name, which is between first '~' and second '~'
	match = re.search(pattern, lyric)
	artist = ' '.join(match.group(0)[1:-1].split('-'))	# substitute the '-' to space
	return artist

