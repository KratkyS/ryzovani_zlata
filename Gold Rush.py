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
#tlačítko
button_path_lobby = os.path.join("images", "button_image.png")
button_image = pygame.image.load(button_path_lobby).convert_alpha()
button_rect = button_image.get_rect(topleft=(600, -15))  # Nastavení pozice tlačítka


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
button_position = (600, -15)
mouse_x, mouse_y = 0, 0

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos  # Souřadnice kliknutí
                if button_rect.collidepoint(mouse_x, mouse_y):  # Kontrola kliknutí na tlačítko
                    print("Tlačítko bylo kliknuto!")
                    lobby = False
                    dirt_minigame = True
                

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
        window.blit(button_image, (button_position))
        pygame.display.flip()

    # DIRT_MINIGAME 
    while dirt_minigame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                   dirt_minigame = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                   dirt_count += 10
            
                        
           

        # Vykreslení dirt minihry
        money = font.render(f'Money: {money_count}', True, (255, 0, 0))
        dirt = font.render(f'Dirt: {dirt_count}/100', True, dirt_color)
        if dirt_count > 99:
            dirt_color = green
            dirt_count = 100
            dirt_minigame = False

        window.blit(background_dirt, (0, -200))
        window.blit(money, (10, 10))
        window.blit(dirt, (300, 10))
        
        pygame.display.flip()
        

