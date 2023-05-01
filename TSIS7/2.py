import pygame
pygame.init()

songs = ["sounds/Flowers.mp3", "sounds/Patron.mp3", "sounds/Brooklyn.mp3"]
current = 0

width, height = 800, 600
screen = pygame.display.set_mode((width, height))

pause = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
                if pause:
                    print(pause)
                    pygame.mixer.music.load(songs[current])
                    pygame.mixer.music.play()
                elif not pause:
                    print(pause)
                    pygame.mixer.music.stop()

            if event.key == pygame.K_RIGHT:
                current += 1
                print(current)
            if event.key == pygame.K_LEFT:
                current -= 1
                print(current)
