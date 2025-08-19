import pygame
import random
from pygame import mixer 

bg_color = (0,170,225)
sp_color = 'red'


class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(bg_color)
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
        self.rect = self.image.get_rect()
    
    def right(self,pixels):
        self.rect.x += pixels 
    def left(self,pixels):
        self.rect.x -= pixels
    def forward(self,pixels):
        self.rect.y += pixels
    def backward(self,pixels):
        self.rect.y -= pixels

bg = pygame.image.load("bg.jpg")
bg = pygame.transform.scale(bg, (500, 400))

pygame.init()
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Sprite Collision")

all_sprites_list = pygame.sprite.Group()

sp1 = Sprite(sp_color, 20, 30)
sp1.rect.x = random.randint(0,480)
sp1.rect.y = random.randint(0,370)
all_sprites_list.add(sp1)

sp2 = Sprite((255,0,0), 20, 30)
sp2.rect.x = random.randint(0,480)
sp2.rect.y = random.randint(0,370)
all_sprites_list.add(sp2)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                running = False
	
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sp1.left(5)
    if keys[pygame.K_RIGHT]:
        sp1.right(5)
    if keys[pygame.K_DOWN]:
        sp1.forward(5)
    if keys[pygame.K_UP]:
        sp1.backward(5)

    screen.fill('pink')
    screen.blit(bg,(0,0))
    all_sprites_list.draw(screen)

    if sp1.rect.colliderect(sp2.rect):
        all_sprites_list.remove(sp2)
        font = pygame.font.SysFont("Times new Roman", 72)  
        text = font.render("You win!", True, (158, 16, 16))
        screen.blit(text,(250 - text.get_width() // 2, 200 - text.get_height() // 2))
        

        if not mixer.music.get_busy():
            mixer.music.load("explosion.wav")
            mixer.music.set_volume(0.3)
            mixer.music.play()
    pygame.display.update()
    clock.tick(60)
running=False

pygame.quit()