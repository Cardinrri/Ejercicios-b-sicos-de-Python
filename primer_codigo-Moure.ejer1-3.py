

print("Hola Mundo")

#Ejercicio 2: Tu Nombre y Edad
Name= "Ricardo"
Edad= 37
print(f"Mi nombre es {Name} y tengo {Edad} años")

#Ejercicio 3: Solicitar datos al usuario
nombre=input("¿Como te llamas?")
print(f"Hola, {nombre}. Bienvenido a Python")

#ejemplos para entender mejor f-strings
numero=8
print(f"El triple de {numero} es {numero * 3}.")

nombre= "Anabella"
print(f"Tu nobre en mayúsculas es {nombre.upper()}")
print(f"Tu nombre en minúsculas es {nombre.lower()}")

#ejemplo con expresiones condicionales
edad=37
print(f"Eres {'mayor' if edad >= 18 else 'menor'} de edad.")