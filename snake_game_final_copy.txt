import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

screen_width = 600
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')
pygame.mixer.init 

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 32)
score_font = pygame.font.SysFont("comicsansms", 35)

def game_score(score):  
    if score > 0:
        value = score_font.render("Score: " + str(score), True, blue)
        screen.blit(value, [0, 0])
    elif score == 0:
        value = score_font.render("Score: 0", True, blue)
        screen.blit(value, [0, 0])
        game_over = True
    else:
        game_over = True 

def snake_growth(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.circle(screen, white, [x[0], x[1]], snake_block)

def message(text, color):
    msg_type = font_style.render(text, True, color)
    screen.blit(msg_type, [screen_width / 22, screen_height / 3])  

def game_loop():
    game_over = False
    close_game = False

    x1 = screen_width / 2
    y1 = screen_height / 2

    x1_movement = 0
    y1_movement = 0

    snake_List = []
    snake_length = 1
    snake_speed = 15 

    x_food = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    y_food = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
    x_rotten_apple = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0 
    y_rotten_apple = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

    while not game_over:
        while close_game == True:
            screen.fill(black)
            message("You Lost! Press C-Play Again or Q-Quit", blue)
            game_score(snake_length - 1)     
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        close_game = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_movement = -snake_block
                    y1_movement = 0
                elif event.key == pygame.K_RIGHT:
                    x1_movement = snake_block
                    y1_movement = 0
                elif event.key == pygame.K_UP:
                    y1_movement = -snake_block
                    x1_movement = 0
                elif event.key == pygame.K_DOWN:
                    y1_movement = snake_block
                    x1_movement = 0
        
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            close_game = True
        x1 += x1_movement
        y1 += y1_movement
        screen.fill(black)
        pygame.draw.circle(screen, green, (x_food, y_food), 7)
        pygame.display.update

        pygame.draw.circle(screen, red, (x_rotten_apple, y_rotten_apple), 7)
        pygame.display.update

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)
        if len(snake_List) > snake_length:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_head:
                close_game = True

        snake_growth(snake_block, snake_List)
        game_score(snake_length - 1)
        pygame.display.update()
    
        if x1 == x_food and y1 == y_food:
            x_food = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            y_food = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
            snake_length += 1
            snake_speed+=3
            crunch_sound = pygame.mixer.Sound("crunch_sound.mp3") 
            pygame.mixer.Sound.play(crunch_sound) 

        if x1 == x_rotten_apple and y1 == y_rotten_apple:
            x_rotten_apple = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            y_rotten_apple = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
            crunch
