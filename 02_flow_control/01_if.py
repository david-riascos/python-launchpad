import os
os.system("clear")

###
# sentencias condicionales
# if, el  if, else
### 


print("\n Sentencia if")

## eres mayor de edad?
edad = int(input("¿Cuál es tu edad? "))


print("\n Sentencia if-elif-else")

if edad < 0:
    print("Edad no válida")
elif edad < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")
    

## operadores de comparación || relacionales
print("\n Operadores de comparación")
a = 5
b = 10
print("a < b:", a < b)
print("a > b:", a > b)
print("a == b:", a == b)
print("a != b:", a != b)
print("a <= b:", a <= b)
print("a >= b:", a >= b)


## operadores lógicos
print("\n Operadores lógicos")
x = True
y = False
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)
print("not y:", not y)
print("x and not y:", x and not y)
print("not x or y:", not x or y)

print("\n Ejemplo con operadores lógicos")
if edad >= 18 and edad < 65:
    print("Eres un adulto")
elif edad >= 65:
    print("Eres un adulto mayor")
else:
    print("Eres un menor de edad")
    

# Ternario
print("\n Operador ternario")
mensaje = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
print(mensaje)





    
