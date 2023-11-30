import pygame, sys
from settings import *

class Checker(pygame.sprite.Sprite):
    def __init__(self, coor, color, direction, pos):
        super().__init__()
        self.coor = coor
        self.color = color
        self.direction = direction
        self.chosen = False
        self.available_moves = []
        self.enemies = []
        # self.max_kills = 0
        
        self.image = pygame.image.load(f'./images/{self.color}_checker.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.pos = pos
        self.rect = self.image.get_rect(center = ((pos[0] + cell_size[0]/2, pos[1] + cell_size[1]/2)))

        self.image_queen = pygame.image.load(f'./images/{self.color}_checker_queen.png').convert_alpha()
        self.image_queen = pygame.transform.scale(self.image_queen, (40, 40))
        
    def update(self):
        pass

class Cell(pygame.sprite.Sprite):
    def __init__(self, coor, pos):
        super().__init__()
        self.coor = coor
        self.clicked = False
        self.occupied = False
        self.able_to_go = False
        
        self.pos = pos
        self.image = pygame.Surface(cell_size)
        self.image.fill('green')
        self.rect = self.image.get_rect(topleft = (pos))
    
    def update(self):
        pass


class Game():     
    def __init__(self, status = "choose_side", chosen_side = None):
        
        self.status = status
        
        self.cellsList = pygame.sprite.Group()
        self.checkersList = pygame.sprite.Group()
        
        self.cellChanges = CellChanges(self.cellsList, self.checkersList)
        self.checkerChanges = CheckerChanges(self.cellsList, self.checkersList)
        
        self.cellChanges.createCells()
        self.checkerChanges.createCheckers()
        
        self.turn = chosen_side
        self.whiteMoveExists = False
        self.blackMoveExists = False
        self.killExists = False
        self.someoneKillied = False
        self.pickedChecker = None
        self.checkerPicked = False

    def createChooseSideWindow(self):
        self.choice_surface = pygame.Surface((300, 200))
        self.choice_surface.fill('grey')
        self.choice_rect = self.choice_surface.get_rect(center = ((screen_size[0]/2, screen_size[1]/2)))
        
        self.choice_text = font_big.render('Choose side', 1, 'black')
        self.choice_text_rect = self.choice_text.get_rect(center = ((screen_size[0]/2, screen_size[1]/2 - 60)))

        self.black_side = pygame.Surface((70, 70))
        self.black_side.fill('black')
        self.white_side = pygame.Surface((70, 70))
        self.white_side.fill('white')
        
        self.black_side_rect = self.black_side.get_rect(center = ((screen_size[0]/2 - 60, screen_size[1]/2 + 20)))
        self.white_side_rect = self.white_side.get_rect(center = ((screen_size[0]/2 + 60, screen_size[1]/2 + 20)))
        
        self.status = 'choice_window'
    
    def createResultWindow(self):
        self.result_surface = pygame.Surface((300, 200))
        self.result_surface.fill('grey')
        self.result_rect = self.result_surface.get_rect(center = ((screen_size[0]/2, screen_size[1]/2)))
        
        if self.turn == 'white':
            self.result_text = font_big.render('black won!', 1, 'black')
        else:
            self.result_text = font_big.render('white won!', 1, 'white')
        self.result_text_rect = self.result_text.get_rect(center = ((screen_size[0]/2, screen_size[1]/2 - 30)))

        self.button = pygame.Surface((80, 30))
        self.button.fill('red')
        self.button_rect = self.button.get_rect(center = ((screen_size[0]/2, screen_size[1]/2 + 70)))
        
        self.button_text = font_small.render('try again', 1, 'white')
        self.button_text_rect = self.button_text.get_rect(center = ((screen_size[0]/2, screen_size[1]/2 + 70)))
        
        self.status = 'show_result'
    
    def availableMoves(self, checkers_for_loop, flag = None):
        self.whiteMoveExists = False
        self.blackMoveExists = False
        self.killExists = False
        
        if flag == 'after_kill':
            for checker in self.checkersList:
                checker.available_moves.clear()
        
        for checker in checkers_for_loop:
            if checker.color != self.turn:
                continue
            
            checkers_coor = checker.coor
            
            # for queen
            if checker.direction == 'back_forward':
                bottom_left = []
                bottom_right = []
                top_left = []
                top_right = []
                directions_list = [bottom_left, bottom_right, top_left, top_right]
                next_cells = [[],[],[],[]]
                closest_enemies = [[],[],[],[]]
                self.queenCanKill = False
                
                for direction in ['bottom_left', 'bottom_right', 'top_left', 'top_right']:
                    x_coor, y_coor = checkers_coor[0], checkers_coor[1]
                    
                    for move in range(7):
                        if direction == 'bottom_left' and (x_coor > 1 and y_coor < 8):
                            bottom_left.append((x_coor - 1, y_coor + 1))
                            x_coor, y_coor = bottom_left[move][0], bottom_left[move][1] 
                            
                        elif direction == 'bottom_right' and (x_coor < 8 and y_coor < 8):
                            bottom_right.append((x_coor + 1, y_coor + 1))
                            x_coor, y_coor = bottom_right[move][0], bottom_right[move][1]
                            
                        elif direction == 'top_left' and (x_coor > 1 and y_coor > 1):
                            top_left.append((x_coor - 1, y_coor - 1))
                            x_coor, y_coor = top_left[move][0], top_left[move][1]
                            
                        elif direction == 'top_right' and (x_coor < 8 and y_coor > 1):
                            top_right.append((x_coor + 1, y_coor - 1))
                            x_coor, y_coor = top_right[move][0], top_right[move][1]
                            
                        else:
                            break
                                
                for ally in self.checkersList:
                    if ally.color == checker.color:
                        for direction in directions_list:
                            for index, cell in enumerate(direction):
                                if ally.coor == cell:
                                    del direction[index:]
                                    
            else: # for simple
                bottom_left = (checkers_coor[0] - 1, checkers_coor[1] + 1)
                bottom_right = (checkers_coor[0] + 1, checkers_coor[1] + 1)
                top_left = (checkers_coor[0] - 1, checkers_coor[1] - 1)
                top_right = (checkers_coor[0] + 1, checkers_coor[1] - 1)
            
            for cell in self.cellsList:
                if not cell.occupied and flag != 'after_kill':
                    if checker.direction == 'back':
                        if (cell.coor == bottom_left or cell.coor == bottom_right):
                            checker.available_moves.append(cell.coor)
                            self.blackMoveExists = True
                            
                    elif checker.direction == 'forward':
                        if (cell.coor == top_left or cell.coor == top_right):
                            checker.available_moves.append(cell.coor)
                            self.whiteMoveExists = True
                            
                    elif checker.direction == 'back_forward':
                        for way in directions_list:
                            if cell.coor in way:
                                checker.available_moves.append(cell.coor)
                                if checker.color == 'white':
                                    self.whiteMoveExists = True
                                else:
                                    self.blackMoveExists = True
                                break

                        
                elif cell.occupied:
                    for enemy in self.checkersList:
                        if cell.coor == enemy.coor and enemy.color != checker.color:
                            if checker.direction == 'back_forward': # for queen
                                for index, way in enumerate(directions_list):
                                    if cell.coor in way:
                                        x_coor, y_coor = cell.coor[0], cell.coor[1]
                                        possible_moves = []
                        
                                        for move in range(6):
                                            if index == 0 and (x_coor > 1 and y_coor < 8):
                                                possible_moves.append((x_coor - 1, y_coor + 1))
                                            elif index == 1 and (x_coor < 8 and y_coor < 8):
                                                possible_moves.append((x_coor + 1, y_coor + 1))
                                            elif index == 2 and (x_coor > 1 and y_coor > 1):
                                                possible_moves.append((x_coor - 1, y_coor - 1))
                                            elif index == 3 and (x_coor < 8 and y_coor > 1):
                                                possible_moves.append((x_coor + 1, y_coor - 1))   
                                            else:
                                                break
                                            x_coor, y_coor = possible_moves[move][0], possible_moves[move][1]
                                        
                                        if len(possible_moves) > len(next_cells[index]):
                                            next_cells[index] = possible_moves
                                            closest_enemies[index] = enemy
                                        break
                                                        
                            else: # for simple
                                if cell.coor == bottom_left:
                                    next_cell = (cell.coor[0] - 1, cell.coor[1] + 1) 
                                elif cell.coor == bottom_right:
                                    next_cell = (cell.coor[0] + 1, cell.coor[1] + 1)
                                elif cell.coor == top_left:
                                    next_cell = (cell.coor[0] - 1, cell.coor[1] - 1)
                                elif cell.coor == top_right:
                                    next_cell = (cell.coor[0] + 1, cell.coor[1] - 1)
                                else:
                                    continue
                                        
                                for extra_cell in self.cellsList:
                                    if not extra_cell.occupied and extra_cell.coor == next_cell:
                                        checker.available_moves.append(extra_cell.coor)
                                        checker.enemies.append([enemy, extra_cell.coor])
                                        if checker.color == 'white':
                                            self.whiteMoveExists = True
                                        elif checker.color == 'black':
                                            self.blackMoveExists = True
                                        self.killExists = True
                                        
                                        break
                                break
                    
            if checker.direction == 'back_forward':
                for index, direction in enumerate(next_cells): # for queen
                    for next_cell in direction:
                        for extra_cell in self.cellsList:
                            if extra_cell.coor == next_cell:
                                if not extra_cell.occupied:
                                    checker.available_moves.append(extra_cell.coor)
                                    checker.enemies.append([closest_enemies[index], extra_cell.coor])
                                    self.killExists = True
                                    self.queenCanKill = True
                                    break
                                else:
                                    break
                                
                        if not self.queenCanKill:
                            break
                        else:
                            self.queenCanKill = False
                        
    
    def ifCanKill(self):
        if self.killExists:
            for checker in self.checkersList:
                checker.available_moves.clear()
                if checker.color == self.turn:
                    for enemy in checker.enemies:
                        checker.available_moves.append(enemy[1])
    
    def checkGameOver(self):
        if self.turn == 'white' and not self.whiteMoveExists:
            self.status = 'game_over'
        elif self.turn == 'black' and not self.blackMoveExists:
            self.status = 'game_over'
    
    def blur(self):
        self.pickedChecker = None
        self.checkerPicked = False
    
    def draw(self):
        for checker in self.checkersList:
            screen.blit(checker.image, checker.rect)
            
        if self.checkerPicked:
            for move in self.pickedChecker.available_moves:
                for cell in self.cellsList:
                    if move == cell.coor and cell.able_to_go:
                        screen.blit(cell.image, cell.rect)
    
    def ifCheckerPicked(self, click):
        for checker in self.checkersList:
            if checker.color == self.turn and checker.rect.collidepoint(click):
                checker.chosen = True
                self.pickedChecker = checker
                self.checkerPicked = True
            else:
                checker.chosen = False
                
    def ifDoTurn(self, click):
        for cell in self.cellsList:
            if cell.rect.collidepoint(click) and cell.able_to_go:
                self.checkerChanges.moveChecker(self.pickedChecker, cell)
                self.checkerChanges.upgradeChecker()
                
                if self.killExists:
                    self.doKill(self.pickedChecker, cell.coor)
                    self.availableMoves([self.pickedChecker], 'after_kill')
                    
                    if not self.killExists:
                        self.status = 'next_turn'
                else:
                    self.status = 'next_turn'
                    
                break
            
        self.blur()
        
    def doKill(self, checker, cell_coor):
        for enemy in checker.enemies:
            if enemy[1] == cell_coor:
                enemy[0].kill()
                self.someoneKillied = True
                break
        
    def changeTurn(self):
        if self.turn == 'white':
            self.turn = 'black'
        else:
            self.turn = 'white'
    
    def restart_game(self):
        self.cellsList = pygame.sprite.Group()
        self.checkersList = pygame.sprite.Group()
        
        self.cellChanges.createCells()
        self.checkerChanges.createCheckers()
        
        self.status = 'next_turn'
    
    def run(self):
        self.draw()
        
        if self.checkerPicked:
            self.cellChanges.able_cells(self.pickedChecker)
        else:
            self.cellChanges.reset_able_cells()     
        
        if self.status == 'choose_side':
            self.createChooseSideWindow()
        
        elif self.status == 'next_turn':
            self.changeTurn()
            self.cellChanges.checkOccupied()
            self.checkerChanges.reset_moves()
            self.checkerChanges.reset_enemies()
            self.availableMoves(self.checkersList)
            self.ifCanKill()
            self.status = 'wait_moves'
            self.checkGameOver()
            
        elif self.status == 'game_over':
            self.createResultWindow()
        
        elif self.status == 'choice_window':
            screen.blit(self.choice_surface, self.choice_rect)
            screen.blit(self.choice_text, self.choice_text_rect)
            screen.blit(self.black_side, self.black_side_rect)
            screen.blit(self.white_side, self.white_side_rect)
        
        elif self.status == 'show_result':
            screen.blit(self.result_surface, self.result_rect)
            screen.blit(self.result_text, self.result_text_rect)
            screen.blit(self.button, self.button_rect)
            screen.blit(self.button_text, self.button_text_rect)

class CheckerChanges():
    def __init__(self, cellsList, checkersList):
        self.cellsList = cellsList
        self.checkersList = checkersList
        self.pickedChecker = None
    
    def createCheckers(self):
        for y in range(1, 4):
            pos_y = start_pos[1] + (cell_size[1]) * (y - 1)
            for x in range(1 + (y % 2), 9, 2):
                pos_x = start_pos[0] + (cell_size[0]) * (x - 1)
                
                self.checkersList.add(Checker((x, y), 'black', 'back', (pos_x, pos_y)))

        for y in range(6, 9):
            pos_y = start_pos[1] + (cell_size[1]) * (y - 1)
            for x in range(1 + (y % 2), 9, 2):
                pos_x = start_pos[0] + (cell_size[0]) * (x - 1)
                
                self.checkersList.add(Checker((x, y), 'white', 'forward', (pos_x, pos_y)))
        
    def moveChecker(self, checker, cell):
        checker.coor = cell.coor
        checker.pos = cell.pos
        checker.rect = checker.image.get_rect(center = ((checker.pos[0] + cell_size[0]/2, checker.pos[1] + cell_size[1]/2)))
    
    def reset_moves(self):
        for checker in self.checkersList:
            checker.available_moves.clear()
    
    def reset_enemies(self):
        for checker in self.checkersList:
            checker.enemies.clear()
    
    def upgradeChecker(self):
        for checker in self.checkersList:
            if (checker.direction == 'forward' and checker.coor[1] == 1) or (checker.direction == 'back' and checker.coor[1] == 8):
                checker.direction = 'back_forward'
                checker.image = checker.image_queen

    def checkDirection(self):
        pass
    
    def checkStatus(self):
        pass

class CellChanges():
    def __init__(self, cellsList, checkersList):
        self.checkersList = checkersList
        self.cellsList = cellsList
        
    def createCells(self):
        for x in range(1, 9):
            pos_x = start_pos[0] + (cell_size[0]) * (x - 1)
            for y in range(1, 9):
                pos_y = start_pos[1] + (cell_size[1]) * (y - 1)

                self.cellsList.add(Cell((x, y), (pos_x, pos_y)))
    
    def checkOccupied(self):
        for cell in self.cellsList:
            for checker in self.checkersList:
                if cell.rect.colliderect(checker):
                    cell.occupied = True
                    break
                else:    
                    cell.occupied = False
    
    def able_cells(self, picked_checker):
        for cell in self.cellsList:
            for move in picked_checker.available_moves:
                if move == cell.coor:
                    cell.able_to_go = True
                    break
                else:
                    cell.able_to_go = False
    
    def reset_able_cells(self):
        for cell in self.cellsList:
            cell.able_to_go = False
    
    def update(self, screen):
        pass


pygame.init()
pygame.display.set_caption('Checkers')

screen = pygame.display.set_mode((screen_size[0], screen_size[1]))
clock = pygame.time.Clock()

bg = pygame.image.load('./images/desk.webp').convert_alpha()
font_small = pygame.font.Font('./font/ARCADEPI.TTF', 12)
font_big = pygame.font.Font('./font/ARCADEPI.TTF', 32)

game = Game()  
        
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            
            if game.checkerPicked:
                game.ifDoTurn(pos)
            
            if game.status != 'next_turn':
                game.ifCheckerPicked(pos)
                
            if game.status == 'show_result' and game.button_rect.collidepoint(pos):
                game = Game()
                
            if game.status == 'choice_window' and game.black_side_rect.collidepoint(pos):
                game.status == 'next_turn'
                game = Game('next_turn', 'white')
            elif game.status == 'choice_window' and game.white_side_rect.collidepoint(pos):
                game.status == 'next_turn'
                game = Game('next_turn', 'black')
            
    screen.blit(bg, (0, 0))
    game.run()
    
    pygame.display.update()
    clock.tick(60)