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




class Unit(pygame.sprite.Sprite):

    def __init__(self, x, y):

        pygame.sprite.Sprite.__init__(self)


        self.image = pygame.image.load("Units/BlueUnits/blueRank6.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.selected = False

    def getPos(self):
        return self.rect.x, self.rect.y

    
    def update(self):
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
        self.rect.x = x
        self.rect.y = y

    def selectUnit(self):
        mx, my = pygame.mouse.get_pos()
        x = self.rect.x
        y = self.rect.y
        print(x, y, mx, my)
        
        if x <= mx <= x + 40 and y <= mx < y + 40:
            self.selected = True
        else:
            self.selected = False


blue6 = Unit(150, 150)
allUnits.add(blue6)
blueUnits.add(blue6)

allsprites = pygame.sprite.RenderPlain((blue6))

running = True
while running:

    screen.blit(logo, (0,0))
    screen.blit(board, (150, 150))
    allsprites.draw(screen)
    pygame.display.flip()

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
##            mx, my = pygame.mouse.get_pos()
##            blue6.rect.x = mx - 20
##            blue6.rect.y = my - 20
            blue6.selectUnit()
            print(blue6.selected)
