# Example file showing a basic pygame "game loop"
import pygame
import math
import os

# Learning to have more than one python file
import Grid
import Snake

#Run tests
Snake.SnakePart.TestSwap()

# Some configuration
width = 800
height = 600

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")

# pygame setup
pygame.init()
pygame.mixer.init()
pygame.font.init()

screen = pygame.display.set_mode((width, height), vsync=False, flags=pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True

grid = Grid.GridTable()

snakeController = Snake.SnakeController(grid)

mouse = pygame.mouse
key = pygame.key

wasRight = False
wasPressedSpace = False

elapsedTime = 0.0
tickTimeSeconds = 0.1
isPaused = True



while running:   
    dt = clock.tick(60) / 1000
    elapsedTime += dt
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clicks = mouse.get_pressed(3)

    if clicks[0]:
        posX = mouse.get_pos()[0];
        posY = mouse.get_pos()[1];
        snakeController.updateSnake()
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and not wasPressedSpace:
        isPaused = not isPaused
        wasPressedSpace = True
    elif not keys[pygame.K_SPACE] and wasPressedSpace:
        wasPressedSpace = False

    if elapsedTime > tickTimeSeconds:
        elapsedTime = 0.0
        if not isPaused:
            grid.UpdateGrid()

    if keys[pygame.K_DOWN]:
        snakeController.setSnakeDirection(0, 1)
    if keys[pygame.K_UP]:
        snakeController.setSnakeDirection(0, -1)
    if keys[pygame.K_LEFT]:
        snakeController.setSnakeDirection(-1, 0)
    if keys[pygame.K_RIGHT]:
        snakeController.setSnakeDirection(1, 0)


    snakeController.update(dt)
    screen.fill("black")
    snakeController.Draw(screen)

    #grid.draw(screen)

    pygame.display.flip()
    pygame.display.set_caption("Snake | FPS: " + str(round(clock.get_fps(), 3)))
    
pygame.quit()