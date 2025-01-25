import pygame

window = pygame.display.set_mode((500,500))

player = pygame.Rect(200,200,70,100)
player_image  = pygame.image.load("download.jpg")
player_image =  pygame.transform.scale(player_image,(70,100))

game = True
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    window.blit(player_image, player)
    pygame.display.update()
    pygame.time.Clock().tick(60)









