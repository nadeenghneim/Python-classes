import pygame 
import math 
import random 
from pygame import mixer 

pygame.init()

screen=pygame.display.set_mode((500,800))
background=pygame.image.load('background.jpg')
pygame.display.set_caption("SPACE INVASION GAME!")
icon=pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

mixer.music.load("background.wav")
mixer.music.play(-1)

playerimg=pygame.image.load("player.png.jpg")
player_x=370
player_y=380
player_xchange=0

enemyimg=[]
enemy_x=[]
enemy_y=[]
enemy_xchange=[]
enemy_ychange=[]
num_of_enemies=6

for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load("enemy.png"))
    enemy_x.append((0,736))
    enemy_y.append((50,150))
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
testY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
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