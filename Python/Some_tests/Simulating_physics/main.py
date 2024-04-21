import pygame, sys, pymunk

def create_apple(space, pos):
    body = pymunk.Body(1, 50, body_type = pymunk.Body.DYNAMIC)
    body.position = (pos)
    shape = pymunk.Circle(body, 46)
    space.add(body, shape)
    return shape

def draw_apples(apples):
    for apple in apples:
        apple_rect = apple_surface.get_rect(center = apple.body.position)
        screen.blit(apple_surface, apple_rect)
    
def static_ball(space, pos):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = (pos)
    shape = pymunk.Circle(body, 50)
    space.add(body, shape)
    return shape

def draw_static_balls(balls):
    for ball in balls:
        pygame.draw.circle(screen, (0, 0, 0), ball.body.position, 50)
        
        
pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0, 500)
apple_surface = pygame.image.load('apple_red.png').convert_alpha()
apple_surface = pygame.transform.scale(apple_surface, (400, 400))
apples = []

balls = []
balls.append(static_ball(space, (500, 500)))
balls.append(static_ball(space, (230, 250)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            apples.append(create_apple(space, event.pos))
            
    screen.fill((217, 217, 217))
    draw_apples(apples)
    draw_static_balls(balls)
    space.step(1/50)
    pygame.display.flip()
    clock.tick(60)