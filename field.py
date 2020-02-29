from case import Case
from random import choice

class Field ():
	def __init__(self  , minesCnt , dimensions  ):
		self.width = dimensions[0] # larg
		self.height = dimensions[1] # long
		self.minesCnt = minesCnt
		self.field =  [[ Case ((x,y) , 'safe') for x in range(self.width)] for y in range(self.height)]
		self.mines = []

	def initField(self):
		""" Place les bombes dans la grille """
		for _ in range (self.minesCnt):
			placed = False
			while  not placed:
				row = choice(self.field)
				case = choice(row)
				# setType return false si la case contient deja une bombe
				if case.setType('mine') != False:
					placed =True
					self.mines.append(case)

	def countBombs(self):
		directions = [-1,0,1]
		
		for mine in self.mines:
			for y in directions:
				for x in directions:
					if not x == y == 0 :
						pos_x = mine.x + x
						pos_y = mine.y + y
						if  0 <= pos_x < self.width and 0 <= pos_y < self.height:
							case = self.getCase( (pos_x , pos_y))
							if case.type != 'mine':
								case.bombcount+=1

	def countFlags(self, case):
		count = 0
		directions= [-1,0,1]
		for neighbor in self.getNeighbors(case):
			if neighbor.state == 'flagged':
				count += 1
		return count

	def getCase (self , pos):
		return self.field [ pos [1]][ pos[0]]

	def clear(self , pos):
		current_case = self.getCase(pos)
		current_case.state = 'cleared'

		if current_case.type == 'safe' and current_case.bombcount == 0:
			self.clearAllFrom(current_case.pos)

		if current_case.type == 'mine':

			current_case.type = 'mine_expl'
			current_case.state = 'cleared'
			self.lost()


	def showAll(self):
		for row in self.field:
			for case in row:
				case.state = 'cleared'

	def lost(self):
		for m in self.mines:
			if m.state  != 'flagged' and m.type != 'mine_expl':
				m.type = 'perdu'
				m.state = 'cleared'

	def win (self):
		pass

	def getNeighbors(self, case):
		directions= [-1,0,1]
		for y in directions:
			for x in directions:
				if not x == y == 0 :
					pos_x = case.x + x
					pos_y = case.y + y
					if  0 <= pos_x < self.width and 0 <= pos_y < self.height:
						neighbor = self.getCase( (pos_x , pos_y))
						yield neighbor


	def clearAllFrom(self, pos):
		case = self.getCase(pos)
		if case.state == 'hidden':
			return False

		if case.type == 'mine':
			case.type = 'mine_expl'
			self.lost()

		elif case.type == 'safe':
			case.state = 'cleared'
			if self.countFlags(case) != case.bombcount:
				pass
			else :
				for neighbor in self.getNeighbors(case):
					if neighbor.state != 'cleared' and neighbor.state != 'flagged':
						neighbor.state = 'cleared'
						if (neighbor.bombcount == 0 ):
							self.clearAllFrom(neighbor.pos)
	

	def has_exploded(self):
		for mine in self.mines:
			if mine.type == 'mine_expl':
				return True
		return False

	def completed(self):
		for row in self.field:
			for case in row :
				if case.type == 'mine' and case.state != 'flagged':
					return False
				elif case.type == 'safe' and case.state != 'cleared':
					return False

		return True
