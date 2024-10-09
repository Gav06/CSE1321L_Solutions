"""
Class:      CSE1321L
Section:    Module 3
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Assignment: 4A
"""

import pygame, sys, random

user_score = 0

pygame.init()

res = (800, 600)
screen = pygame.display.set_mode(res)
clock = pygame.time.Clock()

# re-usable rects for our game objects
basket_rect = pygame.Rect(0, 0, 100, 20)
basket_surf = pygame.Surface((basket_rect.w, basket_rect.h))
basket_surf.fill((255, 255, 255))

fruit_rect = pygame.Rect(0, 0, 20, 20)
fruit_surf = pygame.Surface((fruit_rect.w, fruit_rect.h))
fruit_surf.fill((255, 0, 0))

# returns a surface for fruit, and updates rect position
def setup(fruit, basket):
    rand_x = random.randint(0 + fruit.w, res[0] - fruit.h)
    fruit.x = rand_x
    fruit.y = fruit.h

    basket.y = res[1] - (basket.h * 2)

# returns if fruit should respawn, also adds to score if touches basket
# params: rect, rect
# returns: bool
def fruit_check(fruit, basket):
    if fruit.y > res[1]:
        return True
    else:
        return basket.colliderect(fruit)

setup(fruit_rect, basket_rect)

running = True
while running:
    """ game logic section """
    # exit on window close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not running:
        break
    # update fruit
    fruit_rect = fruit_rect.move(0, 3)
    if fruit_check(fruit_rect, basket_rect):
        user_score += 1
        setup(fruit_rect, basket_rect)
    # update basket
    move_x = 0
    keys = pygame.key.get_pressed()
    # use individual if statements, so they cancel out if both are pressed
    if keys[pygame.K_LEFT]:
        move_x -= 5
    if keys[pygame.K_RIGHT]:
        move_x += 5
    # move and clamp the position to be within the bounds of the screen
    basket_rect = basket_rect.move(move_x, 0)
    if basket_rect.x <= 0:
        basket_rect.x = 0
    elif basket_rect.x + basket_rect.w >= res[0]:
        basket_rect.x = res[0] - basket_rect.w

    """ game render section """

    # fill screen with black
    screen.fill((0, 0, 0))
    # draw surfaces
    screen.blit(fruit_surf, (fruit_rect.x, fruit_rect.y))
    screen.blit(basket_surf, (basket_rect.x, basket_rect.y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print(f"Score: {user_score}")