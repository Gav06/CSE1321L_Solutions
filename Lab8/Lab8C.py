"""
Class:      CSE1321L
Section:    Module 4
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Lab:        8C
"""

import pygame

pygame.init()

res = (500, 500)
screen = pygame.display.set_mode(res)
clock = pygame.time.Clock()

player_size = (50, 50)
origin = ((res[0] / 2) - (player_size[0] / 2), (res[1] / 2) - (player_size[1] / 2))
player = pygame.Rect(origin[0], origin[1], player_size[0], player_size[1])
surface = pygame.Surface(player.size)
surface.fill((0, 0, 255))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    moveX = 0
    moveY = 0
    # vert
    if keys[pygame.K_w]:
        moveY -= 5
    if keys[pygame.K_s]:
        moveY += 5
    # horz
    if keys[pygame.K_d]:
        moveX += 5
    if keys[pygame.K_a]:
        moveX -= 5

    # keep our player within bounds
    if player.right + moveX > res[0] or player.left + moveX < 0:
        moveX = 0

    if player.top + moveY < 0 or player.bottom + moveY > res[1]:
        moveY = 0

    player = player.move(moveX, moveY)


    # logic to reset player
    if keys[pygame.K_r]:
        dx = origin[0] - player.x
        dy = origin[1] - player.y
        player = player.move(dx, dy)

    screen.fill((0, 0, 0))
    screen.blit(surface, (player.x, player.y))

    pygame.display.flip()
    clock.tick(60)