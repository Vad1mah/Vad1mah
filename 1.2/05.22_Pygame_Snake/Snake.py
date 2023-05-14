import pygame
from random import randrange
pygame.init()

RES = 800
display = pygame.display.set_mode( (RES + 1, RES + 1) )
pygame.display.set_caption('Змейка')
clock = pygame.time.Clock()

part_size = 50
coor_x, coor_y = randrange(0, RES, part_size), randrange(0, RES, part_size)
apple = randrange(0, RES, part_size), randrange(0, RES, part_size)
length = 1
snake = [(coor_x, coor_y)]
dx, dy = 0, 0
FPS = 5

class snake:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.x_speed = 0
        self.y_speed = 0
        self.speed = 0.5
        self.snake_length = 2
        self.frouts_eating = False
        self.pepper_eating = False
        self.body_eating = False
        self.is_dead = False
        self.go_right = False
        self.go_left = False
        self.go_up = False
        self.go_down = False
    
    def handle_input(self):
        self.x_speed = 0
        self.y_speed = 0
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.x_speed = 1
                    self.y_speed = 0
                    
                    self.go_right = True
                    self.go_left = False
                    self.go_up = False
                    self.go_down = False
                    
                elif event.key == pygame.K_a:
                    self.x_speed = -1
                    self.y_speed = 0
                    
                    self.go_right = False
                    self.go_left = True
                    self.go_up = False
                    self.go_down = False
                    
                elif event.key == pygame.K_w:
                    self.x_speed = 0
                    self.y_speed = -1
                    
                    self.go_right = False
                    self.go_left = False
                    self.go_up = True
                    self.go_down = False
                    
                elif event.key == pygame.K_s:
                    self.x_speed = 0
                    self.y_speed = 1
                    
                    self.go_right = False
                    self.go_left = False
                    self.go_up = False
                    self.go_down = True
                    
                else: 
                    if event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                        self.x_speed = 0
                        self.y_speed = 0
            
                        self.go_right = False
                        self.go_left = False
                        self.go_up = False
                        self.go_down = False
            

while True:
    display.fill(pygame.Color('black'))
    
    [(pygame.draw.rect(display, pygame.Color('green'), (coor_1, coor_2, part_size, part_size))) for coor_1, coor_2 in snake]
    pygame.draw.rect(display, pygame.Color('red'), (*apple, part_size, part_size))
    
    
    coor_x += dx * part_size
    coor_y += dy * part_size
    snake.append((coor_x, coor_y))
    snake = snake[-length:]
    
    if snake[-1] == apple:
        apple = randrange(0, RES, part_size), randrange(0, RES, part_size)
        length += 1
        
    if coor_x < 0 or coor_x > RES or coor_y < 0 or coor_y > RES:
        break
    if len(snake) != len(set(snake)):
        break
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
            if event.key == pygame.K_a:
                dx = -1
                dy = 0
            if event.key == pygame.K_d:
                dx = 1
                dy = 0
            if event.key == pygame.K_w:
                dx = 0
                dy = -1
            if event.key == pygame.K_s:
                dx = 0
                dy = 1
                
    pygame.display.flip() 
                    
    
    clock.tick(FPS)