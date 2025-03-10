import random 
import os
import pygame

pygame.init()
clock = pygame.time.Clock()
fps = 60
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
button_rect = button_image.get_rect(topleft=(600, -15))  

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

dirt_object_color = (150, 75, 0)
dirt_penality_max = 20
dirt_penality_min = 3
max_dirt = 10
min_dirt = 5
max_gold = 5
min_gold = 2
gold_money_max_value = 20
gold_money_min_value = 1
dirt_money_max_value = 20
dirt_money_min_value = 1
dirt_value_max = 8
dirt_value_min = 1

dirt_value = random.randint(dirt_value_min, dirt_value_max)
dirt_penality = random.randint(dirt_penality_min, dirt_penality_max)
gold_money_value = random.randint(gold_money_min_value, gold_money_max_value)
dirt_money_value = random.randint(dirt_money_min_value, dirt_money_max_value)
pan_width = 150
pan_height = 75
pan_x = resolution_x // 2 - pan_width // 2
pan_y = resolution_y - pan_height - 20
pan_rect = pygame.Rect(pan_x, pan_y, pan_width, pan_height)
dirt_balls = []
gold_balls = []
ball_size = 30
ball_speed = 3

def create_balls():
    dirt_balls.clear()
    gold_balls.clear()
    num_dirt = random.randint(min_dirt, max_dirt)
    num_gold = random.randint(min_gold, max_gold)
    for _ in range(num_dirt):
        x = random.randint(0, resolution_x - ball_size)
        y = random.randint(-resolution_y, -ball_size)
        dirt_balls.append(pygame.Rect(x, y, ball_size, ball_size))
    for _ in range(num_gold):
        x = random.randint(0, resolution_x - ball_size)
        y = random.randint(-resolution_y, -ball_size)
        gold_balls.append(pygame.Rect(x, y, ball_size, ball_size))

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
popcorn_timer = 0  
popcorn_duration = 300
popcorn_visible2 = False 
popcorn_visible1 = False

gold_popcorn_timer = 0  
gold_popcorn_duration = 300
gold_popcorn_visible = False
gold_popcorn_value = 0 

dirt_popcorn_timer = 0  
dirt_popcorn_duration = 300
dirt_popcorn_visible = False
dirt_popcorn_value = 0

Game = True
 
#tlačítko start

rect_x = 200
rect_y = 100
start = pygame.font.Font(None, 60).render("start", True, (0, 0, 0))
rect_surface = pygame.Surface((rect_x, rect_y))
rect_surface.fill(green)
rect_rect = pygame.Rect(350, 325, rect_x, rect_y) 
rect_render = True


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
                mouse_x, mouse_y = event.pos 
                if button_rect.collidepoint(mouse_x, mouse_y):  
                    print("Tlačítko bylo stisknuto!")
                    lobby = False
                    dirt_minigame = True
                    dirt_render = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos  
                if button2_rect.collidepoint(mouse_x, mouse_y):
                    if dirt_count >99:
                        print("Tlačítko bylo stisknuto!")
                        lobby = False
                        gold_minigame = True
        if money_count > 0:
            money_color = green
        else:
            money_color = red
        # Vykreslení lobby
        objekt_lobby.blit(background, (0, 0))
        money = font.render(f'Money: {money_count}$', True, money_color)
        dirt = font.render(f'Dirt: {dirt_count}/100', True, dirt_color)

        if dirt_count > 99:
            dirt_color = green
            dirt_count = 100
        if dirt_count < -99:
            dirt_count = -100

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
                        dirt_value = random.randint(dirt_value_min, dirt_value_max)
                    
                        dirt_count += dirt_value
                        
                        popcorn_timer = pygame.time.get_ticks()  
                        popcorn_visible2 = True
                        popcorn_2 = pygame.font.Font(None, 60).render(f'+{dirt_value}', True, (0, 255, 0))
                        
                        del dirt_x[index]
                        del dirt_y[index]
                        del dirt_rects[index]
                        dirt_x.append(random.randint(10, 600))
                        dirt_y.append(random.randint(10, 600))
                        dirt_rects.append(pygame.Rect(dirt_x[-1], dirt_y[-1], dirt_size, dirt_size))
                        clicked_inside_dirt = True
                        break
                
              
                if not clicked_inside_dirt:
                    dirt_penality = random.randint(dirt_penality_min, dirt_penality_max)
                    dirt_count -= dirt_penality
                    popcorn_timer = pygame.time.get_ticks()  
                    popcorn_visible1 = True
                    popcorn_1 = pygame.font.Font(None, 60).render(f'-{dirt_penality}', True, (255, 0, 0))
                    
                    
            if popcorn_visible2 and pygame.time.get_ticks() - popcorn_timer >= popcorn_duration:
                popcorn_visible2 = False
            if popcorn_visible1 and pygame.time.get_ticks() - popcorn_timer >= popcorn_duration:
                popcorn_visible1 = False
        # Vykreslení dirt minihry
        if money_count > 0:
            money_color = green
        else:
            money_color = red
        
        if dirt_count > 99:
            dirt_color = green
            dirt_count = 100
            dirt_minigame = False
        if dirt_count < -99:
            dirt_count = -100
        money = font.render(f'Money: {money_count}$', True, money_color)
        dirt = font.render(f'Dirt: {dirt_count}/100', True, dirt_color)
        
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
        money_color = red
        
        pan_path = os.path.join("images", "pan.png")
        pan_image = pygame.image.load(pan_path).convert_alpha()
        resized_pan_image = pygame.transform.scale(pan_image, (pan_width, pan_height))

