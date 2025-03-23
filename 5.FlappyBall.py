import pygame
import time

pygame.init()
pygame.display.set_caption("Flappy Ball Game")

w, h = 400, 600
screen = pygame.display.set_mode((w,h))

def restart_game():
    time.sleep(2)
    game_loop()

def game_loop():
    ball_r = 15
    ball_x, ball_y = w//4, h//2
    ball_velocity = 0
    gravity = 0.5
    jump_strength = -8

    running = True
    clock = pygame.time.Clock()
    
    while running:
        screen.fill("black")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ball_velocity = jump_strength
                    
        ball_velocity += gravity
        ball_y += ball_velocity
        
        if ball_y <= 0:
            screen.fill("black")
            font = pygame.font.Font(None, 50)
            text = font.render("YOU WIN!!!", True, 'white')
            screen.blit(text, (w//2 - 100, h//2))
            pygame.display.flip()
            restart_game()
            return
        elif ball_y >= h:
            screen.fill("black")
            font = pygame.font.Font(None, 20)
            text = font.render("YOU LOST!! RESTARTING THE GAME!!!", True, 'white')
            screen.blit(text, (w//2 - 100, h//2))
            pygame.display.flip()
            restart_game()
            return
        
        pygame.draw.circle(screen, 'blue', (ball_x, int(ball_y)), ball_r)
        
        pygame.display.flip()
        clock.tick(60)

game_loop()  
pygame.quit()