#!/usr/bin/env python

import re

def title(lyric):
	pattern = r'([^~]*).txt$'
	match = re.search(pattern, lyric)
	title = ' '.join(match.group(0)[:-4].split('-'))
	return title

