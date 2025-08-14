#drawing a rectangle
import pygame 
pygame.init()
done=True
screen=pygame.display.set_mode((600,500))
while done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
            pygame.quit()
    pygame.draw.rect(screen,("blue"),(40,40,70,50))
    pygame.draw.circle(screen,'purple',(200,250),40,8)
    pygame.draw.line(screen,'yellow',(300,300),(400,400),10)
    pygame.display.flip()
