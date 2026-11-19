import pygame
import world


TILE_SIZE = 32
SCREEN_WIDTH  = TILE_SIZE * 32
SCREEN_HEIGHT = TILE_SIZE * 24
FPS = 60


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
game_world = world.World(TILE_SIZE)

running = True

going_up = False
going_down = False
going_left = False
going_right = False
while running:
    dt = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_w:
                 going_up = True
             if event.key == pygame.K_s:
                going_down = True
             if event.key == pygame.K_d:
                going_right = True
             if event.key == pygame.K_a:
                going_left = True
        if event.type == pygame.KEYUP:
             if event.key == pygame.K_w:
                 going_up = False
             if event.key == pygame.K_s:
                going_down = False
             if event.key == pygame.K_d:
                going_right = False
             if event.key == pygame.K_a:
                going_left = False
                 
    
    game_world.update(dt, going_up, going_down, going_right, going_left)
    game_world.draw(screen)
    pygame.display.flip()
    
pygame.quit()
    
    