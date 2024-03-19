import pygame
import sys


pygame.init()


WIDTH, HEIGHT = 800, 600


WHITE = (255, 255, 255)
RED = (255, 0, 0)


ball_radius = 25
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_speed = 20


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Exercise 2.Ball")
clock = pygame.time.Clock()


running = True
while running:
    screen.fill(WHITE)
    
    
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP:
                if ball_y - ball_speed >= ball_radius:
                    ball_y -= ball_speed
            elif event.key == pygame.K_DOWN:
                if ball_y + ball_speed <= HEIGHT - ball_radius:
                    ball_y += ball_speed
            elif event.key == pygame.K_LEFT:
                if ball_x - ball_speed >= ball_radius:
                    ball_x -= ball_speed
            elif event.key == pygame.K_RIGHT:
                if ball_x + ball_speed <= WIDTH - ball_radius:
                    ball_x += ball_speed
                    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()