import pygame 
import random
pygame.init()
WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
done=False
colors = {
    'red': pygame.Color('red'),
    'blue': pygame.Color('blue'),
    'green': pygame.Color('green'),
    'purple': pygame.Color('purple'),
    'orange': pygame.Color('orange'),
    'yellow': pygame.Color('yellow'),
    'pink': pygame.Color('pink'),
    'cyan': pygame.Color('cyan'),
    'magenta': pygame.Color('magenta'),
    'lime': pygame.Color('lime'),
    'teal': pygame.Color('teal'),
    'gold': pygame.Color('gold'),
    'salmon': pygame.Color('salmon'),
    'turquoise': pygame.Color('turquoise'),
    'navy': pygame.Color('navy'),
    'maroon': pygame.Color('maroon'),
    'olive': pygame.Color('olive'),
    'skyblue': pygame.Color('skyblue'),
    'coral': pygame.Color('coral'),
    'indigo': pygame.Color('indigo'),
    'brown': pygame.Color('brown'),
    'black': pygame.Color('black'),
    'white': pygame.Color('white'),
    'gray': pygame.Color('gray'),
    'lightgray': pygame.Color('lightgray'),
    'darkgray': pygame.Color('darkgray')
}

background_color=pygame.Color("black")
ball_color = random.choice(list(colors.values()))
ball_radius=25
ball_x = random.randint(ball_radius, WIDTH - ball_radius)
ball_y = random.randint(ball_radius, HEIGHT - ball_radius)

ballx_speed=3
bally_speed=3
clock= pygame.time.Clock()


while not done:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            done=True
    ball_x+=ballx_speed
    ball_y+=bally_speed

   

    screen.fill(background_color)
    pygame.draw.circle(screen,ball_color,(ball_x,ball_y),ball_radius)
    if ball_x <= ball_radius or ball_x >= WIDTH - ball_radius:
        ballx_speed *= -1
        ball_color=random.choice(list(colors.values()))
    if ball_y <= ball_radius or ball_y >= HEIGHT - ball_radius:
        bally_speed *= -1
        ball_color=random.choice(list(colors.values()))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()