import pygame

class Figure:
    def __init__(self, fig_x, fig_y, filename, squareW):
        self.x = fig_x
        self.y = fig_y
        self.bitmap = pygame.image.load(filename)
        self.bitmap = pygame.transform.scale(self.bitmap, squareW)


    def render(self):

        gameDisplay.blit(self.bitmap, (self.x, self.y))

class Pawn(Figure):
    pass
# Вспомогательные функции
def collision(mouse_x, mouse_y ,obj_x ,obj_y, len):
    if mouse_x > obj_x and mouse_x < (obj_x+len) and mouse_y > obj_y and mouse_y < (obj_y+len):
        return True
    else:
        return False


def Dragging(object, mouse_x, mouse_y, offset_x, offset_y):
    object.x = mouse_x + offset_x
    object.y = mouse_y + offset_y

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

def field(x, y):
    gameDisplay.blit(fieldImg, (x, y))


#Фигуры
bp1 = Pawn(100, 100, "black_pawn.png", squareW)
b_pawns = [bp1]



done = False
dragging = False

while not done:
    # Обработчик событий
    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = True
        elif e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                for obj in b_pawns:
                    if collision(mouse_x, mouse_y, obj.x, obj.y, squareW[0]):
                        dragging = True
                        offset_x = obj.x - mouse_x
                        offset_y = obj.y - mouse_y
                        dragging_object = obj
        elif e.type == pygame.MOUSEBUTTONUP:
            if e.button == 1:
                dragging = False
        elif e.type == pygame.MOUSEMOTION:
            for obj in b_pawns:
                if dragging:
                    Dragging(dragging_object, mouse_x, mouse_y, offset_x, offset_y)










    # Цвет и отрисовка
    gameDisplay.fill(fancyBlue)
    field(fieldX, fieldY)
    bp1.render()
    pygame.display.update()
    clock.tick(120)

pygame.quit()
quit()