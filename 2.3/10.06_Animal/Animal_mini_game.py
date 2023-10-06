import pygame, sys     

class Cat(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, staying_spr, playing_spr, feeding_spr):
        super().__init__()
        self.satiety = 100
        self.happyness = 100
        self.is_staying = True
        self.is_playing = False
        self.is_feeding = False
        self.staying_spr = staying_spr
        self.playing_spr = playing_spr
        self.feeding_spr = feeding_spr
        
        self.current_sprite = 0
        self.image = self.staying_spr[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        
        self.time_to_upd_stats = True
        self.game_over = False
        
    def stay(self):
        self.current_sprite = 0
        self.is_staying = True
        self.is_playing = False
        self.is_feeding = False
        
    def play(self):
        self.current_sprite = 0
        self.is_staying = False
        self.is_playing = True
        self.is_feeding = False
    
    def feed(self):
        self.current_sprite = 0
        self.is_staying = False
        self.is_playing = False
        self.is_feeding = True
        
    def update_stats(self):
        if self.is_staying:
            self.satiety -= 5
            self.happyness -= 5
        elif self.is_playing:
            self.satiety -= 10
            self.happyness += 10
        elif self.is_feeding:
            self.satiety += 10
            
        if self.satiety > 100:
            self.satiety = 100
            self.is_staying = True
            self.is_feeding = False
        elif self.happyness > 100:
            self.happyness = 100
            self.is_staying = True
            self.is_playing = False
        elif self.satiety <= 0 or self.happyness <= 0:
            self.game_over = True
            
        self.time_to_upd_stats = False
        
    def update(self):
        if self.is_staying:
            self.current_sprite += 0.25
            if self.current_sprite >= len(self.staying_spr):
                self.current_sprite = 0

            self.image = self.staying_spr[int(self.current_sprite)]
            
        if self.is_playing:
            self.current_sprite += 0.5
            if self.current_sprite >= len(self.playing_spr):
                self.current_sprite = 0

            self.image = self.playing_spr[int(self.current_sprite)]
            
        if self.is_feeding:
            self.current_sprite += 0.25
            if self.current_sprite >= len(self.feeding_spr):
                self.current_sprite = 0

            self.image = self.feeding_spr[int(self.current_sprite)]
        
        if self.time_to_upd_stats:
            self.update_stats()
            
        if self.game_over:
            self.go_away()
            
    def go_away(self):
        self.game_over_text = main_game.fontB.render('GAME OVER', True, 'darkgoldenrod1')
        screen.fill((0, 0, 0))
        screen.blit(self.game_over_text, (160, 260))
        
        
class Main_game():
    def __init__(self, satiety_bar, happyness_bar):
        self.satiety_bar = satiety_bar
        self.satiety_bar_topleft = (383, 259)
        
        self.happyness_bar = happyness_bar
        self.happyness_bar_topleft = (383, 359)
        
        self.bar_max_width = 150
        self.bar_height = 6
        
        self.fontS = pygame.font.Font('./font/ARCADEPI.ttf', 18)
        self.fontB = pygame.font.Font('./font/ARCADEPI.ttf', 40)
        self.satiety_text = self.fontS.render('Satiety', True, 'darkorange1')
        self.happyness_text = self.fontS.render('Happyness', True, 'darkgoldenrod1')
        
        self.play_button = pygame.Rect(100, 500, 70, 40)
        self.play_button_text = self.fontS.render('Play', True, 'darkorange1')
        self.feed_button = pygame.Rect(210, 500, 70, 40)
        self.feed_button_text = self.fontS.render('Feed', True, 'darkorange1')
        self.stay_button = pygame.Rect(320, 500, 70, 40)
        self.stay_button_text = self.fontS.render('Stay', True, 'darkorange1')
        self.exit_button = pygame.Rect(430, 500, 70, 40)
        self.exit_button_text = self.fontS.render('Exit', True, 'darkorange1')
        
    def show_satiety(self, current, full = 100):
        screen.blit(self.satiety_bar, (350, 230))
        current_satiety_ratio = current / full
        current_bar_width = self.bar_max_width * current_satiety_ratio
        satiety_bar_rect = pygame.Rect((self.satiety_bar_topleft), (current_bar_width, self.bar_height))
        pygame.draw.rect(screen, 'darkorange1', satiety_bar_rect)
        
    def show_happyness(self, current, full = 100):
        screen.blit(self.happyness_bar, (350, 330))
        current_happyness_ratio = current / full
        current_bar_width = self.bar_max_width * current_happyness_ratio
        happyness_bar_rect = pygame.Rect((self.happyness_bar_topleft), (current_bar_width, self.bar_height))
        pygame.draw.rect(screen, 'darkgoldenrod1', happyness_bar_rect)
        
    def draw_bars(self):
        self.show_satiety(cat.satiety)
        self.show_happyness(cat.happyness)
        
    def draw_bars_text(self):
        screen.blit(self.satiety_text, (410, 225))
        screen.blit(self.happyness_text, (395, 325))
        
    def draw_buttons(self):
        pygame.draw.rect(screen, 'chocolate4', self.play_button)
        screen.blit(self.play_button_text, (self.play_button.x + 12,  self.play_button.y + 10))
        pygame.draw.rect(screen, 'chocolate4', self.feed_button)
        screen.blit(self.feed_button_text, (self.feed_button.x + 10,  self.feed_button.y + 10))
        pygame.draw.rect(screen, 'chocolate4', self.stay_button)
        screen.blit(self.stay_button_text, (self.stay_button.x + 10,  self.stay_button.y + 10))
        pygame.draw.rect(screen, 'chocolate4', self.exit_button)
        screen.blit(self.exit_button_text, (self.exit_button.x + 14,  self.exit_button.y + 10))
        
pygame.init()
clock = pygame.time.Clock()

screen_width = 600
screen_heigth = 600
screen = pygame.display.set_mode((screen_width, screen_heigth))
pygame.display.set_caption('Cat game')
bg = pygame.image.load('./images/bg/bg.jpg').convert_alpha()

stay_1 = pygame.image.load('./images/stay/1.png').convert_alpha()
stay_1 = pygame.transform.scale(stay_1, (300, 300))
stay_2 = pygame.image.load('./images/stay/2.png').convert_alpha()
stay_2 = pygame.transform.scale(stay_2, (300, 300))
staying_spr = []
staying_spr.append(stay_1)
staying_spr.append(stay_2)

play_1 = pygame.image.load('./images/play/1.png').convert_alpha()
play_1 = pygame.transform.scale(play_1, (300, 300))
play_2 = pygame.image.load('./images/play/2.png').convert_alpha()
play_2 = pygame.transform.scale(play_2, (300, 300))
play_3 = pygame.image.load('./images/play/3.png').convert_alpha()
play_3 = pygame.transform.scale(play_3, (300, 300))
play_4 = pygame.image.load('./images/play/4.png').convert_alpha()
play_4 = pygame.transform.scale(play_4, (300, 300))
play_5 = pygame.image.load('./images/play/5.png').convert_alpha()
play_5 = pygame.transform.scale(play_5, (300, 300))
play_6 = pygame.image.load('./images/play/6.png').convert_alpha()
play_6 = pygame.transform.scale(play_6, (300, 300))
playing_spr = []
playing_spr.append(play_1)
playing_spr.append(play_2)
playing_spr.append(play_3)
playing_spr.append(play_4)
playing_spr.append(play_5)
playing_spr.append(play_6)

feed_1 = pygame.image.load('./images/feed/1.png').convert_alpha()
feed_1 = pygame.transform.scale(feed_1, (300, 300))
feed_2 = pygame.image.load('./images/feed/2.png').convert_alpha()
feed_2 = pygame.transform.scale(feed_2, (300, 300))
feed_3 = pygame.image.load('./images/feed/3.png').convert_alpha()
feed_3 = pygame.transform.scale(feed_3, (300, 300))
feed_4 = pygame.image.load('./images/feed/4.png').convert_alpha()
feed_4 = pygame.transform.scale(feed_4, (300, 300))
feeding_spr = []
feeding_spr.append(feed_1)
feeding_spr.append(feed_2)
feeding_spr.append(feed_3)
feeding_spr.append(feed_4)

satiety_bar = pygame.image.load('./images/bars/satiety_bar.png').convert_alpha()
#satiety_bar = pygame.transform.scale(satiety_bar, (96, 96))
happyness_bar = pygame.image.load('./images/bars/happyness_bar.png').convert_alpha()
#satiety_bar = pygame.transform.scale(satiety_bar, (96, 96))

moving_sprites = pygame.sprite.Group()
cat = Cat(200, screen_heigth/2, staying_spr, playing_spr, feeding_spr)
moving_sprites.add(cat)

main_game = Main_game(satiety_bar, happyness_bar)

tick = pygame.USEREVENT + 0
pygame.time.set_timer(tick, 1500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if main_game.play_button.collidepoint(event.pos):
                cat.play()
            elif main_game.feed_button.collidepoint(event.pos):
                cat.feed()
            elif main_game.stay_button.collidepoint(event.pos):
                cat.stay()
            elif main_game.exit_button.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
                
        elif event.type == tick:
            cat.time_to_upd_stats = True
    
    screen.blit(bg, (0, 0))
    main_game.draw_bars()
    main_game.draw_bars_text()
    main_game.draw_buttons()
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()
    clock.tick(10)