
import os
import re
import random
import class_character
import json


def get_result(lyrics_directory):
	result = []
	dada ={}
	dada["characterizations"] = result
	lyrics = os.listdir(lyrics_directory)				# get all the file names of lyrics as a list 
	lyrics = sorted(lyrics)
	for i in lyrics:
		if i[-4:] == '.txt':					# confirm it is not a hidden file
			path = lyrics_directory + i
			with open(path) as fp:				# read the lyrics strings
				data = fp.read()
			character = class_character.get_character(i, data)	# get the scores from class_character.py file
			result.append(character)
	dada["characterizations"] = sorted(dada["characterizations"], key = lambda i: i['id'])	# sort the result by id

	print(json.dumps(obj=dada,indent=True))				# print as json format output

	return json.dumps(obj=dada,indent = True)
	

if __name__ == '__main__':

	import argparse

	parser = argparse.ArgumentParser('Get Characterizations For All Lyrics')
	parser.add_argument('lyrics_directory', help = 'Directory of the folder containing all lyrics .txt files')
	args = parser.parse_args()

	get_result(args.lyrics_directory)



