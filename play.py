from snake import Snake_game
import pygame

pygame.init()
game = Snake_game(15)

block_size = 30

(width, height) = (game.SIZE*block_size,)*2
screen = pygame.display.set_mode((width, height))
pygame.display.flip()

myfont = pygame.font.SysFont('Comic Sans MS', 30)


running = True
while running:
    direction = None
    # 		12
    #	21		03
    # 		30
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = 1
            if event.key == pygame.K_RIGHT:
                direction = 3
            if event.key == pygame.K_UP:
                direction = 2
            if event.key == pygame.K_DOWN:
                direction = 0
            if event.key == pygame.K_SPACE:
                running = False
            if event.type == pygame.QUIT:
                running = False

    game.game_loop(direction)

    screen.fill(pygame.Color(255, 255, 255, 255))

    for y, row in enumerate(game.field):
        for x, item in enumerate(row):
            if item == 100:
                pygame.draw.rect(screen, pygame.Color(80, 158, 58, 255),
                                 pygame.Rect((y*block_size, x*block_size), (block_size,)*2))
            if item == 101:
                pygame.draw.rect(screen, pygame.Color(57, 114, 41, 255),
                                 pygame.Rect((y*block_size, x*block_size), (block_size,)*2))
            elif item == 666:
                pygame.draw.rect(screen, pygame.Color(188, 70, 62, 255),
                                 pygame.Rect((y*block_size, x*block_size), (block_size,)*2))

    score_surface = myfont.render(str(game.score), False, (0, 0, 0))

    screen.blit(score_surface, (0, 0))

    pygame.display.update()
    pygame.time.wait(300-(game.score*10))
