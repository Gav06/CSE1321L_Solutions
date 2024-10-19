"""
Class:      CSE1321L
Section:    Module 4
Term:       Fall 2024
Instructor: J. Pothuri
Name:       Gavin Conley
Assignment: 5A
"""
from venv import create

import pygame
import random
import math

# Class so we can store everything easily for each meteor
class Meteor:
    def __init__(self, rect, surface, motion, alive):
        self.rect = rect
        self.surface = surface
        self.motion = motion
        self.alive = alive


pygame.init()


res = (800, 800)
screen = pygame.display.set_mode(res)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 48)

score_start = pygame.time.get_ticks()
score_timer = 0
highscore = 0

death_timer = 0

meteor_delay = 5000
meteor_timer = pygame.time.get_ticks()

game_running = True
game_over = False

player_r = pygame.Rect(res[0] / 2 - 20, res[1] / 2 - 20, 40, 40)
player_s = pygame.Surface(player_r.size)
player_s.fill((255, 255, 255))

# sounds
explosion = pygame.mixer.Sound("Explosion.wav")
explosion.set_volume(0.8)

spawn = pygame.mixer.Sound("Spawn.wav")
spawn.set_volume(0.5)

# list of meteor objects
meteor_list = []

# Called when player hit
def kill_player():
    global game_over, death_timer
    explosion.play()
    death_timer = pygame.time.get_ticks()
    game_over = True


# self-explanatory
def reset_game():
    global score_start, death_timer, game_over, score_timer, player_r, player_s

    score_start = pygame.time.get_ticks()
    score_timer = 0
    death_timer = 0
    game_over = False
    meteor_list.clear()
    # calc co-ords to move player back to center
    dx = res[0] / 2 - player_r.x
    dy = res[1] / 2 - player_r.y
    player_r = player_r.move(dx, dy)
    player_s.fill((255, 255, 255))

# Clamps a numerical value
def clamp(value, low, high):
    return max(min(value, high), low)

def meteor_check(x1, y1):
    global player_r
    x2 = player_r.x
    y2 = player_r.y
    dist = math.sqrt(abs((x2 - x1)**2 + (y2 - y1)**2))
    return dist >= 200

# setup each meteor object
def create_meteor():
    global player_r

    meteor_size = random.randint(20, 60)

    # set to player's position just so we can skip to the loop
    random_x = player_r.x
    random_y = player_r.y
    while not meteor_check(random_x, random_y):
        random_x = random.randint(0, res[0] - meteor_size)
        random_y = random.randint(0, res[1] - meteor_size)

    r = random.randint(64, 255)
    g = random.randint(64, 255)
    b = random.randint(64, 255)
    surf = pygame.Surface((meteor_size, meteor_size))
    surf.fill((r, g, b))
    rect = pygame.Rect(random_x, random_y, meteor_size, meteor_size)

    speed = 10.0
    dx = speed * (-1 if random_x > res[0] / 2 else 1) + (score_timer * 0.25)
    dy = speed * (-1 if random_y > res[1] / 2 else 1) + (score_timer * 0.25)

    spawn.play()
    return Meteor(rect, surf, (dx, dy), True)


# Move the player via user input, and keep them within the screen
def move_player(keys):
    global player_r

    move_x = 0
    move_y = 0
    # vert
    if keys[pygame.K_w]:
        move_y -= 5
    if keys[pygame.K_s]:
        move_y += 5
    # horz
    if keys[pygame.K_d]:
        move_x += 5
    if keys[pygame.K_a]:
        move_x -= 5

    # keep our player within bounds
    if player_r.right + move_x > res[0] or player_r.left + move_x < 0:
        move_x = 0

    if player_r.top + move_y < 0 or player_r.bottom + move_y > res[1]:
        move_y = 0

    player_r = player_r.move(move_x, move_y)


def __main__():
    global game_running, score_timer, meteor_delay, meteor_timer, game_over, highscore

    meteor_list.append(create_meteor())
    while game_running:
        events = pygame.event.get()
        keys = pygame.key.get_pressed()

        for e in events:
            match e.type:
                case pygame.QUIT:
                    game_running = False
                    break

        if score_timer > highscore:
            highscore = score_timer

        # update stuff
        if game_over:
            player_s.fill((128, 0, 0))
            if pygame.time.get_ticks() - death_timer >= 3000:
                reset_game()
        else:
            score_timer = (pygame.time.get_ticks() - score_start) // 1000
            meteor_delay = clamp(5000 - ((pygame.time.get_ticks() - score_start) / 5), 500, 5000)


            if pygame.time.get_ticks() - meteor_timer >= meteor_delay:
                meteor_timer = pygame.time.get_ticks()
                meteor_list.append(create_meteor())

            # add meteor if necessary

            # move player
            move_player(keys)

            # update meteors
            remove_list = []
            for meteor in meteor_list:
                # move the rect based on dx and dy
                meteor.rect = meteor.rect.move(meteor.motion[0], meteor.motion[1])

                if not meteor.alive or (meteor.rect.x < -meteor.rect.w
                        or meteor.rect.x > res[0] + meteor.rect.w
                        or meteor.rect.y < -meteor.rect.h
                        or meteor.rect.y > res[1] + meteor.rect.h):
                    remove_list.append(meteor)
                    continue

                # check if player hit
                if player_r.colliderect(meteor.rect):
                    kill_player()

            for removed in remove_list:
                meteor_list.remove(removed)


        # render stuff
        screen.fill((0, 0, 0))
        screen.blit(player_s, player_r.topleft)

        # for meteor in meteor_list:
        for meteor in meteor_list:
            screen.blit(meteor.surface, (meteor.rect.x, meteor.rect.y))

        # draw text
        fs = font.render(f"Score: {score_timer}", True, (255, 255, 255))
        screen.blit(fs, (10, 10))
        hs = font.render(f"Highscore: {highscore}", True, (255, 255, 255))
        screen.blit(hs, (10, 40))

        # game over text
        if game_over:
            death = font.render(f"Game Over! Score: {score_timer}", True, (196, 196, 196))
            text_x = (res[0] / 2) - (death.get_width() / 2)
            text_y = (res[1] / 2) - (death.get_height() / 2)
            screen.blit(death, (text_x, text_y))
        ###
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    __main__()