import pygame, sys, random

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect = self.rect.centerx
        self.gunshot = pygame.mixer.Sound('./audio/shot.mp3')
        
    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair, target_group, True)
        
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 3)

class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = pos_x, pos_y

pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load('./images/background.png')
pygame.mouse.set_visible(False)

crosshair = Crosshair('./images/crosshair.png')
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

target_group = pygame.sprite.Group()
for target in range(20):
    new_target = Target('./images/target.png', random.randrange(0, screen_width), random.randrange(0, screen_height))
    target_group.add(new_target)
       
       
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()
    
    pygame.display.flip()
    for y in range(0,700,256):
            for x in range(0,1280,256):
                screen.blit(background,(x,y))
                
    target_group.draw(screen)
    crosshair_group.draw(screen)
    crosshair_group.update()
    clock.tick(60)