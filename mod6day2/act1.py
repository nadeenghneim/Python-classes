#drawing a rectangle
import pygame 
pygame.init()
done=True
screen=pygame.display.set_mode((600,500))
while done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.draw.rect(screen,("blue"),pygame.Rect(40,40,70,50))
    pygame.display.flip()