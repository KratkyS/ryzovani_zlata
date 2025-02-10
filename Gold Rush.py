import random
import os
import pygame
pygame.init()

#okno aplikace
resolution_x = 800
resolution_y = 600

window = pygame.display.set_mode((resolution_x, resolution_y))
pygame.display.set_caption('Gold Rush')

#lobby
Lobby = True
image_path = os.path.join("images", "background.png")
background = pygame.image.load(image_path).convert_alpha()
objekt = pygame.Surface(background.get_size())
#peníze
money_count = 0
font = pygame.font.Font(None, 60)

#hlína
red = (255, 0, 0)
green = (0, 255, 0)
dirt_color = red
font = pygame.font.Font(None, 60)
dirt_count = 0
try:
    background = pygame.image.load(image_path).convert_alpha()  # Přejmenováno na 'background'
    objekt = pygame.Surface(background.get_size())
    objekt.blit(background, (0, 0))
except FileNotFoundError:
    print(f"Soubor s obrázkem nebyl nalezen: {image_path}")
    pygame.quit()
    exit()
     
lobby = True
while lobby:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lobby = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                lobby = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                dirt_count += 10
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o:
                money_count += 10
    money = font.render(f'Money: {money_count}', True, (255, 0, 0)) # definice vykreslení hodnoty peněz
    dirt = font.render(f'Dirt: {dirt_count}/100', True, dirt_color)
    if dirt_count > 99:
        dirt_color = green
        dirt_count = 100
    window.blit(objekt, (0, -100))  # Vykreslení objektu s pozadím
    window.blit(money, (10, 10)) # Vykreslení počtu peněz
    window.blit(dirt, (300, 10))
    pygame.display.flip()
pygame.quit()