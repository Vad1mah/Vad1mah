import pygame, sys, random
     
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./images/ship.png')
        self.rect = self.image.get_rect(center = (screen_width / 2, screen_height / 2))
        self.last_shoot = pygame.time.get_ticks()
        self.shooting_speed =  100
        self.is_dead = False
    
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        main_game.spawn_enemy()
        
    def shoot(self):
        if self.is_dead == False:
            shooting_time = pygame.time.get_ticks()
            if shooting_time - self.last_shoot >= self.shooting_speed:
                self.last_shoot = shooting_time
                main_game.create_bullet()
                channel_0.play(shooting_s)
    
    def skills(self):
        self.shooting = pygame.USEREVENT + 0
        pygame.time.set_timer(self.shooting, self.shooting_speed)
        

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load('./images/bullet.png')
        self.rect = self.image.get_rect(midleft = (pos_x, pos_y))

    def update(self):
        self.rect.x += 30 
        if self.rect.x >= screen_width + 50:
            self.kill()
    

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = random.choice(enemies_list)
        self.rect = self.image.get_rect(midright = (pos_x, pos_y))
        
    def update(self):
        self.rect.x -= 10 + main_game.score // 10
        if self.rect.x <= -128:
            self.kill()
    

class MainGame():
    def __init__(self):
        self.score = 0
        self.last_spawn = pygame.time.get_ticks()
        self.slowing = 1
        self.deceleration_level = 0
        
    def text_render(self):
        self.score_text = font.render(str(self.score), True, (255, 255, 255))
        self.score_rect = self.score_text.get_rect()
        self.restart_text = font.render('PRESS ANY KEY TO RESTART', True, (255, 255, 255))
        self.restart_rect = self.restart_text.get_rect()
        
        if player.is_dead == False:
            self.score_rect.midtop = (screen_width // 2, 5)
            screen.blit(self.score_text, self.score_rect)
        else:
            self.score_rect.midtop = (screen_width // 2, screen_height / 2 - 100)
            self.restart_rect.midtop = (screen_width // 2, screen_height / 2)
            screen.blit(self.score_text, self.score_rect)
            screen.blit(self.restart_text, self.restart_rect)
            
    def collisions(self):
        if pygame.sprite.groupcollide(enemy_group, bullet_group, True, True):
            self.score += 1
            channel_1.play(killing_s)
            if self.score // 10 > self.deceleration_level:
                self.deceleration_level += 1
                player.shooting_speed += self.slowing
        if pygame.sprite.groupcollide(player_group, enemy_group, True, True):
            player.is_dead = True
            channel_1.play(dying_s)
            
            
    def create_bullet(self):
        return bullet_group.add(Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
    
    def spawn_enemy(self):
        spawn_time = pygame.time.get_ticks()
        self.spawn_delay = 250 - self.score // 10
        if spawn_time - self.last_spawn >= self.spawn_delay:
            self.last_spawn = spawn_time
            self.create_enemy()
    
    def create_enemy(self):
        return enemy_group.add(Enemy(screen_width + 20, random.randrange(40, screen_height, 128)))
    
    def restart_game(self):
        player.is_dead = False
        self.score = 0
        player.shooting_speed = 100
        player_group.add(player)


pygame.mixer.pre_init(44100, -16, 5, 512)
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
screen_width, screen_height = 1280, 850
screen = pygame.display.set_mode((screen_width, screen_height))
bg = pygame.image.load('./images/background.jpeg')
bg = pygame.transform.scale(bg, (1280, 850))
pygame.mouse.set_visible(False)

font_path = './font/GameFont.ttf'
font = pygame.font.Font(font_path, 48)

pygame.mixer.music.load('./audio/bg.wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)
channel_0 = pygame.mixer.Channel(0)
channel_1 = pygame.mixer.Channel(1)
channel_2 = pygame.mixer.Channel(2)
shooting_s = pygame.mixer.Sound('audio/shooting.wav')
dying_s = pygame.mixer.Sound('audio/dying.mp3')
killing_s = pygame.mixer.Sound('audio/killing.mp3')
killing_s.set_volume(0.16)

main_game = MainGame()

player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

bullet_group = pygame.sprite.Group()

enemy_1 = pygame.image.load('./images/enemies/Ship1.png')
pygame.transform.flip(enemy_1, True, False)
enemy_2 = pygame.image.load('./images/enemies/Ship2.png')
pygame.transform.flip(enemy_2, True, False)
enemy_3 = pygame.image.load('./images/enemies/Ship3.png')
pygame.transform.flip(enemy_3, True, False)
enemy_4 = pygame.image.load('./images/enemies/Ship4.png')
pygame.transform.flip(enemy_4, True, False)
enemies_list = [enemy_1, enemy_2, enemy_3, enemy_4]
enemy_group = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        
        if player.is_dead:
            if event.type == pygame.KEYDOWN:
                main_game.restart_game()
            
    if pygame.mouse.get_pressed()[0]:
        player.shoot()
        
    main_game.collisions()
    
    screen.blit(bg, (0, 0))
    bullet_group.draw(screen)
    player_group.draw(screen)
    enemy_group.draw(screen)
    player_group.update()
    bullet_group.update()
    enemy_group.update()
    
    main_game.text_render()
    
    pygame.display.update()
    clock.tick(60)