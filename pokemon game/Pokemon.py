import pygame
import random
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Pokemon_Hunt")
icon = pygame.image.load('pokeball.png')
pygame.display.set_icon(icon)
background = pygame.image.load('_Image 2.png')

player_img = pygame.image.load('south.png')
player_x = 490
player_y = 530
player_x_change = 0
player_y_change = 0
player_speed = 5

pokemon_img = pygame.image.load('pika.png')
pokemon_x = 168
pokemon_y = 180

coin_img = pygame.image.load('dollar.png')
coin_x = 370
coin_y = 500

coin2_img = pygame.image.load('dollar.png')
coin2_x = 320
coin2_y = 500

coin3_img = pygame.image.load('dollar.png')
coin3_x = 270
coin3_y = 500

coin4_img = pygame.image.load('dollar.png')
coin4_x = 220
coin4_y = 500

coin5_img = pygame.image.load('dollar.png')
coin5_x = 170
coin5_y = 500

coin6_img = pygame.image.load('pokeball.png')
coin6_x = 120
coin6_y = 500

score = 0
pokeball = 0
font = pygame.font.Font('freesansbold.ttf', 32)

def player(x,y):
    screen.blit(player_img, (x, y))

def pokemon(x,y):
    screen.blit(pokemon_img, (x, y))

def coin(x,y):
    screen.blit(coin_img, (x, y))

def coin2(x,y):
    screen.blit(coin2_img, (x, y))
def coin3(x,y):
    screen.blit(coin3_img, (x, y))

def coin4(x,y):
    screen.blit(coin4_img, (x, y))

def coin5(x,y):
    screen.blit(coin5_img, (x, y))

def coin6(x,y):
    screen.blit(coin6_img, (x, y))

def isCollision(px, py, cx, cy):
    if px < cx < px + 64 and py < cy < py + 64:
        return True
    return False

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_y -= 10
            if event.key == pygame.K_DOWN:
                player_y += 10
            if event.key == pygame.K_LEFT:
                player_x -= 10
            if event.key == pygame.K_RIGHT:
                player_x += 10

    
    collision = isCollision(player_x, player_y, coin_x, coin_y)
    collect_sound = mixer.Sound('coin.mp3')
    if collision:
        collect_sound.play()
        score += 1
        coin_x = coin_y = -100  

    collision2 = isCollision(player_x, player_y, coin2_x, coin2_y)
    if collision2:
        collect_sound.play()
        score += 1
        coin2_x = coin2_y = -100 

    collision3 = isCollision(player_x, player_y, coin3_x, coin3_y)
    if collision3:
        collect_sound.play()
        score += 1
        coin3_x = coin3_y = -100

    collision4 = isCollision(player_x, player_y, coin4_x, coin4_y)
    if collision4:
        collect_sound.play()
        score += 1
        coin4_x = coin4_y = -100

    collision5 = isCollision(player_x, player_y, coin5_x, coin5_y)
    if collision5:
        collect_sound.play()
        score += 1
        coin5_x = coin5_y = -100

    collision6 = isCollision(player_x, player_y, coin6_x, coin6_y)
    pokeball_sound = mixer.Sound('poke.mp3')
    if collision6:
        pokeball_sound.play()
        pokeball += 1
        coin6_x = coin6_y = -100

    coin(coin_x, coin_y)
    coin2(coin2_x, coin2_y)
    coin3(coin3_x, coin3_y)
    coin4(coin4_x, coin4_y)
    coin5(coin5_x, coin5_y)
    coin6(coin6_x, coin6_y)
    pokemon(pokemon_x, pokemon_y)
    player(player_x, player_y)
    
    
    pokeball_text = font.render("Pokeballs: " + str(pokeball), True, (255, 255, 255))
    screen.blit(pokeball_text, (10, 50))
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()
