
# Ejercicio 1: Usa un bucle while para imprimir los números del 1 al 10
print("Ejercicio 1: Números del 1 al 10 usando while")
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
print("\n" + "-" * 50)

# Ejercicio 2: Usa un bucle for para recorrer la lista e imprimir cada número
print("Ejercicio 2: Recorrer la lista [10, 20, 30, 40, 50] usando for")
lista = [10, 20, 30, 40, 50]
for numero in lista:
    print(numero, end=" ")
print("\n" + "-" * 50)

# Ejercicio 3: Sumar los números del 1 al 100 usando while
print("Ejercicio 3: Sumar los números del 1 al 100 usando while")
i, suma = 1, 0
while i <= 100:
    suma += i
    i += 1
print("La suma es:", suma)
print("-" * 50)

# Ejercicio 4: Imprimir cada carácter de la cadena "Python" usando for
print("Ejercicio 4: Imprimir cada carácter de 'Python'")
cadena = "Python"
for caracter in cadena:
    print(caracter)
print("-" * 50)

# Ejercicio 5: Encontrar el primer número divisible por 7 entre 1 y 50 usando while
print("Ejercicio 5: Primer número divisible por 7 entre 1 y 50")
i = 1
while i <= 50:
    if i % 7 == 0:
        print("El primer número divisible por 7 es:", i)
        break
    i += 1
print("-" * 50)

# Ejercicio 6: Imprimir las claves de un diccionario usando for
print("Ejercicio 6: Recorrer un diccionario e imprimir las claves")
diccionario = {"name": "Brais", "age": 37, "country": "Galicia"}
for clave in diccionario.keys():
    print(clave)
print("-" * 50)

# Ejercicio 7: Imprimir los números pares entre 1 y 20 usando while
print("Ejercicio 7: Números pares entre 1 y 20 usando while")
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1
print("\n" + "-" * 50)

# Ejercicio 8: Imprimir los números del 1 al 10 en orden inverso usando for y range()
print("Ejercicio 8: Números del 10 al 1 usando for y range()")
for i in range(10, 0, -1):
    print(i, end=" ")
print("\n" + "-" * 50)

# Ejercicio 9: Contar cuántas veces aparece el número 30 en una lista
print("Ejercicio 9: Contar las veces que aparece el número 30 en la lista")
lista = [30, 10, 30, 20, 30, 40]
contador = 0
for numero in lista:
    if numero == 30:
        contador += 1
print("El número 30 aparece", contador, "veces.")
print("-" * 50)

# Ejercicio 10: Detener un bucle for al encontrar el nombre "Brais"
print("Ejercicio 10: Detener el bucle al encontrar 'Brais'")
nombres = ["Ana", "Carlos", "Brais", "Diana"]
for nombre in nombres:
    if nombre == "Brais":
        print("Nombre encontrado:", nombre)
        break
    print("Revisando:", nombre)
print("-" * 50)

print("¡Todos los ejercicios han sido completados!")
