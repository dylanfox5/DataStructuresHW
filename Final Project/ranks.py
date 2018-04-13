import pygame



#Define grid size
squareWidth = 50
squareHeight = 50
grid = []
playerMoved = False

#Create grid
for row in range(10):
    grid.append([])
    for col in range(10):
        grid[row].append(0)

#Super Class
class Unit(pygame.sprite.Sprite):

    def __init__(self, row, col):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("Images/blueCover.png")
        self.rect = self.image.get_rect()
        self.rect.x = (row * squareWidth) + 3 #intialize with grid coords - convert to x, y
        self.rect.y = (col * squareHeight) + 3
        self.selected = False

    def getPos(self):
        mx, my = self.rect.x, self.rect.y
        row = mx // (squareWidth)
        col = my // (squareHeight)
        return row, col
    
    def update(self):
        if self.selected == True:
            mx, my = pygame.mouse.get_pos()

            newRow = mx // (squareWidth)
            newCol = my // (squareHeight)

            row = self.rect.x // (squareWidth)
            col = self.rect.y // (squareHeight)

            if newRow == 2 and newCol == 4:
                print("Can't move there, man!")
                self.selected = False
                return
            elif newRow == 2 and newCol == 5:
                print("Can't move there, man!")
                self.selected = False
                return
            elif newRow == 3 and newCol == 4:
                print("Can't move there, man!")
                self.selected = False
                return
            elif newRow == 3 and newCol == 5:
                print("Can't move there, man!")
                self.selected = False
                return
            elif newRow == 6 and newCol == 4:
                print("Can't move there, man!")
                self.selected = False
                return
            elif newRow == 6 and newCol == 5:
                print("Can't move there, man!")
                self.selected = False
                return
            elif newRow == 7 and newCol == 4:
                print("Can't move there, man!")
                self.selected = False
                return
            elif newRow == 7 and newCol == 5:
                print("Can't move there, man!")
                self.selected = False
                return
            elif grid[newRow][newCol] == 1:
                print("Can't move there!")
                self.selected = False
            elif self.rank == 1 or self.rank == 0:
                print("Can't move this unit, man!")
                self.selected = False
                return
            elif self.team == "blue" and (newRow - row > 1 or newCol - col > 1) and self.rank != 2:
                print("Can only move one space!")
            elif self.team == "red" and (row - newRow > 1 or col - newCol > 1) and self.rank != 2:
                print("Can only move one space!")
            else:
                self.rect.x = (newRow * squareWidth) + 3
                self.rect.y = (newCol * squareHeight) + 3
                grid[newRow][newCol] = 1
                grid[row][col] = 0
                self.selected = False
        else:
            return 

    def selectUnit(self):
        mx, my = pygame.mouse.get_pos()
        x = self.rect.x
        y = self.rect.y
        self.selected = True
        
        if x <= mx <= x + 40 and y <= my < y + 40:
            self.selected == True
        else:
            self.selected = False

#Sub Classes
class Rank2(Unit):

    def __init__(self, x, y, team):

        Unit.__init__(self, x, y)
        self.rank = 2
        self.team = team
        
        if self.team == "blue":
            self.image = pygame.image.load("Units/BlueUnits/blueRank2.jpg")
            self.baseImage = "Units/BlueUnits/blueRank2.jpg"
        elif self.team == "red":
            self.image = pygame.image.load("Units/RedUnits/redRank2.jpg")
            self.baseImage = "Units/RedUnits/redRank2.jpg"

class Rank3(Unit):

    def __init__(self, x, y, team):

        Unit.__init__(self, x, y)
        self.rank = 3
        self.team = team
        
        if self.team == "blue":
            self.image = pygame.image.load("Units/BlueUnits/blueRank3.jpg")
            self.baseImage = "Units/BlueUnits/blueRank3.jpg"
        elif self.team == "red":
            self.image = pygame.image.load("Units/RedUnits/redRank3.jpg")
            self.baseImage = "Units/RedUnits/redRank3.jpg"

class Rank4(Unit):

    def __init__(self, x, y, team):

        Unit.__init__(self, x, y)
        self.rank = 4
        self.team = team
        
        if self.team == "blue":
            self.image = pygame.image.load("Units/BlueUnits/blueRank4.jpg")
            self.baseImage = "Units/BlueUnits/blueRank4.jpg"
        elif self.team == "red":
            self.image = pygame.image.load("Units/RedUnits/redRank4.jpg")
            self.baseImage = "Units/RedUnits/redRank4.jpg"

