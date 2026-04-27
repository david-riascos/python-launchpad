###
# Listas
# las listas son una estructura de datos que nos permite almacenar una colección de elementos.
# las listas son mutables, lo que significa que podemos modificar su contenido después de
# haberlas creado. las listas se definen utilizando corchetes [] y los elementos se
# separan por comas.
###
# Crear una lista
mi_lista = [1, 2, 3, 4, 5]
print(mi_lista)
# Acceder a los elementos de una lista
print(mi_lista[0]) # Imprime el primer elemento de la lista
print(mi_lista[1]) # Imprime el segundo elemento de la lista
print(mi_lista[-1]) # Imprime el último elemento de la lista
# Modificar un elemento de la lista
mi_lista[0] = 10
print(mi_lista)
# Agregar un elemento al final de la lista
mi_lista.append(6)
print(mi_lista)
# Insertar un elemento en una posición específica
mi_lista.insert(2, 15)
print(mi_lista)
# Eliminar un elemento de la lista
mi_lista.remove(3)
print(mi_lista)
# Eliminar un elemento por su índice
del mi_lista[0]
print(mi_lista)
# Obtener la longitud de la lista
print(len(mi_lista))
# Iterar sobre los elementos de la lista
for elemento in mi_lista:
    print(elemento)
# Crear una lista de cadenas
nombres = ["Alice", "Bob", "Charlie"]
print(nombres)
# Acceder a los elementos de la lista de cadenas
print(nombres[0]) # Imprime "Alice"
print(nombres[1]) # Imprime "Bob"
print(nombres[2]) # Imprime "Charlie"
# Modificar un elemento de la lista de cadenas
nombres[0] = "Alicia"
print(nombres)
# Agregar un elemento al final de la lista de cadenas
nombres.append("David")
print(nombres)
# Insertar un elemento en una posición específica de la lista de cadenas
nombres.insert(1, "Eve")
print(nombres)
# Eliminar un elemento de la lista de cadenas
nombres.remove("Bob")
print(nombres)
# Eliminar un elemento por su índice de la lista de cadenas
del nombres[0]
print(nombres)
# Obtener la longitud de la lista de cadenas
print(len(nombres))
# Iterar sobre los elementos de la lista de cadenas
for nombre in nombres:
    print(nombre)
# Crear una lista de listas
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz)
# Acceder a los elementos de la lista de listas
print(matriz[0]) # Imprime la primera fila de la matriz
print(matriz[1]) # Imprime la segunda fila de la matriz
print(matriz[2]) # Imprime la tercera fila de la matriz
print(matriz[0][0]) # Imprime el primer elemento de la primera fila
print(matriz[1][1]) # Imprime el segundo elemento de la segunda fila
print(matriz[2][2]) # Imprime el tercer elemento de la tercera fila
# Modificar un elemento de la lista de listas
matriz[0][0] = 10
print(matriz)
# Agregar una nueva fila a la lista de listas
matriz.append([10, 11, 12])
print(matriz)
# Eliminar una fila de la lista de listas
del matriz[0]
print(matriz)
# Obtener la longitud de la lista de listas
print(len(matriz))
# Iterar sobre los elementos de la lista de listas
for fila in matriz:
    for elemento in fila:
        print(elemento)
        

# Crear una lista de números del 1 al 10 utilizando la función range()
numeros = list(range(1, 11))
print(numeros)

# Crear una lista de cuadrados de los números del 1 al 10 utilizando una comprensión de listas
cuadrados = [x**2 for x in range(1, 11)]
print(cuadrados)

# Slice de listas
# El slicing nos permite obtener una parte de la lista utilizando índices.
# La sintaxis es: lista[inicio:fin:paso]
# Obtener los primeros 5 elementos de la lista de números
primeros_cinco = numeros[:5]
print(primeros_cinco)
# Obtener los últimos 5 elementos de la lista de números
ultimos_cinco = numeros[5:]
print(ultimos_cinco)
# Obtener los elementos de la lista de números en pasos de 2
paso_dos = numeros[::2]
print(paso_dos)
# Obtener los elementos de la lista de números en orden inverso
inverso = numeros[::-1]
print(inverso)

inverso_par = numeros[::-2]
print(inverso_par)

# Concatenar listas
# Podemos concatenar dos listas utilizando el operador +.
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_concatenada = lista1 + lista2
print(lista_concatenada)

# copiar una lista
# Para copiar una lista, podemos utilizar el método copy() o la función list().
# Copiar una lista utilizando el método copy()
copia_numeros = numeros.copy()
print(copia_numeros)
# Copiar una lista utilizando la función list()
copia_numeros_2 = list(numeros)
print(copia_numeros_2)

