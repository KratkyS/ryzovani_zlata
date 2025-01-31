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
            
    window.blit(objekt, (0, 0))  # Vykreslení objektu s pozadím
    pygame.display.flip()
    

pygame.quit()
