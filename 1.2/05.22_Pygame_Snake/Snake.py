import pygame, sys, random
from pygame.math import Vector2
import tkinter as tk
from tkinter import font
from tkinter import *

pygame.mixer.pre_init(44100, -16, 5, 512)
pygame.init()
pygame.mixer.init()

def game_over():
    root = tk.Tk()
    lose_window = tk.Toplevel(root)
    
    font_larfe = font.Font(family='Helvetica', size=24, weight='bold')
    font_small = font.Font(family='Helvetica', size=18, weight='bold')
    
    app_width = int(800/2)
    app_height = int(800/8)
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    lose_window_x = (screen_width  / 2) - (app_width / 2)
    lose_window_y = (screen_height / 2) - (app_height / 2)

    lose_window.geometry(f"{app_width}x{app_height}+{int(lose_window_x)}+{int(lose_window_y)}")

    lose_window.attributes("-topmost", True)
    root.attributes('-alpha', 0.0)
    lose_window.overrideredirect(1)
    
    def key_pressed(event):
        root.destroy()
        main_game.update_start_time()
        main_game.respawn()
        
    lose_button = tk.Button(lose_window, text = "GAME OVER\n(press any key to restart)", background='#3E4149', font=font_small, state='disabled')
    lose_button.pack(fill='both', expand = 1)
    
    lose_button.focus_force()
    lose_button.bind("<Key>", key_pressed)
    lose_button.bind("<ButtonPress-1>", key_pressed)
    
    lose_window.mainloop()

