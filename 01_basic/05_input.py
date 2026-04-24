###
# 05_input.py
# la función input() se utiliza para obtener datos del usuario desde la consola.
# esta función devuelve una cadena de texto, por lo que si queremos utilizar los datos
# como un número, debemos convertirlos utilizando funciones como int() o float().
# a continuación, se muestran algunos ejemplos de uso de la función input():
###

nombre = input("¿Cuál es tu nombre? ")
print(f"¡Hola, {nombre}!")

edad = int(input("¿Cuántos años tienes? "))
print(f"Tienes {edad} años.")

altura = float(input("¿Cuál es tu altura en metros? "))
print(f"Tu altura es {altura} metros.")

## multiple inputs
numeros = input("Introduce tres números separados por espacios: ")
num1, num2, num3 = map(int, numeros.split())
print(f"Los números que has introducido son: {num1}, {num2}, {num3}")