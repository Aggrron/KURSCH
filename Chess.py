import pygame

class Figure:
    def __init__(self, coords, filename, squareW, name):
        self.x = coords[0]
        self.y = coords[1]
        self.bitmap = pygame.image.load(filename)
        #squareWX = int(squareW[0]*0.9)
        #squareWY = int(squareW[1]*0.9)
        self.bitmap = pygame.transform.scale(self.bitmap, squareW)
        self.name = name

    def render(self):
        gameDisplay.blit(self.bitmap, (self.x, self.y))

    def return_to_native(self, native_square_index, squares_coords):
        index_x = native_square_index[0]
        index_y = native_square_index[1]
        self.x = squares_coords[index_x][index_y][0]
        self.y = squares_coords[index_x][index_y][1]

    def dragging(self, mouse_x, mouse_y, offset_x, offset_y, fieldX, fieldY, fieldSize):
        self.x = mouse_x + offset_x
        self.y = mouse_y + offset_y
        if mouse_x < fieldX or mouse_x > fieldX + fieldSize[0] or mouse_y < fieldY or mouse_y > fieldY + fieldSize[0]:
            return False

    def is_my_turn(self, turn):
        if self.name[0] == turn:
            return True
        else:
            print("Not my turn!!")
            return False


class PawnB(Figure):
    def correct_move(self, native_square_index, attacked_square_index):
        if attacked_square_index[0] - native_square_index[0] == 1 and attacked_square_index[1] == native_square_index[1] and not square_is_busy(square_states, attacked_square_index):
            return True
        elif native_square_index[0] == 1 and attacked_square_index[1] == native_square_index[1] and attacked_square_index[0]-native_square_index[0]==2 and not square_is_busy(square_states, attacked_square_index):
            return True
        elif attacked_square_index[0] - native_square_index[0] == 1 and attacked_square_index[1] - native_square_index[1] == 1 and square_states[attacked_square_index[0]][attacked_square_index[1]][0] == 'w':
            return True
        elif attacked_square_index[0] - native_square_index[0] == 1 and native_square_index[1] - attacked_square_index[1] == 1 and square_states[attacked_square_index[0]][attacked_square_index[1]][0] == 'w':
            return True
        else:
            return False


class PawnW(Figure):
    def correct_move(self, native_square_index, attacked_square_index):
        if native_square_index[0] - attacked_square_index[0] == 1 and attacked_square_index[1] == native_square_index[1] and not square_is_busy(square_states, attacked_square_index):
            return True
        elif native_square_index[0] == 6 and attacked_square_index[1] == native_square_index[1] and native_square_index[0] - attacked_square_index[0] == 2 and not square_is_busy(square_states, attacked_square_index):
            return True
        elif native_square_index[0] - attacked_square_index[0] == 1 and native_square_index[1] - attacked_square_index[1] == 1 and square_states[attacked_square_index[0]][attacked_square_index[1]][0] == 'b':
            return True
        elif native_square_index[0] - attacked_square_index[0] == 1 and attacked_square_index[1] - native_square_index[1] == 1 and square_states[attacked_square_index[0]][attacked_square_index[1]][0] == 'b':
            return True
        else:
            return False


class RookW(Figure):
    def correct_move(self, native_square_index, attacked_square_index):
        nsi = native_square_index
        asi = attacked_square_index
        if native_square_index == attacked_square_index or square_states[asi[0]][asi[1]][0]== 'w':
            return False
        if native_square_index[0] == attacked_square_index[0] and not sm_is_on_th_way_rook(nsi, asi, square_states):
            return True
        elif native_square_index[1] == attacked_square_index[1] and not sm_is_on_th_way_rook(nsi, asi, square_states):
            return True
        else:
            return False


class RookB(Figure):
    def correct_move(self, native_square_index, attacked_square_index):
        nsi = native_square_index
        asi = attacked_square_index
        if nsi == asi or square_states[asi[0]][asi[1]][0] == 'b':
            return False
        if nsi[0] == asi[0] and not sm_is_on_th_way_rook(nsi, asi, square_states):
            return True
        elif nsi[1] == asi[1] and not sm_is_on_th_way_rook(nsi, asi, square_states):
            return True
        else:
            return False


class BishopW(Figure):
    def correct_move(self, nsi, asi):
        return True


class BishopB(Figure):
    def correct_move(self, nsi, asi):
        return True




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
        result = (-1, -1)
        return result

