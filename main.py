#!/usr/bin/env python


import os
import re
import random


def get_result(lyrics_directory):

	lyrics = os.listdir(lyrics_directory)
	result = []
	for i in lyrics:
		if i[-4:] == '.txt':
			path = lyrics_directory + i
			with open(path) as fp:
				data = fp.read()
			character = get_character(i)
			result.append(character)
	return result


if __name__ == '__main__':

	import argparse

	parser = argparse.ArgumentParser('Get Characterizations For All Lyrics')
	parser.add_argument('lyrics_directory', help = 'Directory of the folder containing all lyrics .txt files')
	args = parser.parse_args()

	get_result(args.lyrics_directory)

