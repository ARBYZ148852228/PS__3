class Tank:
    count = 0
    def __init__(self, x, y, model, ammo):
        Tank.count += 1
        self.model = model
        self.fuel = 100
        self.hp = 0
        self.ammo = ammo
        self.x = x
        self.y = y
    def info(self):
        print(f'Танк1 : {self.model}, Топливо: {self.fuel}, Здоровье: {self.hp},'
              f'патроны: {self.ammo}, Координаты: ({self.x}, {self.y})')

    def fire(self):
        if self.ammo > 0:
            self.ammo -= 1
            print("fire")

    def forvard(self):
        if self.fuel > 0:
            self.y += -1
            self.fuel -= 1

    def backward(self):
        if self.fuel > 0:
            self.y += 1
            self.fuel -= 1

    def left(self):
        if self.fuel > 0:
            self.x += -1
            self.fuel -= 1

    def right(self):
        if self.fuel > 0:
            self.x += 1
            self.fuel -= 1


