import pygame, sys
from pygame.math import Vector2

class Planet(pygame.sprite.Sprite):
    def __init__(self, image, pos, speed, id, size, distance):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center = (pos))
        self.speed = speed
        self.pos = pos
        self.id = id
        self.center = Vector2((539, 501))
        self.offset = Vector2((pos[0] - 539, 0))
        self.angle = 0
        
        self.size_text = font_text.render('Size:', False, 'thistle')
        self.size = font_text.render(f'{str(size)} km', False, 'white')
        if len(str(int(distance[0]))) != 1:
            self.distance_text = font_text.render('Distance (m. km):', False, 'thistle')
        else:
            self.distance_text = font_text.render('Distance (b. km):', False, 'thistle')
        self.distance = font_text.render(f'{distance[0]} - {distance[1]}', False, 'white')
        self.vector_angle = font_text.render('Vector angle:', False, 'thistle')
        
    def update(self):
        self.angle -= self.speed
        self.rect = self.image.get_rect(center = (pos))
        self.rect.center = self.center + self.offset.rotate(self.angle)
        
        self.angle_text = font_text.render(str(int(-self.angle % 360)), False, 'white')
        
class Legend():
    def __init__(self, name, id):
        self.id = id
        self.size = 100
        
        self.stroke = pygame.Surface((290, 74))
        self.stroke = self.stroke.convert_alpha()
        self.stroke.fill((72, 61, 139, 100))
        self.rect = self.stroke.get_rect(topleft = (1131, 333 + 79 * self.id))
        
        self.planet_name = font_text.render(name, False, 'thistle')
        self.planet_size = font_nums.render(str(self.size) + '%', False, 'white')
        
        self.plus_but = plus_but
        self.plus_but_rect = self.plus_but.get_rect(topleft = (self.rect.x + 225, self.rect.y + 44))
        
        self.minus_but = minus_but
        self.minus_but_rect = self.minus_but.get_rect(topleft = (self.rect.x + 260, self.rect.y + 44))
        
    def draw_info(self):
        screen.blit(self.stroke, self.rect)
        screen.blit(leg_img[self.id], (self.rect.x + 8, self.rect.y + 4))
        screen.blit(self.planet_name, (self.rect.x + 95, self.rect.y + 25))
        screen.blit(self.planet_size, (self.rect.x + 225, self.rect.y + 15))
        screen.blit(self.plus_but, self.plus_but_rect)
        screen.blit(self.minus_but, self.minus_but_rect)
        
    def checked(self, pos):
        if self.rect.collidepoint(pos):
            pygame.draw.rect(screen, 'midnightblue', self.rect)
            
            planet = planets_list[index]
            screen.blit(planet.size_text, (1131 + 20, 37 + 40))
            screen.blit(planet.size, (1131 + 100, 37 + 40)) 
            screen.blit(planet.distance_text, (1131 + 20, 37 + 100)) 
            screen.blit(planet.distance, (1131 + 20, 37 + 130)) 
            screen.blit(planet.vector_angle, (1131 + 20, 37 + 190)) 
            screen.blit(planet.angle_text, (1131 + 20, 37 + 220))   
        
        
pygame.init()
clock = pygame.time.Clock()

