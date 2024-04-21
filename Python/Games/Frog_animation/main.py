import pygame, sys

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.is_animating = False
        self.sprites = []
        self.sprites.append(animation_1)
        self.sprites.append(animation_2)
        self.sprites.append(animation_3)
        self.sprites.append(animation_4)
        self.sprites.append(animation_5)
        self.sprites.append(animation_6)
        self.sprites.append(animation_7)
        self.sprites.append(animation_8)
        self.sprites.append(animation_9)
        self.sprites.append(animation_10)
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        
    def animating(self):
        self.is_animating = True 
        
    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.25
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
            
            self.image = self.sprites[int(self.current_sprite)]
        
pygame.init()
clock = pygame.time.Clock()

screen_width = 600
screen_heigth = 600
screen = pygame.display.set_mode((screen_width, screen_heigth))
pygame.display.set_caption('Frog animation')

animation_1 = pygame.image.load('./images/attack_1.png')
animation_1 = pygame.transform.scale(animation_1, (512, 256))
animation_2 = pygame.image.load('./images/attack_2.png')
animation_2 = pygame.transform.scale(animation_2, (512, 256))
animation_3 = pygame.image.load('./images/attack_3.png')
animation_3 = pygame.transform.scale(animation_3, (512, 256))
animation_4 = pygame.image.load('./images/attack_4.png')
animation_4 = pygame.transform.scale(animation_4, (512, 256))
animation_5 = pygame.image.load('./images/attack_5.png')
animation_5 = pygame.transform.scale(animation_5, (512, 256))
animation_6 = pygame.image.load('./images/attack_6.png')
animation_6 = pygame.transform.scale(animation_6, (512, 256))
animation_7 = pygame.image.load('./images/attack_7.png')
animation_7 = pygame.transform.scale(animation_7, (512, 256))
animation_8 = pygame.image.load('./images/attack_8.png')
animation_8 = pygame.transform.scale(animation_8, (512, 256))
animation_9 = pygame.image.load('./images/attack_9.png')
animation_9 = pygame.transform.scale(animation_9, (512, 256))
animation_10 = pygame.image.load('./images/attack_10.png')
animation_10 = pygame.transform.scale(animation_10, (512, 256))

moving_sprites = pygame.sprite.Group()
player = Player(screen_width/2, screen_heigth/2)
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.is_animating = True
            
            
    screen.fill((0, 0, 0))
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()
    clock.tick(60)