
import os
import re
import random
import class_character
import json


def get_result(lyrics_directory):
	dada ={}
	dada["characterizations"] = result
	lyrics = os.listdir(lyrics_directory)
	lyrics = sorted(lyrics)
	result = []
	for i in lyrics:
		if i[-4:] == '.txt':
			path = lyrics_directory + i
			with open(path) as fp:
				data = fp.read()
			character = class_character.get_character(i, data)
			result.append(character)
	print(dada)
	   
	return dada
	

if __name__ == '__main__':

	import argparse

	parser = argparse.ArgumentParser('Get Characterizations For All Lyrics')
	parser.add_argument('lyrics_directory', help = 'Directory of the folder containing all lyrics .txt files')
	args = parser.parse_args()

	get_result(args.lyrics_directory)



