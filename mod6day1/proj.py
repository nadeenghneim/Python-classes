import pygame 

pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("adding an image to the middle of the screen ")
screen.fill("grey")
image=pygame.image.load("handala.png")
image=pygame.transform.scale(image,(150,250))

done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done= True
        screen.blit(image,(175,100))
        pygame.display.flip()
