import pygame

class Figure:


    def __init__(self, fig_x, fig_y, filename, squareW):
        self.x = fig_x
        self.y = fig_y
        self.bitmap = pygame.image.load(filename)
        self.bitmap = pygame.transform.scale(self.bitmap, squareW)

    def render(self):

        gameDisplay.blit(self.bitmap, (self.x, self.y))




pygame.init()
#Параметры экрана
display_w = 800
display_h = 600
#Цвета
black = (0, 0, 0)
grey = (100, 100, 100)
white = (255, 255, 255)
fancyBlue = (71, 71, 71)

gameDisplay = pygame.display.set_mode((display_w, display_h))
pygame.display.set_caption("Chess")
clock = pygame.time.Clock()


#Параметры поля
fieldImg = pygame.image.load('chess field.png')
fieldSize = ((display_w*2)//3, (display_w*2)//3)
fieldX = display_w/2 - fieldSize[0]/2
fieldY = display_h/2 - fieldSize[1]/2
fieldImg = pygame.transform.scale(fieldImg, fieldSize)
squareW = (int((fieldSize[0]//8)*0.8), int((fieldSize[1]//8)*0.8))

#Фигуры
bp1 = Figure(100, 100, "black_pawn.png", squareW)

def field(x, y):
    gameDisplay.blit(fieldImg, (x, y))


done = False

while not done:
    # Обработчик событий
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = True
        if e.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())



    # Цвет и отрисовка
    gameDisplay.fill(fancyBlue)
    field(fieldX, fieldY)
    bp1.render()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()