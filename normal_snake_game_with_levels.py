import pygame, time
from random import randint as r
import sqlite3

def game_over():
    connection = sqlite3.connect('save_game_info.sqlite')
    cusor = connection.cursor()
    ex = cusor.execute
    ex(f'UPDATE snake SET level = 1')
    ex(f'UPDATE snake SET size = 1')
    connection.commit()
    connection.close()

connection = sqlite3.connect('save_game_info.sqlite')
cusor = connection.cursor()
ex = cusor.execute

ex('SELECT * FROM snake')

level, score = cusor.fetchall()[0]

connection.close()

win_size = 800
applesize = win_size//30
playersize = win_size//30
pygame.init()
window = pygame.display.set_mode((win_size, win_size))
pygame.display.set_caption("snake (lead enginer-shmuli keller)")  # Set the window caption
player = pygame.Rect(100, 100, playersize, playersize)
apple = pygame.Rect(r(30, win_size-applesize-10), r(30, win_size-applesize-10), applesize, applesize)
direction = 'r'
clock = pygame.time.Clock()
score = 1
snakebody = [pygame.Rect(player.x, player.y, playersize, playersize) for _ in range(score)]
font = pygame.font.Font(None, 36)
run = True
fps = 16
# level = 1
nextlevel = False

while run:
    window.fill('black')

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            connection = sqlite3.connect('save_game_info.sqlite')
            cusor = connection.cursor()
            ex = cusor.execute
            ex(f'UPDATE snake SET level = {level}')
            ex(f'UPDATE snake SET size = {score if score > 0 else 1}')
            connection.commit()
            connection.close()
            pygame.quit()
            run = False
    clock.tick(fps)
    
    if player.colliderect(apple):
        apple = pygame.Rect(r(30, win_size-applesize-10), r(30, win_size-applesize-10), applesize, applesize)
        score += 1
        snakebody.append(pygame.Rect(player.x, player.y, playersize, playersize))
        
    for i in range(len(snakebody)-1):
        snakebody[i].x = snakebody[i+1].x
        snakebody[i].y = snakebody[i+1].y

    if score == level*5:
        score = 0
        level += 1 
        snakebody = [pygame.Rect(player.x, player.y, playersize, playersize)]
        fps += 2
        player.x, player.y = win_size//2, win_size//2
        nextlevel = True

    score_text = font.render(f"level: {level}  Score: {score}  speed: {fps}", True, (255, 255, 255))

    snakebody[-1].x = player.x
    snakebody[-1].y = player.y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and direction != 'r':
        direction = 'l' 
    elif keys[pygame.K_RIGHT] and direction != 'l':
        direction = 'r'
    elif keys[pygame.K_UP] and direction != 'd':
        direction = 'u' 
    elif keys[pygame.K_DOWN] and direction != 'u':
        direction = 'd'

    if direction == 'd':
        player.y += playersize
    elif direction == 'u':
        player.y -= playersize
    elif direction == 'r':
        player.x += playersize
    elif direction == 'l':
        player.x -= playersize

    pygame.draw.rect(window, (255, 0, 0), apple)
    pygame.draw.rect(window, (0, 255, 0), player)

    bc = 255/(len(snakebody)+1)
    for i in snakebody:
        pygame.draw.rect(window, (0, 255, 255-snakebody.index(i)*bc), i)

    if not (win_size - playersize > player.y > 0 and win_size - playersize > player.x > 0):
        score_text = font.render(f"Game Over", True, (255, 255, 255))
        window.blit(score_text, (win_size//2-50, 0))
        pygame.display.update()
        game_over()
        run = False
 
    for i in snakebody:
        if player.colliderect(i):
            score_text = font.render(f"Game Over", True, (255, 255, 255))
            window.blit(score_text, (win_size//2-50, 0))
            pygame.display.update()
            game_over()
            run = False

    if not nextlevel:
        window.blit(score_text, (10, 10))  # Display the score text at (10, 10)
    else:
        window.blit(score_text, (20, 20))  # Display the score text at (10, 10)

    pygame.display.update()
    if nextlevel:
        if win_size > 500:
            window.blit(score_text, (win_size/4, win_size/4)) 
        pygame.display.update()
        time.sleep(2.5)
        nextlevel = False

while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()
            break