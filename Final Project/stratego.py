import pygame
import ranks

#Define screen size, grid size
(width, height) = (500, 500)
##squareWidth = 50
##squareHeight = 50
##grid = []


#Load images/colors onto screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Stratego")
board = pygame.image.load("Images/strategoBoard.jpg")
logo = pygame.image.load("Images/strategoLogo.png")
introScreen = pygame.display.set_mode((width, height))
screen.convert()


#Initialize sprite groups
allUnits = pygame.sprite.Group()
blueUnits = pygame.sprite.Group()
redUnits = pygame.sprite.Group()

def setupUnits():

    #--Blue Units--#

    blueFlag = ranks.RankFlag(0, 0, "blue")
    allUnits.add(blueFlag)
    blueUnits.add(blueFlag)

    blueSpy = ranks.RankSpy(1, 0, "blue")
    allUnits.add(blueSpy)
    blueUnits.add(blueSpy)

    blueBomb = ranks.RankBomb(2, 0, "blue")
    allUnits.add(blueBomb)
    blueUnits.add(blueBomb)

    blue2 = ranks.Rank2(3, 0, "blue")
    allUnits.add(blue2)
    blueUnits.add(blue2)

    blue3 = ranks.Rank3(4, 0, "blue")
    allUnits.add(blue3)
    blueUnits.add(blue3)

    blue4 = ranks.Rank4(5, 0, "blue")
    allUnits.add(blue4)
    blueUnits.add(blue4)

    blue5 = ranks.Rank5(6, 0, "blue")
    allUnits.add(blue5)
    blueUnits.add(blue5)

    blue6 = ranks.Rank6(7, 0, "blue")
    allUnits.add(blue6)
    blueUnits.add(blue6)

    blue7 = ranks.Rank7(8, 0, "blue")
    allUnits.add(blue7)
    blueUnits.add(blue7)

    blue8 = ranks.Rank8(9, 0, "blue")
    allUnits.add(blue8)
    blueUnits.add(blue8)

    blue9 = ranks.Rank9(4, 1, "blue")
    allUnits.add(blue9)
    blueUnits.add(blue9)

    blue10 = ranks.Rank10(5, 1, "blue")
    allUnits.add(blue10)
    blueUnits.add(blue10)

    #--Red Units--#

    redFlag = ranks.RankFlag(0, 9, "red")
    allUnits.add(redFlag)
    redUnits.add(redFlag)

    redSpy = ranks.RankSpy(1, 9, "red")
    allUnits.add(redSpy)
    redUnits.add(redSpy)

    redBomb = ranks.RankBomb(2, 9, "red")
    allUnits.add(redBomb)
    redUnits.add(redBomb)

    red2 = ranks.Rank2(3, 9, "red")
    allUnits.add(red2)
    redUnits.add(red2)

    red3 = ranks.Rank3(4, 9, "red")
    allUnits.add(red3)
    redUnits.add(red3)

    red4 = ranks.Rank4(5, 9, "red")
    allUnits.add(red4)
    redUnits.add(red4)

    red5 = ranks.Rank5(6, 9, "red")
    allUnits.add(red5)
    redUnits.add(red5)

    red6 = ranks.Rank6(7, 9, "red")
    allUnits.add(red6)
    redUnits.add(red6)

    red7 = ranks.Rank7(8, 9, "red")
    allUnits.add(red7)
    redUnits.add(red7)

    red8 = ranks.Rank8(9, 9, "red")
    allUnits.add(red8)
    redUnits.add(red8)

    red9 = ranks.Rank9(4, 8, "red")
    allUnits.add(red9)
    redUnits.add(red9)

    red10 = ranks.Rank10(5, 8, "red")
    allUnits.add(red10)
    redUnits.add(red10)

def printRow():
    for row in ranks.grid:
        print(row)

#Main Functions
setupUnits()

for unit in allUnits:
    row, col = unit.getPos()
    ranks.grid[row][col] += 1
printRow()

def intro():
    pygame.init()
    gameloop = True

    
    introScreen.fill((0, 0, 128))
    introScreen.blit(logo, (0,0))
    pygame.display.flip()
    
    while gameloop:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameloop = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pygame.display.flip()
                return
    
def gameloop():
    running = True
    while running:

        screen.blit(board, (0, 0))
        allUnits.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            for unit in allUnits:

                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if unit.selected == True:
                        unit.update()
                        printRow()
                    else:
                        unit.selectUnit()

                    print(unit.selected)




intro()
gameloop()
