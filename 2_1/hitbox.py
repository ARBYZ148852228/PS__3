class HitBox:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def __str__(self):
        return(f"({self.x=}, {self.y=}, "
               f"{self.width=}, {self.height=})")

