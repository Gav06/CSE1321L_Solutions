"""
Class:      CSE1321L
Section:    Module 4
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Lab:        9
"""

import pygame

pygame.init()
pygame.mixer.init()

res = (500, 500)
origin = (res[0] / 2, res[1] / 2)
screen = pygame.display.set_mode(res)
clock = pygame.time.Clock()
channel = pygame.mixer.Channel(1)

# width & height
bsize = 100

# Sprites
BUTTON_ON = pygame.image.load("button-7086658_640_on.png").convert_alpha()
BUTTON_OFF = pygame.image.load("button-7086658_640_off.png").convert_alpha()
LASER = pygame.image.load("laser-98735_640.png").convert_alpha()
# Scaled
ON_S = pygame.transform.scale(BUTTON_ON, (bsize, bsize))
OFF_S = pygame.transform.scale(BUTTON_OFF, (bsize, bsize))
LASER_S = pygame.transform.scale(LASER, (bsize, bsize))

# Sounds
SOUND_BLASTER = pygame.mixer.Sound("blaster-2-81267.mp3")
SOUND_ON = pygame.mixer.Sound("power-up-7103.mp3")
SOUND_OFF = pygame.mixer.Sound("power-down-7103.mp3")

# Rects
fire_rect = pygame.Rect(origin[0] - (bsize / 2), origin[1] - (bsize / 2), bsize, bsize)
on_rect = pygame.Rect(fire_rect.x - bsize - 20, fire_rect.y, bsize, bsize)
off_rect = pygame.Rect(fire_rect.right + 20, fire_rect.y, bsize, bsize)

# Fonts
f_small = pygame.font.Font(None, 32)
f_large = pygame.font.Font(None, 64)


OFF = 0
CHARGING = 1
DISCHARGING = 2
READY = 3
SHOOTING = 4

system_state = OFF

def get_status(state):
    match state:
        case 0:
            return "Off"
        case 1:
            return "Charging"
        case 2:
            return "Discharging"
        case 3:
            return "Ready"
        case 4:
            return "Shooting"



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if on_rect.collidepoint(event.pos):
                if system_state == OFF:
                    system_state = CHARGING
                    channel.play(SOUND_ON)
            elif off_rect.collidepoint(event.pos):
                if system_state == READY:
                    system_state = DISCHARGING
                    channel.play(SOUND_OFF)
            elif fire_rect.collidepoint(event.pos):
                if system_state == READY:
                    system_state = SHOOTING
                    channel.play(SOUND_BLASTER)

    # update system state based on if the sound we queued is currently playing anymore
    if not channel.get_busy():
        if system_state == CHARGING or system_state == SHOOTING:
            system_state = READY
        elif system_state == DISCHARGING:
            system_state = OFF

    screen.fill((255, 255, 255))

    # Draw buttons
    screen.blit(LASER_S, (fire_rect.x, fire_rect.y))
    screen.blit(ON_S, (on_rect.x, on_rect.y))
    screen.blit(OFF_S, (off_rect.x, off_rect.y))
    # Button text
    power_up = f_small.render("Power Up", True, (0, 0, 0))
    screen.blit(power_up, (on_rect.centerx - (power_up.get_width() / 2), on_rect.bottom + 20))

    shoot = f_small.render("Shoot", True, (0, 0, 0))
    screen.blit(shoot, (fire_rect.centerx - (shoot.get_width() / 2), fire_rect.bottom + 20))

    power_down = f_small.render("Power Down", True, (0, 0, 0))
    screen.blit(power_down, (off_rect.centerx - (power_down.get_width() / 2), off_rect.bottom + 20))

    # Large text
    status_msg = get_status(system_state)
    status = f_large.render(status_msg, True, (0, 0, 0))
    status_x = origin[0] - (status.get_width() / 2)
    status_y = origin[1] - (status.get_height() / 2) - 80
    screen.blit(status, (status_x, status_y))

    pygame.display.flip()
    clock.tick(60)