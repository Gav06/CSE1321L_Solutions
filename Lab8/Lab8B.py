"""
Class:      CSE1321L
Section:    Module 4
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Lab:        8B
"""

import pygame

pygame.init()

res = (400, 400)
screen = pygame.display.set_mode(res)
clock = pygame.time.Clock()

r1 = pygame.Rect((res[0] / 2) - 25, 0, 50, 400)
s1 = pygame.Surface((r1.w, r1.h))

# dimensions of our box
box_d = (50, 50)

box1 = pygame.Rect(0, (res[1] / 2) - (box_d[1] / 2), box_d[0], box_d[1])
box2 = pygame.Rect(0, 0, box_d[0], box_d[1])
box3 = pygame.Rect(0, res[1] - box_d[1], box_d[0], box_d[1])
box_surf = pygame.Surface(box1.size)
box_surf.fill((0, 0, 255))

dir1 = 1
dir2 = 1
dir3 = 1

def should_bounce(rect):
    return (rect.x + rect.w) > res[0] or rect.x < 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # box 1 (middle)
    box1 = box1.move(dir1 * 5, 0)
    if should_bounce(box1):
        dir1 *= -1

    # box 2 (top)
    box2 = box2.move(dir2 * 10, 0)
    if should_bounce(box2):
        dir2 *= -1

    # box3 (bottom)
    box3 = box3.move(dir3 * 20, 0)
    if should_bounce(box3):
        dir3 *= -1

    if r1.collidelist([box1, box2, box3]) is not -1:
        s1.fill((0, 255, 0))
    else:
        s1.fill((255, 0, 0))

    screen.fill((0, 0, 0))
    screen.blit(s1, (r1.x, r1.y))

    screen.blit(box_surf, (box1.x, box1.y))
    screen.blit(box_surf, (box2.x, box2.y))
    screen.blit(box_surf, (box3.x, box3.y))

    pygame.display.flip()
    clock.tick(60)