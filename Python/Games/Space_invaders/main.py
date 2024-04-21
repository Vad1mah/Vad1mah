import pygame, sys
from player import Player
import obstacle
from alien import Alien, Extra
from random import choice, randint
from laser import Laser

class Game:
    def __init__(self):
        player_sprite = Player((screen_width / 2, screen_hight), screen_width, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)
        
        self.lives = 3
        self.live_surf = pygame.image.load('graphics/player.png').convert_alpha()
        self.live_x_start_pos = screen_width - self.live_surf.get_width() * self.lives - 1 + 20
        self.score = 0
        self.font = pygame.font.Font('font/Pixeled.ttf', 20)
        
        self.shape = obstacle.shape
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.obstacle_amount = 4
        self.obstacle_x_positions = [num * (screen_width / self.obstacle_amount) for num in range(self.obstacle_amount)]
        self.create_multiple_obstacles(*self.obstacle_x_positions, x_start = screen_width / 15, y_start = 480)
        
        self.aliens = pygame.sprite.Group()
        self.alien_lasers = pygame.sprite.Group()
        self.alien_setup(rows = 6, cols = 8)
        self.alien_direction = 1
        
        self.extra = pygame.sprite.GroupSingle()
        
        music = pygame.mixer.Sound('audio/music.wav')
        music.set_volume(0.1)
        music.play(-1)
        self.laser_sound = pygame.mixer.Sound('audio/laser.wav')
        self.laser_sound.set_volume(0.2)
        self.explosion_sound = pygame.mixer.Sound('audio/explosion.wav')
        self.explosion_sound.set_volume(0.3)
        
    def create_obstacle(self, x_start, y_start, offset_x):
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == 'x':
                    x = x_start + col_index * self.block_size + offset_x
                    y = y_start + row_index * self.block_size
                    block = obstacle.Block(self.block_size, (241, 79, 80), x, y)
                    self.blocks.add(block)
                    
    def create_multiple_obstacles(self, *offset, x_start, y_start):
        for offset_x in offset:
            self.create_obstacle(x_start, y_start, offset_x)
        
    def alien_setup(self, rows, cols, width = 60, height = 48, x_offset = 70, y_offset = 100):
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = col_index * width + x_offset
                y = row_index * height + y_offset
                
                if row_index == 0:
                    alien_sprite = Alien('yellow', x, y)
                elif 1 <= row_index <= 2:
                    alien_sprite = Alien('green', x, y)
                elif 3 <= row_index <= 5:
                    alien_sprite = Alien('red', x, y)
                
                self.aliens.add(alien_sprite)
    
    def alien_position_checker(self):
        all_aliens = self.aliens.sprites()
        for alien in all_aliens:
            if alien.rect.left <= 0:
                self.alien_direction = 1
                self.alien_move_down(2)
            elif alien.rect.right >= screen_width:
                self.alien_direction = -1
                self.alien_move_down(2)
                
    def alien_move_down(self, distance):
        if self.aliens:
            for alien in self.aliens.sprites():
                alien.rect.y += distance
                
    def alien_shoot(self):
        if self.aliens.sprites():
            random_alien = choice(self.aliens.sprites())
            laser_sprite = Laser(random_alien.rect.center, 6, screen_hight)
            self.alien_lasers.add(laser_sprite)
            self.laser_sound.play()
    
    def collisions_checks(self):
        pygame.sprite.groupcollide(self.player.sprite.lasers, self.blocks, True, True)
        pygame.sprite.groupcollide(self.player.sprite.lasers, self.alien_lasers, True, True)
        aliens_hit = pygame.sprite.groupcollide(self.aliens, self.player.sprite.lasers, True, True)
        for alien in aliens_hit:
            self.score += alien.value
            self.explosion_sound.play()
            
        if pygame.sprite.groupcollide(self.player.sprite.lasers, self.extra, True, True):
            self.score += 500
            self.explosion_sound.play()
            
        pygame.sprite.groupcollide(self.player.sprite.lasers, self.blocks, True, True)
        pygame.sprite.groupcollide(self.aliens, self.blocks, False, True)
        pygame.sprite.groupcollide(self.alien_lasers, self.blocks, True, True)
        if pygame.sprite.groupcollide(self.alien_lasers, self.player, True, False):
            self.lives -= 1
            if self.lives <= 0:
                pygame.quit()
            
        # if self.player.sprite.lasers:
        #     for laser in self.player.sprite.lasers:
        #         if pygame.sprite.spritecollide(laser, self.blocks, True):
        #             laser.kill()

    def display_lives(self):
        for live in range(self.lives - 1):
            x = self.live_x_start_pos + live * (self.live_surf.get_width() + 20)
            y = 8
            screen.blit(self.live_surf, (x, y))
    
    def display_score(self):
        score_surf = self.font.render(f'score: {self.score}', False, 'white')
        score_rect = score_surf.get_rect(topleft = (20, -10))
        screen.blit(score_surf, score_rect)
    
    def victory_message(self):
        if not self.aliens.sprites():
            victory_surf = self.font.render('You won', False, 'white')
            victory_rect = victory_surf.get_rect(center = (screen_width / 2, screen_hight / 2))
            screen.blit(victory_surf, victory_rect)
    
    def run(self):
        self.player.update()
        self.aliens.update(self.alien_direction)
        self.alien_lasers.update()
        self.extra.update()
        
        self.collisions_checks()
        self.alien_position_checker()
        
        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)
        self.blocks.draw(screen)
        self.aliens.draw(screen)
        self.alien_lasers.draw(screen)
        self.extra.draw(screen)
        self.display_lives()
        self.display_score()
        self.victory_message()
            
    
class CRT:
    def __init__(self):
        self.tv = pygame.image.load('graphics/tv.png').convert_alpha()
        self.tv = pygame.transform.scale(self.tv, (screen_width, screen_hight))
    
    def create_crt_lines(self):
        line_height = 30
        line_amount = int(screen_hight/ line_height)
        for line in range(line_amount):
            y_pos = line * line_height
            pygame.draw.line(self.tv, 'gray10', (0, y_pos), (screen_width, y_pos), 1)
        
    def draw(self):
        self.tv.set_alpha(randint(180, 200))
        self.create_crt_lines()
        screen.blit(self.tv, (0, 0))

if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_hight = 600
    screen = pygame.display.set_mode((screen_width, screen_hight))
    pygame.display.set_caption('Space Invaders')
    FPS = 60
    clock = pygame.time.Clock()
    
    game = Game()
    crt = CRT()

    ALIENLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIENLASER, 800)
    EXTRASPAWN = pygame.USEREVENT + 2
    pygame.time.set_timer(EXTRASPAWN, 1000)

    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == ALIENLASER:
                    game.alien_shoot()
                if event.type == EXTRASPAWN:
                    game.extra.add(Extra(choice(['left', 'right']), screen_width))
                    pygame.time.set_timer(EXTRASPAWN, 7000)

        screen.fill((30, 30, 30))
        game.run()
        crt.draw()
        
        pygame.display.flip()
        clock.tick(FPS)