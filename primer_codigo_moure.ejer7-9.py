#ejercicio 7: menores, mayores e iguales

numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

if numero1 > numero2:
    print(f"El numero {numero1} es mayor que el número {numero2}")
elif numero1 < numero2:
    print(f"El numero {numero1} es menor que el número {numero2}")
else:
    print("Ambos números son iguales")

#Ejercicio 8: Solicitar un Nombre y Saludar.

nombre = input("Como te llamas?")
print(f"¡Hola, {nombre}! Espero que estes pasando un día maravilloso")

# Ejercicio 9: Suma de dos números y tipo de dato
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
resultado = numero1 + numero2

print(f"La suma de {numero1} y {numero2} es {resultado}.")
print(f"El tipo de dato del resultado es {type(resultado)}.")

# Ejercicio 10: Comentarios explicativos

# Solicita al usuario que introduzca el primer número y lo convierte a tipo float
numero1 = float(input("Introduce el primer número: "))

# Solicita al usuario que introduzca el segundo número y lo convierte a tipo float
numero2 = float(input("Introduce el segundo número: "))

# Realiza la suma de los dos números ingresados
resultado = numero1 + numero2

# Imprime el resultado de la suma
print(f"La suma de {numero1} y {numero2} es {resultado}.")

# Imprime el tipo de dato del resultado utilizando la función type()
print(f"El tipo de dato del resultado es {type(resultado)}.")
