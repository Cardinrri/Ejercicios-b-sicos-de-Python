#Ejercicio 25: repetir una cadena con multiplicación

repetición = "python " * 10
print(repetición)

#Ejercicio 26: Comparar dos números

a = 12
b = 8
resultado = a > b

print(f"¿Es {a} mayor que {b}? {resultado}")

#Comparar cadenas de texto alfabéticamente
# Declarar las cadenas
cadena1 = "apple"
cadena2 = "banana"

# Comparar las cadenas alfabéticamente
mayor = cadena1 > cadena2
menor = cadena1 < cadena2

# Imprimir los resultados
print(f"¿'{cadena1}' está después de '{cadena2}' alfabéticamente? {mayor}")
print(f"¿'{cadena1}' está antes de '{cadena2}' alfabéticamente? {menor}")

# Ejercicio 27: Comparacion lógica con and:

# Comparación lógica con 'and'
resultado = (10 > 5) and (10 < 20)

# Imprimir el resultado
print(f"¿El número 10 es mayor que 5 y menor que 20? {resultado}")

print((5 > 3) and (8 > 6))  # Salida: True (ambas son verdaderas)
print((5 > 3) and (8 < 6))  # Salida: False (una es falsa)
