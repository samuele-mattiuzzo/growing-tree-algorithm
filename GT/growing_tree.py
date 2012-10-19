#!/usr/bin/python

import sys
import os
import random

class GrowingTree():
	'''
		GrowingTree maze generator main class
		Further description will be provided soon
	'''
	def __init__(self, width, height,
		outer_wall=False, method="newest first"):
		
		# maze related variables
		self.width = width
		self.height = height
		self.walk = 1
		self.wall = 0
		self.start = (0,0)
		self.end = (0,0)
		self.shortest_path = 0
		self.outer_wall = outer_wall
		self.method = method

		# internal variables
		self.__DIRS = ((1,0),(-1,0),(0,1),(0,-1))
		self.__MAZE = [self.wall]*self.width*self.height
		self.__CELLS = []

	def generate(self):
		'''
			Generates the maze using the Growing Tree algorithm
		'''
		x, y, opts = random.randint(0, self.width-1), random.randint(0, self.height-1), self.shuf(self.__DIRS)
		
		print x,y,opts, self.__DIRS

		self.__CELLS.append((x,y))

		while len(self.__CELLS):
			index = self.choose_next(len(self.__CELLS), self.method)
			x, y = self.__CELLS[index]

			for DIR in opts:
				nx, ny = x+DIR[0], y+DIR[1]

				if self.check_bounds(nx, ny):
					self.__MAZE[y][x] = 1
					self.__MAZE[y][x] = DIR
					self.__MAZE[ny][nx] = self.opposite(DIR)
					self.__CELLS.append((nx, ny))
					index = 0

	def as_string(self):
		'''
			Returns the growing tree maze as string
		'''
		return "".join([x for x in self.__MAZE])
	
	def as_array(self):
		'''
			Returns the growing tree maze as an array
		'''
		return self.__MAZE

	def as_matrix(self):
		'''
			Returns the growing tree maze as a double dimensional array
		'''
		pass

	def get_properties(self):
		'''
			Returns dictionary containing start, end and score
		'''
		return {
			'start' : self.start,
			'end' : self.end,
			'shortest_path' : self.shortest_path
		}

	# utilities, parametrized for external use
	def opposite(self, direction):
		'''
			Inverts a tuple (x,y) to get the opposite direction
		'''
		return tuple([-1*x for x in direction])

	def check_bounds(self, nx, ny):
		'''
			Checks bounds for given x,y
		'''
		return nx >=0 and ny >=0 and nx<self.width and ny<self.height and self.__MAZE[nx][ny]==0

	def shuf(self, l):
		'''
			Shuffles a list
		'''
		l = list(l)
		random.shuffle(l)
		return l

	def choose_next(self, size, type="newest first"):
		'''
			Chooses next index to inspect
			type:
			- "newest first" : pops newest element from __CELLS (LIFO)
			- "oldest first" : pops oldest element from __CELLS (FIFO)
			- "primm" : pops random element from __CELLS (Primm's algorithm)
		'''

		# newest first, implicit (avoids wrong type inputs)
		index = size-1

		if type.lower() == "primm":
			index = random.randint(0, size-1)

		elif type.lower() == "oldest first":
			index = 0

		return index

