import pygame, sys, random

class MinesweeperGame():     # Управление ходом игры
    def __init__(self):
        # Задание основых параметров для дальнейшей работы с ячейками и минами
        self.width = 800
        self.height = 600
        self.numMines = None
        self.playerGrid = [list() for _ in range(10)]
        self.status = 'menu'
        self.win = False
        self.fistCellCoor = None
    
    def initializeGame(self):     # Инициализация состояния
        
        # Запуск пайгема и создание вспомогательных переменных
        if self.status == 'menu':
            pygame.init()
            pygame.display.set_caption('Minesweeper')

            self.screen = pygame.display.set_mode((self.width, self.height))
            self.clock = pygame.time.Clock()
            
            self.fontS = pygame.font.Font('./font/Realest-Extended.otf', 32)
            self.fontB = pygame.font.Font('./font/Realest-Extended.otf', 48)
            self.fontNums = pygame.font.Font('./font/Realest-Extended.otf', 24)
            
            self.mineImg = pygame.image.load('./images/mine.png').convert_alpha()
            self.mineImg = pygame.transform.scale(self.mineImg, (30, 30))
            self.flagImg = pygame.image.load('./images/flag.png').convert_alpha()
            self.flagImg = pygame.transform.scale(self.flagImg, (30, 30))
        
        elif self.status == 'waitForClick':
            # Создание и задание расположения клеток
            for y, row in enumerate(self.playerGrid):
                for x in range(10):
                    # Отступ слева и сверху по 120px, размер клетки 40x40 px
                    pos = (120 + x * 40, 120 + y * 40)
                    row.append(Cell(pos))
        
        # минирование поля после первого клика
        elif self.status == 'gameStart':

            # Минирование рандомных клеток за исключением первой кликнутой клетки
            self.numMines = random.randint(10, 20)
            
            fistGenerate = True
            correctNums = False
            for _ in range(self.numMines):
                while not correctNums:
                    row = random.randint(0, 9)
                    cell = random.randint(0, 9)
                    # минируем, если первая генерация (так как ещё нет предыдущих координат) или
                    # координаты предыдущей поставленной бомбы не совпадают с новыми как и с координатами первого клика
                    if fistGenerate or (row != lastRow and row != self.fistCellCoor[0] and cell != lastCell and cell != self.fistCellCoor[1]):
                        lastRow = row
                        lastCell = cell
                        correctNums = True
                        fistGenerate = False
                    
                # Обновляем статус клетки
                self.playerGrid[row][cell].isMine = True
                correctNums = False
            
            # Открываем первую клеткой, по которой нажимали
            for rowIndex in range(10):
                for cellIndex in range(10):
                    if rowIndex == self.fistCellCoor[0] and cellIndex == self.fistCellCoor[1]:
                        self.revealCell(rowIndex, cellIndex)
                        break
                    
        # Обновление списка клеток, обнуление итога и перезапуск   
        elif self.status == 'gameEnd':
            self.playerGrid = [list() for _ in range(10)]
            self.win = False
            self.fistCellCoor = None
            game.status = 'waitForClick'
            self.initializeGame()
            
    def showMenu(self):     # Создание названия игры, кнопок и текстом внутри них
           
        # Название игры
        gameName = self.fontB.render('Minesweeper', 1, 'white')
        gameNameRect = gameName.get_rect(center = ((self.width/2, self.height/2 - 200)))
        
        # Кнопка Start
        startButton = pygame.Surface((200, 60))
        startButton.fill('red')
        self.startButtonRect = startButton.get_rect(center = ((self.width/2, self.height/2 - 70)))
        
        startButtonText = self.fontS.render('start', 1, 'white')
        startButtonTextRect = startButtonText.get_rect(center = ((self.width/2, self.height/2 - 70)))
        
        # Кнопка Exit
        exitButton = pygame.Surface((200, 60))
        exitButton.fill('red')
        self.exitButtonRect = exitButton.get_rect(center = ((self.width/2, self.height/2 + 20)))
        
        exitButtonText = self.fontS.render('exit', 1, 'white')
        exitButtonTextRect = exitButtonText.get_rect(center = ((self.width/2, self.height/2 + 20)))
        
        
        # Отображение названия игры
        self.screen.blit(gameName, gameNameRect)
        
        # Отображение кнопок с текстом
        self.screen.blit(startButton, self.startButtonRect)
        self.screen.blit(startButtonText, startButtonTextRect)
        
        self.screen.blit(exitButton, self.exitButtonRect)
        self.screen.blit(exitButtonText, exitButtonTextRect)
    
    def showEndButtons(self):     # Отображение кнопок результата
        # Проверка результата
        if self.win:
            result = 'won'
        else:
            result = 'lost'
        
        # Результат
        resultText = self.fontS.render(('You ' + result), 1, 'white')
        resultTextRect = resultText.get_rect(center = ((self.width/2 + 250, self.height/2 - 100)))
        
        # Кнопка Try again
        tryAgainButton = pygame.Surface((250, 60))
        tryAgainButton.fill('red')
        self.tryAgainButtonRect = tryAgainButton.get_rect(center = ((self.width/2 + 250, self.height/2 + 30)))
        
        tryAgainButtonText = self.fontS.render('try again', 1, 'white')
        tryAgainButtonTextRect = tryAgainButtonText.get_rect(center = ((self.width/2 + 250, self.height/2 + 30)))
        
        # Кнопка Exit
        exitButton = pygame.Surface((250, 60))
        exitButton.fill('red')
        self.exitButtonRect = exitButton.get_rect(center = ((self.width/2 + 250, self.height/2 + 120)))
        
        exitButtonText = self.fontS.render('exit', 1, 'white')
        exitButtonTextRect = exitButtonText.get_rect(center = ((self.width/2 + 250, self.height/2 + 120)))
        
        
        # Отображение результата
        self.screen.blit(resultText, resultTextRect)
        
        # Отображение кнопок с текстом
        self.screen.blit(tryAgainButton, self.tryAgainButtonRect)
        self.screen.blit(tryAgainButtonText, tryAgainButtonTextRect)
        
        self.screen.blit(exitButton, self.exitButtonRect)
        self.screen.blit(exitButtonText, exitButtonTextRect)
    
    def showCells(self):    # Отображение клеток
        for row in self.playerGrid:
            for cell in row:
                # Отрисовка цвета клетки и рамки
                self.screen.blit(cell.surface, cell.rect)
                pygame.draw.rect(cell.surface, 'dimgray', (0, 0, 40, 40), 1)
                
                if cell.isRevealed:
                    # Если клетка только что открылась, проверяем, заминирована или нет
                    
                    # Если да, то отображаем мину
                    if cell.isMine:
                        mineRect = cell.surface.get_rect(center = (cell.pos[0] + 5, cell.pos[1] + 5))
                        self.screen.blit(self.mineImg, mineRect)
                     
                    # Если нет, считаем сколько мин рядом и отображаем число на ней    
                    elif cell.adjacentMinesCount > 0:
                        if cell.adjacentMinesCount == 1:
                            color = 'blue'
                        elif cell.adjacentMinesCount == 2:
                            color = 'green'
                        elif cell.adjacentMinesCount == 3:
                            color = 'red'
                        elif cell.adjacentMinesCount == 4:
                            color = 'midnightblue'
                        elif cell.adjacentMinesCount == 5:
                            color = 'darkred'
                        elif cell.adjacentMinesCount == 6:
                            color = 'lightseagreen'
                        elif cell.adjacentMinesCount == 7:
                            color = 'pink'
                        elif cell.adjacentMinesCount == 8:
                            color = 'black'
                            
                        adjacentMines = self.fontNums.render(str(cell.adjacentMinesCount), 5, color)
                        numRect = cell.surface.get_rect(center = (cell.pos[0] + 8, cell.pos[1] + 8))
                        self.screen.blit(adjacentMines, numRect)
                        
                        
                # Если на ней стоит флажок, и клетка не откралась, то отображаем его на ней
                elif cell.isFlagged:
                    flagRect = cell.surface.get_rect(center = (cell.pos[0] + 5, cell.pos[1] + 5))
                    self.screen.blit(self.flagImg, flagRect)
                 
    
    def revealCell(self, row, col, autoRevealing = False):     # Вскрытие клетки
        cell = self.playerGrid[row][col]
        
        # Открываем, если она ещё не была открыта, и на ней нет флага или это автоматическое открытие соседних клеток после клика
        if not cell.isRevealed and (not cell.isFlagged or autoRevealing):
            cell.reveal()
            
            # Проверяем после открытия, есть ли нераскрытые свободные клетки, если вдруг игрок победил
            self.unrevealedCellsExistence()
            
            # Если клетка не заминирована, расчитываем мины и свободные клетки в округе. В противном случае проиграли
            if not cell.isMine:
                self.adjacentMines(row, col)
            else:
                self.status = 'gameEnd'
    
    def placeFlag(self, row, col):     # Установка/убирание флага
        cell = self.playerGrid[row][col]
        
        # Если клетка ещё не открыта, на ней можно поставить/убрать флаг
        if not cell.isRevealed:
            cell.toggleFlag()
    
    def adjacentMines(self, row, col, secondTime = False):     # Расчёт мин вокруг ячейки
        cell = self.playerGrid[row][col]
        
        # Проверяем все 8 ячеек вокруг кликнутой 
        for direction in range(8):
            if row - 1 >= 0 and col - 1 >= 0 and direction == 0:   # Левая верхняя
                newRow = row - 1
                newCol = col - 1
            elif row - 1 >= 0 and direction == 1:                  # Левая
                newRow = row - 1
                newCol = col
            elif row - 1 >= 0 and col + 1 <= 9 and direction == 2: # Левая нижняя
                newRow = row - 1
                newCol = col + 1
            elif col - 1 >= 0 and direction == 3:                  # Верхняя
                newRow = row
                newCol = col - 1
            elif col + 1 <= 9 and direction == 4:                  # Нижняя
                newRow = row
                newCol = col + 1
            elif row + 1 <= 9 and col - 1 >= 0 and direction == 5: # Правая верхняя
                newRow = row + 1
                newCol = col - 1
            elif row + 1 <= 9 and direction == 6:                  # Правая
                newRow = row + 1
                newCol = col
            elif row + 1 <= 9 and col + 1 <= 9 and direction == 7: # Правая нижняя
                newRow = row + 1
                newCol = col + 1
            else:
                continue
            
            # Если такая существует, находим её
            newCell = self.playerGrid[newRow][newCol]
            
            # Если она заминирована и это не повторный расчёт расчёт мин, то увеличиваем кол-во ближайших мин клетки на 1
            if newCell.isMine and not secondTime:
                cell.adjacentMinesCount += 1

            # Если же мин не нашлось за первую функцию и это повторная, то по очереди открываем каждую из 8 клеток вокруг кликнутой с учётом, что это автооткрытие после клика
            elif secondTime:
                self.revealCell(newRow, newCol, True)
        
        # Если это не повторная функция и вокруг клетки не нашли мин, вызываем её снова для открытия соседних клеток от кликнутой
        if not secondTime and cell.adjacentMinesCount == 0: 
            self.adjacentMines(row, col, True)
    
    def unrevealedCellsExistence(self):     # Определения существования незаминированных нераскрытых клеток
        unrevealedCellExist = False
        
        # Ищем такие клетки и если не находим, то игрок победил
        for row in self.playerGrid:
            for cell in row:
                if not cell.isRevealed and not cell.isMine:
                    unrevealedCellExist = True
        
        if not unrevealedCellExist:
            self.win = True
            self.status = 'gameEnd'
            
    def revealAllMines(self):     # Открываем все мины в конце игры
        for row in self.playerGrid:
            for cell in row:
                if cell.isMine:
                    cell.reveal()
        
