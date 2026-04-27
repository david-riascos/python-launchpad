###
# Ejercicio 4: Métodos de listas
# metodos_de_listas.py
# En este ejercicio, exploraremos algunos métodos comunes de las listas en Python.
# A continuación, se presentan algunos ejercicios para practicar el uso de métodos de listas.
###

# Ejercicio 1: Agregar elementos a una lista
# Dada la siguiente lista:
# frutas = ["manzana", "banana", "naranja"]
# Utiliza el método append() para agregar "uva" al final de la lista.
print("\nEjercicio 1:")
frutas = ["manzana", "banana", "naranja"]
frutas.append("uva")
print(frutas)
# Ejercicio 2: Eliminar elementos de una lista
# Dada la siguiente lista:
# numeros = [1, 2, 3, 4, 5]
# Utiliza el método remove() para eliminar el número 3 de la lista.
print("\nEjercicio 2:")
numeros = [1, 2, 3, 4, 5]
numeros.remove(3)
print(numeros)
# Ejercicio 3: Ordenar una lista
# Dada la siguiente lista:
# palabras = ["banana", "manzana", "naranja"]
# Utiliza el método sort() para ordenar la lista alfabéticamente.
print("\nEjercicio 3:")
palabras = ["banana", "manzana", "naranja"]
palabras.sort()
print(palabras)
# Ejercicio 4: Contar elementos en una lista
# Dada la siguiente lista:
# letras = ["a", "b", "c", "a", "d", "a"]
# Utiliza el método count() para contar cuántas veces aparece la letra "a" en la lista.
print("\nEjercicio 4:")
letras = ["a", "b", "c", "a", "d", "a"]
contador_a = letras.count("a")
print(f"La letra 'a' aparece {contador_a} veces en la lista.")
# Ejercicio 5: Invertir una lista
# Dada la siguiente lista:
# numeros = [1, 2, 3, 4, 5]
# Utiliza el método reverse() para invertir el orden de los elementos en la lista.
print("\nEjercicio 5:")
numeros = [1, 2, 3, 4, 5]
numeros.reverse()
print(numeros)

# Ejercicio 6: Limpiar una lista
# Dada la siguiente lista:
# elementos = [1, 2, 3, 4, 5]
# Utiliza el método clear() para eliminar todos los elementos de la lista.
print("\nEjercicio 6:")
elementos = [1, 2, 3, 4, 5]
elementos.clear()
print(elementos)

# Ejercicio 7: Copiar una lista
# Dada la siguiente lista:
# original = [1, 2, 3, 4, 5]
# Utiliza el método copy() para crear una copia de la lista original.
print("\nEjercicio 7:")
original = [1, 2, 3, 4, 5]
copia = original.copy()
print("Original:", original)
print("Copia:", copia)  

###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

mi_lista = range(1, 6) # Crea una lista con los números del 1 al 5
print("\nEjercicio 1:")
mi_lista = list(mi_lista) # Convertimos el rango a una lista para poder modificarla
mi_lista.append(6) # Añade el número 6 al final usando append()
print("Después de append:", mi_lista)
mi_lista.insert(2, 10) # Inserta el número 10 en la posición 2 usando insert()
print("Después de insert:", mi_lista)
mi_lista[0] = 0 # Modifica el primer elemento de la lista para que sea 0
print("Después de modificar el primer elemento:", mi_lista)

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

lista_a , lista_b = list(range(1, 4)) , [4, 5, 6, 1, 2]

lista_a.extend(lista_b) # Extiende lista_a con lista_b usando extend()
print("Después de extend:", lista_a)

lista_a.remove(1) # Elimina la primera aparición del número 1 en lista_a usando remove()
print("Después de remove:", lista_a)
elemento_eliminado = lista_a.pop(3) # Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
print("Elemento eliminado con pop:", elemento_eliminado)
print("Después de pop:", lista_a)

lista_b.clear() # Limpia completamente lista_b usando clear()
print("Después de clear:", lista_b)

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

mi_lista = list(range(1, 11)) # Crea una lista con los números del 1 al 10
del mi_lista[2:5]
print(mi_lista)


# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

mi_lista = [5, 2, 8, 1, 9, 4, 2] # Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2]
mi_lista.sort() # Ordena la lista de forma ascendente usando sort()
print("Después de sort:", mi_lista)
contador_2 = mi_lista.count(2) # Cuenta cuántas veces aparece el número 2 en la lista usando count()
print(f"El número 2 aparece {contador_2} veces en la lista.")
esta_7 = 7 in mi_lista # Comprueba si el número 7 está en la lista usando in
print(f"¿El número 7 está en la lista? {esta_7}")

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

original = [1, 2, 3] # Crea una lista llamada original con los números [1, 2, 3]
copia_1 = original[:] # Crea una copia de la lista original llamada copia_1 usando slicing
copia_2 = original.copy() # Crea otra copia llamada copia_2 usando copy()
referencia = original # Crea una referencia a la lista original llamada referencia
referencia[0] = 10 # Modifica el primer elemento de la lista referencia a 10
print("Original:", original)
print("Copia 1:", copia_1)
print("Copia 2:", copia_2)
print("Referencia:", referencia)


# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.

cadenas = ["Manzana", "pera", "BANANA", "naranja"] # Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"]
cadenas.sort(key=str.lower) # Ordena la lista sin diferenciar entre mayúsculas y minúsculas usando el parámetro key con str.lower
print(cadenas)

