#drawing hollow and filled circles
import pygame 
pygame.init()
screen= pygame.display.set_mode((450,450))
screen.fill("black")
done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
            
    pygame.draw.circle(screen,"yellow",(100,200),80,10)
    pygame.draw.circle(screen,'blue',(300,300),100)
    pygame.display.update()
pygame.quit()