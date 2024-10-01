import pygame

screen = pygame.display.set_mode((500,500))

surf1 = pygame.Surface((100,100))
surf1.fill((255,0,0))
surf2 = pygame.Surface((50,50))
surf2.fill((0,255,0))

while True:
    surf1.blit(surf2, (0, 0))
    screen.blit(surf1, (250,250))

    pygame.display.flip()