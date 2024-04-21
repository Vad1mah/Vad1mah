import pygame, sys, random

def ball_animation():
    global ball_speed_x, ball_speed_y
    
    if ball.colliderect(player):
        if ball.left <= player.right:
            ball_speed_x *= -1
            ball_speed_x += 1
            print(ball_speed_x, ball_speed_y)
        elif ball.top == player.bottom:
            ball_speed_y *= -1
        elif ball.bottom == player.top:
            ball_speed_y *= -1
        
            
    if ball.colliderect(opponent):
        if ball.right >= opponent.left:
            ball_speed_x *= -1
        elif ball.top == opponent.bottom:
            ball_speed_y *= -1
        elif ball.bottom == opponent.top:
            ball_speed_y *= -1
                
             
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    if ball.bottom >= screen_height or ball.top <= 0:
        ball_speed_y *= -1
    if ball.right >= screen_width or ball.left <= 0:
        restart_ball()


def restart_ball():
    global ball_speed_x, ball_speed_y
    
    ball.center = (screen_width/2, screen_height/2)
    
    ball_speed_x = 0
    ball_speed_y = 0
    

pygame.init()
clock = pygame.time.Clock()

screen_width, screen_height = 1280, 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(10, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)

ball_speed_x = 0
ball_speed_y = 0

light_grey = pygame.Color('grey12')
bg_color = pygame.Color('grey40')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ball_speed_x = random.choice([12, -12])
                ball_speed_y = random.choice([12, -12])
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        if player.bottom < screen_height:
            player.y += 10
    if keys[pygame.K_w]:
        if player.top > 0:
            player.y -= 10
    if keys[pygame.K_DOWN]:
        if opponent.bottom < screen_height:
            opponent.y += 10
    if keys[pygame.K_UP]:
        if opponent.top > 0:
            opponent.y -= 10
            
    ball_animation()
    
    screen.fill(bg_color)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw. aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))
    
    pygame.display.flip()
    clock.tick(60)