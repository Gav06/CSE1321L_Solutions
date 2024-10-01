"""
Class:      CSE1321L
Section:    Module 4
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Lab:        7B
"""
import pygame, sys

pygame.init()

res = (600, 600)
screen = pygame.display.set_mode(res)
clock = pygame.time.Clock()

rect = pygame.Rect(0, 0, 60, 60)
surface = pygame.Surface((rect.w, rect.h))
surface.fill((255, 0, 0))

# top left
screen.blit(surface, (0, 0))
# top right
screen.blit(surface, (res[0] - rect.w, 0))
# bottom left
screen.blit(surface, (0, res[1] - rect.h))
# bottom right
screen.blit(surface, (res[0] - rect.w, res[1] - rect.h))
# center
center_x = (res[0] / 2) - rect.centerx
center_y = (res[1] / 2) - rect.centery
screen.blit(surface, (center_x, center_y))


while True:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)

    pygame.display.flip()
    clock.tick(60)