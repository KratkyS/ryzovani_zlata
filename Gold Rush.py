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

#tlačítko 2
button2_path_lobby = os.path.join("images", "Gold_panning_button.png")
button2_image = pygame.image.load(button2_path_lobby).convert_alpha()
button2_rect = button2_image.get_rect(topleft=(610, 175))
resized_button2 = pygame.transform.scale(button2_image, (175, 175))

#minihra zlata
image_path_gold = os.path.join("images", "Gold_panning_background.png")
background_gold = pygame.image.load(image_path_gold).convert_alpha()
resized_gold_background = pygame.transform.scale(background_gold, (800, 700)) 

# Dirt minihra
image_path_dirt = os.path.join("images", "dirt_minigame.png")
background_dirt = pygame.image.load(image_path_dirt).convert_alpha()
objekt_dirt = pygame.Surface(background_dirt.get_size())
dirt_count = 3
dirt_size = 100
dirt_x = []
dirt_y = []
dirt_rects = []
dirt_value = 2
dirt_object_color = (150, 75, 0)
dirt_penality = 1

# popcorn čísla
popcorn_2 = pygame.font.Font(None, 60).render(f'+{dirt_value}', True, (0, 255, 0))

popcorn_1 = pygame.font.Font(None, 60).render(f'-{dirt_penality}', True, (255, 0, 0))

def popcorn_plus():
    window.blit(popcorn_2, (300, 40))  
def popcorn_minus():
    window.blit(popcorn_1, (430, 40)) 

for index in range(dirt_count):
    dirt_x.append(random.randint(10, 600))
    dirt_y.append(random.randint(10, 600))
    dirt_rects.append(pygame.Rect(dirt_x[index], dirt_y[index], dirt_size, dirt_size))


# Herní proměnné
money_count = 0
font = pygame.font.Font(None, 60)
red = (255, 0, 0)
green = (0, 255, 10)
dirt_color = red
dirt_count = 0
button_position = (600, -15)
button2_position = (610, 175)
mouse_x, mouse_y = 0, 0

# Časování pro popcorn
popcorn_timer = 0  # Čas, kdy má být text zobrazen
popcorn_duration = 500  # Délka zobrazení v milisekundách (2 sekundy)
popcorn_visible2 = False # Určuje, zda je popcorn text viditelný
popcorn_visible1 = False
Game = True
 

while Game:
    lobby = True
    dirt_minigame = False
    gold_minigame = False
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
                    print("Tlačítko bylo stisknuto!")
                    lobby = False
                    dirt_minigame = True
                    dirt_render = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos  # Souřadnice kliknutí
                if button2_rect.collidepoint(mouse_x, mouse_y):
                    if dirt_count >99:
                        print("Tlačítko bylo stisknuto!")
                        lobby = False
                        gold_minigame = True
                        
                    
                 

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
        window.blit(resized_button2, (button2_position))
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

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                mouse_rect = pygame.Rect(mouse_x, mouse_y, 1, 1)
                
                clicked_inside_dirt = False
                for index in range(len(dirt_rects)-1, -1, -1):  
                    if dirt_rects[index].colliderect(mouse_rect):  
                        dirt_count += dirt_value
                        
                        popcorn_timer = pygame.time.get_ticks()  # Uložíme aktuální čas
                        popcorn_visible2 = True
                        
                        del dirt_x[index]
                        del dirt_y[index]
                        del dirt_rects[index]
                        dirt_x.append(random.randint(10, 600))
                        dirt_y.append(random.randint(10, 600))
                        dirt_rects.append(pygame.Rect(dirt_x[-1], dirt_y[-1], dirt_size, dirt_size))
                        clicked_inside_dirt = True
                        break
                
                # Pokud bylo kliknuto mimo objekt hlíny, odečteme 1 od dirt_count
                if not clicked_inside_dirt:
                    dirt_count -= dirt_penality
                    popcorn_timer = pygame.time.get_ticks()  # Uložíme aktuální čas
                    popcorn_visible1 = True
                    
            if popcorn_visible2 and pygame.time.get_ticks() - popcorn_timer >= popcorn_duration:
                popcorn_visible2 = False
            if popcorn_visible1 and pygame.time.get_ticks() - popcorn_timer >= popcorn_duration:
                popcorn_visible1 = False
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
        
        for index in range(len(dirt_x)):
          pygame.draw.ellipse(window, dirt_object_color, (dirt_x[index], dirt_y[index], dirt_size, dirt_size))
        if popcorn_visible2:
            popcorn_plus()
        if popcorn_visible1:
            popcorn_minus()
        pygame.display.flip()
        
#minihra rýžování zlata        
    while gold_minigame:
        dirt_count = 0
        dirt_color = red
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                   dirt_minigame = False
        money = font.render(f'Money: {money_count}', True, (255, 0, 0))
        dirt = font.render(f'Dirt: {dirt_count}/100', True, dirt_color)
        window.blit(resized_gold_background, (0, 0))
        window.blit(money, (10, 10))
        window.blit(dirt, (300, 10))
        pygame.display.flip()
        
        

