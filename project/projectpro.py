import pygame
import sys

pygame.init()

# Константи
WINDOW_WIDTH, WINDOW_HEIGHT = 1020, 720
GROUND_OFFSET = 320  # Земля на 320 пікселів вище
GRAVITY = 0.5
JUMP_POWER = -10
PLAYER_SPEED = 6  # Збільшена швидкість руху гравця
MAX_PLAYER_X = 200000  # Збільшена межа руху гравця

# Створення вікна гри
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Digger Machine")

# Завантаження зображень
try:
    menu_bg = pygame.image.load("fon2.jpg")
    game_bg = pygame.image.load("fon.jpeg")
    player_image = pygame.image.load("player1.png")
except pygame.error as e:
    print(f"Помилка завантаження зображення: {e}")
    pygame.quit()
    sys.exit()

# Масштабування гравця
player_image = pygame.transform.scale(player_image, (300, 100))
player_rect = player_image.get_rect()

# Функція масштабування фону
def scale_background(image):
    window_width, window_height = window.get_size()
    return pygame.transform.scale(image, (window_width, window_height))

# Функція для відзеркалення фону
def flip_background(image):
    return pygame.transform.flip(image, True, False)

# Стани гри
in_main_menu = True

# Параметри гравця
player = pygame.Rect(100, 100, 300, 100)
velocity_y = 0
on_ground = False

# Параметри камери
camera_x = 0
camera_speed = 0.1  # Швидкість слідування камери за гравцем

clock = pygame.time.Clock()

# Шрифт
font = pygame.font.SysFont(None, 48)

# Малювання головного меню
def draw_main_menu():
    background = scale_background(menu_bg)
    window.blit(background, (0, 0))
    title = font.render("DIGGER MACHINE", True, (255, 200, 0))
    text = font.render("Натисни 1 щоб почати гру", True, (0, 0, 0))
    window.blit(title, (window.get_width() // 2 - title.get_width() // 2, 200))
    window.blit(text, (window.get_width() // 2 - text.get_width() // 2, 300))

# Основний цикл гри
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_1 and in_main_menu:
                in_main_menu = False
                player.x, player.y = 100, 100
                velocity_y = 0
            elif event.key == pygame.K_SPACE and not in_main_menu and on_ground:
                velocity_y = JUMP_POWER
                on_ground = False
        elif event.type == pygame.VIDEORESIZE:
            window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

    if in_main_menu:
        draw_main_menu()
    else:
        # Масштабуємо фон
        background = scale_background(game_bg)
        if player.x > 400:
            background2 = scale_background(game_bg)
        flipped_background = flip_background(background)  # Відзеркалений фон

        # Обчислюємо бажану позицію камери
        target_camera_x = player.centerx - WINDOW_WIDTH // 2
        target_camera_x = max(0, min(target_camera_x, MAX_PLAYER_X - WINDOW_WIDTH))

        # Плавно рухаємо камеру до бажаної позиції
        camera_x += (target_camera_x - camera_x) * camera_speed

        # Відображаємо фон (основний, ліворуч та праворуч)
        window.blit(background, (-camera_x, 0))
        window.blit(flipped_background, (window.get_width() - camera_x, 0))

        # Гравітація та стрибки
        velocity_y += GRAVITY
        player.y += int(velocity_y)

        # Перевірка зіткнення з землею (320 пікселів вище)
        ground_level = window.get_height() - GROUND_OFFSET
        if player.bottom >= ground_level:
            player.bottom = ground_level
            velocity_y = 0
            on_ground = True

        # Управління рухом
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.left > 0:  # Мінімум 0 для лівого руху
            player.x -= PLAYER_SPEED
        if keys[pygame.K_d] and player.right < MAX_PLAYER_X:  # Максимум MAX_PLAYER_X для правого руху
            player.x += PLAYER_SPEED
        

        # Малювання гравця
        window.blit(player_image, (player.x - camera_x, player.y))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
