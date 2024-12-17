
# Ejercicio 1: Crear un diccionario e imprimirlo
persona = {
    "name": "Juan",
    "age": 30,
    "country": "España"
}
print("Ejercicio 1 - Diccionario creado:", persona)

# Ejercicio 2: Acceder al valor de la clave 'name'
valor_name = persona["name"]
print("Ejercicio 2 - Valor de la clave 'name':", valor_name)

# Ejercicio 3: Añadir una nueva clave 'job' al diccionario
persona["job"] = "Programador"
print("Ejercicio 3 - Diccionario actualizado con 'job':", persona)

# Ejercicio 4: Modificar el valor de la clave 'age' a 38
persona["age"] = 38
print("Ejercicio 4 - Diccionario actualizado con 'age' modificada:", persona)

# Ejercicio 5: Eliminar la clave 'country' del diccionario
del persona["country"]
print("Ejercicio 5 - Diccionario después de eliminar 'country':", persona)

# Ejercicio 6: Crear un diccionario con claves 1-5 y valores como sus cuadrados
cuadrados = {x: x**2 for x in range(1, 6)}
print("Ejercicio 6 - Diccionario de cuadrados:", cuadrados)

# Ejercicio 7: Verificar si la clave 'age' existe en otro diccionario
persona_brais = {"name": "Brais", "age": 37, "country": "Galicia"}
existe_age = "age" in persona_brais
print("Ejercicio 7 - ¿La clave 'age' está presente?:", existe_age)

# Ejercicio 8: Imprimir solo las claves del diccionario
claves_persona = persona.keys()
print("Ejercicio 8 - Claves del diccionario:", claves_persona)

# Ejercicio 9: Convertir las claves del diccionario en una lista
lista_claves = list(persona.keys())
print("Ejercicio 9 - Lista de claves:", lista_claves)

# Ejercicio 10: Crear un diccionario con fromkeys() y valor "Desconocido"
claves = ["name", "age", "job"]
diccionario_desconocido = dict.fromkeys(claves, "Desconocido")
print("Ejercicio 10 - Diccionario creado con fromkeys():", diccionario_desconocido)