class Rank5(Unit):

    def __init__(self, x, y, team):

        Unit.__init__(self, x, y)
        self.rank = 5
        self.team = team
        
        if self.team == "blue":
            self.image = pygame.image.load("Units/BlueUnits/blueRank5.jpg")
            self.baseImage = "Units/BlueUnits/blueRank5.jpg"
        elif self.team == "red":
            self.image = pygame.image.load("Units/RedUnits/redRank5.jpg")
            self.baseImage = "Units/RedUnits/redRank5.jpg"

class Rank6(Unit):

    def __init__(self, x, y, team):

        Unit.__init__(self, x, y)
        self.rank = 6
        self.team = team
        
        if self.team == "blue":
            self.image = pygame.image.load("Units/BlueUnits/blueRank6.jpg")
            self.baseImage = "Units/BlueUnits/blueRank6.jpg"
        elif self.team == "red":
            self.image = pygame.image.load("Units/RedUnits/redRank6.jpg")
            self.baseImage = "Units/RedUnits/redRank6.jpg"
        

class Rank7(Unit):

    def __init__(self, x, y, team):

        Unit.__init__(self, x, y)
        self.rank = 7
        self.team = team
        
        if self.team == "blue":
            self.image = pygame.image.load("Units/BlueUnits/blueRank7.jpg")
            self.baseImage = "Units/BlueUnits/blueRank7.jpg"
        elif self.team == "red":
            self.image = pygame.image.load("Units/RedUnits/redRank7.jpg")
            self.baseImage = "Units/RedUnits/redRank7.jpg"

class Rank8(Unit):
    
    def __init__(self, x, y, team):

        Unit.__init__(self, x, y)
        self.rank = 8
        self.team = team
        
        if self.team == "blue":
            self.image = pygame.image.load("Units/BlueUnits/blueRank8.jpg")
            self.baseImage = "Units/BlueUnits/blueRank8.jpg"
        elif self.team == "red":
            self.image = pygame.image.load("Units/RedUnits/redRank8.jpg")
            self.baseImage = "Units/RedUnits/redRank8.jpg"

class Rank9(Unit):

    def __init__(self, x, y, team):

        Unit.__init__(self, x, y)
        self.rank = 9
        self.team = team
        
        if self.team == "blue":
            self.image = pygame.image.load("Units/BlueUnits/blueRank9.jpg")
            self.baseImage = "Units/BlueUnits/blueRank9.jpg"
        elif self.team == "red":
            self.image = pygame.image.load("Units/RedUnits/redRank9.jpg")
            self.baseImage = "Units/RedUnits/redRank9.jpg"

class Rank10(Unit):
    
    def __init__(self, x, y, team):

        Unit.__init__(self, x, y)
        self.rank = 10
        self.team = team
        
        if self.team == "blue":
            self.image = pygame.image.load("Units/BlueUnits/blueRank10.jpg")
            self.baseImage = "Units/BlueUnits/blueRank10.jpg"
        elif self.team == "red":
            self.image = pygame.image.load("Units/RedUnits/redRank10.jpg")
            self.baseImage = "Units/RedUnits/redRank10.jpg"

class RankBomb(Unit):
    
    def __init__(self, x, y, team):

        Unit.__init__(self, x, y)
        self.rank = 11
        self.team = team
        
        if self.team == "blue":
            self.image = pygame.image.load("Units/BlueUnits/blueRankBomb.jpg")
            self.baseImage = "Units/BlueUnits/blueRankBomb.jpg"
        elif self.team == "red":
            self.image = pygame.image.load("Units/RedUnits/redRankBomb.jpg")
            self.baseImage = "Units/RedUnits/redRankBomb.jpg"


class RankSpy(Unit):
    
    def __init__(self, x, y, team):

        Unit.__init__(self, x, y)
        self.rank = 1
        self.team = team
        
        if self.team == "blue":
            self.image = pygame.image.load("Units/BlueUnits/blueRankSpy.jpg")
            self.baseImage = "Units/BlueUnits/blueRankSpy.jpg"
        elif self.team == "red":
            self.image = pygame.image.load("Units/RedUnits/redRankSpy.jpg")
            self.baseImage = "Units/RedUnits/redRankSpy.jpg"

class RankFlag(Unit):
    
    def __init__(self, x, y, team):

        Unit.__init__(self, x, y)
        self.rank = 0
        self.team = team

        if self.team == "blue":
            self.image = pygame.image.load("Units/BlueUnits/blueRankFlag.jpg")
            self.baseImage = "Units/BlueUnits/blueRankFlag.jpg"
        elif self.team == "red":
            self.image = pygame.image.load("Units/RedUnits/redRankFlag.jpg")
            self.baseImage = "Units/RedUnits/redRankFlag.jpg"
