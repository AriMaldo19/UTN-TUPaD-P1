### TRABAJO PRÁCTICO Nº6 ###
# FUNCIONES #

"""
1) Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje:
 “Hola Mundo!”. Llamar a esta función desde el programa principal.
"""

# Definición de función
def imprimir_hola_mundo():
    print("Hola Mundo")

# Programa principal
imprimir_hola_mundo()

"""
2) Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre
 y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
“Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.
"""

# Definición de función
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

# Programa principal
ingresar_nombre = input("Indique su nombre, por favor: ")
saludar_usuario(ingresar_nombre)

"""
3) Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) 
que reciba cuatro parámetros e imprima: “Soy[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
Pedir los datos al usuario y llamar a esta función con los valores ingresados.
"""

# Definición de función
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Programa principal
ingresar_nombre = input("Indique su nombre, por favor: ")
ingresar_apellido = input("Indique su apellido, por favor: ")
ingresar_edad = int(input("Indique su edad, por favor: "))
ingresar_residencia = input("Indique donde reside, por favor: ")
informacion_personal(ingresar_nombre, ingresar_apellido, ingresar_edad, ingresar_residencia)

"""
4) Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y 
devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro 
y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar 
los resultados.
"""

# Importar biblioteca "math" para usar math.pi
from math import pi

# Definición de funciones
def calcular_area_circulo(radio):
    area = pi * radio ** 2
    print(f"el radio es de {area}")

def calcular_perimetro_circulo(radio):
    perimetro = 2 * pi * radio
    print(f"el radio es de {perimetro}")

# Programa principal
ingresar_radio = float(input("Ingrese el radio del circulo, por favor: "))
calcular_area_circulo(ingresar_radio)
calcular_perimetro_circulo(ingresar_radio)

"""
5) Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro 
y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado 
usando esta función.
"""

# Definición de funciones
def segundos_a_horas(segundos):
    horas = segundos/3600
    return horas

# Programa principal
ingresar_segundos = int(input("Ingrese una cantidad de segundos, por favor: "))
horas_obtenidas = segundos_a_horas(ingresar_segundos)
print(f"Los segundos ingresados corresponden a {horas_obtenidas} hora/s.")

"""
6) Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función.
"""

# Definición de funciones
def tabla_multiplicar(numero):
    for i in range(1,11):
        resultado = numero * i
        print(f"{numero} * {i} = {resultado}")

# Programa principal
ingresar_num = int(input("Ingresa un número entero para ver su tabla de multiplicar, por favor: "))
tabla_multiplicar(ingresar_num)

"""
7) Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros
y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
Mostrar los resultados de forma clara.
"""

# Definición de funciones
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a/b if b != 0 else "No es posible dividir por 0, elija otro número"
    return (suma, resta, multiplicacion, division)

# Programa principal
param1 = int(input("Ingresa un número entero, por favor: "))
param2 = int(input("Ingresa otro número entero: "))

suma, resta, multiplicacion, division = operaciones_basicas(param1, param2)

# Mostrar el resultado obtenido
print(f"resultado de operaciones basicas usando {param1} y {param2}: ")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")

"""
8) Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos
 y la altura en metros, y devuelva el índice de masa corporal (IMC). 
 Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
"""

# Definición de funciones
def calcular_imc(peso, altura):
    indice_masa_corporal = peso / (altura ** 2)
    return indice_masa_corporal

# Programa principal
ingresar_peso = float(input("Ingrese su peso en kilogramos, por favor: "))
ingresar_talla = float(input("Ingrese su altura en metros, por favor: "))

resultado_imc = calcular_imc(ingresar_peso, ingresar_talla)
print(f"El IMC acorde a su peso y talla es de: {resultado_imc:.2f}")  #:.2f mostrará el resultado con 2 decimales

"""
9) Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y 
devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar elresultado usando la función.
"""

# Definición de funciones
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32    
    return fahrenheit

# Programa principal
ingresar_celsius = float(input("Ingrese la temperatura en grados Celsius, por favor: "))
fahrenheit_obtenidas = celsius_a_fahrenheit(ingresar_celsius)
print(f"La temperatura de {ingresar_celsius}°C en Celsius equivale a {fahrenheit_obtenidas:.2f}°F en Fahrenheit.")

"""
10) Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y 
devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.
"""

# Definición de funciones
def calcular_promedio(a, b, c):
    promedio = (a + b + c)/3
    return promedio

# Programa principal
num1 = int(input("Ingrese un número, por favor: "))
num2 = int(input("Ingrese otro número, por favor: "))
num3 = int(input("Ingrese un último número, por favor: "))

resultado = calcular_promedio(num1, num2, num3)

print(f"El promedio de los 3 valores ingresados es de: {resultado}")
