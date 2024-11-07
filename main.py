from classPezPayazo import PezPayaso

miPez = PezPayaso("Carpa", "naranja", "grande", "agua salada",True)
miPez.info()
miPez.nadar()

print(f"mi pez se llama {miPez.getNombre()}")
miPez.setNombre("dori")
print(f"mi pez se llama {miPez.getNombre()}")


print(f"mi pez tiene el color {miPez.getColor()}")
