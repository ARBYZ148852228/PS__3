# Перенести код из 1_2 tank часть 2
from hitbox import Hitbox

class Tank:
    __count = 0
    __SIZE = 100
    def __init__(self, canvas, x, y,model = 'Т-14 Армата', ammo = 100, speed = 10):
        self.__hitbox = Hitbox(x, y, Tank.__SIZE, Tank.__SIZE)   # 1. добавить атрибут hitbox
        self.__canvas = canvas
        Tank.__count += 1
        self.__model = model
        self.__hp = 100
        self.__xp = 0
        self.__ammo = ammo
        self.__fuel = 100
        self.__speed = speed
        self.__x = x
        self.__y = y
        if self.__x < 0:
            self.__x = 0
        if self.__y < 0:
            self.__y = 0

        self.__create()

    @staticmethod
    def get_quantity():
        return Tank.__count

    @staticmethod
    def get_size():
        return Tank.__SIZE

#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
    def get_ammo(self):
        return self.__ammo

    def get_model(self):
        return self.__model

    def get_hp(self):
        return self.__hp

    def get_xp(self):
        return self.__xp

    def get_fuel(self):
        return self.__fuel

    def get_speed(self):
        return self.__speed

    def fire(self):
        if self.__ammo > 0:
            self.__ammo -= 1
            print('стреляю')

    def forvard(self):
        if self.__fuel > 0:
            self.__y += -self.__speed
            self.__update_hitbox()  # 2.1 вызвать метод движения HB при смене позиции
            self.__fuel -= 1
            self.__repaint()
            print(self)

    def backward(self):
        if self.__fuel > 0:
            self.__y += self.__speed
            self.__update_hitbox()   # 2.1 вызвать метод движения HB при смене позиции
            self.__fuel -= 1
            self.__repaint()
            print(self)

    def left(self):
        if self.__fuel > 0:
            self.__x += -self.__speed
            self.__update_hitbox()  # 2.1 вызвать метод движения HB при смене позиции
            self.__fuel -= 1
            self.__repaint()
            print(self)

    def right(self):
        if self.__fuel > 0:
            self.__x += self.__speed
            self.__update_hitbox()  # 2.1 вызвать метод движения HB при смене позиции
            self.__fuel -= 1
            self.__repaint()
            print(self)

    def __create(self):
        self.id = self.__canvas.create_rectangle(self.__x, self.__y, self.__x + Tank.__SIZE,
                                                 self.__y + Tank.__SIZE, fill='red')

    def __repaint(self):
        self.__canvas.moveto(self.id, x = self.__x, y = self.__y)



    #  2 метод движения хитбокса
    def __update_hitbox(self):
        self.__hitbox.moveto(self.__x, self.__y)

#    3   метод проверки столкновения - обертка
    def inersects(self, other_tank):
        return self.__hitbox.intersects(other_tank.__hitbox)

    def __str__(self):
        return (f'координаты: x = {self.__x}, y = {self.__y}, модель: {self.__model}, '
                f'здоровье: {self.__hp}, опыт: {self.__xp}, боеприпасы: {self.__ammo}')

