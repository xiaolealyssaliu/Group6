#!/usr/bin/env python

import re

def id_(lyric):
	pattern = r'^\d+'
	match = re.search(pattern, lyric)
	id_ = int(match.group(0))
	return id_

