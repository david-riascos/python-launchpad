##
# 04_variables.py
# las variables son espacios en memoria que se utilizan para almacenar datos.
# en python no es necesario declarar el tipo de variable, ya que es un
# lenguaje de tipo dinámico, lo que significa que el tipo de variable se determina
# en tiempo de ejecución. para crear una variable, simplemente asignamos un valor
# a un nombre de variable utilizando el operador de asignación (=). el nombre de la
# variable debe seguir ciertas reglas, como no comenzar con un número, no contener
# espacios y no ser una palabra reservada de python. las variables pueden contener
# diferentes tipos de datos, como números enteros, números decimales, cadenas de texto,
# listas, diccionarios, etc. para imprimir el valor de una variable, podemos utilizar
# la función print(). también podemos realizar operaciones con variables, como sumar,
# restar, multiplicar, dividir, etc.a continuación, se muestran algunos ejemplos de
# variables en python: asignación de variables
##


# asignación de variables
x = 10
y = 5.5
nombre = "Juan"
lista = [1, 2, 3, 4, 5]
diccionario = {"nombre": "Juan", "edad": 30}

# imprimir variables
print(x)  # 10
print(y)  # 5.5
print(nombre)  # Juan
print(lista)  # [1, 2, 3, 4, 5]
print(diccionario)  # {'nombre': 'Juan', 'edad': 30}

# operaciones con variables
suma = x + y
resta = x - y
multiplicacion = x * y
division = x / y
print(suma)  # 15.5
print(resta)  # 4.5
print(multiplicacion)  # 55.0
print(division)  # 1.8181818181818181

# Tipado dinámico
x = 10
print(x)  # 10
x = "Ahora soy una cadena"
print(x)  # Ahora soy una cadena

# Tipado fuerte
x = 10
y = "5"
# print(x + y)  # Esto generará un error de tipo, ya que no se pueden sumar un entero y una cadena

# Variables múltiples
a, b, c = 1, 2, 3
print(a)  # 1
print(b)  # 2
print(c)  # 3

# f-strings para imprimir variables
nombre = "Juan"
edad = 30
print(f"Mi nombre es {nombre} y tengo {edad} años.")  # Mi nombre es Juan y tengo 30 años.

# constantes
PI = 3.14159  # Por convención, las constantes se escriben en mayúsculas
print(PI)  # 3.14159

