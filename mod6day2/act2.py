#drawing hollow and filled circles
import pygame 
pygame.init()
screen= pygame.display.set_mode((450,450))
done=True

while done:
    for i in pygame.event.get():
        if pygame.event==pygame.QUIT:
            done=True
    pygame.draw.circle(screen,"yellow",(50,200),80,10)
    pygame.draw.circle(screen,'blue',(100,300),100)
    pygame.display.update()