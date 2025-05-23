## TRABAJO PRÁCTICO RECURSIVIDAD ##

## EJERCICIO 1 ##
# Crea una función recursiva que calcule el factorial de un número. 
# Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de
# todos los números enteros entre 1 y el número que indique el usuario. 

# Definir función recursiva para calcular el factorial de un número. 
def calcular_factorial(num):
    if num == 0:   # caso base: el factorial de 0 es 1 por definición. 
        return 1
    else:
        return num * calcular_factorial (num-1)  # llamada recursiva (num * factorial del número anterior)

# Solicitar al usuario que ingrese un número entero. 
num_usuario= int(input("Ingrese un número entero, por favor: "))

# Usar bucle for para calcular y mostrar el factorial de cada número.
for i in range(1, num_usuario + 1): # Recorre desde 1 hasta el número ingresado por el usuario. 
    print(f"{i}! = {calcular_factorial(i)}")
# Imprime el número actual y su factorial utilizando f-strings


## EJERCICIO 2 ##
# Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

# Crea una función recursiva que calcule la serie de fibonacci hasta una posición dada. 
def serie_fibonacci(posicion):
    if posicion == 0:        # si la posición es 0 devolverá 0
        return 0 
    elif posicion == 1:      # si la posición es 1 devolverá 1
        return 1
    else:                    # de lo contrario, suma los 2 numeros anteriores
        return serie_fibonacci(posicion-1)+serie_fibonacci(posicion-2)

# Solicitar al usuario que ingrese una posición. 
posicion_usuario = int(input("Ingrese una posición, por favor: "))

# Usar bucle for para mostrar la serie desde la posición 0 hasta la ingresada 
for i in range(0, posicion_usuario + 1):  # Recorre desde 0 hasta la posición ingresada por el usuario. 
    print(f"{i} = {serie_fibonacci(i)}")  # Muestra el valor en cada posición


## EJERCICIO 3 ##
# Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, 
# utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). 
# Prueba esta función en un algoritmo general.

# Crea una función recursiva que calcule la potencia de un número base elevado a un exponente. 
def potencia_num(n, m):
    if m == 0:           # todo número elevado a la 0 da como resultado 1
        return 1
    else:
        return n * potencia_num(n, m-1)

# Solicitar al usuario que ingrese un valor de base y un valor de exponente. 
n = int(input("Ingrese el número de base (n): "))
m = int(input("Ingrese un número exponente (m): "))  # cantidad de veces que la base se multiplicará por si misma. 

# Mostrar el resultado de aplicar la función
print(f"{n} elevado a la {m} da como resultado: {potencia_num(n, m)}")


## EJERCICIO 4 ##
# Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.
# Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y unos (1), en base 2. 
# Para convertir un número decimal a binario, se puede seguir este procedimiento:
# 1. Dividir el número por 2.
# 2. Guardar el resto (0 o 1).
# 3. Repetir el proceso con el cociente hasta que llegue a 0.
# 4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.

#Ejemplo:
#Convertir el número 10 a binario:
#10 ÷ 2 = 5 resto: 0
#5 ÷ 2 = 2 resto: 1
#2 ÷ 2 = 1 resto: 0
#1 ÷ 2 = 0 resto: 1
#Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010".

# Crear una función recursiva que convierta un número decimal a binario (como cadena de texto)
def convertidor_decimal_binario(num):
    if num == 0:          # si el valor es 0 devolverá 0
        return "0"        
    elif num == 1:        # si el valor es 0 devolverá 1
        return "1"
    else:
        # Aplicar recursión: dividir entre 2 y concatenar el resto
        return convertidor_decimal_binario(num // 2) + str(num % 2)

# Solicitar al usuario un número entero positivo
numero_decimal = int(input("Ingrese un valor entero positivo, por favor: "))

# Validación simple
if numero_decimal < 0:
    print("Por favor, ingrese un número positivo.")
else:
# Llamar a la función y mostrar el resultado
    binario = convertidor_decimal_binario(numero_decimal)
    print(f"El número {numero_decimal} en binario es: {binario}")


## EJERCICIO 5 ##
# Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, 
# y devuelva True si es un palíndromo o False si no lo es.
# Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().

# Crear una función recursiva que devuelva "True" si la palabra es palindromo, o "False" si no es una palabra palindromo. 
def es_palindromo(palabra):
    if len(palabra) <= 1:  # si queda una letra o ninguna, es palíndromo
        return True
    elif palabra[0] != palabra[-1]:  # si los extremos no coinciden, NO es palíndromo
        return False
    else:
        return es_palindromo(palabra[1:-1])  # llamada recursiva con la palabra sin los extremos
 
# Mostrar el resultado de aplicar la función
print(es_palindromo("anana"))   # palabra elegida que es palindromo
print(es_palindromo("python"))  # palabra elegida que no es palindromo


## EJERCICIO 6 ##
# Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)

# Crear una función recursiva que sume los dígitos de un nùmero entero. 
def suma_digitos(num):
    if num <10:       # Caso base: si el número tiene un solo dígito, se devuelve ese mismo dígito. 
        return num
    else:
        return num % 10 + suma_digitos(num // 10) # Suma el último dígito y llama recursivamente con el resto del número //  num % 10: da el último digito del nùmero // (num // 10): elimina el último dígito. 
    
# Mostrar el resultado de aplicar la función.
print(suma_digitos(305))
print(suma_digitos(9))
print(suma_digitos(1234))


## EJERCICIO 7 ##
# Un niño está construyendo una pirámide con bloques. 
# En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.
# Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)


# Crear una función recursiva que calcule el total de bloques necesarios para construir una pirámide. 
def contar_bloques(n):
    if n == 1:
        return 1           # caso base: si el nº de bloques es 1 devolverá 1. (1 nivel = 1 bloque)
    else:  
        return n + contar_bloques(n-1)  # suma los bloques del nivel actual y llama recursivamente al nivel superior

# Mostrar el resultado de aplicar la función. 
print (contar_bloques(1))
print (contar_bloques(2))
print (contar_bloques(4))


## EJERCICIO 8 ##
# Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y 
# un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.
# Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4
# contar_digito(123456, 7) → 0

# Crear una función recursiva que permita contar la cantidad de veces que aparece x digito en un nùmero
def contar_digito(numero, digito):
    if numero == 0:        # caso base: 0 significa que ya no hay más digitos. 
        return 0
    else:
        ultimo_digito = numero % 10  # obtener el ultimo digito
        resto_digito = numero // 10  # elimina el ultimo digito
        if ultimo_digito == digito:
            return 1 + contar_digito(resto_digito, digito) # si coincide el dígito del nº con el dígito elegido, contamos 1. 
        else: 
            return contar_digito(resto_digito, digito) # si no coincide el dígito del nº con el dígito elegido, seguimos sin sumar

# Mostrar el resultado de aplicar la función.
print (contar_digito(12233421, 2))
print (contar_digito(5555, 5))
print (contar_digito(123456, 7))
print (contar_digito(34566896, 6))
