import pygame
pygame.init()

window = pygame.display.set_mode((800, 600))
background_color = (0, 0, 0)  # Чорний колір

player = pygame.Rect(70,70,30,30) # (x,y,ширина,висота)
walls = [pygame.Rect(50,50,200,10),
         pygame.Rect(250,50,10,120),
         pygame.Rect(50,50,10,450),
         pygame.Rect(50,350,100,10),
         pygame.Rect(50,490,590,10),
         pygame.Rect(640,50,10,450),
         pygame.Rect(350,50,300,10),
         pygame.Rect(500,380,150,10),
         pygame.Rect(150,170,350,10),
         pygame.Rect(500,170,10,250),
         pygame.Rect(150,170,10,250),
         pygame.Rect(150,410,360,10)
         
         
         
         
         
         
         ]
bullets = []
# Головний цикл програми
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                bullet = pygame.Rect(player.x,player.y,5,5)
                bullets.append(bullet)
    window.fill(background_color)
    for b in bullets:
        b.y += 3
        pygame.draw.rect(window,(255,0,0),b)
        if b.colliderect(walls[1]):
            walls[1].x = 1000
    
    for wall in walls:
        pygame.draw.rect(window,(255,0,0),wall)

    pygame.draw.rect(window,(255,0,0),player)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.x -= 5
        for wall in walls:
            if player.colliderect(wall):
                player.x += 5
    if keys[pygame.K_d]:
        player.x += 5
    if keys[pygame.K_w]:
        player.y -= 5
    if keys[pygame.K_s]:
        player.y += 5

    pygame.display.update()
    pygame.time.Clock().tick(60)