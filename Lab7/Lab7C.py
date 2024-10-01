"""
Class:      CSE1321L
Section:    Module 4
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Lab:        7C
"""
import pygame, sys

pygame.init()

res = (1000, 500)
screen = pygame.display.set_mode(res)
clock = pygame.time.Clock()

top_rect = pygame.Rect(0, 0, 100, 100)
bot_rect = pygame.Rect(0, res[1] - 100, 100, 100)

top_surf = pygame.Surface((100, 100))
bot_surf = pygame.Surface((100, 100))

top_surf.fill((0, 255, 0))
bot_surf.fill((0, 0, 255))

sliding_right = True

while True:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)

    screen.fill((0, 0, 0))
    screen.blit(top_surf, (top_rect.x, top_rect.y))
    screen.blit(bot_surf, (bot_rect.x, bot_rect.y))

    # for when we hit the right side
    if top_rect.x + top_rect.w >= res[0] or bot_rect.x + bot_rect.w >= res[0]:
        sliding_right = False

    # for when we hit left side
    if top_rect.x <= 0 or bot_rect.x <= 0:
        sliding_right = True

    if sliding_right:
        top_rect = top_rect.move(5, 0)
        bot_rect = bot_rect.move(5, 0)
    else:
        top_rect = top_rect.move(-5, 0)
        bot_rect = bot_rect.move(-5, 0)



    pygame.display.flip()
    clock.tick(60)