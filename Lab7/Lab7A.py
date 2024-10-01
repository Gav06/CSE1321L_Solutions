"""
Class:      CSE1321L
Section:    Module 4
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Lab:        7A
"""
import math

import pygame, sys

pygame.init()

resolution = (400, 400)
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

color = 0

# duration in seconds
duration_s = 5.0

# function to normalize value between zero and 1
def normalize(value, min, max):
    return (value - min) / (max - min)

while True:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)

    # use our total milliseconds mod by our duration and then divided by our duration (in millis)
    x = (pygame.time.get_ticks() % (1000 * duration_s)) / (1000 * duration_s)

    # multiply our value times 2pi so our sine wave makes a full period of the sine wave
    TWOPI = 2 * math.pi
    val = math.sin(x * TWOPI)

    # normalize our value between 0 and 1
    normal = 1.0 - (normalize(val, -1.0, 1.0))

    color = int(255 * normal)
    screen.fill(color=(color, color, color))
    pygame.display.flip()
    clock.tick(60)
