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
floor_rect.centery = 215

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
player_kill = False

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

# Spike
spike = pygame.image.load('src/spike/spike.png')
spike = pygame.transform.scale(spike, (35, 35))
spike_rect = spike.get_rect()
spike_rect.centerx = WINDOW_WIDTH // 2
spike_rect.centery = WINDOW_WIDTH // 2 + 40

spike_exists = True

# Explosion
#explosion = []

#for frame in range(4, 7):
#    image = pygame.image.load(f'src/explosion/{frame}.png')
#    image = image.convert_alpha()
#    image = pygame.transform.scale(image, (40, 40))
#    #explosion.append(image)

#current_frame_explosion = 0
#explosion_rect = explosion[current_frame_explosion].get_rect()
#explosion_rect.centerx = WINDOW_WIDTH // 2
#explosion_rect.centery = WINDOW_WIDTH // 2

explosion = []

for frame in range(0, 4):
    image = pygame.image.load(f'src/explosion/{frame}.png')
    image = image.convert_alpha()
    image = pygame.transform.scale(image, (40, 40))
    explosion.append(image)

current_frame_explosion = 0
explosion_rect = explosion[current_frame_explosion].get_rect()
explosion_rect.centerx = WINDOW_WIDTH // 2
explosion_rect.centery = WINDOW_WIDTH // 2 + 40

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

pause = pygame.image.load('src/ui/pause.png')
pause_rect = pause.get_rect()
pause_rect.centerx = 375
pause_rect.centery = 20

pause_open = False

line2 = pygame.image.load('src/ui/line2.png')
line2_rect = line2.get_rect()
line2_rect.centerx = WINDOW_WIDTH // 2
line2_rect.centery = WINDOW_HEIGHT

menu = pygame.image.load('src/ui/menu.png')
menu = pygame.transform.scale(menu, (270, 225))
menu_rect = menu.get_rect()
menu_rect.centerx = WINDOW_WIDTH // 2
menu_rect.centery = WINDOW_WIDTH // 2 - 20

restart = pygame.image.load('src/ui/restart.png')
restart = pygame.transform.scale(restart, (100, 100))
restart_rect = restart.get_rect()
restart_rect.centerx = WINDOW_WIDTH // 2 - 60
restart_rect.centery = WINDOW_WIDTH // 2 - 20

play = pygame.image.load('src/ui/play.png')
play = pygame.transform.scale(play, (120, 120))
play_rect = restart.get_rect()
play_rect.centerx = WINDOW_WIDTH // 2 + 60
play_rect.centery = WINDOW_WIDTH // 2 - 30

# Render
clock = pygame.time.Clock()
FPS = 20