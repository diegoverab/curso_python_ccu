"""
Tipos de datos
Capacidad de detección de los tipos para tratarlos (entenderlos) como tal
"""

# tipos numéricos: enteros y punto flotante
entero = 15
flotante = 10.445

# tipos numéricos: complejos
x = (1 + 10.5j)
y = complex(2.5,6.8)

# conversiones
int(10.25)
float(12)
x.real
x.imag

2 + 2

# cadenas de texto
cadena = 'hola mundo'
variaslineas = "Esto es un texto bastante largo que contiene\n\
                varias líneas de texto, como si fuera C.\n\
                Observa que el espacio en blanco al principio de la línea es\
                significativo.\n"

# acceso a los caracteres
letras = "hola mundo"
letras[5]
letras[0:4] # de 0 a 3

# las cadenas de texto son inmutables
letras[4] = 'x'

# los índices de los rangos pueden ser negativos
x = "hola"
len(x)
x[:-2]
x[-2:]
x[1:3]

""" listas
Para python las listas contienen objetos independiente de sus tipos

Una lista también es un objeto, y ya tiene definido varios métodos
len, append, insert, pop, remove, ...
"""
lista = [] # lista vacía
lista2 = ['hola', 8, 10.7, 'fin']

lista.append('texto')
lista.append(10)
lista.append('mas texto')
print(lista)
lista.pop() # se utiliza para eliminar un elemento de la lista (por defecto el último elemento),
            # y devuelve el valor de dicho elemento.
print(lista)

lista.insert(1, 'uno') # index, valor
lista.remove(10) # elimina el valor
lista.append(['lenguaje','script']) # inserta una lista dentro de la lista
print(lista[0:2])
lista.sort()

tupla = (1,2,3) # la tupla es un uso menos habitual son inmutable
tupla[2]

# Arreglos bidimensional
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

matriz = []
matriz.append(a)
matriz.append(b)
matriz.append(c)
print(matriz)

matriz[2][1]

# Diccionarios (hash tables)
num = {}
num['uno'] = 1
num['dos'] = 2
num['tres'] = 3
num['cuatro'] = 4
num[10] = 'diez'
print(num['tres'])
print(num.get('tres'))
print(num[10])
len(num)

""" Estructuras de control: Asignaciones múltiples, primero se resuelven todas la expresiones de
                            derecha a izquierda, y luego se realizan las asignaciones. """
# if-else-...-else
from math import sqrt

a = int(input("ingrese numero"))
b = int(input("ingrese numero"))
c = int(input("ingrese numero"))
D = b*b - 4*a*c

if D > 0:
    print((-b + sqrt(D))/(2*a))
    print((-b - sqrt(D))/(2*a))
elif D == 0:
    print(-b/(2*a))
else:
    print("sin solución en los reales")

# for (recorrer listas)
range(5)
range(5, 10)

for i in range(10):
    print(i, i*i)

for name in ['uno', 'dos', 'tres', 'cuatro'] :
    print(name.upper())
    print(name, len(name))

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
suma = 0

for i in range(len(m)):
    for j in range(len(m[i])):
        print(i, j, m[i][j])
        suma = suma + m[i][j]

# while
a, b = 0, 1
while b < 10:       # ojo: identación
    print(b)
    a, b = b, a+b

# break
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '=', x, '*', n/x)
            break # rompe los ciclos
        else:
            print(n, 'es primo')

while 1:
    pass # detiene la ejecución hasta teclear algo

for i in range(1, 13):
    if i % 2 == 0:
        continue  # continuar con la siguiente iteración
    else:
        print(i)
else:
    print("lista recorrida") # se ejecuta cuando termina la lista el for,
                             # y en el while cuando la condición no cumple


""" Funciones """

# Procedimiento

def fib(n):
    "escribir la serie Fibonacci hasta n"
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a+b

fib(100)
fib(0)


# Función

def fib2(n):
    "Devolver una lista con los números de la serie de Fibonacci hasta n"
    resultado = []
    a, b = 0, 1
    while b < n:
        resultado.append(b)
        a, b = b, a+b
    return resultado


x = fib2(100)
print(x)

# Funciones: argumentos por omisión (funciones que pueden ser llamadas con menos argumentos)
def confirmar(indicador, intentos = 4, queja = 'sí o no'):
    while 1:
        respuesta = input(indicador)
        if respuesta in ('s', 'si', 'sí'):
            return 1
        elif respuesta in ('n', 'no'):
            intentos = intentos - 1
        if intentos < 0:
            raise(IOError, 'Usuario rechazado')
        print(queja)

confirmar('todo ok')
confirmar('desea continuar?', 2)

# Funciones: argumentos por clave
def loro(tension,estado='tieso',accion='voom',tipo='Azul noruego'):
    print("-- Este loro no podría", accion)
    print("aunque le aplicara", tension, "voltios.")
    print("-- Bello plumaje, el", tipo)
    print("-- ¡Está", estado, "!")

loro(1000)
loro(accion='VOOOOOM', tension=1000000)
loro('mil', estado='criando malvas')
loro('un millón de', 'desprovisto de vida', 'saltar')





