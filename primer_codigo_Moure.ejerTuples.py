
# Ejercicio 1: Crear una tupla y mostrarla
tupla1 = (10, 20, 30, 40, 50)
print("Ejercicio 1:", tupla1)

# Ejercicio 2: Acceder al segundo elemento de una tupla
tupla2 = (100, 200, 300, 400, 500)
print("Ejercicio 2:", tupla2[1])

# Ejercicio 3: Intentar modificar un elemento de una tupla
tupla3 = (1, 2, 3)
try:
    tupla3[0] = 10
except TypeError as e:
    print("Ejercicio 3: Error al modificar una tupla -", e)

# Ejercicio 4: Contar cuántas veces aparece un elemento en una tupla
tupla4 = (1, 2, 3, 3, 4, 5, 3)
print("Ejercicio 4: El número 3 aparece", tupla4.count(3), "veces.")

# Ejercicio 5: Encontrar el índice de la primera aparición de un elemento en una tupla
tupla5 = ("Java", "Python", "JavaScript", "Python")
print("Ejercicio 5: El índice de 'Python' es", tupla5.index("Python"))

# Ejercicio 6: Concatenar dos tuplas
tupla6a = (1, 2, 3)
tupla6b = (4, 5, 6)
tupla_concatenada = tupla6a + tupla6b
print("Ejercicio 6:", tupla_concatenada)

# Ejercicio 7: Crear una subtupla usando slicing
tupla7 = (10, 20, 30, 40, 50)
subtupla = tupla7[2:4]
print("Ejercicio 7:", subtupla)

# Ejercicio 8: Convertir una tupla en lista, modificarla y volver a tupla
tupla8 = ("rojo", "verde", "azul")
lista8 = list(tupla8)
lista8[1] = "amarillo"
tupla_modificada = tuple(lista8)
print("Ejercicio 8:", tupla_modificada)

# Ejercicio 9: Eliminar una tupla con del
my_tuple = (1, 2, 3)
del my_tuple
try:
    print("Ejercicio 9:", my_tuple)
except NameError as e:
    print("Ejercicio 9: Error -", e)

# Ejercicio 10: Crear una tupla con un solo elemento
tupla10 = (100,)
print("Ejercicio 10:", tupla10)