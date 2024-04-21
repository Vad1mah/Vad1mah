import pygame, sys
        
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

player_surface = pygame.Surface((50, 50))
player_surface.fill('red')
player_rect = player_surface.get_rect(center = (300, 300))
player_mask = pygame.mask.from_surface(player_surface)

obstacle_surface = pygame.image.load('alpha.png').convert_alpha()
obstacle_pos = (100, 100)
obstacle_mask = pygame.mask.from_surface(obstacle_surface)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill('white')
    
    screen.blit(obstacle_surface, obstacle_pos)
    
    if pygame.mouse.get_pos():
        player_rect.center = pygame.mouse.get_pos()
    screen.blit(player_surface, player_rect)
    
    offset_x = obstacle_pos[0] - player_rect.left
    offset_y = obstacle_pos[1] - player_rect.top
    #if player_mask.overlap(obstacle_mask, (offset_x, offset_y)):
    #    print('collision')
    
    if player_mask.overlap_area(obstacle_mask, (offset_x, offset_y)) >= 100:
        print('collision')
    
    pygame.display.update()
    clock.tick(60)