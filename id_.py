#!/usr/bin/env python

import re

def id_(lyric):
	pattern = r'^\d+'				# extract the id information from the file name
	match = re.search(pattern, lyric)
	id_ = int(match.group(0))			# change to integer type
	return id_

