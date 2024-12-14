import texture
from tkinter import NW
from random import randint, choice

_camera_x = 0
_camera_y = 0
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
WIDTH = SCREEN_WIDTH * 6
HEIGHT = SCREEN_HEIGHT * 4
GROUND = 'g'
WATER = 'w'
CONCRETE = 'c'
BRICK = 'b'
BLOCK_SIZE = 64

_Canvas = None
_map = []



def get_rows():
    return len(_map)

def get_cols():
    return len(_map[0])

def get_width():
    return get_cols() * BLOCK_SIZE

def get_height():
    return get_rows() * BLOCK_SIZE





def create_map(rows = 20, cols = 20):
    global _map
    _map = []
    for i in range(rows):
        row = []
        for j in range(cols):
            block = GROUND
            if i == 0 or j == 0 or i == rows - 1 or j == cols - 1:
                block = CONCRETE
            elif randint(1, 100) <= 15:
                block = choice([BRICK, WATER, CONCRETE])
            cell = _Cell(_Canvas, block, j * BLOCK_SIZE, i * BLOCK_SIZE)
            row.append(cell)
        _map.append(row)



def initialize(canv):
    global _Canvas, _map
    _Canvas = canv
    create_map(20, 20)

def set_camera_xy(x, y):
    global _camera_x, _camera_y
    if x < 0:
        x = 0
    if y < 0:
        y = 0

    if x > get_width() - SCREEN_WIDTH:
        x = get_width() - SCREEN_WIDTH

    if y > get_height() - SCREEN_HEIGHT:
        y = get_height() - SCREEN_HEIGHT

        _camera_x = x
        _camera_y = y

def update_map():
    for i in range(0, get_rows()):
        for j in range(0, get_cols()):
            update_cell(i, j)

def update_cell(row, col):
    if row < 0 or col < 0 or row >= get_rows() or col >= get_cols():
        return
    _map[row][col].update()













class _Cell:
    def __init__(self, canvas, block, x, y):
        self.__canvas = canvas
        self.__block = block
        self.__x = x
        self.__y = y

    def update(self):
        if self.__block == GROUND:
            return
        screen_x = get_screen_x(self.__x)
        screen_y = get_screen_y(self.__y)
        self.__canvas.moveto(self.__id, x = screen_x, y = screen_y)

        if self.__block == GROUND:
            return



    def __create_element(self, block):
        if block != GROUND:
            self.__id = self.__canvas.create_image(self.__x, self.__y,
                                                   image = texture.get(block), anchor = NW)

    def __del__(self):
        try:
            self.__canvas.delete(self.__id)
        except:
            pass

    def get_block(self):
        return self.__block






def move_camera(delta_x, delta_y):
    set_camera_xy(_camera_x + delta_x, _camera_y + delta_y)

def get_screen_x(world_X):
    return world_X - _camera_x

def get_screen_y(world_Y):
    return world_Y - _camera_y






