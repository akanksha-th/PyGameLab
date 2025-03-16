import pygame

pygame.init()
pygame.display.set_caption("Character Sprite in Pygame")

w, h = 1200, 300
screen = pygame.display.set_mode((w,h))

clock = pygame.time.Clock()

#sprite_sheet = pygame.image.load("C:/Users/Akanksha/Downloads/demo_sprite_sheet.png").convert_alpha()
sprite_sheet = pygame.image.load("C:/Users/Akanksha/Downloads/demo_sprite_sheet_nobg.png").convert_alpha()
sprite_w, sprite_h = 120.6667, 139
animation_frames = 3

frames = []
for i in range(animation_frames):
    frame = sprite_sheet.subsurface((i * sprite_w, 0, sprite_w, sprite_h))
    frames.append(frame)
    
character_x, character_y = 0, h-sprite_h
frame_index = 0
animation_speed = 0.1

font_small = pygame.font.Font(None, 40)
font_large = pygame.font.Font(None, 60)
text_message = "Hold keys to move the character across!"
frame_counter = 0

# ---------------THE GAME LOOP------------------
running = True
while running:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_x -= 5
        frame_index += animation_speed
    elif keys[pygame.K_RIGHT]:
        character_x += 5
        frame_index += animation_speed
    else:
        frame_index = 0
        
    # Restarting the Game
    if character_x > w or character_x < 0:
        screen.fill("black")
        font = pygame.font.Font(None, 40)
        text1 = font.render("Game Over!!", True, 'red')
        text2 = font.render("RESTARTING.....", True, 'red')
        text1_rect = text1.get_rect(center=(w // 2, h // 2 - 20))
        text2_rect = text2.get_rect(center=(w // 2, h // 2 + 20))
        screen.blit(text1, text1_rect)
        screen.blit(text2, text2_rect)
        pygame.display.flip()
        pygame.time.delay(2000)
        character_x, character_y = 0, h-sprite_h
        frame_index = 0
        animation_speed = 0.1
        
    frame_index = frame_index % animation_frames
    screen.blit(frames[int(frame_index)], (character_x, character_y))
    
    if frame_counter // 30 % 2 == 0:
        text_surface = font_small.render(text_message, True, 'white')
    else:
        text_surface = font_large.render(text_message, True, 'white')
    
    text_rect = text_surface.get_rect(center=(w // 2, 20))
    screen.blit(text_surface, text_rect)
    
    pygame.display.flip()
    frame_counter += 1
    clock.tick(60)
    
pygame.quit()
