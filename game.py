#!/usr/bin/python

#This program is free software: you can redistribute it and/or modify
#it under the terms of the IIIT General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#You should have received a copy of the IIIT General Public License
#along with this program.
from random import *

class Person(object):
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def checkWall(self,m,n):
		try: 
			if MAZE[n][m] != 'X' and m >= 0 and n >= 0:
				return True
			else :
				return False
		except :
			return False
		
class Pacman(Person):
	def __init__(self,x,y):
		self.x =x 
		self.y = y
		self.score = 0
		MAZE[self.y][self.x] = 'P'
		
	def updatePosition(self,move):
		MAZE[self.y][self.x] = '.'
		if move == 'w' and  self.checkWall(self.x,self.y-1) :
			self.y -= 1
		elif move == 's' and self.checkWall(self.x,self.y+1) :
			self.y += 1
		elif move == 'a' and self.checkWall(self.x-1,self.y) :
			self.x -= 1
		elif move == 'd' and self.checkWall(self.x+1,self.y) :
			self.x += 1	
		if MAZE[self.y][self.x] == 'C':
			self.score += 1
		MAZE[self.y][self.x] = 'P'

	def collectCoin(self):
		self.score =+ 1
	
	def pacmanPosition(self):
		return (self.x,self.y)

	def outputScore(self):
		print "Score : " , self.score
		return 

	def checkGhost(self,m,n):
		if self.x == m and self.y == n :
			return True
		else: 
			return False


def outputMAZE():
	for lines in MAZE:
		for chars in lines:
			print chars ,
		print


class Ghost(Person):

	""" ghost inherits from person """
	def __init__(self,x,y):
		global MAZE
		MAZE = list([(line.strip().split()) for line in open("FIELD")])
		self.x = x
		self.y = y
		MAZE[self.y][self.x]='G'
		self.coin = 0


	def ghostPosition(self):
		return (self.x,self.y)

	def updateGhostPosition(self):
		if self.coin == 1:
			if MAZE[self.y][self.x] == 'P' :
				pacman.collectCoin()
			else:		
				MAZE[self.y][self.x] = 'C'
		elif MAZE[self.y][self.x] != 'P': 
			MAZE[self.y][self.x] = '.'
		if randint(0,1) == 1:
			if self.checkWall(self.x +1 ,self.y):
				self.x += 1
			elif self.checkWall(self.x - 1, self.y):
				self.x -= 1
		else:
			if self.checkWall(self.x ,self.y+1):
				self.y += 1
			elif self.checkWall(self.x , self.y - 1):
				self.y -= 1
		if MAZE[self.y][self.x] == 'C':
			self.coin =1
		else:
			self.coin =0	
		MAZE[self.y][self.x] = 'G'

class Game():
	def start(self):
		outputMAZE()
		while pacman.score < 125:
			pacman.outputScore()
			move = raw_input('Enter move: ')
			if move == 'q':
				print "You Quit"
				break
			pacman.updatePosition(move)
			ghost.updateGhostPosition()
			x,y=ghost.ghostPosition()
			outputMAZE()
			if pacman.checkGhost(x,y) :
				print 'You Lost! :('
				break
		pacman.outputScore()
	def stop(self):
		import sys
		print 'Your final Score is : ', pacman.score
		sys.exit()

if __name__ == "__main__":
	try:			# loading map from file MAZE
		ghost = Ghost(0,0)
		pacman = Pacman(13,13)
		g = Game()
		g.start()  
	except KeyboardInterrupt:
		g.stop()