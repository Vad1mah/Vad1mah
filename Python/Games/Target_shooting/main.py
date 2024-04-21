import pygame, sys, random

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.image_rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.inflate_ip(-25,-25)
        self.gunshot = pygame.mixer.Sound('./audio/shot.mp3')
        
    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair, target_group, True)
        
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        self.image_rect.center = pygame.mouse.get_pos()
        screen.blit(self.image, self.image_rect)
        

class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = pos_x, pos_y


class GameState():
    def __init__(self):
        self.state = 'intro'
        
    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                crosshair.shoot()
                self.state = 'main_game'

        for y in range(0,700,256):
                for x in range(0,1280,256):
                    screen.blit(background,(x,y))
                    screen.blit(ready_text, (screen_width/2 - 115, screen_height/2 - 33))
        
        crosshair_group.update()
        
        pygame.display.flip()   
        
    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                crosshair.shoot()
    
        for y in range(0,700,256):
                for x in range(0,1280,256):
                    screen.blit(background,(x,y))
                    
        target_group.draw(screen)
        crosshair_group.update()
        
        pygame.display.flip()
        
    def state_manager(self):
        if self.state == 'intro':
            self.intro()
        if self.state == 'main_game':
            self.main_game()
        


pygame.init()
clock = pygame.time.Clock()
game_state = GameState()

screen_width = 1280
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load('./images/background.png')
ready_text = pygame.image.load('./images/text_ready.png')
pygame.mouse.set_visible(False)

crosshair = Crosshair('./images/crosshair.png')
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

target_group = pygame.sprite.Group()
for target in range(20):
    new_target = Target('./images/target.png', random.randrange(0, screen_width), random.randrange(0, screen_height))
    target_group.add(new_target)
       
       
while True:
    game_state.state_manager()
    clock.tick(60)