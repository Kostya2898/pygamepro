import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))
background_color = (0, 0, 0)  # Чорний колір

player = pygame.Rect(100,100,50,50)

walls =  [pygame.Rect(50,50,600,30),#верня стіна
          pygame.Rect(650,50,30,400),
          pygame.Rect(50,450,630,30),
          pygame.Rect(50,450,630,30),
          pygame.Rect(50,150,330,30)
          ]

# Головний цикл програми
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    # Заповнення фону
    window.fill(background_color)

    pygame.draw.rect(window,(255,0,0),player)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.x -=5
        for i in walls:
            if player.colliderect(i):
                player.x += 5
    if keys[pygame.K_d]:
        player.x += 5
    if keys[pygame.K_w]:
        player.y -= 5
    if keys[pygame.K_s]:
        player.y += 5


    for i in walls:
        pygame.draw.rect(window,(255,0,0),i)
    # Оновлення екрану
    pygame.display.update()
    # Встановлення частоти кадрів
    pygame.time.Clock().tick(60)