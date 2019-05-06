#!/usr/bin/env python

import re

def title(lyric):
	pattern = r'([^~]*).txt$'			# get title information from the file name, which is after second '~'
	match = re.search(pattern, lyric)
	title = ' '.join(match.group(0)[:-4].split('-'))	# substitute '-' to space
	return title

