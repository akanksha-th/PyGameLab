import pygame

pygame.init()
w, h = 800, 600
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("Brick Breaker")

clock = pygame.time.Clock()

# ---------- CREATING GAME ELEMENTS------------

# Paddle
pad_w, pad_h = 100, 10
pad_color = 'white'
pad_x = (w-pad_w) // 2
pad_y = h - 50
pad_speed = 7

# Ball
ball_x, ball_y = w//2, h//2
ball_r = 10
ball_speed_x, ball_speed_y = 3, 3

# Bricks
brick_w, brick_h = 80, 20
bricks = []
for row in range(5):
    for col in range(10):
        brick_x = col * (brick_w + 10)
        brick_y = row * (brick_h + 10)
        bricks.append(pygame.Rect(brick_x, brick_y, brick_w, brick_h))


# ---------- THE WORKING OF THE GAME------------
running = True
while running:
    screen.fill("black")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Moving the Paddle (it'll move in x direction only)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and pad_x>0:
        pad_x -= pad_speed
    if keys[pygame.K_RIGHT] and pad_x < w - pad_w:
        pad_x += pad_speed
    
    # Moving the Ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    
    # Ball collision with wall
    if (ball_x - ball_r <=0) or (ball_x + ball_r >= w):
        ball_speed_x *= -1
    if ball_y - ball_r <= 0:
        ball_speed_y *= -1
        
    # Ball collision with paddle
    if (pad_y <= (ball_y + ball_r) <= (pad_y + pad_h)) and (pad_x <= ball_x <= (pad_x + pad_w)):
        ball_speed_y *= -1
        
    # Ball collision with bricks
    for brick in bricks[:]:
        if brick.collidepoint(ball_x, ball_y):
            bricks.remove(brick)
            ball_speed_y *= -1
            break
    
    # Draw Paddle
    pygame.draw.rect(screen, pad_color, (pad_x, pad_y, pad_w, pad_h))
    
    # Draw Ball
    pygame.draw.circle(screen, 'white', (ball_x, ball_y), ball_r)
    
    # Draw Bricks
    for brick in bricks:
        pygame.draw.rect(screen, 'red', brick)
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()