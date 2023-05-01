import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Red Circle")
clock = pygame.time.Clock()
done = False

x = 400
y = 300

pygame.display.flip()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= 10
    elif keys[pygame.K_RIGHT]:
        x += 10
    elif keys[pygame.K_UP]:
        y -= 10
    elif keys[pygame.K_DOWN]:
        y += 10

    if x >= 800 or x <= 0 or y >= 600 or y <= 0:
        x = 400
        y = 300

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)
    pygame.display.update()

    clock.tick(60)
