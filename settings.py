from pygame.locals import QUIT
from pygame import *
import pygame, sys
import random

pygame.init()

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 330
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
coin_rect.centerx = random.randint(-110, 515)
coin_rect.centery = random.randint(60, 280)

coin_exists = True

# Sound
sound_coin = pygame.mixer.Sound('src/music/coin.mp3')

pygame.mixer.music.load('src/music/music.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Text
pygame.font.init()
font = pygame.font.SysFont('JetBrains Mono Bold', 60)
font2 = pygame.font.SysFont('JetBrains Mono Bold', 20)

text_score = font.render(str(score), True, (255, 171, 0))
text_score_rect = text_score.get_rect()
text_score_rect.center = (73, 23)

text_rect = font2.render(f'x={floor_rect.centerx} y={floor_rect.centery}', True, (255, 255, 255))
text_rect_rect = text_rect.get_rect()
text_rect_rect.center = (43, 323)

# UI
line = pygame.image.load('src/ui/line.png')
line_rect = line.get_rect()
line_rect.centerx = WINDOW_WIDTH // 2
line_rect.centery = 20

line2 = pygame.image.load('src/ui/line2.png')
line2_rect = line2.get_rect()
line2_rect.centerx = WINDOW_WIDTH // 2
line2_rect.centery = WINDOW_HEIGHT

# Render
clock = pygame.time.Clock()
FPS = 15