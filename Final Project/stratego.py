import pygame
import ranks

pygame.init()


#Define screen size
(width, height) = (500, 500)
myFont = pygame.font.SysFont("Times New Roman", 100)
startLabel = myFont.render("Start", 1, (255, 255, 255))

#Load images/colors onto screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Stratego")
board = pygame.image.load("Images/strategoBoard.jpg")
logo = pygame.image.load("Images/strategoLogo.png")
blueCover = pygame.image.load("Images/blueCover.png")
redCover = pygame.image.load("Images/redCover.png")
introScreen = pygame.display.set_mode((width, height))
screen.convert()

#Initialize sprite groups
##allUnits = pygame.sprite.Group()
##blueUnits = pygame.sprite.Group()
##redUnits = pygame.sprite.Group()

def setupUnits():

    #--Blue Units--#

    blueFlag = ranks.RankFlag(0, 0, "blue")
    ranks.allUnits.add(blueFlag)
    ranks.blueUnits.add(blueFlag)

    blueSpy = ranks.RankSpy(1, 0, "blue")
    ranks.allUnits.add(blueSpy)
    ranks.blueUnits.add(blueSpy)

    blueBomb_0 = ranks.RankBomb(2, 0, "blue")
    ranks.allUnits.add(blueBomb_0)
    ranks.blueUnits.add(blueBomb_0)

    blueBomb_1 = ranks.RankBomb(2, 1, "blue")
    ranks.allUnits.add(blueBomb_1)
    ranks.blueUnits.add(blueBomb_1)

    blueBomb_2 = ranks.RankBomb(2, 2, "blue")
    ranks.allUnits.add(blueBomb_2)
    ranks.blueUnits.add(blueBomb_2)

    blue2_0 = ranks.Rank2(3, 0, "blue")
    ranks.allUnits.add(blue2_0)
    ranks.blueUnits.add(blue2_0)

    blue2_1 = ranks.Rank2(3, 1, "blue")
    ranks.allUnits.add(blue2_1)
    ranks.blueUnits.add(blue2_1)

    blue2_2 = ranks.Rank2(3, 2, "blue")
    ranks.allUnits.add(blue2_2)
    ranks.blueUnits.add(blue2_2)

    blue3_0 = ranks.Rank3(4, 0, "blue")
    ranks.allUnits.add(blue3_0)
    ranks.blueUnits.add(blue3_0)

    blue3_1 = ranks.Rank3(4, 1, "blue")
    ranks.allUnits.add(blue3_1)
    ranks.blueUnits.add(blue3_1)

    blue4_0 = ranks.Rank4(5, 0, "blue")
    ranks.allUnits.add(blue4_0)
    ranks.blueUnits.add(blue4_0)

    blue4_1 = ranks.Rank4(5, 1, "blue")
    ranks.allUnits.add(blue4_1)
    ranks.blueUnits.add(blue4_1)

    blue5_0 = ranks.Rank5(6, 0, "blue")
    ranks.allUnits.add(blue5_0)
    ranks.blueUnits.add(blue5_0)

    blue6_0 = ranks.Rank6(7, 0, "blue")
    ranks.allUnits.add(blue6_0)
    ranks.blueUnits.add(blue6_0)

    blue6_1 = ranks.Rank6(7, 1, "blue")
    ranks.allUnits.add(blue6_1)
    ranks.blueUnits.add(blue6_1)

    blue7 = ranks.Rank7(8, 0, "blue")
    ranks.allUnits.add(blue7)
    ranks.blueUnits.add(blue7)

    blue8_0 = ranks.Rank8(9, 0, "blue")
    ranks.allUnits.add(blue8_0)
    ranks.blueUnits.add(blue8_0)

    blue8_1 = ranks.Rank8(9, 1, "blue")
    ranks.allUnits.add(blue8_1)
    ranks.blueUnits.add(blue8_1)

    blue9 = ranks.Rank9(0, 1, "blue")
    ranks.allUnits.add(blue9)
    ranks.blueUnits.add(blue9)

    blue10 = ranks.Rank10(1, 1, "blue")
    ranks.allUnits.add(blue10)
    ranks.blueUnits.add(blue10)

    #--Red Units--#

    redFlag = ranks.RankFlag(0, 9, "red")
    ranks.allUnits.add(redFlag)
    ranks.redUnits.add(redFlag)

    redSpy = ranks.RankSpy(1, 9, "red")
    ranks.allUnits.add(redSpy)
    ranks.redUnits.add(redSpy)

    redBomb_0 = ranks.RankBomb(2, 9, "red")
    ranks.allUnits.add(redBomb_0)
    ranks.redUnits.add(redBomb_0)

    redBomb_1 = ranks.RankBomb(2, 8, "red")
    ranks.allUnits.add(redBomb_1)
    ranks.redUnits.add(redBomb_1)

    redBomb_2 = ranks.RankBomb(2, 7, "red")
    ranks.allUnits.add(redBomb_2)
    ranks.redUnits.add(redBomb_2)

    red2_0 = ranks.Rank2(3, 9, "red")
    ranks.allUnits.add(red2_0)
    ranks.redUnits.add(red2_0)

    red2_1 = ranks.Rank2(3, 8, "red")
    ranks.allUnits.add(red2_1)
    ranks.redUnits.add(red2_1)

    red2_2 = ranks.Rank2(3, 7, "red")
    ranks.allUnits.add(red2_2)
    ranks.redUnits.add(red2_2)

    red3_0 = ranks.Rank3(4, 9, "red")
    ranks.allUnits.add(red3_0)
    ranks.redUnits.add(red3_0)

    red3_1 = ranks.Rank3(4, 8, "red")
    ranks.allUnits.add(red3_1)
    ranks.redUnits.add(red3_1)

    red4_0 = ranks.Rank4(5, 9, "red")
    ranks.allUnits.add(red4_0)
    ranks.redUnits.add(red4_0)

    red4_1 = ranks.Rank4(5, 8, "red")
    ranks.allUnits.add(red4_1)
    ranks.redUnits.add(red4_1)

    red5 = ranks.Rank5(6, 9, "red")
    ranks.allUnits.add(red5)
    ranks.redUnits.add(red5)

    red6_0 = ranks.Rank6(7, 9, "red")
    ranks.allUnits.add(red6_0)
    ranks.redUnits.add(red6_0)

    red6_1 = ranks.Rank6(7, 8, "red")
    ranks.allUnits.add(red6_1)
    ranks.redUnits.add(red6_1)

    red7 = ranks.Rank7(8, 9, "red")
    ranks.allUnits.add(red7)
    ranks.redUnits.add(red7)

    red8_0 = ranks.Rank8(9, 9, "red")
    ranks.allUnits.add(red8_0)
    ranks.redUnits.add(red8_0)

    red8_1 = ranks.Rank8(9, 8, "red")
    ranks.allUnits.add(red8_1)
    ranks.redUnits.add(red8_1)

    red9 = ranks.Rank9(0, 8, "red")
    ranks.allUnits.add(red9)
    ranks.redUnits.add(red9)

    red10 = ranks.Rank10(1, 8, "red")
    ranks.allUnits.add(red10)
    ranks.redUnits.add(red10)

def printRow():
    for row in ranks.grid:
        print(row)            

#Main Functions
setupUnits()
#player1 = True

for unit in ranks.allUnits:
    row, col = unit.getPos()
    ranks.grid[col][row] += 1
printRow()

def intro():
    pygame.init()
    gameloop = True

    
    introScreen.fill((0, 0, 128))
    introScreen.blit(logo, (0,0))
    introScreen.blit(startLabel, (150, 150))
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
    player1 = True #blue team is player1
    running = True
    while running:
        for unit in ranks.allUnits:
            if player1 == True:
                    if unit.team == "red":
                        unit.image = redCover
                    else:
                        unit.image = pygame.image.load(unit.baseImage)
            elif player1 == False:
                    if unit.team == "blue":
                        unit.image = blueCover
                    else:
                        unit.image = pygame.image.load(unit.baseImage)

        screen.blit(board, (0, 0))
        ranks.allUnits.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            for unit in ranks.allUnits:

                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:

                    if unit.selected == True:
                        unit.update()
                        if player1 == True:
                            player1 = False
                        else:
                            player1 = True
                        printRow()
                    else:
                        unit.selectUnit()
                    print(unit.selected)




intro()
gameloop()
