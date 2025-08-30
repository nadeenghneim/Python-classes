import pygame 
import math 
import random 
from pygame import mixer 

pygame.init()

screen=pygame.display.set_mode((800,500))
background=pygame.image.load('background.jpg')
background=pygame.transform.scale(background,(800,500))
pygame.display.set_caption("SPACE INVASION GAME!")
icon=pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
clock=pygame.time.Clock()
mixer.music.load("background.wav")
mixer.music.play(-1)
playerimg=pygame.image.load("player.png.jpg")
player_x=250
player_y=470
player_xchange=0

enemyimg=[]
enemy_x=[]
enemy_y=[]
enemy_xchange=[]
enemy_ychange=[]
num_of_enemies=6

for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load("enemy.png"))
    enemy_x.append(random.randint(0,736))
    enemy_y.append(50+i*60)
    enemy_xchange.append(4)
    enemy_ychange.append(40)

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 380
bulletX_change = 0
bulletY_change = 10
bullet_state ="ready"

score_value=0
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (0, 0, 0))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerimg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))#distance formula
    if distance < 27:
        return True
    else:
        return False
    
running= True 
while running:

    screen.fill('black')
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                player_xchange=-10
            if event.key== pygame.K_RIGHT:
                player_xchange=10
            if event.key==pygame.K_SPACE:
                if bullet_state=='ready':
                    bulletSound=mixer.Sound('laser.wav')
                    bulletSound.play()
                    bulletX=player_x
                    fire_bullet(bulletX,bulletY)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                player_xchange=0
        player_x+=player_xchange
        if player_x<=0:
            player_x=0
        elif player_x>=736:
            player_x=736
    for i in range(num_of_enemies):
        if enemy_y[i]>500:
            for j in range(num_of_enemies):
                enemy_y[j] = 2000
            game_over_text()
            break

        enemy_x[i] += enemy_xchange[i]
        if enemy_x[i] <= 0:
            enemy_xchange[i] = 1
            enemy_y[i] += enemy_ychange[i]
        elif enemy_x[i] >= 736:
            enemy_xchange[i] = -1
            enemy_y[i] += enemy_ychange[i]

        # Collision
        collision = isCollision(enemy_x[i], enemy_y[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bulletY = 380
            bullet_state = "ready"
            score_value += 1
            enemy_x[i] = random.randint(0, 736)
            enemy_y[i] = random.randint(50, 150)

        enemy(enemy_x[i], enemy_y[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 380
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(player_x, player_y)
    show_score(textX, textY)
    pygame.display.update()
    clock.tick(60)