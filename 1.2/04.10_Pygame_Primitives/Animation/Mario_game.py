import pygame
import random
pygame.mixer.pre_init(44100, -16, 5, 4096)
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

pygame.mixer.music.load('audio/background_music.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.4)
channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)
channel3 = pygame.mixer.Channel(2)
channel4 = pygame.mixer.Channel(3)
s_enemy_die = pygame.mixer.Sound('audio/enemy_die.wav')
s_player_die = pygame.mixer.Sound('audio/player_die.wav')
s_player_jump_1 = pygame.mixer.Sound('audio/player_jump_1.wav')
s_player_jump_2 = pygame.mixer.Sound('audio/player_jump_2.wav')
s_player_jumps =[s_player_jump_1, s_player_jump_2]
s_player_respawn = pygame.mixer.Sound('audio/player_respawn.wav')

game_over = False
retry_text = font_small.render('НАЖМИТЕ ЛЮБУЮ КЛАВИШУ', True, (255, 255, 255))
retry_rect = retry_text.get_rect()
retry_rect.midtop = (W // 2, H // 2)

ground_image = pygame.image.load('images/ground.png')
ground_image = pygame.transform.scale(ground_image, (800, 100))
GROUND_H = ground_image.get_height()

enemy_image = pygame.image.load('images/goomba.png')
enemy_image = pygame.transform.scale(enemy_image, (60, 80))

enemy_dead_image = pygame.image.load('images/goomba.png')
enemy_dead_image = pygame.transform.scale(enemy_dead_image, (60, 50)) 

player_image = pygame.image.load('images/mario.png')
player_image = pygame.transform.scale(player_image, (60, 80))

mario_walk_left = [pygame.image.load('images/l1.png'), 
                   pygame.image.load('images/l2.png'), 
                   pygame.image.load('images/l3.png'), 
                   pygame.image.load('images/l4.png'), 
                   pygame.image.load('images/l5.png')]
mario_walk_left = [pygame.transform.scale(img, (60, 80)) for img in mario_walk_left]

mario_walk_right = [pygame.image.load('images/r1.png'), 
                   pygame.image.load('images/r2.png'), 
                   pygame.image.load('images/r3.png'), 
                   pygame.image.load('images/r4.png'), 
                   pygame.image.load('images/r5.png')]
mario_walk_right = [pygame.transform.scale(img, (60, 80)) for img in mario_walk_right]


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
        self.gravity = 0.4
        self.is_grounded = False
        self.walk_left = False
        self.walk_right = False
        self.anim_count = 0
        
    def handle_input(self):
        pass
    
    def kill(self, dead_image):
        self.image = dead_image
        self.is_dead = True
        self.x_speed = -self.x_speed
        self.y_speed = self.jump_speed
        
    def update(self):
        self.rect.x += self.x_speed
        self.y_speed += self.gravity
        self.rect.y += self.y_speed 
        
        if self.is_dead:
            if self.rect.top > H:
                self.is_out = True
        else:
            self.handle_input()
            
            if self.rect.bottom > H - GROUND_H:
                self.is_grounded = True
                self.y_speed = 0
                self.rect.bottom = H - GROUND_H
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(Entity):
         
    def __init__(self):
        super().__init__(player_image)
        self.respawn()
        self.hasPlayedGameOverSound = False
        
    def handle_input(self):
        self.x_speed = 0
        
        keys = pygame.key.get_pressed()
        if self.anim_count + 2 >= 60:
            self.anim_count = 0
            
        if keys[pygame.K_a]:
            if self.rect.x > 0:
                self.x_speed = -self.speed
            self.walk_left = True
            self.walk_right = False
            self.anim_count += 2
            
        elif keys[pygame.K_d]:
            if self.rect.x < W - 60:
                self.x_speed = self.speed
            self.walk_left = False
            self.walk_right = True
            self.anim_count += 2
    
        else:
            self.walk_left = False
            self.walk_right = False
            self.anim_count = 0
            
        if self.is_grounded and keys[pygame.K_SPACE]:
            self.is_grounded = False
            self.jump()
            
    def respawn(self):
        self.is_out = False
        self.is_dead = False
        self.rect.midbottom = (W // 2, H - GROUND_H)
        pygame.mixer.music.play(-1)
        channel2.play(s_player_respawn)
        channel4.stop()
            
    def jump(self):
        self.y_speed = self.jump_speed
        
        random_player_jump_s = random.choice(s_player_jumps)
        channel1.play(random_player_jump_s, loops = 0)


class Goomba(Entity):
    def __init__(self):
        super().__init__(enemy_image)
        self.spawn()
        
    def spawn(self):
        direction = random.randint(0, 1)
        
        if direction == 0:
            self.x_speed = self.speed
            self.rect.bottomright = (0,0)
        else:
            self.x_speed = -self.speed
            self.rect.bottomleft = (W, 0)
    
    def update(self):
        super().update()
        if self.x_speed > 0 and self.rect.left > W or self.x_speed < 0  and self.rect.right < 0:
            self.is_out = True

player = Player()
score = 0

goombas = []
INIT_DELAY = 2000
spawn_delay = INIT_DELAY
DECREASE_BASE = 1.01
last_spawn_time = pygame.time.get_ticks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if player.is_out:
                score = 0
                spawn_delay = INIT_DELAY
                last_spawn_time = pygame.time.get_ticks()
                player.respawn()
                goombas.clear()
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
        
    clock.tick(FPS)

    display.fill((92, 148, 252))
    
    display.blit(ground_image, (0, H - GROUND_H))
    
    score_text = font_large.render(str(score), True, (255, 255, 255))
    score_rect = score_text.get_rect()
    
    if player.is_out:
        score_rect.midbottom = (W // 2, H // 2)
        
        display.blit(retry_text, retry_rect)
    else:        
        if player.walk_left:
            player.update()
            display.blit(mario_walk_left[player.anim_count // 12], (player.rect.x, player.rect.y))
        
        elif player.walk_right:
            player.update()
            display.blit(mario_walk_right[player.anim_count // 12], (player.rect.x, player.rect.y))
            
        else:
            player.update()
            player.draw(display)
        
        now = pygame.time.get_ticks()
        elapsed = now - last_spawn_time
        if elapsed > spawn_delay:
            last_spawn_time = now
            goombas.append(Goomba())
            
        for goomba in list(goombas):
            if goomba.is_out:
                goombas.remove(goomba)
            else:
                goomba.update()
                goomba.draw(display)
                
            if not player.is_dead and not goomba.is_dead and player.rect.colliderect(goomba.rect):
                if player.rect.bottom - player.y_speed < goomba.rect.top:
                    goomba.kill(enemy_dead_image)
                    channel3.play(s_enemy_die)
                    player.jump()
                    score += 1
                    spawn_delay = INIT_DELAY / (DECREASE_BASE ** score)
                else:
                    player.kill(player_image)
                    pygame.mixer.music.stop()
                    channel4.play(s_player_die)
        
        score_rect.midtop = (W // 2, 5)
    
    display.blit(score_text, score_rect)
    pygame.display.flip()
    
quit()