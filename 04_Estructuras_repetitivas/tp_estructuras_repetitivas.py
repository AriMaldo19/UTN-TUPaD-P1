### TRABAJO PRÁCTICO Nº4 ###
# ESTRUCTURAS REPETITIVAS #

"""
1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 
"""

for num in range(101):  # Usar el bucle for para iterar desde 0 hasta 100 inclusive. 
    print(num)  # Mostrar en pantalla el resultado obtenido.

"""
2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad
de dígitos que contiene.
"""

num = 0  # Inicializar variables. 
cant_digitos = 0

num = int(input("Ingrese un númerto entero: ")) # Solicitar al usuario que escriba un número entero. 
cant_digitos = len(str(num)) # Calcular la cantidad de digitos ingresados.
print("El número ingresado contiene: ", cant_digitos, "dígitos") # Mostrar en pantalla el resultado obtenido.

"""
3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados 
por el usuario, excluyendo esos dos valores. 
"""

suma_total = 0  # Inicializar variable.
 
num1 = int(input("Ingrese un número entero: ")) # Solicitar al usuario que ingrese 2 números enteros.
num2 = int(input("Ingresa otro número entero: "))

menor = min(num1, num2) # Identificar el número más chico, y el número más grande. 
mayor = max(num1, num2)

for numero in range(menor +1, mayor): # Usar bucle for para iterar desde menor + 1 hasta mayor - 1 (excluyendo el valor de mayor).
    suma_total += numero  # Sumar el número a la suma total.  
print("La suma entre los números enteros ingresados da como resultado: ", suma_total) # Mostrar en pantalla el resultado obtenido.

"""
4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. 
El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0. 
"""

suma_total = 0  # Inicializar variable. 

while True:  # Inicializar un bucle infinito, el cual se detendrá al colocar 0. 
    num = int(input("Ingresa un número: "))  # Solicitar al usuario que ingrese un número entero. 
    if num == 0:   # Verificar si el número ingresado es 0, si es 0 frenar el programa
        break    
    suma_total += num  # Sumar el número ingresado a la suma total. 
print("El total acumulado es de:", suma_total) # Mostrar en pantalla el resultado obtenido.

"""
5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. 
Al final el programa debe mostrar cuantos intentos fueron necesarios para acertar el número. 
"""

import random  # Importar la libreria "random" para generar números aleatorios. 

num_aleatorio = random.randint(0,9)  # Generar un número aleatorio entre 0 y 9. 
intentos = 0 # Inicializar variable.

num_a_adivinar = int(input("Ingresa un número entre 0 y 9: ")) # Solicitar al usuario que ingrese un número. 

while num_a_adivinar != num_aleatorio: # Usar bucle while para seguir pidiendo un número hasta adivinar. 
    intentos += 1 # Incrementar el contador de intentos. 
    num_a_adivinar = int(input("Ingresa un número entre 0 y 9: ")) # En caso que el usuario no haya adivinado el número, requerir otro número.
intentos += 1  # Incrementar el intento final para contar el último intento correcto.
print(f"Felicidades! adivinaste el número en el intento {intentos}")  # Mostrar en pantalla el resultado obtenido. 

"""
6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
entre 0 y 100, en orden decreciente. 
"""

for num_par in range (100, -1, -2): # Usar el bucle for para iterar los números pares de 100 a 0.
    print(num_par, "Este es un número par") # Imprimir en pantalla el resultado obtenido. 

"""
7) Crear un programa que calcule la suma de todos los números comprendidos entre 
0 y un número entero positivo indicado por el usuario. 
"""

num_usuario = int(input("Ingresar un número entero positivo: ")) # Solicitar al usuario que ingrese un número entero positivo. 
if num_usuario < 0:  # Verificar si el número es positivo. 
    print("El número ingresado debe ser positivo.")
else:
    suma = 0 # Inicializo la variable para la suma. 

for i in range(num_usuario + 1):  # Usar bucle for para sumar desde el 0 al número ingresado por el usuario. 
    suma += i      #Sumar cada número en el rango. 
print(f"La suma de los números comprendidos entre 0 y {num_usuario} es de: {suma}") # Mostrar en pantalla el resultado obtenido. 

"""
8) Escribe un programa que permita al usuario ingresar 100 números enteros. 
Luego el programa debe indicar cuántos de estos números son pares, cuántos son impares, 
cuántos son negativos y cuántos son positivos. 
Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para 
procesar 100 números con un solo cambio. 
"""

par = 0     # Inicializar cada una de las variables requeridas.
impar = 0
positivo = 0
negativo = 0

cantidad_num = 100  # Definir la cantidad de intentos que puede realizar el usuario.

for i in range(cantidad_num): # Solicitar 100 números enteros al usuario. 
    num = int(input("Ingresa un número entero: "))
    

    if num % 2 == 0: # Contar si el número es par o impar.
        par += 1
    else:
        impar += 1
    
    if num > 0:  # Contar si el número es positivo o negativo.
        positivo += 1
    elif num < 0:
        negativo += 1

print(f"En total hay {par} números pares") # Mostrar en pantalla los resultados obtenidos. 
print(f"En total hay {impar} números impares")
print(f"En total hay {positivo} números positivos")
print(f"En total hay {negativo} números negativos")

"""
9) Elabora un programa que permita al usuario ingresar 100 números enteros y 
luego calcule la media de esos valores.
Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números
cambiando solo un valor. 
"""

suma = 0  # Inicializar variable. 
cantidad_num = 100  # Definir la cantidad de intentos que puede realizar el usuario.

for i in range(cantidad_num):  # Usar el bucle for para iterar la cantidad de veces indicada.
    num = int(input("Ingresa un número entero: ")) # Solicitar 100 números enteros al usuario.
    suma += num   # sumar cada número a la variable suma. 
promedio = suma/cantidad_num  # Obtener el promedio.
print(f"El promedio obtenido es de: {promedio}") # Mostrar en pantalla el resultado obtenido. 

"""
10) Escribir un programa que invierta el orden de los digitos de un número ingresado 
por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 
"""

numInvertido = 0   # Definir variable.

num = int(input("Ingresar un número entero: "))  # Solicitar al usuario que ingrese un número entero.

while num > 0:  # Usar bucle while para extraer y procesar cada dígito del número original.
    digito = num % 10 # Obtener el último dígito del número usando el operador "módulo".
    numInvertido = numInvertido * 10 + digito  # Construir el número invertido añadiendo el dígito extraído.
    num = num // 10   # Eliminar el último dígito del número usando división entera.
print("El número invertido es:", numInvertido) # Mostrar en pantalla el resultado obtenido. 

    