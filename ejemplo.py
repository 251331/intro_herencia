# Clase padre
class Pez:
    def __init__(self, nombre, color, size, habitad):
        self.__nombre = nombre
        self.__color = color
        self.__size = size
        self.__habitad = habitad

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def nadar(self):
        print(f"{self.__nombre} está nadando.")

    def info(self):
        print(f"El pez se llama {self.__nombre} y es de color {self.__color} y vive en {self.__habitad}")

# Clase hija 1
class PezPayaso(Pez):
    def __init__(self, nombre, color, size, habitad, esconderse):
        super().__init__(nombre, color, size, habitad)
        self.__esconderse = esconderse


    def info(self):
        super().info()
        print(f"Este pez se esconde? {self.__esconderse}")


# Ejemplos de objetos
#pez1 = Pez("Carpa", "naranja", "grande", "agua salada" )

# Llamadas a métodos de cada clase
#pez1.info()

miPez = PezPayaso("Carpa", "naranja", "grande", "agua salada",True)
miPez.info()
miPez.nadar()

print(f"mi pez se llama {miPez.getNombre()}")

miPez.setNombre("dori")
print(f"mi pez se llama {miPez.getNombre()}")

