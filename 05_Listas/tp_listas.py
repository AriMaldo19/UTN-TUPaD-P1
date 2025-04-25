### TRABAJO PRÁCTICO Nº5 ###
# LISTAS #

# Actividades
# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
lista_rango_numeros = list(range(4,101,4)) # el 101 se excluye

print(lista_rango_numeros)

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. 
# ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!

lista_elementos = ["Programacion I", 9.5 , "Listas", 10 , True]
lista_nueva = lista_elementos[3]

print(lista_nueva)

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. 
# Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por ejemplo: lista_vacia = []

lista_vacia = []
lista_vacia.append("manzana")
lista_vacia.append("pera")
lista_vacia.append("naranja")

print(lista_vacia)

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. 
# Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona 
# el indexing con números negativos! animales = ["perro", "gato", "conejo", "pez"]

animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[3] = "oso"

print(animales)

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
numeros = [8, 15, 3, 22, 7] 
numeros.remove(max(numeros))
print(numeros)

# En este programa se crea en la primera linea la lista de números enteros, que incluye 5 elementos
# En la segunda linea la "sentencia remove" se usa para eliminar elementos, en este caso se requiere eliminar mediante "max" el numero mayos
# en la ultima linea se imprime el resultado de la nueva lista, en la cual se elimino el valor más alto de la lista, el número 22". 


# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.
lista_numeros = list(range(10, 31, 5))  # el 31 se excluye
print(lista_numeros)
rango_lista = lista_numeros[0:2]   # el 2 se excluye 
print(rango_lista)

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera. 
# autos = ["sedan", "polo", "suran", "gol"]

autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "amarok"
autos[2] = "torino"

print(autos)

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. 
# Imprimir la lista resultante por pantalla.

dobles = []
dobles.append(10)
dobles.append(20)
dobles.append(30)

print(dobles)

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente usando append.
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")

print(compras)

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras[1][compras[1].index("fideos")] = "tallarines"

print(compras)

# c) Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")
print(compras)

# d) Imprimir la lista resultante por pantalla
print(compras)

# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lisa_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)