from classPeces import Pez

class PezPayaso(Pez):
    def __init__(self, nombre, color, size, habitad, esconderse):
        super().__init__(nombre, color, size, habitad)
        self.__esconderse = esconderse


    def info(self):
        super().info()
        print(f"Este pez se esconde? {self.__esconderse}")

    def getColor(self):
        return self.color
