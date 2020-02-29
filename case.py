from sprites import *

class Case ():
	def __init__(self , pos , _type):
		self.pos = pos
		self.x = pos[0]
		self.y = pos[1]
		self.type = _type
		self.state = 'hidden' # hidden
		self.bombcount = 0

	def show(self,):
		self.state = 'cleared'
		return self.type

	def putFlag(self):
		if self.state  == 'hidden':
			self.state = 'flagged'
			return True

		if self.state == 'flagged':
			self.state = 'hidden'
		return False

	def setType(self , newtype):
		if self.type == newtype :
			return False
		self.type = newtype
		return True

	
	def getImage(self):
		if self.state == 'hidden' :
			return images['hidden']

		elif self.state == 'flagged' :
			return images['flag']

		else :
			if self.type == 'safe':
				return  images['number'][self.bombcount]
			# mine_expl or mine
			return images[self.type]


		