def sm_is_on_th_way_rook(nsi, asi, states):
    y_st = nsi[0]
    x_st = nsi[1]
    y_en = asi[0]
    x_en = asi[1]
    da_way_is_blocked = False
    if nsi[0] == asi[0]:
        if x_st+1 < x_en:
            for i in range(x_st+1, x_en):
                if states[y_st][i] != 'None':
                    da_way_is_blocked = True
        if x_st-1 > x_en:
            for i in range(x_en+1, x_st):
                if states[y_st][i] != 'None':
                    da_way_is_blocked = True
    if nsi[1] == asi[1]:
        if y_st-1 > y_en:
            for i in range(y_en+1, y_st):
                if states[i][x_st] != 'None':
                    da_way_is_blocked = True
        if y_st+1 < y_en:
            for i in range(y_st+1, y_en):
                if states[i][x_st] != 'None':
                    da_way_is_blocked = True
    return da_way_is_blocked



def display_turn(turn, color):
    if turn[0] == 'w':
        textsurface = myfont.render('White turn', False, color)
        gameDisplay.blit(textsurface, (0, 0))
    if turn[0] == 'b':
        textsurface = myfont.render('Black turn', False, color)
        gameDisplay.blit(textsurface, (0,0))


def print_text(text, coords, color):
    textsurface = myfont.render(text, False, color)
    gameDisplay.blit(textsurface, coords)

def change_turn(obj):
    if obj.name[0] == 'w':
        return True
    elif obj.name[0] == 'b':
        return False

def off_screen(mouse_x, mouse_y, fieldX, fieldY, fieldSize):
    if mouse_x < fieldX or mouse_x > fieldX + fieldSize or mouse_y < fieldY or mouse_y > fieldY + fieldSize:
        return True
    else:
        return False

# def attacked(figures, nsi, asi, square_coords, states):
#     attacked_x = square_coords[asi[0]][asi[1]][0]
#     attacked_y = square_coords[asi[0]][asi[1]][1]
#     attacker_color = states[nsi[0]][nsi[1]][0]
#     #defender_color = obj.name[0]
#     for obj in figures:
#         if obj.x == attacked_x and obj.y == attacked_y:
#             if attacker_color == 'w' and obj.name[0] == 'b':
#                 figures.remove(obj)
#             elif attacker_color == 'b' and obj.name[0] == 'w':
#                 figures.remove(obj)




def square_is_busy(square_states, index_set):
    if square_states[index_set[0]][index_set[1]] is not 'None':
        return True
    else:
        return False



pygame.init()

#Параметры экрана
display_w = 860
display_h = 640
#Цвета
black = (0, 0, 0)
grey = (100, 100, 100)
white = (255, 255, 255)
fancyBlue = (71, 71, 71)
# Текст на экране
font_size = 25

gameDisplay = pygame.display.set_mode((display_w, display_h))
pygame.display.set_caption("Chess")
clock = pygame.time.Clock()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', font_size)



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

#-------------------------------------------------------

#Фигуры
bp1 = PawnB(square_coordinates[1][0], "black_pawn.png", squareW, "b_pawn")
bp2 = PawnB(square_coordinates[1][1], "black_pawn.png", squareW, "b_pawn")
bp3 = PawnB(square_coordinates[1][2], "black_pawn.png", squareW, "b_pawn")
bp4 = PawnB(square_coordinates[1][3], "black_pawn.png", squareW, "b_pawn")
bp5 = PawnB(square_coordinates[1][4], "black_pawn.png", squareW, "b_pawn")
bp6 = PawnB(square_coordinates[1][5], "black_pawn.png", squareW, "b_pawn")
bp7 = PawnB(square_coordinates[1][6], "black_pawn.png", squareW, "b_pawn")
bp8 = PawnB(square_coordinates[1][7], "black_pawn.png", squareW, "b_pawn")

br1 = RookB(square_coordinates[0][0], "black_rook.png", squareW, "b_rook")
br2 = RookB(square_coordinates[0][7], "black_rook.png", squareW, "b_rook")

bb1 = BishopB(square_coordinates[0][2], "black_bishop.png", squareW, "b_bishop")
bb2 = BishopB(square_coordinates[0][5], "black_bishop.png", squareW, "b_bishop")

wp1 = PawnW(square_coordinates[6][0], "white_pawn.png", squareW, "w_pawn")
wp2 = PawnW(square_coordinates[6][1], "white_pawn.png", squareW, "w_pawn")
wp3 = PawnW(square_coordinates[6][2], "white_pawn.png", squareW, "w_pawn")
wp4 = PawnW(square_coordinates[6][3], "white_pawn.png", squareW, "w_pawn")
wp5 = PawnW(square_coordinates[6][4], "white_pawn.png", squareW, "w_pawn")
wp6 = PawnW(square_coordinates[6][5], "white_pawn.png", squareW, "w_pawn")
wp7 = PawnW(square_coordinates[6][6], "white_pawn.png", squareW, "w_pawn")
wp8 = PawnW(square_coordinates[6][7], "white_pawn.png", squareW, "w_pawn")

