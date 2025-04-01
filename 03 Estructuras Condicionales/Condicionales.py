## PRÁCTICO Nª3: ESTRUCTURAS CONDICIONALES ##

###### ACTIVIDAD ######

""" 
1. 
Escribir un programa que solicite la edad del usuario. 
Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
"""
# Solicitar al usuario su edad.
edad = int(input("Ingrese su edad, por favor: "))    # Convertimos la entrada del usuario a entero.

# Comprobar si la edad es mayor que 18.
if edad > 18:
    print("Es mayor de edad")

"""
2. 
Escribir un programa que solicite su nota al usuario. 
Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; 
en caso contrario deberá mostrar el mensaje “Desaprobado”."
"""
# Solicitar al usuario su nota.
nota = int(input("Ingrese la nota que obtuvo: "))

# Comprobar si la nota fue "Aprobado" o "Desaprobado". 
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

"""
3.
Escribir un programa que permita ingresar solo números pares. 
Si el usuario ingresa un número par, imprimir por pantalla el mensaje "Ha ingresado un número par"; 
en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". 
Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar. "
"""
# Solicitar al usuario un número par. 
numero_par = int(input("Ingrese un número par: "))

# Comprobar que haya ingresado un número par. 
if numero_par % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")

"""
4.
Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
● Niño/a: menor de 12 años. 
● Adolescente: mayor o igual que 12 años y menor que 18 años. 
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
● Adulto/a: mayor o igual que 30 años. "
"""
# Solicitar al usuario su edad. 
edad = int(input("Ingrese su edad, por favor: "))

# Comprobar a que categoría pertenece el usuario, según el rango de edad.
# Verificar si la edad es menor de 12 años
if edad < 12:
    print("Niño/a")

# Verificar si la edad está entre 12 y 17 años. 
elif 12 <= edad < 18:
    print("Adolescente")

# Verificar si la edad está entre 18 y 29 años. 
elif 18 <= edad < 30:
    print("Adulto/a joven")

# Verificar si la edad es igual o mayor a 30. 
elif edad >= 30:
    print("Adulto/a")

"""
5.
Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). 
Si el usuario ingresa una contraseña de longitud adecuada, imprimir 
en pantalla el mensaje: "Ha ingresado una contraseña correcta". 
en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 
Nota:investigue uso de la función len() para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.
"""
# Solicitar al usuario que ingrese una contraseña 
contraseña = input("Ingresa una contraseña, por favor: ")

# Verificar que la contraseña contenga entre 8 y 14 caracteres. 
if (8 <= len(contraseña) <= 14):
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

"""
6. 
Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare 
para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
                           ###### ACLARACIONES ######
● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda. 
● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda. 
● Sin sesgo: cuando la media, la mediana y la moda son iguales. 
"""
# Importar las funciones: moda(mode), mediana(median) y mean(promedio), de la libreria statistics. 
from statistics import mode, median, mean

# Importar libreria random para generan números pseudoaleatorios. 
import random

# Crear una lista con 50 números entre 1 y 100 elegidos de forma aleatoria.
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular la media, mediana y moda de una lista de números aleatorios.
mean_aleatorio = mean(numeros_aleatorios)
median_aleatorio = median(numeros_aleatorios)
mode_aleatorio = mode(numeros_aleatorios)

print("media: ",mean_aleatorio)
print("mediana: ",median_aleatorio)
print("moda: ",mode_aleatorio)

# Evaluar el sesgo de los datos comparando la media, mediana y moda.
if mean_aleatorio > median_aleatorio > mode_aleatorio:
    print("Hay Sesgo positivo")

elif mean_aleatorio == median_aleatorio == mode_aleatorio:
    print("Sin Sesgo")

elif mean_aleatorio < median_aleatorio < mode_aleatorio:
    print("Hay Sesgo negativo")

else:
    print("no se cumple ninguna de las condiciones")

"""
7.
Escribir un programa que solicite una frase o palabra al usuario. 
Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante 
por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
"""
# Solicitar al usuario que ingrese una frase. 
frase = input("Ingrese una frase o palabra, por favor: ")

# Verificar si la frase no está vacía y si la ultima letra es una vocal.
if frase and frase[-1].lower() in 'aeiou':    
    print(f"{frase}!")
else:
    print(frase)

"""
8. 
Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
● 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
● 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
● 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. 
Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.
"""
# Solicitar al usuario que ingrese un nombre, y un número a elección.  
nombre = input("Ingrese su nombre, por favor: ")
numero = int(input("Ingrese 1 si quiere su nombre en mayúsculas, 2 en minúsculas, 3 primera letra mayúscula: "))

# Modificar la cadena 'nombre' según el valor de 'numero'. 
if numero == 1:
    print(nombre.upper())
elif numero == 2:
    print(nombre.lower())
elif numero == 3:
    print(nombre.capitalize())

"""
9.
Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías "
"según la escala de Richter e imprima el resultado por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
"""
# Solicitar al usuario que ingrese una magnitud de terremoto. 
magnitud_terremoto = float(input("Ingrese la magnitud del terremoto: "))

# Clasificar la magnitud de un terremoto según la escala de Richter y mostrar su impacto potencial.
if magnitud_terremoto < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud_terremoto < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud_terremoto < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud_terremoto < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud_terremoto < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

"""
10. 
Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. 
El programa deberá usar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.
"""
# Solicitar al usuario que ingrese el hemisferio en el que se encuentra ubicado, el mes y el día actual para conocer la estación del año en la que se encuentra.
hemisferio = input("Ingrese el hemisferio en el que se encuentra, N(norte) o S(sur): ")
mes = int(input("Ingrese el mes de año en el que se encuentra actualmente: "))
dia = int(input("Ingrese el dia en el que se encuentra actualmente: "))

# Si la fecha está entre el 21 de diciembre y el 20 de marzo, en hemisferio norte: es INVIERNO.En hemisferio sur: es VERANO. 
if hemisferio == 'N' and ((mes == 12 and dia >= 21) or (mes >= 1 and mes <= 2) or (mes == 3 and dia <= 20)):
    print("Se encuentra en la estación INVIERNO")
elif hemisferio == 'S' and ((mes == 12 and dia >= 21) or (mes >= 1 and mes <= 2) or (mes == 3 and dia <= 20)):
    print("Se encuentra en la estación VERANO")
elif hemisferio == 'N' and ((mes == 3 and dia >= 21) or (mes >= 4 and mes <= 5) or (mes == 6 and dia <= 20)):
    print("Se encuentra en la estación PRIMAVERA")
elif hemisferio == 'S' and ((mes == 3 and dia >= 21) or (mes >= 4 and mes <= 5) or (mes == 6 and dia <= 20)):
    print("Se encuentra en la estación OTOÑO")
elif hemisferio == 'N' and ((mes == 6 and dia >= 21) or (mes >= 7 and mes <= 8) or (mes == 9 and dia <= 20)):
    print("Se encuentra en la estación VERANO")
elif hemisferio == 'S' and ((mes == 6 and dia >= 21) or (mes >= 7 and mes <= 8) or (mes == 9 and dia <= 20)):
    print("Se encuentra en la estación INVIERNO")
elif hemisferio == 'N' and ((mes == 9 and dia >= 21) or (mes >= 10 and mes <= 11) or (mes == 12 and dia <= 20)):
    print("Se encuentra en la estación OTOÑO")
elif hemisferio == 'S' and ((mes == 9 and dia >= 21) or (mes >= 10 and mes <= 11) or (mes == 12 and dia <= 20)):
    print("Se encuentra en la estación PRIMAVERA")"

    