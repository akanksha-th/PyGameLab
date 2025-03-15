import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Dot Dash)
clock = pygame.time.Clock()
dt = 0
running = True

player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill("black")
    
    pygame.font.init()
    font = pygame.font.Font(pygame.font.match_font("courier"), 17)
    text = font.render("WASD to move | ESC to quit", True, 'white')
    screen.blit(text, (20,20))
    
    pygame.draw.circle(screen, 'red', player_pos, 40)
    pygame.draw.circle(screen, "white", player_pos, 40, 3) #circle's border
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300*dt
    if keys[pygame.K_s]:
        player_pos.y += 300*dt
    if keys[pygame.K_a]:
        player_pos.x -= 300*dt
    if keys[pygame.K_d]:
        player_pos.x += 300*dt

    pygame.display.flip()
    
    dt = clock.tick(60)/1000
pygame.quit()
