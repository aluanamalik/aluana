import pygame
import datetime
pygame.init()

width, height = 800, 450
screen = pygame.display.set_mode((width, height))
screen.fill((255, 255, 255))

clock = pygame.image.load("image/mickey.jpeg")
clock_scale = pygame.transform.scale(clock, (clock.get_width() // 2, clock.get_height() // 2))
clock_rect = clock_scale.get_rect(center=(width//2, height//2))

second = pygame.image.load("image/arrow.png")
second_scale = pygame.transform.scale(second, (second.get_width() // 2, second.get_height() // 2))

minute = pygame.image.load("image/arrow.png")
minute_scale = pygame.transform.scale(minute, (minute.get_width() // 2, minute.get_height() // 2))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill((255, 255, 255))
    screen.blit(clock_scale, clock_rect)
    t = datetime.datetime.now()
    minutes, seconds = t.minute, t.second

    second_rotation = pygame.transform.rotate(second_scale, (seconds * -6) + 90)
    second_rect = second_rotation.get_rect(center=(width // 2, height // 2))
    screen.blit(second_rotation, second_rect)

    minute_rotation = pygame.transform.rotate(minute_scale, (minutes * -6) + 90)
    minute_rect = minute_rotation.get_rect(center=(width // 2, height // 2))
    screen.blit(minute_rotation, minute_rect)

    pygame.display.update()
