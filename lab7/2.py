import pygame
import sys


pygame.init()


WIDTH, HEIGHT =800, 600


WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ex2")


music_file = 'hymn.mp3'

music_playing = False


font = pygame.font.SysFont(None, 24)
text_load = font.render("Load ", True, WHITE)
text_play_once = font.render("Play", True, WHITE)
text_play_loop = font.render("Loop", True, WHITE)
text_stop = font.render("Stop", True, WHITE)


load_rect = text_load.get_rect(topleft=(10, 10))
play_once_rect = text_play_once.get_rect(topleft=(10, 50))
play_loop_rect = text_play_loop.get_rect(topleft=(10, 90))
stop_rect = text_stop.get_rect(topleft=(10, 130))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if load_rect.collidepoint(event.pos):
                pygame.mixer.music.load(music_file)
            elif play_once_rect.collidepoint(event.pos):
                pygame.mixer.music.play(0)
                music_playing = True
            elif play_loop_rect.collidepoint(event.pos):
                pygame.mixer.music.play(-1)
                music_playing = True
            elif stop_rect.collidepoint(event.pos):
                pygame.mixer.music.stop()
                music_playing = False
    
    
    screen.fill(GRAY)
    pygame.draw.rect(screen, GREEN, load_rect, border_radius=10)
    pygame.draw.rect(screen, GREEN if music_playing else RED, play_once_rect, border_radius=10)
    pygame.draw.rect(screen, GREEN if music_playing else RED, play_loop_rect, border_radius=10)
    pygame.draw.rect(screen, RED, stop_rect, border_radius=10)
    screen.blit(text_load, load_rect.topleft)
    screen.blit(text_play_once, play_once_rect.topleft)
    screen.blit(text_play_loop, play_loop_rect.topleft)
    screen.blit(text_stop, stop_rect.topleft)
    
    pygame.display.flip()




