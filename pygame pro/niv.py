import pygame

pygame.init()
obj = pygame.Rect(200, 200, 100, 100)
window = pygame.display.set_mode((800, 600))
zoom = 1
color = (255, 0, 0)

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                print("Натиснуто ліву клавішу")
            if e.button == 3:
                print("Натиснуто праву клавішу")
            if e.button == 4:
                print("Скроллінг вверх")
                zoom += 0.05
                if color == (255, 0, 0):
                    color = (0, 255, 0)
                elif color == (0, 255, 0):
                    color = (0, 0, 255)
                else:
                    color = (255, 0, 0)
            if e.button == 5:
                print("Скроллінг вниз")
                zoom -= 0.05
                if zoom < 0.1:
                    zoom = 0.1
                if color == (255, 0, 0):
                    color = (0, 255, 0)
                elif color == (0, 255, 0):
                    color = (0, 0, 255)
                else:
                    color = (255, 0, 0)

    x, y = pygame.mouse.get_pos()

    # Задаємо нову позицію квадрата, якщо курсор на ньому
    if obj.x < x < obj.x + 100 and obj.y < y < obj.y + 100:
        if obj.centerx < 400:
            obj.x += 5
        elif obj.centerx > 400:
            obj.x -= 5
        if obj.centery < 300:
            obj.y += 5
        elif obj.centery > 300:
            obj.y -= 5

    window.fill((0, 0, 0))

 
    if obj.x < x < obj.x + 100 and obj.y < y < obj.y + 100:
        pygame.draw.rect(window, (0, 255, 0), obj)
    else:
        pygame.draw.rect(window, (0, 0, 250), obj)

    pygame.draw.circle(window, color, (400, 300), int(50 * zoom))
    pygame.display.update()