wr1 = RookW(square_coordinates[7][0], "white_rook.png", squareW, "w_rook")
wr2 = RookW(square_coordinates[7][7], "white_rook.png", squareW, "w_rook")

wb1 = BishopW(square_coordinates[7][2], "white_bishop.png", squareW, "w_bishop")
wb2 = BishopW(square_coordinates[7][5], "white_bishop.png", squareW, "w_bishop")

b_pawns = [bp1, bp2, bp3, bp4, bp5, bp6, bp7, bp8]
figures = [bp1, bp2, bp3, bp4, bp5, bp6, bp7, bp8,
           wp1, wp2, wp3, wp4, wp5, wp6, wp7, wp8,
           wr1, wr2, br1, br2,
           wb1, wb2, bb1, bb2]



done = False
dragging = False
turn = 'w'

def start_states(states, coords, figures, len):
    for obj in figures:
        row_n = 0
        x_n = 0
        for row in coords:
            for x in row:
                if collision(obj.x + len//2, obj.y + len//2, x[0], x[1], len):
                    states[row_n][x_n] = obj.name
                x_n += 1
            x_n = 0
            row_n += 1

start_states(square_states, square_coordinates, figures, squareW[0])

while not done:
    # Обработчик событий
    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]

    for e in pygame.event.get():
# - - - - - - -  Выход - - - - - - -
        if e.type == pygame.QUIT:
            done = True
# - - - - -  Отслеживание инпута мыши - - - - -
        # Нажатие конпки мыши
        elif e.type == pygame.MOUSEBUTTONDOWN:
            # if e.button == 3:
            #     index_set = pressed_square(mouse_x, mouse_y, square_coordinates, squareW[0], fieldX, fieldY)
            #     for obj in figures:
            #         if collision(mouse_x, mouse_y, obj.x, obj.y, squareW[0]):
            #             attacked(figures, obj, square_states, index_set)

            dragging_object = None
            # Передвижние фигур мышкой
            if e.button == 1:
                index_set = pressed_square(mouse_x, mouse_y, square_coordinates, squareW[0], fieldX, fieldY)
                print(index_set)
                for obj in figures:
                    if collision(mouse_x, mouse_y, obj.x, obj.y, squareW[0]) and obj.is_my_turn(turn):
                        dragging = True
                        obj.x = mouse_x - squareW[0] // 2
                        obj.y = mouse_y - squareW[0] // 2
                        offset_x = obj.x - mouse_x
                        offset_y = obj.y - mouse_y
                        #index_set = pressed_square(mouse_x, mouse_y, square_coordinates, squareW[0], fieldX, fieldY)
                        #square_states[index_set[0]][index_set[1]] = "None"
                        dragging_object = obj
        # Отжатие кнопки мыши
        elif e.type == pygame.MOUSEBUTTONUP:
            if e.button == 1:
                index_set_up = pressed_square(mouse_x, mouse_y, square_coordinates, squareW[0], fieldX, fieldY)
                dragging = False

            # Привязка фигур к квадратам
            row_n = 0  # Вспомогательный кал для другого массива статуса квадратов, лучше ничего не придумал
            x_n = 0
            for row in square_coordinates:
                for x in row:
                    if dragging_object is not None:
                        if collision(dragging_object.x + squareW[0] // 2, dragging_object.y + squareW[0] // 2, x[0], x[1], squareW[0]):
                            if dragging_object.correct_move(index_set, index_set_up):
                                for obj in figures:
                                    if obj.x == square_coordinates[index_set_up[0]][index_set_up[1]][0] and obj.y == \
                                            square_coordinates[index_set_up[0]][index_set_up[1]][1] and dragging_object.name[0] != obj.name[0]:
                                        figures.remove(obj)
                                dragging_object.x = x[0]
                                dragging_object.y = x[1]
                                square_states[row_n][x_n] = dragging_object.name
                                square_states[index_set[0]][index_set[1]] = "None"
                                if change_turn(dragging_object):
                                    turn = 'b'
                                else:
                                    turn = 'w'
                            else:
                                dragging_object.return_to_native(index_set, square_coordinates)
                    x_n += 1
                x_n = 0
                row_n += 1
            row_n = 0
            # for rx in square_states:
            #     print(rx)
        elif e.type == pygame.MOUSEMOTION:
            if dragging:
                if off_screen(mouse_x, mouse_y, fieldX, fieldY, fieldSize[0]):
                    dragging_object.return_to_native(index_set, square_coordinates)
                else:
                    dragging_object.dragging(mouse_x, mouse_y, offset_x, offset_y, fieldX, fieldY, fieldSize)





    # Цвет и отрисовка
    gameDisplay.fill(fancyBlue)
    field(fieldX, fieldY)
    display_turn(turn, white)
    for obj in figures:
        obj.render()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()