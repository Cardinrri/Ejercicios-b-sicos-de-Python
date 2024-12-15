
# Ejercicio 1: Crear un set e imprimirlo
set1 = {1, 2, 3, 4, 5}
print("Ejercicio 1:", set1)

# Ejercicio 2: Añadir un elemento al set
set2 = {1, 2, 3, 4, 5}
set2.add(6)
print("Ejercicio 2:", set2)

# Ejercicio 3: Intentar añadir un elemento duplicado
set3 = {1, 2, 3, 4, 5}
set3.add(5)  # No pasa nada porque los sets no permiten duplicados
print("Ejercicio 3:", set3)

# Ejercicio 4: Verificar si un elemento está en el set
set4 = {1, 2, 3, 4, 5}
print("Ejercicio 4: ¿Está el número 3?", 3 in set4)

# Ejercicio 5: Eliminar un elemento del set
set5 = {1, 2, 3, 4, 5}
set5.remove(4)
print("Ejercicio 5:", set5)

# Ejercicio 6: Vaciar un set y verificar su longitud
set6 = {1, 2, 3, 4, 5}
set6.clear()
print("Ejercicio 6: Set vaciado, longitud =", len(set6))

# Ejercicio 7: Convertir un set en lista y acceder al primer elemento
set7 = {"manzana", "naranja", "plátano"}
lista7 = list(set7)
print("Ejercicio 7: Primer elemento de la lista:", lista7[0])

# Ejercicio 8: Unión de dos sets
set8a = {1, 2, 3}
set8b = {4, 5, 6}
union_set = set8a.union(set8b)
print("Ejercicio 8:", union_set)

# Ejercicio 9: Diferencia entre dos sets
set9a = {1, 2, 3, 4}
set9b = {3, 4, 5, 6}
diferencia = set9a.difference(set9b)
print("Ejercicio 9:", diferencia)

# Ejercicio 10: Eliminar un set y manejar el error al intentar imprimirlo
my_set = {1, 2, 3}
del my_set
try:
    print("Ejercicio 10:", my_set)
except NameError as e:
    print("Ejercicio 10: Error -", e)
