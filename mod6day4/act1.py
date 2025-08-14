import pygame 
import random
from pygame import mixer 


bg_color=(0,170,225)
sp_color='red'

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()

        self.image=pygame.Surface([width,height])
        self.image.fill(bg_color)
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
        self.rect= self.image.get_rect()
    
    def Right(self,pixels):
        self.rect.x += pixels 
    def Left(self,pixels):
        self.rect.x -=pixels
    def Forward(self,pixels):
        self.rect.y +=pixels
    def Backward(self,pixels):
        self.rect.y -=pixels
bg = pygame.image.load("bg.jpg")

bg = pygame.transform.scale(bg, (500, 400))

pygame.init()

screen = pygame.display.set_mode((500, 400))

pygame.display.set_caption("Sprite Collision")

all_sprites_list = pygame.sprite.Group()

# Add a sprite

sp1 = Sprite(sp_color, 20, 30)

sp1.rect.x = random.randint(0,480)

sp1.rect.y = random.randint(0,370)

all_sprites_list.add(sp1)

# Add one enemy

# set the random position

rad = 20

cxp = random.randint(0,480)

cyp = random.randint(0,370)

sp2 = Sprite((255,0,0), 20, 30)

sp2.rect.x = cxp

sp2.rect.y = cyp

all_sprites_list.add(sp2)

exit = True

clock = pygame.time.Clock()
while exit:
    for event in pygame.event.get():
        if event.type==pygame.Quit:
            exit=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x:
                exit=False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
		sp1.moveLeft(5)
	if keys[pygame.K_RIGHT]:
		sp1.moveRight(5)
	if keys[pygame.K_DOWN]:
		sp1.moveForward(5)
	if keys[pygame.K_UP]:
		sp1.moveBack(5)

	all_sprites_list.update()
	screen.fill(surf_color)
	screen.blit(bg,(0,0))
	all_sprites_list.draw(screen)
	pygame.display.flip()
if sp1.rect.colliderect(sp2.rect):
		all_sprites_list.remove(sp2)
		text = "You win!"
		#load the fonts  
		font = pygame.font.SysFont("Times new Roman", 72)  
		# Render the text in new surface  
		text = font.render(text, True, (158, 16, 16))
		screen.blit(text,(200 - text.get_width() // 2, 140 - text.get_height() // 2))
		# Loading the song
		mixer.music.load("explosion.wav")
		
		# Setting the volume
		mixer.music.set_volume(0.3)
		
		# Start playing the song
		mixer.music.play()
		
	pygame.display.update()
	clock.tick(60)

pygame.quit()