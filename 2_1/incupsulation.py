class Test:

    def __init__(self):
        self.public = "публичный"
        self._protected = "защищенный"
        self.__private = "приватный"

    def get_private(self):
        return self.__private
    def set_private(self, value):
        self.__private = value
test = Test()
print(test.public)
print(test._protected)
#print(test.__private)

print(test.get_private())
test.set_private("новое значение")
print(test.get_private())