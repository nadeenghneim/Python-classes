import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("adding an image")
screen.fill("blue")
pygame.display.flip()

image_surface=pygame.Surface((200,300))
image=pygame.image.load("cat.png")
screen.blit(image,(150,100))

done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done==True
pygame.quit()