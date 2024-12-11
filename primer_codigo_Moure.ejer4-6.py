
#Ejercicio 4: Suma de números
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
resultado = numero1 + numero2

print(f"La suma de {numero1} y {numero2} es {resultado}.")
print(f"El tipo de dato del resultado es {type(resultado)}.")

# Ejercicio 5: Verificar si un número es positivo, negativo o cero
numero = float(input("Introduce un número: "))

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El numero es cero.")

# Ejercicio 6: Verificar si un número es par o impar
numero = int(input("Introduce un número: "))

if numero % 2 == 0:
    print(f"El número {número} es par.")
else:
    print(f"El número {numero} es impar.")