import pygame, sys
        
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

obstacle_surface = pygame.image.load('alpha.png').convert_alpha()
obstacle_pos = (100, 100)
obstacle_mask = pygame.mask.from_surface(obstacle_surface)

new_obstacle_surface = obstacle_mask.to_surface()
new_obstacle_surface.set_colorkey((0, 0, 0))
new_obstacle_surface.fill('orange', special_flags=pygame.BLEND_RGB_MULT)
# surf_w, surf_h = new_obstacle_surface.get_size()
# for x in range(surf_w):
#     for y in range(surf_h):
#         if new_obstacle_surface.get_at((x, y))[0] != 0:
#             new_obstacle_surface.set_at((x, y), 'orange')
            

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill('grey')
    
    offset = 4
    screen.blit(new_obstacle_surface, (obstacle_pos[0] + offset, obstacle_pos[1])) # right
    screen.blit(new_obstacle_surface, (obstacle_pos[0] - offset, obstacle_pos[1])) # left
    screen.blit(new_obstacle_surface, (obstacle_pos[0], obstacle_pos[1] + offset)) # bottom
    screen.blit(new_obstacle_surface, (obstacle_pos[0], obstacle_pos[1] - offset)) # top
    screen.blit(new_obstacle_surface, (obstacle_pos[0] + offset, obstacle_pos[1] - offset)) # topright 
    screen.blit(new_obstacle_surface, (obstacle_pos[0] - offset, obstacle_pos[1] - offset)) # topleft
    screen.blit(new_obstacle_surface, (obstacle_pos[0] - offset, obstacle_pos[1] + offset)) # bottomleft
    screen.blit(new_obstacle_surface, (obstacle_pos[0] + offset, obstacle_pos[1] + offset)) # bottomright
    screen.blit(obstacle_surface, obstacle_pos)
    
    # for point in obstacle_mask.outline():
    #     x = point[0] + obstacle_pos[0]
    #     y = point[1] + obstacle_pos[1]
    #     pygame.draw.circle(screen, 'red', (x, y), 3)
    
    pygame.display.update()
    clock.tick(60)