# Vykreslení pánve místo šedého obdélníku


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gold_minigame = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if rect_render and rect_rect.collidepoint(mouse_x, mouse_y):
                    rect_render = False  
                    create_balls()

        # Ovládání pánve
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and pan_rect.x > 0:
            pan_rect.x -= 5
        if keys[pygame.K_RIGHT] and pan_rect.x < resolution_x - pan_width:
            pan_rect.x += 5
        if keys[pygame.K_UP] and pan_rect.x > 0:
            pan_rect.y -= 5
        if keys[pygame.K_DOWN] and pan_rect.x < resolution_x - pan_width:
            pan_rect.y += 5

        # Pohyb koulí
        for ball in dirt_balls[:]: 
            ball.y += ball_speed
            if ball.y > resolution_y:
                dirt_balls.remove(ball)
                

        for ball in gold_balls[:]: 
            ball.y += ball_speed
            if ball.y > resolution_y:
                gold_balls.remove(ball)

        # Kontrola kolize
        for ball in dirt_balls[:]:
            if pan_rect.colliderect(ball):
                dirt_money_value = random.randint(dirt_money_min_value, dirt_money_max_value)  
                money_count -= dirt_money_value  
                
                dirt_popcorn_value = -dirt_money_value  
                dirt_popcorn_timer = pygame.time.get_ticks()
                dirt_popcorn_visible = True
        
                dirt_balls.remove(ball)  

        for ball in gold_balls[:]:
            if pan_rect.colliderect(ball):
                gold_money_value = random.randint(gold_money_min_value, gold_money_max_value)
                money_count += gold_money_value
                gold_popcorn_value = gold_money_value  
                gold_popcorn_timer = pygame.time.get_ticks()
                gold_popcorn_visible = True
                
                gold_balls.remove(ball)
        # Vykreslení scény
        window.blit(resized_gold_background, (0, 0))
        if money_count > 0:
            money_color = green
        else:
            money_color = red 
        money = font.render(f'Money: {money_count}$', True, money_color)
        dirt = font.render(f'Dirt: {dirt_count}/100', True, dirt_color)
         
        window.blit(money, (10, 10))
        window.blit(dirt, (300, 10))
        
        
        if gold_popcorn_visible:
            gold_popcorn_text = font.render(f"+{gold_popcorn_value}", True, (0, 255, 0))
            window.blit(gold_popcorn_text, (350, 40))  

        if dirt_popcorn_visible:
            dirt_popcorn_text = font.render(f"{dirt_popcorn_value}", True, (255, 0, 0))
            window.blit(dirt_popcorn_text, (450, 40))  

        # Skrýt popcorn efekt po určité době
        if gold_popcorn_visible and pygame.time.get_ticks() - gold_popcorn_timer >= gold_popcorn_duration:
            gold_popcorn_visible = False

        if dirt_popcorn_visible and pygame.time.get_ticks() - dirt_popcorn_timer >= dirt_popcorn_duration:
            dirt_popcorn_visible = False

        if rect_render:
            window.blit(rect_surface, (300, 300))
            window.blit(start, (350, 325))

        window.blit(resized_pan_image, pan_rect.topleft)

        # Vykreslení koulí
        for ball in dirt_balls:
            pygame.draw.circle(window, (150, 75, 0), ball.center, ball_size // 2)
        for ball in gold_balls:
            pygame.draw.circle(window, (255, 255, 0), ball.center, ball_size // 2)

        
        if not dirt_balls and not gold_balls and not rect_render:
            gold_minigame = False
            rect_render = True

        clock.tick(fps)
        pygame.display.flip()

