import pygame
pygame.init()

def change_color():
    global color
    global color_num
    
    if 0 <= color_num < 6:
        color_num += 1
        color = list_colors[color_num]
    else:
        color_num = 0
        color = list_colors[color_num]
    

W = 300
H = 300
display = pygame.display.set_mode( (W, H) )
pygame.display.set_caption('Рисовалка квадратиком')

white = ((255,255,255))
blue = ((0,0,255))
green = ((0,255,0))
red = ((255,0,0))
black = ((0,0,0))
orange = ((255,100,10))
yellow = ((255,255,0))
blue_green = ((0,255,170))

FPS = 60
clock = pygame.time.Clock()

list_colors = [blue, green, red, black, orange, yellow, blue_green]
color_num = 0
color = list_colors[color_num]
x = W // 2
y = H // 2
speed = 2

display.fill(white)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                change_color()
            if event.key == pygame.K_SPACE:
                display.fill(white)
                
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
        if x > 0:
            x -= speed
    if keys[pygame.K_d]:
        if x < 290:
            x += speed
    if keys[pygame.K_w]:
        if y > 0:
            y -= speed
    if keys[pygame.K_s]:
        if y < 290:
            y += speed
    
    pygame.draw.rect(display, color, (x, y, 10, 10))
    pygame.display.update()
    
    clock.tick(FPS)
    
    