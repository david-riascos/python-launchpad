"""
    Transformar los datos de un valor o tipo a otro Ej:
    Int 0 a Bool False

"""

print("Conversión de tipos")

print(type("100"))

print("pasar de str a int")
print(type(int("100")))

# Cualquier valor diferente de 0 sera True
print(bool(0))
print(bool(-1))
print(bool(2))

# Cualquier cadena diferente de vacía sera True
print(bool(""))
print(bool(" "))
print(bool("False"))