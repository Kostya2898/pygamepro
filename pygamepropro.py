import pygame  
import random
pygame.init()  

window = pygame.display.set_mode((500, 500))
player = pygame.Rect(250, 250, 50, 50)  
level = "center"

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


    if level == "center":
        if player.x < -50:  
            player.x = 500
            level = "left"
        if player.x > 500:  
            player.x = -50
            level = "right"
        if player.y < -50:  
            player.y = 500
            level = "up"
        if player.y > 500:  
            player.y = -50
            level = "down"

    if level == "left" and player.x > 500:  
        player.x = -50
        level = "center"

    if level == "right" and player.x < -50:  
        player.x = 500
        level = "center"

    if level == "up" and player.y > 500:  
        player.y = -50
        level = 'center'

    if level == 'down' and player.y < -50:  
        player.y = 500
        level = 'center'


    if level == 'center':
        window.fill((255, 255, 0))  
    if level == 'left':
        window.fill((0, 255, 0))  
    if level == 'right':
        window.fill((0, 0, 255))  
    if level == 'up':
        window.fill((255, 0, 0))  
    if level == 'down':
        window.fill((0, 255, 255))  

   
    pygame.draw.rect(window, (54, 36, 65), player)

   
    pygame.display.update()
    pygame.time.Clock().tick(60)  