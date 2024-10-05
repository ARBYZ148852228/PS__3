class Tank:
    count = 0
    SIZE = 100
    def __init__(self,canvas, x, y, model, ammo = 100, speed = 10):
        Tank.count += 1
        self.model = model
        self.fuel = 500
        self.hp = 0
        self.ammo = ammo
        self.x = x
        self.y = y
        self.x = max(x, 0)
        self.y = max(y, 0)
        self.speed = speed
        self.canvas = canvas
        self.create()

    def repaint(self):
        self.canvas.moveto(self.id, x = self.x, y= self.y)

    def create(self):
        self.id = self.canvas.create_rectangle(self.x, self.y, self.x + Tank.SIZE,
                                               self.y + Tank.SIZE, fill = "red")
    def __str__(self):
        return (f'Танк1 : {self.model}, Топливо: {self.fuel}, Здоровье: {self.hp},'
              f'патроны: {self.ammo}, Координаты: ({self.x}, {self.y})')

    def fire(self):
        if self.ammo > 0:
            self.ammo -= 1
            print("fire")

    def forvard(self):
        if self.fuel > 0:
            self.y += -self.speed
            self.fuel -= 1
            self.repaint()
            print(self)


    def backward(self):
        if self.fuel > 0:
            self.y += self.speed
            self.fuel -= 1
            self.repaint()
            print(self)

    def left(self):
        if self.fuel > 0:
            self.x += -self.speed
            self.fuel -= 1
            self.repaint()
            print(self)

    def right(self):
        if self.fuel > 0:
            self.x += self.speed
            self.fuel -= 1
            self.repaint()
            print(self)



