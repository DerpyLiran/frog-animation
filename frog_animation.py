from sys import exit
from frog_class import FrogPlayer
import pygame

pygame.init()
clock = pygame.time.Clock()

# Game Screen
(screen_width, screen_height) = (700, 200)
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Frog sprite animation")

# Adding our sprite to a sprite group
moving_sprites = pygame.sprite.Group()
frog_player = FrogPlayer(0, screen_height)
moving_sprites.add(frog_player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                frog_player.animate()
    
    # Drawing our stuff to the screen
    win.fill((50, 50, 50))
    # This will draw our sprite but not move it
    moving_sprites.draw(win)
    moving_sprites.update()
    pygame.display.flip()
    clock.tick(60)
