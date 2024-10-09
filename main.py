from pygame.locals import QUIT
from pygame import *
import pygame, sys
import asyncio

pygame.init()

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
BACKGROUND_COLOR = (141, 227, 255)
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('pupya`s Game')

# Score
score = 0

# Floor
floor = pygame.image.load('src/world/floor.png')
floor_rect = floor.get_rect()
floor_rect.centerx = WINDOW_WIDTH // 2
floor_rect.centery = 295

# Player
player = pygame.image.load('src/player/3.png')
player = player.convert_alpha()
player_rect = player.get_rect()
player_rect.centerx = WINDOW_WIDTH // 2
player_rect.centery = WINDOW_HEIGHT // 2

player_down = []
player_up = []
player_left = []
player_right = []

for frame in range(0, 4):
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

player_speed = 5

# Coin
coin = []

for frame in range(0, 8):
    image = pygame.image.load(f'src/coin/{frame}.png')
    image = image.convert_alpha()
    image = pygame.transform.scale(image, (40, 40))
    coin.append(image)

current_frame_coin = 0
coin_rect = coin[current_frame_coin].get_rect()
coin_rect.centerx = WINDOW_WIDTH // 2
coin_rect.centery = WINDOW_HEIGHT // 2

coin_exists = True

# Text
pygame.font.init()
font = pygame.font.SysFont('JetBrains Mono Bold', 60)
text_score = font.render(str(score), True, (255, 171, 0))
text_score_rect = text_score.get_rect()
text_score_rect.center = (70, 23)

# UI
line = pygame.image.load('src/ui/line.png')
line_rect = line.get_rect()
line_rect.centerx = WINDOW_WIDTH // 2
line_rect.centery = 20

# Render
clock = pygame.time.Clock()
FPS = 15

while True:
    window.fill(BACKGROUND_COLOR)
    window.blit(floor, floor_rect)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if coin_exists:
        current_frame_coin = (current_frame_coin + 1) % 8
        window.blit(coin[current_frame_coin], coin_rect)

    if player_rect.colliderect(coin_rect):
        print('Coin!')

    if keys[pygame.K_RIGHT]:
        if not floor_rect.left <= -520:
            floor_rect.centerx -= player_speed
            coin_rect.centerx -= player_speed
        current_frame_right = (current_frame_right + 1) % 4
        window.blit(player_right[current_frame_right], player_rect)

    elif keys[pygame.K_LEFT]:
        if not floor_rect.left >= 125:
            floor_rect.centerx += player_speed
            coin_rect.centerx += player_speed
        current_frame_left = (current_frame_left + 1) % 4
        window.blit(player_left[current_frame_left], player_rect)

    elif keys[pygame.K_UP]:
        if not floor_rect.top >= 40:
            floor_rect.centery += player_speed
            coin_rect.centery += player_speed
        else:
            if not player_rect.top <= 60:
                player_rect.centery -= player_speed
        current_frame_up = (current_frame_up + 1) % 4
        window.blit(player_up[current_frame_up], player_rect)

    elif keys[pygame.K_DOWN]:
        if not floor_rect.top <= -200:
            floor_rect.centery -= player_speed
            coin_rect.centery -= player_speed
        else:
            if not player_rect[1] >= 200:
                player_rect.centery += player_speed
        current_frame_down = (current_frame_down + 1) % 4
        window.blit(player_down[current_frame_down], player_rect)

    else:
        window.blit(player, player_rect)

    window.blit(line, line_rect)
    window.blit(text_score, text_score_rect)

    clock.tick(FPS)
    pygame.display.update()