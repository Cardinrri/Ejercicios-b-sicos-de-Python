
#Ejercicio 19: Calcular la longitud de una dirección

Adrees = "Camino carrasca numero 6"
Adrees_len = len(Adrees)
print(f"La dirección tiene {Adrees_len} carateres.")

#Ejercicio 20: Declarar y verificar el tipo de una variable forzando el tipo

# Declarar la variable forzando el tipo a entero
phone = int(123456789)
print(f"Número de teléfono inicial: {phone} (tipo: {type(phone)})")

# Cambiar el valor de la variable
phone = int(987654321)
print(f"Número de teléfono actualizado: {phone} (tipo: {type(phone)})")

    # Otro ejemplo
valor = "42"  # Es una cadena
valor_forzado = int(valor)  # Lo convertimos a entero
print(type(valor_forzado))  # Salida: <class 'int'>


