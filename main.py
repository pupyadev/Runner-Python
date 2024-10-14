from pygame.locals import QUIT
from pygame import *
import pygame, sys
import asyncio
from settings import *

# Function
def coin_colliderect():
    global score, text_score, coin_exists, coin_rect
    score = score + 1
    text_score = font.render(str(score), True, (255, 171, 0))
    sound_coin.play()
    coin_exists = False
    del coin_rect

while True:
    window.fill(BACKGROUND_COLOR)
    window.blit(floor, floor_rect)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if coin_exists:
        if player_rect.colliderect(coin_rect):
            coin_colliderect()

    if coin_exists:
        current_frame_coin = (current_frame_coin + 1) % 8
        window.blit(coin[current_frame_coin], coin_rect)

    if keys[pygame.K_RIGHT]:
        if not floor_rect.left <= -520:
            floor_rect.centerx -= player_speed
            if coin_exists:
                coin_rect.centerx -= player_speed
        current_frame_right = (current_frame_right + 1) % 4
        window.blit(player_right[current_frame_right], player_rect)
    elif keys[pygame.K_LEFT]:
        if not floor_rect.left >= 125:
            floor_rect.centerx += player_speed
            if coin_exists:
                coin_rect.centerx += player_speed
        current_frame_left = (current_frame_left + 1) % 4
        window.blit(player_left[current_frame_left], player_rect)
    elif keys[pygame.K_UP]:
        if not floor_rect.top >= 40:
            floor_rect.centery += player_speed
            if coin_exists:
                coin_rect.centery += player_speed
        else:
            if not player_rect.top <= 60:
                player_rect.centery -= player_speed
        current_frame_up = (current_frame_up + 1) % 4
        window.blit(player_up[current_frame_up], player_rect)
    elif keys[pygame.K_DOWN]:
        if not floor_rect.top <= -200:
            floor_rect.centery -= player_speed
            if coin_exists:
                coin_rect.centery -= player_speed
        else:
            if not player_rect.top >= 200:
                player_rect.centery += player_speed
        current_frame_down = (current_frame_down + 1) % 4
        window.blit(player_down[current_frame_down], player_rect)
    else:
        window.blit(player, player_rect)

    # Text
    text_rect = font2.render(f'x={floor_rect.centerx} y={floor_rect.centery}', True, (255, 255, 255))

    # Render
    window.blit(line, line_rect)
    window.blit(text_score, text_score_rect)
    window.blit(line2, line2_rect)
    window.blit(text_rect, text_rect_rect)

    clock.tick(FPS)
    pygame.display.update()