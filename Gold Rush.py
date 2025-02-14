import random
import os
import pygame

pygame.init()

# Okno aplikace
resolution_x = 800
resolution_y = 700
window = pygame.display.set_mode((resolution_x, resolution_y))
pygame.display.set_caption('Gold Rush')

# Lobby
image_path_lobby = os.path.join("images", "background.png")
background = pygame.image.load(image_path_lobby).convert_alpha()
objekt_lobby = pygame.Surface(background.get_size())

# Dirt minihra
image_path_dirt = os.path.join("images", "dirt_minigame.png")
background_dirt = pygame.image.load(image_path_dirt).convert_alpha()
objekt_dirt = pygame.Surface(background_dirt.get_size())

# Herní proměnné
money_count = 0
font = pygame.font.Font(None, 60)
red = (255, 0, 0)
green = (0, 255, 0)
dirt_color = red
dirt_count = 0

Game = True
while Game:
    lobby = True
    dirt_minigame = False  

    # LOBBY SMYČKA
    while lobby:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                

        # Vykreslení lobby
        objekt_lobby.blit(background, (0, 0))
        money = font.render(f'Money: {money_count}', True, (255, 0, 0))
        dirt = font.render(f'Dirt: {dirt_count}/100', True, dirt_color)

        if dirt_count > 99:
            dirt_color = green
            dirt_count = 100

        window.blit(objekt_lobby, (0, -100))  
        window.blit(money, (10, 10))  
        window.blit(dirt, (300, 10))
        pygame.display.flip()

    # DIRT_MINIGAME 
    while dirt_minigame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
           

        # Vykreslení dirt minihry
        window.blit(background_dirt, (0, -200)) 
        pygame.display.flip()

