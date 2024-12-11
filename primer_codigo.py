# Ejemplo de diferentes tipos de datos en Python

# 1. Tipos de datos
# - Entero
numero_entero = 10
print("Número entero:", numero_entero)

# - Flotante
numero_decimal = 3.14
print("Número decimal:", numero_decimal)

# - Cadena de texto (string)
texto = "Hola, soy una cadena"
print("Cadena de texto:", texto)

# - Booleano
es_verdad = True
es_falso = False
print("Es verdad:", es_verdad)
print("Es falso:", es_falso)

# 2. Operaciones matemáticas
suma = numero_entero + numero_decimal
print("La suma de", numero_entero, "y", numero_decimal, "es:", suma)

# 3. Solicitar un número al usuario y verificar si es positivo, negativo o cero
numero_usuario = float(input("\nIntroduce un número: "))
if numero_usuario > 0:
    print("El número es positivo")
elif numero_usuario < 0:
    print("El número es negativo")
else:
    print("El número es cero")

# 4. Verificar si un número es par o impar
if int(numero_usuario) % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

# 5. Comparar dos números
num1 = float(input("\nIntroduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if num1 > num2:
    print(num1, "es mayor que", num2)
elif num1 < num2:
    print(num1, "es menor que", num2)
else:
    print("Ambos números son iguales")
