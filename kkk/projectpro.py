import pygame
import sys

pygame.init()

# Константи
WINDOW_WIDTH, WINDOW_HEIGHT = 1020, 720
GROUND_OFFSET = 320
GRAVITY = 0.5
JUMP_POWER = -10
PLAYER_SPEED = 6
MAX_PLAYER_X = 2000
MIN_PLAYER_X = 0

# Створення вікна гри
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Digger Machine")

# Завантаження зображень
try:
    menu_bg = pygame.image.load("fon2.jpg")
    game_bg = pygame.image.load("fon.jpeg")
    player_image = pygame.image.load("player2.png")  # Без масштабування
    drill_image = pygame.image.load("playerses.png")
except pygame.error as e:
    print(f"Помилка завантаження зображення: {e}")
    pygame.quit()
    sys.exit()

# Масштабування свердла
drill_image = pygame.transform.scale(drill_image, (50, 50))  # Підлаштуй розмір свердла, якщо потрібно

# Функція масштабування фону
def scale_background(image):
    window_width, window_height = window.get_size()
    return pygame.transform.scale(image, (window_width, window_height))

# Функція відзеркалення фону
def flip_background(image):
    return pygame.transform.flip(image, True, False)

# Стани гри
in_main_menu = True

# Параметри гравця
player = player_image.get_rect()  # Отримуємо оригінальний розмір гравця з його зображення
velocity_y = 0
on_ground = False
drill_direction = None  # Напрямок свердла

# Параметри камери
camera_x = 0
camera_speed = 0.1

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
        flipped_background = flip_background(background)

        # Камера
        target_camera_x = player.centerx - WINDOW_WIDTH // 2
        target_camera_x = max(MIN_PLAYER_X, min(target_camera_x, MAX_PLAYER_X - WINDOW_WIDTH))
        camera_x += (target_camera_x - camera_x) * camera_speed

        # Виводимо фон
        window.blit(background, (-camera_x, 0))
        window.blit(flipped_background, (window.get_width() - camera_x, 0))

        # Гравітація
        velocity_y += GRAVITY
        player.y += int(velocity_y)

        ground_level = window.get_height() - GROUND_OFFSET
        if player.bottom >= ground_level:
            player.bottom = ground_level
            velocity_y = 0
            on_ground = True

        # Управління рухом + напрямок свердла
        keys = pygame.key.get_pressed()
        drill_direction = None

        if keys[pygame.K_a] and player.left > 0:
            player.x -= PLAYER_SPEED
            drill_direction = "left"
        if keys[pygame.K_d] and player.right < MAX_PLAYER_X:
            player.x += PLAYER_SPEED
            drill_direction = "right"
        if keys[pygame.K_s]:
            drill_direction = "down"

        # Малювання гравця
        window.blit(player_image, (player.x - camera_x, player.y))

        # Малювання свердла
        if drill_direction == "right":
            drill_pos = (player.right - camera_x, player.centery - 25)
            window.blit(drill_image, drill_pos)
        elif drill_direction == "left":
            drill_pos = (player.left - 50 - camera_x, player.centery - 25)
            flipped_drill = pygame.transform.flip(drill_image, True, False)
            window.blit(flipped_drill, drill_pos)
        elif drill_direction == "down":
            drill_pos = (player.centerx - 25 - camera_x, player.bottom)
            window.blit(drill_image, drill_pos)

    pygame.display.update()
    clock.tick(60)

pygame.quit()



