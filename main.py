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
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    game_world.draw(screen)
    pygame.display.flip()
    
pygame.quit()
    
    