import random

import pygame
from random import randrange

RES = 800
SIZE = 50

x, y = randrange(1, 16) * 50, randrange(1, 16) * 50
apple = randrange(1, 16) * 50, randrange(1, 16) * 50
length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 60
dirs = {'W': True, 'S': True, 'A': True, 'D': True, }
score = 0
speed_count, snake_speed = 0, 10
time = 5
time_int = 5

rand_apple_color = random.randint(1, 3)

pygame.init()
surface = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)


def close_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


while True:
    surface.fill((0, 0, 0))
    [pygame.draw.rect(surface, pygame.Color('green'), (i, j, SIZE - 1, SIZE - 1)) for i, j in snake]

    if rand_apple_color == 1:
        pygame.draw.rect(surface, pygame.Color('red'), (*apple, SIZE, SIZE))
    elif rand_apple_color == 2:
        pygame.draw.rect(surface, pygame.Color('white'), (*apple, SIZE, SIZE))
    elif rand_apple_color == 3:
        pygame.draw.rect(surface, pygame.Color('blue'), (*apple, SIZE, SIZE))

    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
    surface.blit(render_score, (5, 5))
    timer = font_score.render(f'TIME: {time_int}', 1, pygame.Color('orange'))
    surface.blit(timer, (5, 30))
    speed_count += 1

    time -= 0.02
    time_int = int(time)
    if time_int == 0:
        time = 6
        apple = randrange(1, 16) * 50, randrange(1, 16) * 50

    if not speed_count % snake_speed:
        x += dx * SIZE
        y += dy * SIZE
        snake.append((x, y))
        snake = snake[-length:]

    if snake[-1] == apple:
        apple = randrange(1, 16) * 50, randrange(1, 16) * 50
        length += 1
        score += rand_apple_color
        snake_speed -= 1
        snake_speed = max(snake_speed, 4)
        rand_apple_color = random.randint(1, 3)
        time = 6

    if x < 0 or x > 750 or y < 0 or y > 750 or len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
            surface.blit(render_end, (250, 250))
            pygame.display.flip()
            close_game()

    pygame.display.flip()
    clock.tick(fps)
    close_game()
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        if dirs['W']:
            dx, dy = 0, -1
            dirs = {'W': True, 'S': False, 'A': True, 'D': True, }
    elif key[pygame.K_s]:
        if dirs['S']:
            dx, dy = 0, 1
            dirs = {'W': False, 'S': True, 'A': True, 'D': True, }
    elif key[pygame.K_a]:
        if dirs['A']:
            dx, dy = -1, 0
            dirs = {'W': True, 'S': True, 'A': True, 'D': False, }
    elif key[pygame.K_d]:
        if dirs['D']:
            dx, dy = 1, 0
            dirs = {'W': True, 'S': True, 'A': False, 'D': True, }
