import pygame  # підключення бібліотеки
import random
pygame.init()  # запуск бібліотеки

# створення вікна
window = pygame.display.set_mode((500, 500))
player = pygame.Rect(250, 250, 50, 50)  # створення гравця у вигляді прямокутника

# запускаємо цикл гри
game = True
while game:
    for e in pygame.event.get():  
        if e.type == pygame.QUIT:  
            game = False
        if e.type == pygame.MOUSEBUTTONDOWN:  
            if player.collidepoint(e.pos): 
               player.x  = random.randint(0,100)

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]: 
        player.x -= 2
    if keys[pygame.K_d]:  
        player.x += 2
    if keys[pygame.K_w]:  
        player.y -= 2
    if keys[pygame.K_s]:  
        player.y += 2

    # перевірка на вихід за межі екрану
    if player.x < -50:  
        player.x = 500
    elif player.x > 500:  
        player.x = -50
    if player.y < -50: 
        player.y = 500
    elif player.y > 500:  
        player.y = -50

    # очищення вікна та оновлення зображення
    window.fill((255, 255, 0))  # жовтий фон
    pygame.draw.rect(window, (54, 36, 65), player)  # малювання гравця

    pygame.display.update()  # оновлення екрану
    pygame.time.Clock().tick(60)  # обмеження FPS
