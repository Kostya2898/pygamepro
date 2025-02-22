import pygame  
import random
pygame.init()  

window = pygame.display.set_mode((500, 500))
player = pygame.Rect(250, 250, 50, 50)

game = True
while game:
    for e in pygame.event.get():  
        if e.type == pygame.QUIT:  
            game = False
        if e.type == pygame.MOUSEBUTTONDOWN:  
            if player.collidepoint(e.pos): 
               player.x = random.randint(0, 100)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]: 
        player.x -= 2
    if keys[pygame.K_d]:  
        player.x += 2
    if keys[pygame.K_w]:  
        player.y -= 2
    if keys[pygame.K_s]:  
        player.y += 2

    # Keep the player inside the window boundaries
    if player.x < 0:
        player.x = 0
    if player.x > 450:  # 500 - player.width
        player.x = 450
    if player.y < 0:
        player.y = 0
    if player.y > 450:  # 500 - player.height
        player.y = 450

    window.fill((255, 255, 0))  # Yellow background

    pygame.draw.rect(window, (54, 36, 65), player)

    pygame.display.update()
    pygame.time.Clock().tick(60)
