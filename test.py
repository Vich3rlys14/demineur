import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((300,300))

font = pygame.font.SysFont("notosansmonocjkkr" , 16)
text = font.render("1", False, (0,199,199))
all_fonts= pygame.font.get_fonts()
print (all_fonts)
Done = False
while not Done:
	for event in pygame.event.get():
		if event.type == QUIT:
			Done = True
	screen.blit(text , [0,0])
	pygame.display.update()
