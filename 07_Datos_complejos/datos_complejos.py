### TRABAJO PRÁCTICO Nº7 ###
# DATOS COMPLEJOS #

"""
1) Dado el diccionario precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
Añadir las siguientes frutas con sus respectivos precios:
"""
Naranja = 1200
Manzana = 1500
Pera = 2300 

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
precios_frutas['Naranja']= 1200
precios_frutas['Manzana']= 1500
precios_frutas['Pera']=2300 

print(precios_frutas)

# resultado: {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}

"""
2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, 
actualizar los precios de las siguientes frutas:
"""
Banana = 1330
Manzana = 1700
Melón = 2800

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

# resultado: {'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}

"""
3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, 
crear una lista que contenga únicamente las frutas sin los precios.
"""
precios_frutas = {'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}

lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

# resultado: ['Banana', 'Ananá', 'Melón', 'Uva', 'Naranja', 'Manzana', 'Pera']

"""
4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe. 
"""
# contactos = {"Maria": 351263748, "Pablo": 351263748, "Ana": 351263749, "Mariano": 351236479, "Camila": 351263748}

# Creamos un diccionario vacío, posterormente se guardaran los datos ingresados por el usuario. 
contactos = {}

# Cargamos 5 contactos: con nombre y telefono. 
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto #{i + 1}: ")
    telefono = input(f"Ingresá el número de {nombre}: ")
    contactos[nombre] = telefono

# Consultamos un contacto por nombre.
nombre_buscar = input("Ingresá el nombre del contacto que querés buscar: ")

# Verificamos si el nombre existe y mostramos el número.
if nombre_buscar in contactos:
    print(f"El número de {nombre_buscar} es {contactos[nombre_buscar]}")
else:
    print(f"No se encontró un contacto con el nombre '{nombre_buscar}'.")

# resultado: 
# Ingresá el nombre del contacto #1: Maria
# Ingresá el número de Maria: 351263748
# Ingresá el nombre del contacto #2: Pablo
# Ingresá el número de Pablo: 351263748
# Ingresá el nombre del contacto #3: Ana"
# Ingresá el número de Ana": 351263749
# Ingresá el nombre del contacto #4: Mariano
# Ingresá el número de Mariano: 351236479
# Ingresá el nombre del contacto #5: Camila
# Ingresá el número de Camila: 351263748
# Ingresá el nombre del contacto que querés buscar: Maria
# El número de Maria es 351263748

"""
5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra.
"""
# Solicitamos al usuario que coloque una frase. 
frase = input("Ingresá una frase: ")

# Separaramos la frase en palabras.
palabras = frase.split()

# Obtenemos palabras únicas usando un set.
palabras_unicas = set(palabras)

# Contamos la cantidad de veces que aparece cada palabra usando un diccionario.
frecuencias = {}

for palabra in palabras:
    if palabra in frecuencias:
        frecuencias[palabra] += 1
    else:
        frecuencias[palabra] = 1

# Mostramos resultados en pantalla. 
print("\nPalabras únicas:")
print(palabras_unicas)

print("\nFrecuencia de cada palabra:")
for palabra, cantidad in frecuencias.items():
    print(f"'{palabra}': {cantidad} veces")

# resultado:
# Palabras únicas:
# {'hola', 'mundo'}

# Frecuencia de cada palabra:
# 'hola': 2 veces
# 'mundo': 1 veces

"""
6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
Luego, mostrá el promedio de cada alumno.
"""
# Diccionario donde se guardaran los estudiantes y sus notas. 
alumno = {}

# Solicitar el ingreso de alumnos y notas. 
for i in range(3):
    nombre_alumno = input(f"Ingrese el nombre del alumno, por favor {i + 1}: ")
    notas = tuple(float(input(f"Ingresa la nota {j + 1} del estudiante {nombre_alumno}: " )) for j in range(3))
    alumno[nombre_alumno] = notas

# Calcular y mostrar el promedio de cada alumno
print("\nPromedios:")
for nombre_alumno, notas in alumno.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre_alumno}: {promedio}")

# resultado:
#Ingrese el nombre del alumno, por favor 1: mateo 
#Ingresa la nota 1 del estudiante mateo: 7
#Ingresa la nota 2 del estudiante mateo: 9
#Ingresa la nota 3 del estudiante mateo: 8
#Ingrese el nombre del alumno, por favor 2: anna
#Ingresa la nota 1 del estudiante anna: 5
#Ingresa la nota 2 del estudiante anna: 7
#Ingresa la nota 3 del estudiante anna: 8
#Ingrese el nombre del alumno, por favor 3: juan
#Ingresa la nota 1 del estudiante juan: 9
#Ingresa la nota 2 del estudiante juan: 5
#Ingresa la nota 3 del estudiante juan: 9

#Promedios:
#mateo: 8.0
#anna: 6.666666666666667
#juan: 7.666666666666667

"""
7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 
"""

# Sets de estudiantes que aprobaron cada parcial
primer_parcial = {"Maria", "Bruno", "Manuela", "Juanita", "Federico"}
segundo_parcial = {"Federico", "Daiana", "Luz", "Marcelo"}

# Estudiantes que aprobaron ambos parciales (intersección)
ambos_parciales_aprobados = primer_parcial & segundo_parcial

