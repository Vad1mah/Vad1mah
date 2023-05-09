import pygame
pygame.init()

W = 300
H = 300
display = pygame.display.set_mode( (W, H) )
pygame.display.set_caption('Рисовалка квадратиком')

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

FPS = 60
clock = pygame.time.Clock()

x = W // 2
y = H // 2
speed = 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
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
    
    display.fill(WHITE)
    pygame.draw.rect(display, BLUE, (x, y, 10, 10))
    pygame.display.update()
    
    clock.tick(FPS)
    
    