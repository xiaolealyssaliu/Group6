#!/usr/bin/env python

import id_
import artist
import title
import kid_safe
import love
import mood
import length
import complexity

class Characterization:
	
	# value attribute of the class

	id_ = 0
	artist = " "
	title = " "
	kid_safe = 0
	love = 0
	mood = 0
	length = 0
	complexity = 0
	
	# initial the characterization as well as set as an attribute
	characterization = {"id": id_, "artist": artist, "title": title, "kid_safe": kid_safe,
			"love": love, "mood": mood, "length": length, "complexity": complexity}

	def __init__(self, lyric):
		self.lyric = lyric

	# get the values by the methods in each .py file

	def id_(self):
		self.id_ = id_.id_(self.lyric)

	def artist(self):
		self.artist = artist.artist(self.lyric)

	def title(self):
		self.title = title.title(self.lyric)

	def kid_safe(self, data):
		self.kid_safe = kid_safe.kid_safe(data)

	def love(self, data):
		self.love = love.love(data)

	def mood(self, data):
		self.mood = mood.mood(data)

	def length(self, data):
		self.length = length.length(data)

	def complexity(self, data):
		self.complexity = complexity.complexity(data)

	# get the total characterization of the lyrics
	def get_characterization(self):
		self.characterization = {"id": self.id_, "artist": self.artist, "title": self.title, "kid_safe": self.kid_safe,
					"love": self.love, "mood": self.mood, "length": self.length, "complexity": self.complexity}

def get_character(lyric, data):
	# process the class to get the characterization result
	c = Characterization(lyric)
	c.id_()
	c.artist()
	c.title()
	c.kid_safe(data)
	c.love(data)
	c.mood(data)
	c.length(data)
	c.complexity(data)
	c.get_characterization()
	return c.characterization

