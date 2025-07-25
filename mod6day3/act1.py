import pygame 
import random
pygame.init()
WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
done=True

background_color=pygame.Color("black")
ball_color="pink"
ball_radius=25
ball_x = random.randint(ball_radius, WIDTH - ball_radius)
ball_y = random.randint(ball_radius, HEIGHT - ball_radius)

ballx_speed=3
bally_speed=3
clock= pygame.time.Clock()


while done:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            done=False
    ball_x+=ballx_speed
    ball_y+=bally_speed

    if ball_x <= ball_radius or ball_x >= WIDTH - ball_radius:
        ballx_speed *= -1
    if ball_y <= ball_radius or ball_y >= HEIGHT - ball_radius:
        bally_speed *= -1

    screen.fill(background_color)
    pygame.draw.circle(screen,ball_color,(ball_x,ball_y),ball_radius)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()