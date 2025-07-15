import pygame 
pygame.init()
screen= pygame.display.set_mode((500,600))
done=True
while done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.display.flip()