class Snake:
    def __init__(self):
        self.body = [Vector2(9,17), Vector2(9,18), Vector2(9,19)]
        self.direction = Vector2(0,-1)
        self.meal = Meal()
        self.eating_pepper = False
        self.new_block = False
        self.is_dead = False
        self.very_fast = pygame.USEREVENT + 2
        
        self.head_up = pygame.image.load('images/head_up.png').convert_alpha()
        self.head_up = pygame.transform.scale(self.head_up, (cell_size, cell_size))
        self.head_down = pygame.image.load('images/head_down.png').convert_alpha()
        self.head_down = pygame.transform.scale(self.head_down, (cell_size, cell_size))
        self.head_right = pygame.image.load('images/head_right.png').convert_alpha()
        self.head_right = pygame.transform.scale(self.head_right, (cell_size, cell_size))
        self.head_left = pygame.image.load('images/head_left.png').convert_alpha()
        self.head_left  = pygame.transform.scale(self.head_left, (cell_size, cell_size))
        
        self.body_horizontal = pygame.image.load('images/body_horizontal.png').convert_alpha()
        self.body_horizontal = pygame.transform.scale(self.body_horizontal, (cell_size, cell_size))
        self.body_vertical = pygame.image.load('images/body_vertical.png').convert_alpha()
        self.body_vertical = pygame.transform.scale(self.body_vertical, (cell_size, cell_size))
        
        self.body_tr = pygame.image.load('images/body_tr.png').convert_alpha()
        self.body_tr = pygame.transform.scale(self.body_tr, (cell_size, cell_size))
        self.body_tl = pygame.image.load('images/body_tl.png').convert_alpha()
        self.body_tl = pygame.transform.scale(self.body_tl, (cell_size, cell_size))
        self.body_br = pygame.image.load('images/body_br.png').convert_alpha()
        self.body_br = pygame.transform.scale(self.body_br, (cell_size, cell_size))
        self.body_bl = pygame.image.load('images/body_bl.png').convert_alpha()
        self.body_bl = pygame.transform.scale(self.body_bl, (cell_size, cell_size))
        
        self.tail_up = pygame.image.load('images/tail_up.png').convert_alpha()
        self.tail_up = pygame.transform.scale(self.tail_up, (cell_size, cell_size))
        self.tail_down = pygame.image.load('images/tail_down.png').convert_alpha()
        self.tail_down = pygame.transform.scale(self.tail_down, (cell_size, cell_size))
        self.tail_right = pygame.image.load('images/tail_right.png').convert_alpha()
        self.tail_right = pygame.transform.scale(self.tail_right, (cell_size, cell_size))
        self.tail_left = pygame.image.load('images/tail_left.png').convert_alpha()
        self.tail_left = pygame.transform.scale(self.tail_left, (cell_size, cell_size))
        
        self.s_speed_up = pygame.mixer.Sound('audio/speed_up.mp3')
        self.s_speed_up.set_volume(0.3)
        self.s_eating = pygame.mixer.Sound('audio/eating.mp3')
        self.s_dying = pygame.mixer.Sound('audio/dying.mp3')
        
    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        
        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            
            if index == 0:
                display.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                display.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    display.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    display.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        display.blit(self.body_tl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        display.blit(self.body_tr, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        display.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        display.blit(self.body_br, block_rect)
                
    def update_head_graphics(self):
        head_direction_vector = self.body[1] - self.body[0]
        if head_direction_vector == Vector2(1, 0):
            self.head = self.head_left
        elif head_direction_vector == Vector2(-1, 0):
            self.head = self.head_right
        elif head_direction_vector == Vector2(0, 1):
            self.head = self.head_up
        elif head_direction_vector == Vector2(0, -1):
            self.head = self.head_down
            
    def update_tail_graphics(self):
        tail_direction_vector = self.body[-2] - self.body[-1]
        if tail_direction_vector == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_direction_vector == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_direction_vector == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_direction_vector == Vector2(0, -1):
            self.tail = self.tail_down           
                    
    def move_snake(self):
        if self.new_block and self.eating_pepper:
            for _ in range(3):
                body_copy = self.body[:]
                body_copy.insert(0, body_copy[0] + self.direction)
                self.body = body_copy[:]
            self.new_block = False
            self.eating_pepper = False
        elif self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
    
    def add_block(self):
        self.new_block = True
        
    def speed_up(self):
        pygame.mixer.music.pause()
        channel3.play(self.s_speed_up, loops = 0)
        pygame.time.set_timer(SCREEN_UPDATE, 100)
        pygame.time.set_timer(self.very_fast, 5000)
        
    def speed_normal(self):
        pygame.time.set_timer(SCREEN_UPDATE, 150)
        
    def eating_sound(self):
        channel1.play(self.s_eating, loops = 0)
        
    def death_sound(self):
        if self.body[0] != Vector2(9,13):
            channel2.play(self.s_dying, loops = 0)
        
            
class Meal:
    def __init__(self):
        self.red_apple = pygame.image.load('images/red_apple.png').convert_alpha()
        self.red_apple = pygame.transform.scale(self.red_apple, (cell_size, cell_size))
        self.green_apple = pygame.image.load('images/green_apple.png').convert_alpha()
        self.green_apple = pygame.transform.scale(self.green_apple, (cell_size, cell_size))
        self.yellow_apple = pygame.image.load('images/yellow_apple.png').convert_alpha()
        self.yellow_apple = pygame.transform.scale(self.yellow_apple, (cell_size, cell_size))

        self.green_pear = pygame.image.load('images/green_pear.png').convert_alpha()
        self.green_pear = pygame.transform.scale(self.green_pear, (cell_size, cell_size))
        self.yellow_pear = pygame.image.load('images/yellow_pear.png').convert_alpha()
        self.yellow_pear = pygame.transform.scale(self.yellow_pear, (cell_size, cell_size))

        self.banana = pygame.image.load('images/banana.png').convert_alpha()
        self.banana = pygame.transform.scale(self.banana, (cell_size, cell_size))

        self.pepper = pygame.image.load('images/pepper.png').convert_alpha()
        self.pepper = pygame.transform.scale(self.pepper, (cell_size, cell_size))
        
        self.food = [self.red_apple, self.green_apple, self.yellow_apple, self.green_pear, self.yellow_pear, self.banana, self.pepper]
        
        self.randomize()
        self.eating_object = random.choice(self.food)
        self.respawn_pepper = pygame.USEREVENT + 1
        
    def draw_food(self):
        food_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        display.blit(self.eating_object, food_rect)
        
    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)
        self.eating_object = random.choice(self.food)
        
    def update_food_list(self):
        self.food = [self.red_apple, self.green_apple, self.yellow_apple, self.green_pear, self.yellow_pear, self.banana, self.pepper]
        
    def add_pepper(self):
        pygame.time.set_timer(self.respawn_pepper, 10000)
        
class Main():
    def __init__(self):
        self.snake = Snake()
        self.meal = Meal()
        self.is_paused = False
        self.time_pass = 0
        self.last_dy_time = 0
        
    def update(self):
        if not self.snake.is_dead and not self.is_paused:
            self.snake.move_snake()
            self.check_collision()
            self.check_fail()
        self.time_pass = pygame.time.get_ticks() - self.last_dy_time
        
    def draw_elements(self):
        self.draw_platforms()
        self.meal.draw_food()
        self.snake.draw_snake()
        
    def check_collision(self):
        if self.meal.pos == self.snake.body[0]:
            if self.meal.eating_object == self.meal.pepper:
                self.snake.eating_pepper = True
                self.snake.speed_up()
                self.meal.food.remove(self.meal.pepper)
                self.meal.add_pepper()
            self.meal.randomize()
            self.snake.add_block()
            self.snake.eating_sound()
            
        for block in self.snake.body[1:]:
            if block == self.meal.pos:
                self.meal.randomize()
            
    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.snake.is_dead = True
            self.snake.death_sound()
            self.unps_mx_stp_spd_up()
            self.update_start_time()
            self.is_paused = True
            game_over()
            
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.snake.is_dead = True
                self.snake.death_sound()
                self.unps_mx_stp_spd_up()
                self.update_start_time()
                self.is_paused = True
                game_over()
        
    def respawn(self):
        print(self.meal.food)
        self.snake.body = [Vector2(9,17), Vector2(9,18), Vector2(9,19)]
        self.snake.direction = Vector2(0,-1)
        self.meal.update_food_list()
        self.meal.randomize()
        for block in self.snake.body[:]:
            if block == self.meal.pos:
                self.respawn()
        self.snake.is_dead = False
        pygame.time.set_timer(SCREEN_UPDATE, 150)
        
    def draw_platforms(self):
        square_color = (205,179,164)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        sqaure_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(display, square_color, sqaure_rect)
            else:
                for col in range(cell_number):
                    if col % 2 == 1:
                        sqaure_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(display, square_color, sqaure_rect)
                        
    def update_start_time(self):
        self.last_dy_time = pygame.time.get_ticks()
        
    def unps_mx_stp_spd_up(self):
        channel3.stop()
        pygame.mixer.music.unpause()
        
  
cell_size = 40
cell_number = 20
display = pygame.display.set_mode((cell_size * cell_number, cell_number * cell_size))
FPS = 60
clock = pygame.time.Clock()

pygame.mixer.music.load('audio/background_music.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)
channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)
channel3 = pygame.mixer.Channel(2)
channel4 = pygame.mixer.Channel(3)

SCREEN_UPDATE = pygame.USEREVENT + 0 
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = Main()  
snake = Snake()
meal = Meal()

while True:
    if not main_game.is_paused:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
                
            if event.type == SCREEN_UPDATE:
                main_game.update()
                
            if event.type == meal.respawn_pepper:
                pygame.time.set_timer(meal.respawn_pepper, 0)
                meal.update_food_list()
                
            if event.type == snake.very_fast:
                channel3.stop()
                pygame.mixer.music.unpause()
                pygame.time.set_timer(snake.very_fast, 0)
                snake.speed_normal()
                
            if keys[pygame.K_r]:
                main_game.respawn()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    main_game.is_paused = True
                    
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if main_game.snake.direction.x != 1:
                        main_game.snake.direction = Vector2(-1,0)
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if main_game.snake.direction.x != -1:
                        main_game.snake.direction = Vector2(1,0)
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    if main_game.snake.direction.y != 1:
                        main_game.snake.direction = Vector2(0,-1)
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if main_game.snake.direction.y != -1:
                        main_game.snake.direction = Vector2(0,1)
                        
                        
        display.fill((236,205,177))
        main_game.draw_elements()
        pygame.display.update()
        clock.tick(FPS)
        
    else:
        if main_game.time_pass > 100:
            pygame.mixer.music.pause()
        channel3.pause()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                main_game.is_paused = False
                pygame.mixer.music.unpause()
                channel3.unpause()