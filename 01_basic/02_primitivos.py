# Tipos de Datos Primitivos en Python

numero_entero = 1                    # int (En Python no hay distinción 'number', es int o float)
numero_flotante = 1.5                    # int (En Python no hay distinción 'number', es int o float)
texto = "Variable de Tipo Texto 1." # str
Texto = "Variable de Tipo Texto 2." # str
verdadero = True               # bool (¡Ojo! La primera letra siempre es Mayúscula)
falso = False                  # bool

# En Python no existe 'undefined'. Si quieres declarar algo sin valor, usamos None.
no_definido = None             # NoneType
nulo = None                    # NoneType (Es la ausencia de valor)

print(type(numero_entero))
print(type(numero_flotante))
numero_flotante = "numero flotante"  # tipado dinamico pasamos de un numero flotante a un str
print(type(numero_flotante))

print(texto, Texto) # Case Sensitive diferencia mayusculas de minusculas

print(type(nulo))