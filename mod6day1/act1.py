import pygame 
pygame.init()
screen= pygame.display.set_mode((500,600))#creating the screen of the game and deciding its size
done=True
while done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()#if x is pressed window closes, game ends 
    pygame.display.flip()#as long as they dont press x this function displays everything