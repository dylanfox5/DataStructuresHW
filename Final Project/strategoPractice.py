import pygame

background_colour = (0, 0, 0)
(width, height) = (255, 255)
sqWidth, sqHeight = 20, 20
margin = 5

grid = []
for row in range(10):
    grid.append([])
    for col in range(10):
        grid[row].append(0)

print(grid)

##screen = pygame.display.set_mode((width, height))
##pygame.display.set_caption("Stratego")
##board = pygame.image.load("strategoBoard.jpg")
##logo = pygame.image.load("strategoLogo.png")
##screen.fill(background_colour)
##screen.convert()


##screen.blit(logo, (0,0))
##screen.blit(board, (150, 150))
##pygame.display.flip()


running = True
pygame.init()
screen = pygame.display.set_mode((width, height))
screen.fill(background_colour)
while running:

##    screen.blit(logo, (0,0))
##    screen.blit(board, (150, 150))
##    pygame.display.flip()

    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (sqWidth + margin)
            row = pos[1] // (sqHeight + margin)
            grid[row][column] = 1
            print(row, column)


    for row in range(10):
        for col in range(10):
            color = (255, 255, 255)
            if grid[row][col] == 1:
                color = (0, 255, 0)
            pygame.draw.rect(screen, color, [(margin + sqWidth) * col + margin,
                              (margin + sqHeight) * row + margin,
                              width,
                              sqHeight])

    pygame.display.flip()
pygame.quit()
