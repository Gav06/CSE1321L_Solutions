"""
Class:      CSE1321L
Section:    Module 4
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Lab:        8A
"""

import pygame

pygame.init()

res = (400, 400)
screen = pygame.display.set_mode(res)
clock = pygame.time.Clock()

r1 = pygame.Rect((res[0] / 2) - 25, 0, 50, 400)
s1 = pygame.Surface((r1.w, r1.h))


r2 = pygame.Rect(0, (res[1] / 2) - 25, 50, 50)
s2 = pygame.Surface(r2.size)
s2.fill((0, 0, 255))

dirx = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    r2 = r2.move(5 * dirx, 0)

    if (r2.x + r2.w) > res[0] or r2.x < 0:
        dirx *= -1


    if r1.colliderect(r2):
        s1.fill((0, 255, 0))
    else:
        s1.fill((255, 0, 0))

    screen.fill((0, 0, 0))
    screen.blit(s1, (r1.x, r1.y))
    screen.blit(s2, (r2.x, r2.y))


    pygame.display.flip()
    clock.tick(60)