class Cell():     # Класс игровой ячейки поля
    def __init__(self, pos):
        self.isMine = False
        self.isRevealed = False
        self.isFlagged = False
        self.adjacentMinesCount = 0
        self.pos = pos
        
        # Красим клетки 40x40 px и создаём рамку вокруг через pygame.Rect()
        self.surface = pygame.Surface((40, 40))
        self.surface.fill('lightblue')
        self.rect = self.surface.get_rect(center = (pos))
        
    def reveal(self):     # Метод вскрытия
        
        # Меняем статус клетки на вскрытую и цвет
        self.isRevealed = True
        if not self.isMine:
            self.surface.fill('white')
        else:
            self.surface.fill('red')
            
    def toggleFlag(self):     # Метод переключения флажка
        if self.isFlagged:
            self.isFlagged = False
        else:
            self.isFlagged = True


game = MinesweeperGame()
game.initializeGame()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            
            # Добавляем события на кнопки start и exit при запуске игры
            if game.status == 'menu':
                if game.startButtonRect.collidepoint(pos):
                    game.status = 'waitForClick'
                    game.initializeGame()
                elif game.exitButtonRect.collidepoint(pos):
                    sys.exit()
            
            # Проверяем первый клик по клетке
            elif game.status == 'waitForClick':
                for rowIndex in range(10):
                    for cellIndex in range(10):
                        
                        # Запоминаем координаты первой клетки и меняем статус
                        if game.playerGrid[rowIndex][cellIndex].rect.collidepoint(pos):
                            game.fistCellCoor = (rowIndex, cellIndex)
                            game.status = 'gameStart'
                            game.initializeGame()
                            break
            
            # Проверяем клики по клетке
            elif game.status == 'gameStart':
                for rowIndex in range(10):
                    for cellIndex in range(10):
                        
                        # Если это клики по клетке
                        if game.playerGrid[rowIndex][cellIndex].rect.collidepoint(pos):
                            if event.button == 1:     # лкм
                                game.revealCell(rowIndex, cellIndex)
                            elif event.button == 3:   # пкм
                                game.placeFlag(rowIndex, cellIndex)
            
            # Добавляем события на кнопки try again и exit при выводе результата
            elif game.status == 'gameEnd':
                if game.tryAgainButtonRect.collidepoint(pos):
                    game.initializeGame()
                elif game.exitButtonRect.collidepoint(pos):
                    sys.exit()
                      

    game.screen.fill((127,127,127))
    
    # Отображаем меню, если только что запустили игру
    if game.status == 'menu':
        game.showMenu()

    # Отображаем ячейки, если ждём первого клика или он уже был
    elif game.status == 'waitForClick' or game.status == 'gameStart':
        game.showCells()

    # Отображаем ячейки, бомбы и результат, если проиграли/выиграли
    elif game.status == 'gameEnd':
        game.showCells()
        game.revealAllMines()
        game.showEndButtons()

    pygame.display.update()
    game.clock.tick(60)