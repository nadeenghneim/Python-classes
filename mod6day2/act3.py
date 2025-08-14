import pygame 
import random 
pygame.init()
colors={'red':pygame.Color('red'),'blue':pygame.Color('blue'),'purple':pygame.Color('purple'),'orange':pygame.Color('orange'),'yellow':pygame.Color('yellow')}
current_color=colors['red']
screen=pygame.display.set_mode((500,500))
screen_width,screen_height=500,500
sprite_width, sprite_height= 20,25
clock=pygame.time.Clock()
pressed=pygame.key.get_pressed()
x= 30
y=30
done=False
while not done:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            done=True
    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y-=3
    if pressed[pygame.K_DOWN]:
        y+=3
    if pressed[pygame.K_RIGHT]:
        x+=3
    if pressed[pygame.K_LEFT]:
        x-=3
    x=min(max(0,x),screen_width-sprite_width)
    y=min(max(0,y),screen_height-sprite_height)
    if x==0:
        current_color=colors['blue']
    elif x==screen_width-sprite_width:
        current_color=colors['orange']
    elif y==0:
        current_color=colors['purple']
    elif y==screen_height-sprite_height:
        current_color=colors['yellow']
    screen.fill("black")
    pygame.draw.rect(screen,current_color,pygame.Rect(x,y,sprite_width,sprite_height))
    clock.tick(30)
    pygame.display.flip()