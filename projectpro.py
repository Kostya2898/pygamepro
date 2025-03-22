import pygame

pygame.init()

# Створюємо вікно гри
window = pygame.display.set_mode((1020, 720), pygame.RESIZABLE)

# Завантажуємо фон
fon_image = pygame.image.load("fon2.jpg")
fon_rect = fon_image.get_rect()

# Завантажуємо зображення для гравця
player_image = pygame.image.load("player1.png")
player_rect = player_image.get_rect()

# Функція для масштабування фону
def scale_background():
    # Отримуємо розміри вікна
    window_width, window_height = window.get_size()
    
    # Масштабуємо фон за розмірами вікна, зберігаючи пропорції
    background = pygame.transform.scale(fon_image, (window_width, window_height))
    return background

# Швидкість і гравітація
gravity = 0.5  # прискорення гравітації
velocity_y = 0  # початкова швидкість по вертикалі
is_jumping = False  # чи в польоті
jump_height = -12  # сила стрибка

# Земля (розташування на фоні)
ground_y = window.get_height() // 2 - 45  # Земля буде на 100 пікселів вище середини

# Годинник для контролю кадрів
clock = pygame.time.Clock()

game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            fon_image = pygame.image.load("fon.jpeg")
            fon_rect = fon_image.get_rect()
            player_rect.x = 100
            player_rect.y = 100
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not is_jumping:
            # Стрибаємо
            velocity_y = jump_height
            is_jumping = True
        if event.type == pygame.VIDEORESIZE:
            window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
    
    # Масштабуємо фон згідно з розмірами вікна
    background = scale_background()

    # Заповнюємо вікно фоном
    window.blit(background, (0, 0))

    # Гравітація
    velocity_y += gravity  # збільшуємо швидкість по вертикалі

    # Оновлюємо координати гравця по вертикалі
    player_rect.y += velocity_y

    # Якщо гравець досяг землі
    if player_rect.y >= ground_y:
        player_rect.y = ground_y  # позиціонуємо гравця на землі
        is_jumping = False  # він більше не в польоті
        velocity_y = 0  # швидкість по вертикалі обнуляється

    # Малюємо гравця
    window.blit(player_image, player_rect)
    
    # Управління гравцем по горизонталі
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player_rect.x > 0:
        player_rect.x -= 3
    if keys[pygame.K_s] and player_rect.y < 720:
        player_rect.y += 3
    if keys[pygame.K_d] and player_rect.x < 1050:
        player_rect.x += 3
    if keys[pygame.K_w] and player_rect.y > 0:
        player_rect.y -= 3
    
    # Обновляємо екран
    clock.tick(160)
    pygame.display.update()

pygame.quit()
