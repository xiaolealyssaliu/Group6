#!/usr/bin/env python

import re

def artist(lyric):
	pattern = r'~([^~]*)~'
	match = re.search(pattern, lyric)
	artist = ' '.join(match.group(0)[1:-1].split('-'))
	return artist

