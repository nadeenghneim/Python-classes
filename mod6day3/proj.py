import pygame 
import random 
pygame.init()
screen=pygame.display.set_mode((600,600))
clock=pygame.time.Clock()
x,y=300,300
done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done= True 
    pygame.draw.rect(screen,'indigo',pygame.Rect(200,100,150,75))
    image=pygame.image.load("smileyface.png")
    image = pygame.transform.scale(image, (150, 75))
    sprite_rect=image.get_rect()
    screen.fill("black")
    screen.blit(image,sprite_rect)
    pressed= pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y-=3
    if pressed[pygame.K_DOWN]:
        y+=3
    if pressed[pygame.K_LEFT]:
        x-=3
    if pressed[pygame.K_RIGHT]:
        x+=3
    clock.tick(60)
pygame.quit()