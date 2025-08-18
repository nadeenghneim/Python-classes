import pygame 
import random 
pygame.init()
screen=pygame.display.set_mode((600,600))
clock=pygame.time.Clock()
x,y=100,100
screen.fill("black")
pygame.display.set_caption("")
target_x=random.randint(0,600)
target_y=random.randint(0,600)
done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done= True 
    purple_rect=pygame.draw.rect(screen,'indigo',pygame.Rect(x,y,50,50))
    image=pygame.image.load("smileyface.png")
    image = pygame.transform.scale(image, (100,75))
    target= pygame.draw.rect(screen,'black',pygame.Rect(target_x,target_y,40,40))

    screen.blit(image,(300,100))
    pressed= pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y-=3
    if pressed[pygame.K_DOWN]:
        y+=3
    if pressed[pygame.K_LEFT]:
        x-=3
    if pressed[pygame.K_RIGHT]:
        x+=3
    x=min(max(0,x),600-50)
    y=min(max(0,y),600-50)
    font=pygame.font.SysFont('Times New Roman',18)
    surface=font.render("Hello! Walk over the treasure hidden on the screen to win!!(hint:it won't br visible)",True,'white')
    text_rect = surface.get_rect()
    screen.blit(surface,text_rect)
    if purple_rect.colliderect(target):
        win_text = font.render("Great Job!!! You win!", True, 'yellow')
        screen.blit(win_text, (240, 300))
        
    pygame.display.flip()
    clock.tick(60)
pygame.quit()