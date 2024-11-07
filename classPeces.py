class Pez:
    def __init__(self, nombre, color, size, habitad):
        self.__nombre = nombre
        self.color = color
        self.__size = size
        self.__habitad = habitad

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def nadar(self):
        print(f"{self.__nombre} está nadando.")

    def info(self):
        print(f"El pez se llama {self.__nombre} y es de color {self.color} y vive en {self.__habitad}")
