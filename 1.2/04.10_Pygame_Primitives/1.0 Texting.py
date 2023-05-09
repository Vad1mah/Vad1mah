import pygame
pygame.init()

display = pygame.display.set_mode( (200, 200) )

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print('enter')
            elif event.key == pygame.K_SPACE:
                print('space')
            elif event.key == pygame.K_w:
                print('w')
            elif event.key == pygame.K_a:
                print('a')
            elif event.key == pygame.K_s:
                print('s')
            elif event.key == pygame.K_d:
                print('d')
            elif event.key == pygame.K_ESCAPE:
                print('esc')
            elif event.key == pygame.K_LEFT:
                print('Левая стрелка')
            elif event.key == pygame.K_RIGHT:
                print('Правая стрелка')
            elif event.key == pygame.K_UP:
                print('Стрелка вверх')
            elif event.key == pygame.K_DOWN:
                print('Стрелка вниз')
        elif event.type == pygame.QUIT:
                pygame.quit()
                exit()