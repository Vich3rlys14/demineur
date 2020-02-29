import pygame

tile_size = 16
size = (tile_size,tile_size)

scale = lambda surface: pygame.transform.smoothscale(surface,size)

# image drapeau
flag = scale(pygame.image.load("./Images/drapeau.bmp"))
# mine
mine = scale(pygame.image.load("./Images/mine.bmp"))
# mine barrer avec croix
mine2 = scale(pygame.image.load("./Images/mine2.bmp"))
# image de case vide
empt = scale( pygame.image.load("./Images/rien.bmp"))
# image mine ayant exploser
expl = scale(pygame.image.load("./Images/perdu.bmp"))
# image mine nonpassee
hidden = scale(pygame.image.load("./Images/nonpassee.bmp"))
# Image pour nombre de 1 a 8
img_num = [ empt if n == 0 else scale(pygame.image.load("./Images/"+str(n)+".bmp")) for n in range(9)]
	

images  = {
	'hidden':hidden,
	'number':img_num,
	'mine': mine,
	'perdu': mine2,
	'mine_expl': expl,
	'flag': flag
}