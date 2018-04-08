import pygame

background_colour = (0, 0, 128)
(width, height) = (800, 800)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Stratego")
board = pygame.image.load("strategoBoard.jpg")
logo = pygame.image.load("strategoLogo.png")
screen.fill(background_colour)
screen.convert()

allUnits = pygame.sprite.Group()
blueUnits = pygame.sprite.Group()
redUnits = pygame.sprite.Group()




#Super Class
class Unit(pygame.sprite.Sprite):

    def __init__(self, x, y):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("blueCover.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.selected = False

    def getPos(self):
        return self.rect.x, self.rect.y

    
    def update(self):
        if self.selected == True:
            mx, my = pygame.mouse.get_pos()
            self.rect.x = mx - 20
            self.rect.y = my - 20
            self.selected = False
        else:

    def selectUnit(self):
        mx, my = pygame.mouse.get_pos()
        x = self.rect.x
        y = self.rect.y
        print(x, y, mx, my)
        
        if x <= mx <= x + 40 and y <= my < y + 40:
            self.selected = True
        
##        else:
##            self.selected = False


#Sub Classes

class Rank2(Unit):

    def __init__(self, x, y, team):

        Unit.__init__(self, x, y)
        self.rank = 2
        self.team = team


class Rank3(Unit):

    def __init__(self, x, y, team):

        Unit.__init__(self, x, y)
        self.rank = 3
        self.team = team

class Rank4(Unit):

    def __init__(self, x, y, team):

        Unit.__init__(self, x, y)
        self.rank = 4
        self.team = team

class Rank5(Unit):

    def __init__(self, x, y, team):

        Unit.__init__(self, x, y)
        self.rank = 5
        self.team = team

class Rank6(Unit):

    def __init__(self, x, y, team):

        Unit.__init__(self, x, y)
        self.rank = 6
        self.team = team
        self.image = pygame.image.load("Units/BlueUnits/blueRank6.jpg")
        

class Rank7(Unit):

    def __init__(self, x, y, team):

        Unit.__init__(self, x, y)
        self.rank = 7
        self.team = team






blue6 = Rank6(200, 200, "blue")
allUnits.add(blue6)
blueUnits.add(blue6)



#allsprites = pygame.sprite.RenderPlain((blue6))

running = True
while running:

    screen.blit(logo, (0,0))
    screen.blit(board, (150, 150))
    allUnits.draw(screen)
    pygame.display.flip()

    for event in pygame.event.get():
        for unit in allUnits:
    
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                unit.update()
                if unit.selected == False:
                    unit.selectUnit()
                
                print(unit.selected)