screen_width = 1464
screen_heigth = 1000
screen = pygame.display.set_mode((screen_width, screen_heigth))
pygame.display.set_caption('Solar system')
bg = pygame.image.load('./images/bg/bg.png').convert_alpha()
font_text = pygame.font.Font('./font/ARCADEPI.ttf', 24)
font_nums = pygame.font.Font('./font/ARCADEPI.ttf', 18)
pygame.mixer.music.load('./music/bg.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

mercury_img = pygame.image.load('./images/planets/mercury.png').convert_alpha()
venus_img = pygame.image.load('./images/planets/venus.png').convert_alpha()
earth_img = pygame.image.load('./images/planets/earth.png').convert_alpha()
mars_img = pygame.image.load('./images/planets/mars.png').convert_alpha()
jupiter_img = pygame.image.load('./images/planets/jupiter.png').convert_alpha()
saturn_img = pygame.image.load('./images/planets/saturn.png').convert_alpha()
uranus_img = pygame.image.load('./images/planets/uranus.png').convert_alpha()
neptune_img = pygame.image.load('./images/planets/neptune.png').convert_alpha()
start_img = [
    mercury_img,
    venus_img,
    earth_img,
    mars_img,
    jupiter_img,
    saturn_img,
    uranus_img,
    neptune_img
]

plus_but = pygame.image.load('./images/buttons/plus.png').convert_alpha()
minus_but = pygame.image.load('./images/buttons/minus.png').convert_alpha()

start_sizes = [
    (3.5, 3.5),
    (8.65, 8.65),
    (9.11, 9.11),
    (4.85, 4.85),
    (100, 100),
    (90, 80),
    (36.3, 36.3),
    (35.2, 35.2)
]

mercury_img_orb = pygame.transform.scale(mercury_img, start_sizes[0])
venus_img_orb = pygame.transform.scale(venus_img, start_sizes[1])
earth_img_orb = pygame.transform.scale(earth_img, start_sizes[2])
mars_img_orb = pygame.transform.scale(mars_img, start_sizes[3])
jupiter_img_orb = pygame.transform.scale(jupiter_img, start_sizes[4])
saturn_img_orb = pygame.transform.scale(saturn_img, start_sizes[5])
uranus_img_orb = pygame.transform.scale(uranus_img, start_sizes[6])
neptune_img_orb = pygame.transform.scale(neptune_img, start_sizes[7])

mercury_img_leg = pygame.transform.scale(mercury_img, (74, 66))
venus_img_leg = pygame.transform.scale(venus_img, (74, 66))
earth_img_leg = pygame.transform.scale(earth_img, (74, 66))
mars_img_leg = pygame.transform.scale(mars_img, (74, 66))
jupiter_img_leg = pygame.transform.scale(jupiter_img, (74, 66))
saturn_img_leg = pygame.transform.scale(saturn_img, (84, 66))
uranus_img_leg = pygame.transform.scale(uranus_img, (74, 66))
neptune_img_leg = pygame.transform.scale(neptune_img, (74, 66))
leg_img = [
    mercury_img_leg,
    venus_img_leg,
    earth_img_leg,
    mars_img_leg,
    jupiter_img_leg,
    saturn_img_leg,
    uranus_img_leg,
    neptune_img_leg
]

mercury = Planet(mercury_img_orb, (638, 501), 1.6, 0, 4879, (46, 69.8))
venus = Planet(venus_img_orb, (667, 501), 1.17, 1, 12103, (107.4, 108.9))
earth = Planet(earth_img_orb, (695, 501), 1, 2, 12742, (147, 152))
mars = Planet(mars_img_orb, (745, 501), 0.8, 3, 6780, (206, 249))
jupiter = Planet(jupiter_img_orb, (809, 501), 0.44, 4, 139822, (740, 816))
saturn = Planet(saturn_img_orb, (870, 501), 0.32, 5, 116464, (1.353, 1.513))
uranus = Planet(uranus_img_orb, (933, 501), 0.29, 6, 50724, (2.748, 3.004))
neptune = Planet(neptune_img_orb, (997, 501), 0.18, 7, 49244, (4.452, 4.554))

planets = pygame.sprite.Group()
planets.add(mercury)
planets.add(venus)
planets.add(earth)
planets.add(mars)
planets.add(jupiter)
planets.add(saturn)
planets.add(uranus)
planets.add(neptune)

planets_list = [
    mercury,
    venus,
    earth,
    mars,
    jupiter,
    saturn,
    uranus,
    neptune
]

mercur_leg = Legend('Mercury', 0)
venus_leg = Legend('Venus', 1)
earth_leg = Legend('Earth', 2)
mars_leg = Legend('Mars', 3)
jupiter_leg = Legend('Jupiter', 4)
saturn_leg = Legend('Saturn', 5)
uranus_leg = Legend('Uranus', 6)
neptune_leg = Legend('Neptune', 7)

leg_list = [mercur_leg,
            venus_leg,
            earth_leg,
            mars_leg,
            jupiter_leg,
            saturn_leg,
            uranus_leg,
            neptune_leg
]

earth_count_img = pygame.transform.scale(earth_img, (25, 25))

while True:
    pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for elem in leg_list:
                if elem.plus_but_rect.collidepoint(pos):
                    if elem.size < 500:
                        elem.size += 10
                        elem.planet_size = font_nums.render(str(elem.size) + '%', False, 'white')
                if elem.minus_but_rect.collidepoint(pos):
                    if elem.size > 10:
                        elem.size -= 10
                        elem.planet_size = font_nums.render(str(elem.size) + '%', False, 'white')
                        
                for planet in planets:
                    if elem.id == planet.id:
                        new_image = pygame.transform.scale(start_img[elem.id], (start_sizes[elem.id][0] * elem.size / 100, start_sizes[elem.id][1] * elem.size / 100))
                        planet.image = new_image
    
    screen.blit(bg, (0, 0))
    
    planets.draw(screen)
    planets.update()
    
    for index, elem in enumerate(leg_list):
        elem.checked(pos)
        elem.draw_info()
    
    screen.blit(earth_count_img, (20, 45))
    screen.blit(font_nums.render('days: ' + str(int(-earth.angle * (360/365))), False, 'white'), (55, 50))
    
    pygame.display.flip()
    clock.tick(10)