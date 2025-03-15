import pygame
import random

pygame.init()
pygame.display.set_caption("Bouncing Ball")

w, h = 700, 700
screen = pygame.display.set_mode((w, h))

clock = pygame.time.Clock()

# --------------CREATING THE ELEMENTS---------------
# Ball
ball_r = 10
ball_x, ball_y = w//2, h//2
speed = 4 * random.choice([-1, 1])
ball_speed_x, ball_speed_y = speed, speed

# Paddle
paddle_w, paddle_h = 100, 10
paddle_speed = 7
top_paddle = pygame.Rect((w - paddle_w) // 2, 20, paddle_w, paddle_h)
bottom_paddle = pygame.Rect((w - paddle_w) // 2, (h - 20), paddle_w, paddle_h)
left_paddle = pygame.Rect(20, (h - paddle_w) // 2, paddle_h, paddle_w)
right_paddle = pygame.Rect((w - 20), (h - paddle_w) // 2, paddle_h, paddle_w)

# --------------THE GAME LOOP---------------
running = True
while running:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    # Moving paddles using WASD and arrow_keys
    # TOP PADDLE
    if keys[pygame.K_LEFT] and top_paddle.left > 0:
        top_paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and top_paddle.right < w:
        top_paddle.x += paddle_speed
        
    # BOTTOM PADDLE
    if keys[pygame.K_a] and bottom_paddle.left > 0:
        bottom_paddle.x -= paddle_speed
    if keys[pygame.K_d] and bottom_paddle.right < w:
        bottom_paddle.x += paddle_speed
    
    # LEFT PADDLE
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= paddle_speed
    if keys[pygame.K_s] and left_paddle.bottom < h:
        left_paddle.y += paddle_speed
    
    # RIGHT PADDLE
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle.bottom < h:
        right_paddle.y += paddle_speed 
        
    # Ball Movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    
    if top_paddle.colliderect((ball_x - ball_r, ball_y - ball_r, ball_r * 2, ball_r * 2)) and ball_speed_y < 0:
        ball_speed_y *= -1
    if bottom_paddle.colliderect((ball_x - ball_r, ball_y - ball_r, ball_r * 2, ball_r * 2)) and ball_speed_y > 0:
        ball_speed_y *= -1
    if left_paddle.colliderect((ball_x - ball_r, ball_y - ball_r, ball_r * 2, ball_r * 2)) and ball_speed_x < 0:
        ball_speed_x *= -1
    if right_paddle.colliderect((ball_x - ball_r, ball_y - ball_r, ball_r * 2, ball_r * 2)) and ball_speed_x > 0:
        ball_speed_x *= -1
    
    # Game Over if Ball Escapes
    if ball_x < 0 or ball_x > w or ball_y < 0 or ball_y > h:
        screen.fill("black")
        font = pygame.font.Font(None, 40)
        text = font.render("Game Over!! RESTARTING.....", True, 'red')
        screen.blit(text, (w // 2 - 150, h // 2 ))
        pygame.display.flip()
        pygame.time.delay(2000) # 2 seconds' wait
        ball_x, ball_y = w//2, h//2
        ball_speed_x, ball_speed_y = speed, speed
    
    # Draw Ball      
    pygame.draw.circle(screen, 'white', (ball_x, ball_y), ball_r)
    
    # Draw Paddles
    pygame.draw.rect(screen, 'white', top_paddle)
    pygame.draw.rect(screen, 'white', bottom_paddle)
    pygame.draw.rect(screen, 'white', left_paddle)
    pygame.draw.rect(screen, 'white', right_paddle)
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()