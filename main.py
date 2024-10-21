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

def spike_colliderect():
    global spike_exists, spike_rect, player_kill, explosion_rect, current_frame_explosion
    print('Kill!')
    spike_exists = False
    del spike_rect
    player_kill = True
    current_frame_explosion = 0
    explosion_rect.center = player_rect.center

# while True:
#     window.fill(BACKGROUND_COLOR)
#     window.blit(floor, floor_rect)
#
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#
#     keys = pygame.key.get_pressed()
#
#     if coin_exists and player_rect.colliderect(coin_rect):
#         coin_colliderect()
#
#     if coin_exists:
#         current_frame_coin = (current_frame_coin + 1) % 8
#         window.blit(coin[current_frame_coin], coin_rect)
#
#     if spike_exists and player_rect.colliderect(spike_rect):
#         spike_colliderect()
#
#     if spike_exists:
#         window.blit(spike, spike_rect)
#
#     if not player_kill:
#         if keys[pygame.K_RIGHT]:
#             if not floor_rect.left <= -520:
#                 floor_rect.centerx -= player_speed
#                 if coin_exists:
#                     coin_rect.centerx -= player_speed
#                 if spike_exists:
#                     spike_rect.centerx -= player_speed
#             if not player_kill:
#                 current_frame_right = (current_frame_right + 1) % 4
#                 window.blit(player_right[current_frame_right], player_rect)
#         elif keys[pygame.K_LEFT]:
#             if not floor_rect.left >= 125:
#                 floor_rect.centerx += player_speed
#                 if coin_exists:
#                     coin_rect.centerx += player_speed
#                 if spike_exists:
#                     spike_rect.centerx += player_speed
#             if not player_kill:
#                 current_frame_left = (current_frame_left + 1) % 4
#                 window.blit(player_left[current_frame_left], player_rect)
#         elif keys[pygame.K_UP]:
#             if not floor_rect.top >= 40:
#                 floor_rect.centery += player_speed
#                 if coin_exists:
#                     coin_rect.centery += player_speed
#                 if spike_exists:
#                     spike_rect.centery += player_speed
#             else:
#                 if not player_rect.top <= 60:
#                     player_rect.centery -= player_speed
#             if not player_kill:
#                 current_frame_up = (current_frame_up + 1) % 4
#                 window.blit(player_up[current_frame_up], player_rect)
#         elif keys[pygame.K_DOWN]:
#             if not floor_rect.top <= -200:
#                 floor_rect.centery -= player_speed
#                 if coin_exists:
#                     coin_rect.centery -= player_speed
#                 if spike_exists:
#                     spike_rect.centery -= player_speed
#             else:
#                 if not player_rect.top >= 200:
#                     player_rect.centery += player_speed
#             if not player_kill:
#                 current_frame_down = (current_frame_down + 1) % 4
#                 window.blit(player_down[current_frame_down], player_rect)
#         else:
#             window.blit(player, player_rect)
#     else:
#         # Анимация взрыва
#         if current_frame_explosion < len(explosion):
#             window.blit(explosion[current_frame_explosion], explosion_rect)
#             current_frame_explosion += 1
#         else:
#             # Действие после окончания анимации взрыва
#             pygame.quit()
#             sys.exit()
#
#     # Обновление текста и интерфейса
#     text_rect = font2.render(f'x={floor_rect.centerx} y={floor_rect.centery}', True, (255, 255, 255))
#     window.blit(line, line_rect)
#     window.blit(text_score, text_score_rect)
#     window.blit(line2, line2_rect)
#     window.blit(text_rect, text_rect_rect)
#
#     clock.tick(FPS)
#     pygame.display.update()

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

    if spike_exists:
        if player_rect.colliderect(spike_rect):
            spike_colliderect()

    if spike_exists:
        window.blit(spike, spike_rect)

    if pause_open:
        window.blit(menu, menu_rect)
        window.blit(restart, restart_rect)
        window.blit(play, play_rect)

    if not pause_open:
        if keys[pygame.K_RIGHT]:
            if not floor_rect.left <= -520:
                floor_rect.centerx -= player_speed
                if coin_exists:
                    coin_rect.centerx -= player_speed
                if spike_exists:
                    spike_rect.centerx -= player_speed
            if not player_kill:
                current_frame_right = (current_frame_right + 1) % 4
                window.blit(player_right[current_frame_right], player_rect)
        elif keys[pygame.K_LEFT]:
            if not floor_rect.left >= 125:
                floor_rect.centerx += player_speed
                if coin_exists:
                    coin_rect.centerx += player_speed
                if spike_exists:
                    spike_rect.centerx += player_speed
            if not player_kill:
                current_frame_left = (current_frame_left + 1) % 4
                window.blit(player_left[current_frame_left], player_rect)
        elif keys[pygame.K_UP]:
            if not floor_rect.top >= 40:
                floor_rect.centery += player_speed
                if coin_exists:
                    coin_rect.centery += player_speed
                if spike_exists:
                    spike_rect.centery += player_speed
            else:
                if not player_rect.top <= 60:
                    player_rect.centery -= player_speed
            if not player_kill:
                current_frame_up = (current_frame_up + 1) % 4
                window.blit(player_up[current_frame_up], player_rect)
        elif keys[pygame.K_DOWN]:
            if not floor_rect.top <= -200:
                floor_rect.centery -= player_speed
                if coin_exists:
                    coin_rect.centery -= player_speed
                if spike_exists:
                    spike_rect.centery -= player_speed
            else:
                if not player_rect.top >= 200:
                    player_rect.centery += player_speed
            if not player_kill:
                current_frame_down = (current_frame_down + 1) % 4
                window.blit(player_down[current_frame_down], player_rect)
        else:
            if not player_kill:
                window.blit(player, player_rect)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    if pause_rect.left < mouse_x < pause_rect.right and pause_rect.top < mouse_y < pause_rect.bottom:
        print('Ok')

    # Text
    text_rect = font2.render(f'x={floor_rect.centerx} y={floor_rect.centery}', True, (255, 255, 255))

    # Render
    window.blit(line, line_rect)
    window.blit(text_score, text_score_rect)
    window.blit(pause, pause_rect)
    window.blit(line2, line2_rect)
    window.blit(text_rect, text_rect_rect)

    #window.blit(explosion[current_frame_explosion], explosion_rect)

    clock.tick(FPS)
    pygame.display.update()