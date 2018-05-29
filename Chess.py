import pygame

class Figure:
    def __init__(self, fig_x, fig_y, filename, squareW, name):
        self.x = fig_x
        self.y = fig_y
        self.bitmap = pygame.image.load(filename)
        #squareWX = int(squareW[0]*0.9)
        #squareWY = int(squareW[1]*0.9)
        self.bitmap = pygame.transform.scale(self.bitmap, squareW)
        self.name = name


    def render(self):

        gameDisplay.blit(self.bitmap, (self.x, self.y))

class Pawn(Figure):
    pass
# Вспомогательные функции
# Детекция коллижна мышки и объекта
def collision(mouse_x, mouse_y ,obj_x ,obj_y, len):
    if mouse_x > obj_x and mouse_x < (obj_x+len) and mouse_y > obj_y and mouse_y < (obj_y+len):
        return True
    else:
        return False

# Таскание мышкой объекта
def Dragging(object, mouse_x, mouse_y, offset_x, offset_y):
    object.x = mouse_x + offset_x
    object.y = mouse_y + offset_y

def pressed_square(mouse_x, mouse_y, square_coordinates, squareW, fieldX, fieldY):
    if mouse_x > fieldX and mouse_x < fieldX + squareW*8 and mouse_y > fieldY and mouse_y < fieldY + squareW*8:
        row_index = 0
        x_index = 0
        for row in square_coordinates:
            for x in row:
                if mouse_x > x[0] and mouse_x < (x[0] + squareW) and mouse_y > x[1] and mouse_y < (x[1] + squareW):
                    result = (row_index, x_index)
                x_index += 1
            x_index = 0
            row_index += 1
        return result
    else:
        result = (0, 0)
        return result



pygame.init()
#Параметры экрана
display_w = 860
display_h = 640
#Цвета
black = (0, 0, 0)
grey = (100, 100, 100)
white = (255, 255, 255)
fancyBlue = (71, 71, 71)

gameDisplay = pygame.display.set_mode((display_w, display_h))
pygame.display.set_caption("Chess")
clock = pygame.time.Clock()


#----------------------------Параметры поля-----------------------
fieldImg = pygame.image.load('chess field.png')
fieldSize = ((display_w*2)//3, (display_w*2)//3)
fieldX = display_w/2 - fieldSize[0]/2
fieldY = display_h/2 - fieldSize[0]/2
fieldImg = pygame.transform.scale(fieldImg, fieldSize)
squareW = (int((fieldSize[0]//8)), int((fieldSize[1]//8)))


# Получение границ квадратов поля
def coordinates(square_coordinates, row_coords, fieldX, fieldY, squareW):
    fX = fieldX
    fY = fieldY
    for y in range(8):
        for x in range(8):
            coords = (fX, fY)
            row_coords.append(coords)
            fX += squareW[0]
        fX = fieldX
        square_coordinates.append(row_coords)
        fY += squareW[1]
        row_coords = []
square_coordinates = []
row_coords = []
coordinates(square_coordinates, row_coords, fieldX, fieldY, squareW)
print(square_coordinates[6][2])
def field(x, y):
    gameDisplay.blit(fieldImg, (x, y))

square_states = []
def states(states):
    row = []
    for y in range(8):
        for x in range(8):
            row.append('None')
        square_states.append(row)
        row = []

states(square_states)
for rx in square_states:
    print(rx)



#-------------------------------------------------------

#Фигуры
bp1 = Pawn(100, 100, "black_pawn.png", squareW, "b_pawn")
bp2 = Pawn(150, 100, "black_pawn.png", squareW, "b_pawn")
bp3 = Pawn(200, 100, "black_pawn.png", squareW, "b_pawn")
bp4 = Pawn(250, 100, "black_pawn.png", squareW, "b_pawn")
bp5 = Pawn(300, 100, "black_pawn.png", squareW, "b_pawn")
bp6 = Pawn(350, 100, "black_pawn.png", squareW, "b_pawn")
bp7 = Pawn(400, 100, "black_pawn.png", squareW, "b_pawn")
bp8 = Pawn(450, 100, "black_pawn.png", squareW, "b_pawn")
b_pawns = [bp1, bp2, bp3, bp4, bp5, bp6, bp7, bp8]



done = False
dragging = False

while not done:
    # Обработчик событий
    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]
    for e in pygame.event.get():
# - - - - - - -  Выход - - - - - - -
        if e.type == pygame.QUIT:
            done = True
# - - - - -  Отслеживание инпута мыши - - - - -
        elif e.type == pygame.MOUSEBUTTONDOWN:
            print(mouse_x, mouse_y)
            print(pressed_square(mouse_x, mouse_y, square_coordinates, squareW[0], fieldX, fieldY))

            if e.button == 1:
                for obj in b_pawns:
                    if collision(mouse_x, mouse_y, obj.x, obj.y, squareW[0]):
                        dragging = True
                        obj.x = mouse_x - squareW[0] // 2
                        obj.y = mouse_y - squareW[0] // 2
                        offset_x = obj.x - mouse_x
                        offset_y = obj.y - mouse_y
                        index_set = pressed_square(mouse_x, mouse_y, square_coordinates, squareW[0], fieldX, fieldY)
                        square_states[index_set[0]][index_set[1]] = "None"
                        dragging_object = obj
        elif e.type == pygame.MOUSEBUTTONUP:
            if e.button == 1:
                dragging = False
            # Привязка фигур к квадратам
            for obj in b_pawns:
                row_n = 0 # Вспомогательный кал для другого массива статуса квадратов, лучше ничего не придумал
                x_n = 0
                for row in square_coordinates:
                    for x in row:
                        if collision(obj.x+squareW[0]//2, obj.y+squareW[0]//2, x[0], x[1], squareW[0]):
                             obj.x = x[0]
                             obj.y = x[1]
                             square_states[row_n][x_n] = obj.name
                        x_n += 1
                    x_n = 0
                    row_n += 1
                row_n = 0
            for rx in square_states:
                print(rx)
        elif e.type == pygame.MOUSEMOTION:
            for obj in b_pawns:
                if dragging:
                    Dragging(dragging_object, mouse_x, mouse_y, offset_x, offset_y)















    # Цвет и отрисовка
    gameDisplay.fill(fancyBlue)
    field(fieldX, fieldY)
    for obj in b_pawns:
        obj.render()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()