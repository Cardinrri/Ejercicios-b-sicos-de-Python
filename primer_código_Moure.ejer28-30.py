
# Ejercicio 28: Comparación lógica con or:

# Comparación lógica con 'or'
resultado = (7 < 3) or (7 > 5)

# Imprimir el resultado
print(f"¿El número 7 es menor que 3 o mayor que 5? {resultado}")

#otros ejemplos:

print((5 > 3) or (8 > 6))  # Salida: True (ambas son verdaderas)
print((5 > 3) or (8 < 6))  # Salida: True (una es verdadera)
print((5 < 3) or (8 < 6))  # Salida: False (ambas son falsas)


# ejercicio 29:  Usar el operador lógico not

# Invertir el resultado de una comparación con 'not'
comparacion = 15 > 20
resultado = not comparacion

# Imprimir los resultados
print(f"¿Es 15 mayor que 20? {comparacion}")
print(f"Invertido con 'not': {resultado}")

# Ejercicio 30: Combinar operadores aritméticos y lógicos

compi = (5*3) + 2
resultado = (compi > 10) and (compi < 20)

print(f"El resultado de la expresión (5 * 3) + 2 es: {compi}")
print(f"¿Es mayor que 10 y menor que 20? {resultado}")