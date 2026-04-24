###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

from math import pi

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
nombre = input("¿Cuál es tu nombre? ")
ciudad = input("¿En qué ciudad vives? ")
print(f"Tu nombre es {nombre} y vives en {ciudad}.")


print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

print(f"El tipo de a es: {type(a)}")
print(f"El tipo de b es: {type(b)}")
print(f"El tipo de c es: {type(c)}")
print(f"El tipo de d es: {type(d)}")
print(f"El tipo de e es: {type(e)}")

### Completa aquí

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí

string_num = "12345"
int_num = int(string_num)
float_num = float(int_num)
print(f"Cadena '{string_num}' convertida a entero: {int_num} Tipo: {type(int_num)}")
print(f"Entero {int_num} convertido a float: {float_num} Tipo: {type(float_num)}")



print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí

nombre = "David"
edad = 29
altura = 1.80
print(f"Hola! Me llamo {nombre} y tengo {edad} años, mido {altura} metros.")

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

### Completa aquí

pi_redondeado = round(pi)
division_entera = pi_redondeado // 2
print(f"El número PI redondeado es: {pi_redondeado}")
print(f"La división entera de {pi_redondeado} entre 2 es: {division_entera}")
