#!/usr/bin/python3 
#-*-coding : utf-8 -*-
# written with Python 3.5.2
# author : vicherlys

""" Jeu du Demineur """
try:
	import pygame
	from pygame.locals import * 

	from sprites import tile_size,mine
	from field import Field

except ImportError as err:
	print (" Importation error : {}".format(err))

pygame.init()
def mouseToCoord(mousepos):
	return (mousepos[0]//tile_size, mousepos[1]//tile_size)

def placeFlag(field , pos):
	""" Place or remove a flag on the field"""
	field.getCase(pos).putFlag()

def clear(field , pos):
	field.clear(pos)
	return field.has_exploded()

def clearAll(field , pos):
	field.clearAllFrom(pos)
	return field.has_exploded()

def drawfield (screen,field):
	for y in range(field.height):
		for x in range(field.width):
			screen_pos = (x*tile_size,y*tile_size)
			tile_image = field.getCase((x,y)).getImage()
			screen.blit( tile_image , screen_pos)



def main():
	nb_larg , nb_haut = 40, 30
	mine_count = int((nb_haut*nb_larg)/6)
	title = "demineur"
	icon = pygame.image.load("./Images/mine.bmp")

	width  ,height = tile_size * nb_larg, tile_size * nb_haut
	screen  = pygame.display.set_mode((width, height))

	field = Field( mine_count , ( nb_larg , nb_haut))
	field.initField()
	field.countBombs()
	font = pygame.font.SysFont('ubuntu', 60)

	gameovermessage = font.render( 'Game Over ' , True, (0,0,0))
	pygame.display.set_caption(title)
	
	pygame.display.set_icon(icon)

	done = False
	gameover = False 
	win = lambda : field.completed()

	while not done:

		if win ():
			gameover = True
			gameovermessage = font.render(' Congrats , you cleared the mine field ' , True , (0,0,0))


		for event in pygame.event.get():
			if event.type == QUIT :
				done = True
			elif event.type == KEYDOWN and event.key == K_ESCAPE:
				done = True

			elif event.type == MOUSEBUTTONDOWN:
				if gameover :
					done = True 
				mousecoord = mouseToCoord(pygame.mouse.get_pos())

				if pygame.mouse.get_pressed()[0]:
					boom = clear(field,mousecoord)
					if boom:
						gameover = True
				elif pygame.mouse.get_pressed()[2]:
					placeFlag (field,mousecoord)

				elif pygame.mouse.get_pressed()[1]:
					boom = clearAll(field, mousecoord)
					if boom:
						gameover = True

		
		drawfield (screen , field)

		if gameover:
			screen.blit(gameovermessage , ((width // 2 )- gameovermessage.get_rect().center[0], (height // 2)- gameovermessage.get_rect().center[1] ))
		

		pygame.display.update()


if __name__ == "__main__":
	main()