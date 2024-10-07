import pygame, sys
from pygame import *
from pygame.locals import QUIT
import time
import random
import asyncio

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('pupya`s game')
NEON_BLUE = (173, 216, 230)

# Score
score = 0

# Floor
floor_page = 1

floor = pygame.image.load(f'src/world/floor.png')

floor_rect = floor.get_rect()
floor_rect.centerx = WINDOW_WIDTH // 2
floor_rect.centery = 295

# Player
player = pygame.image.load(f'src/player/3.png')
player = player.convert_alpha()

# Это переменная нужна чтобы хранить предыдущую координату игрока
backup_player_rect = 0

player_rect = player.get_rect()
player_rect.centerx = WINDOW_WIDTH // 2
player_rect.centery = WINDOW_HEIGHT // 2

player_down = []
player_up = []
player_left = []
player_right = []

for frame in range(0, 5):
    image = pygame.image.load(f'src/player/{frame}.png')
    image = image.convert_alpha()
    player_down.append(image)

for frame in range(12, 16):
    image = pygame.image.load(f'src/player/{frame}.png')
    image = image.convert_alpha()
    player_up.append(image)

for frame in range(4, 8):
    image = pygame.image.load(f'src/player/{frame}.png')
    image = image.convert_alpha()
    player_left.append(image)

for frame in range(8, 12):
    image = pygame.image.load(f'src/player/{frame}.png')
    image = image.convert_alpha()
    player_right.append(image)

current_frame_down = 0
current_frame_up = 0
current_frame_left = 0
current_frame_right = 0

# Text
pygame.font.init()

font = pygame.font.SysFont(name='JetBrains Mono Bold', size=60)

text_score = font.render(str(score), True, (255, 171, 0))
text_score_rect = text_score.get_rect()
text_score_rect.center = (70, 23)

# Ui
line = pygame.image.load(f'src/ui/line.png')

line_rect = line.get_rect()
line_rect.centerx = WINDOW_WIDTH // 2
line_rect.centery = 20

# Render
clock = pygame.time.Clock()
FPS = 20

while True:
    window.fill(NEON_BLUE)
    window.blit(floor, floor_rect)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            print(player_rect)
            print(floor_rect)
            player_speed = 5
            if not floor_rect[0] == -400:
                floor_rect.centerx -= player_speed
            current_frame_right = current_frame_right + 1
            if current_frame_right == 4:
                current_frame_right = 0
            window.blit(player_right[current_frame_right], player_rect)

        elif event.key == pygame.K_LEFT:
            print(player_rect)
            print(floor_rect)
            player_speed = 5
            if not floor_rect[0] == 0:
                floor_rect.centerx += player_speed
            current_frame_left = current_frame_left + 1
            if current_frame_left == 4:
                current_frame_left = 0
            window.blit(player_left[current_frame_left], player_rect)

        elif event.key == pygame.K_UP:
            print(player_rect)
            print(backup_player_rect)
            print(floor_rect)
            player_speed = 5
            if not player_rect[1] > backup_player_rect:
                floor_rect.centery += player_speed
            else:
                print('ok')
                if floor_rect[1] >= 40:
                    pass
                else:
                    print('ok')
                    player_rect.centery -= player_speed
            current_frame_up = current_frame_up + 1
            if current_frame_up == 4:
                current_frame_up = 0
            window.blit(floor, floor_rect)
            window.blit(player_up[current_frame_up], player_rect)

        elif event.key == pygame.K_DOWN:
            print(player_rect)
            print(floor_rect)
            player_speed = 5
            if not floor_rect[1] <= 0:
                backup_player_rect = player_rect[1]
                floor_rect.centery -= player_speed
            else:
                if not player_rect[1] >= 200:
                    player_rect.centery += player_speed
            current_frame_down = current_frame_down + 1
            if current_frame_down == 4:
                current_frame_down = 0
            window.blit(floor, floor_rect)
            window.blit(player_down[current_frame_down], player_rect)

    else:
        window.blit(player, player_rect)

    window.blit(line, line_rect)
    window.blit(text_score, text_score_rect)

    clock.tick(FPS)
    pygame.display.update()