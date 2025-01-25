import pygame 
pygame.init() 

window = pygame.display.set_mode((500, 500))

player = pygame.Rect(10, 400, 70, 100)  
player_image = pygame.image.load("rocket.png")
player_image = pygame.transform.scale(player_image, (70, 100)) 

timer = pygame.time.Clock()
bullets = []
bullets2 = []
bullets_up = []
bullets_down = []

game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:  
                bullet = pygame.Rect(player.centerx, player.centery, 5, 5)
                bullets.append(bullet)
            if event.key == pygame.K_2: 
                bullet = pygame.Rect(player.centerx, player.centery, 5, 5)
                bullets2.append(bullet)
            if event.key == pygame.K_3:  
                bullet = pygame.Rect(player.centerx, player.centery, 5, 5)
                bullets_down.append(bullet)
            if event.key == pygame.K_4:  
                bullet = pygame.Rect(player.centerx, player.centery, 5, 5)
                bullets_up.append(bullet)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        player.x -= 5
    if keys[pygame.K_d]:
        player.x += 5

    if player.x < 0:
        player.x = 0
    if player.x > 500 - player.width:
        player.x = 500 - player.width

 
    player.y = 400

    window.fill((0, 0, 0))

    for b in bullets:  
        b.x += 4
        if b.x > 500:  
            bullets.remove(b)  
        pygame.draw.rect(window, (255, 0, 0), b)  
    for b in bullets2:  
        b.x -= 4
        if b.x < 0:  
            bullets2.remove(b)  
        pygame.draw.rect(window, (255, 255, 0), b)  
    for b in bullets_down:  
        b.y += 4
        if b.y > 500:  
            bullets_down.remove(b)  
        pygame.draw.rect(window, (0, 255, 0), b)  
    for b in bullets_up:  
        b.y -= 4
        if b.y < 0:  
            bullets_up.remove(b)  
        pygame.draw.rect(window, (0, 0, 255), b)  

    window.blit(player_image, player)

    pygame.display.update()
    timer.tick(30)

