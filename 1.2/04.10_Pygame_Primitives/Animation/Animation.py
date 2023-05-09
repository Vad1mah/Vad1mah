import pygame
pygame.init()


W = 800 
H = 800
display = pygame.display.set_mode( (W, H) )
pygame.display.set_caption('Анимация Марио')

FPS = 60
clock = pygame.time.Clock()

font_path = 'mario_font.otf'
font_large = pygame.font.Font(font_path, 48)
font_small = pygame.font.Font(font_path, 24)

game_over = False
retry_text = font_small.render('НАЖМИТЕ ЛЮЬУЮ КЛАВИШУ', True, (255, 255, 255))
retry_rect = retry_text.get_rect()
retry_rect.midtop = (W // 2, H // 2)

class Entity:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.x_speed = 0
        self.y_speed = 0
        self.speed = 5
        self.is_out = False
        self.is_dead = False
        self.jump_speed = -12
        self.gravity = 20
        self.is_grounded = False
        
    def handle_input(self):
        pass
    
    def kill(self, dead_image):
        self.image = self.dead_image
        self.is_dead = True
        self.x_speed = -self.x_speed
        self.y_speed = self.jump_speed
        
    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.gravity
        self.rect.y += self.y_speed
        
    def drawing(self, surface):
        surface.blit(self.image, self.rect)
        

entity = Entity(pygame.Surface((100, 100))) 
        

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    clock.tick(FPS)

    display.fill((92, 148, 252))
    
    entity.update()
    entity.drawing (display)
    
    pygame.display.flip()
quit()
    
mario_img_right = [pygame.image.load('images/r1.png'), 
                   pygame.image.load('images/r2.png'), 
                   pygame.image.load('images/r3.png'), 
                   pygame.image.load('images/r4.png'), 
                   pygame.image.load('images/r5.png')]