# Estudiantes que aprobaron solo uno de los dos (diferencia simétrica)
solo_uno = primer_parcial ^ segundo_parcial

# Estudiantes que aprobaron al menos un parcial (unión)
al_menos_uno = primer_parcial | segundo_parcial

# Mostrar resultados
print("Estudiantes que aprobaron ambos parciales:", ambos_parciales_aprobados)
print("Estudiantes que aprobaron solo uno de los dos:", solo_uno)
print("Estudiantes que aprobaron al menos un parcial:", al_menos_uno)

# resultado:
# Estudiantes que aprobaron ambos parciales: {'Federico'}
# Estudiantes que aprobaron solo uno de los dos: {'Marcelo', 'Maria', 'Luz', 'Daiana', 'Juanita', 'Manuela', 'Bruno'}
# Estudiantes que aprobaron al menos un parcial: {'Marcelo', 'Maria', 'Federico', 'Luz', 'Juanita', 'Daiana', 'Manuela', 'Bruno'}

"""
8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe. 
"""

# Diccionario con productos y su stock inicial
stock_productos = {
    "alfajores": 12,
    "yerba mate": 7,
    "dulce de leche": 5,
    "chipá": 10
}

# Mostrar stock inicial
print("Stock inicial de productos:")
for producto, cantidad in stock_productos.items():
    print(f"- {producto.capitalize()}: {cantidad} unidades")

# Ingresar el producto a consultar o modificar
producto = input("\nIngresá el nombre del producto que querés consultar o modificar: ").lower()

if producto in stock_productos:
    print(f"\nStock actual de {producto}: {stock_productos[producto]} unidades.")
    agregar = input("¿Querés agregar unidades a este producto? (s/n): ").lower()
    if agregar == "s":
        cantidad = int(input("¿Cuántas unidades querés agregar?: "))
        stock_productos[producto] += cantidad
        print(f"Nuevo stock de {producto}: {stock_productos[producto]} unidades.")
else:
    print(f"\nEl producto '{producto}' no está en el stock.")
    agregar_nuevo = input("¿Querés agregar este nuevo producto al stock? (s/n): ").lower()
    if agregar_nuevo == "s":
        cantidad = int(input("¿Cuántas unidades tiene el nuevo producto?: "))
        stock_productos[producto] = cantidad
        print(f"Producto '{producto}' agregado con {cantidad} unidades.")

# Mostrar el stock actualizado
print("\nStock actualizado:")
for producto, cantidad in stock_productos.items():
    print(f"- {producto.capitalize()}: {cantidad} unidades")

# resultado:
# Stock inicial de productos:
#- Alfajores: 12 unidades
#- Yerba mate: 7 unidades
#- Dulce de leche: 5 unidades
#- Chipá: 10 unidades

#Ingresá el nombre del producto que querés consultar o modificar: alfajores

#Stock actual de alfajores: 12 unidades.
#¿Querés agregar unidades a este producto? (s/n): s
#¿Cuántas unidades querés agregar?: 10
#Nuevo stock de alfajores: 22 unidades.

#Stock actualizado:
#- Alfajores: 22 unidades
#- Yerba mate: 7 unidades
#- Dulce de leche: 5 unidades
#- Chipá: 10 unidades

"""
9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
Permití consultar qué actividad hay en cierto día y hora.
"""

# Crear la agenda: clave = (día, hora), valor = evento
agenda = {
    ("sabado", "10:00"): "clase de yoga",
    ("lunes", "12:00"): "Reunion con equipo de trabajo",
    ("miércoles", "09:00"): "Llamada con cliente internacional",
    ("viernes", "18:00"): "Gimnasio"
}

# Mostrar agenda inicial
print("Agenda actual:")
for clave, evento in agenda.items():
    print(f"{clave[0].capitalize()} a las {clave[1]}: {evento}")

# Consultar una actividad
dia = input("\nIngrese el día sobre el que desea consultar: ").lower()
hora = input("Ingrese la hora (formato HH:MM): ")

clave_consulta = (dia, hora)

if clave_consulta in agenda:
    print(f"\nActividad programada el {dia} a las {hora}: {agenda[clave_consulta]}")
else:
    print(f"\nNo hay actividades programadas el {dia} a las {hora}.")

# resultado:
# Agenda actual:
# Sabado a las 10:00: clase de yoga
# Lunes a las 12:00: Reunion con equipo de trabajo
# Miércoles a las 09:00: Llamada con cliente internacional
# Viernes a las 18:00: Gimnasio

# Ingrese el día sobre el que desea consultar: sabado
# Ingrese la hora (formato HH:MM): 10:00

# Actividad programada el sabado a las 10:00: clase de yoga

"""
10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores.
"""

# Diccionario original: país : capital
paises_a_capitales = {
    "Argentina": "Buenos Aires",
    "Uruguay": "Montevideo",
    "Brasil": "Brasilia",
    "Chile": "Santiago"
}

# Crear un nuevo diccionario: capital : país
capitales_a_paises = {capital: pais for pais, capital in paises_a_capitales.items()}

# Mostrar el nuevo diccionario
print("Diccionario invertido (capitales como claves):")
print(capitales_a_paises)

# resultado:
# Diccionario invertido (capitales como claves):
# {'Buenos Aires': 'Argentina', 'Montevideo': 'Uruguay', 'Brasilia': 'Brasil', 'Santiago': 'Chile'}
