
print('\n' *100)

cadena = " Hola José "

# espacios
cadenas = cadena.lstrip() # rstrip / lstrip
print(cadena)
print(cadenas)

#formatos
mayuscula = cadena.upper()
minuscula = cadena.lower()

print(mayuscula)
print(minuscula)

# split
cadena_completa = "Pedro ? Miguel ? Sofia"
cadena_split = cadena_completa.split(sep="?")

print(cadena_completa)
print(cadena_split)

#lista / sort
lista = [9, 3, 6, 2, 7, 0, 0, 4]

print(sorted(lista))
print(sorted(lista, reverse=True))

print(lista)
lista.sort()
print(lista)

lista = ['Za', 'Fg', 'Az', 'Ij']
print(sorted(lista))

lista.sort()
print(lista)

#conjuntos forma 1
conjunto = set('9976') # set crea un conjunto {'6', '7', '9'}
print(conjunto)

#conjunto forma 2
conjunto2 = {'6', '7', '8'}
print(conjunto2)

#intersección
print(conjunto)
print(conjunto2)

print(conjunto & conjunto2)
print(conjunto.intersection(conjunto2))

# modulos
import modulo
import moduloN

modulo.metodo()
moduloN.metodo()

# modulos: usando alias
import modulo as A
import modulo as B

A.metodo()
B.metodo()

# en caso de que una referencia no esta en la misma ubicación actual
import sys
print(sys.path)

# trabajar con csv
import csv

doc = open("archivoW.csv","w") # w = escritura, te permite generar un archivo
doc_csv_w = csv.writer(doc)

lista = ["Pedro", 99836]
doc_csv_w.writerow(lista) #para escribir una por fila

lista2 = [["Pedro",99836],["Uno",1000],["Dos",2000],["Tres",3000]]
doc_csv_w.writerows(lista2) #para escribir más de una fila

for x in lista2:
    doc_csv_w.writerow(x)

doc.close() # cerrar archivo

# abrir un csv
doc = open("archivoW.csv","r") #a = append, r= read, w= write (si existe, se sobreescribe o crea)
doc_csv = csv.reader(doc)

# leer los datos y pasarlos a una lista
# forma larga
data = []
for r in doc_csv:
    data.append(r)
print(data)

# forma corta
data = [r for r in doc_csv]
print(data)

# with
with open("archivoW.csv") as f:
    reader = csv.reader(f)
    data = [r for r in reader]
    f.close()

print(data)

#bbdd instalar conector https://dev.mysql.com/downloads/connector/python/
import mysql.connector
con = mysql.connector.connect(user="root", password="Emol.com5", host="localhost", database="db")
cursor = con.cursor()
cursor.execute("CREATE TABLE example (id INT, data VARCHAR(100));")
cursor.execute("INSERT INTO example (id, data) VALUES (9, 'hola');")
con.commit()

cursor.execute("SELECT * FROM example WHERE id =9;")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.execute("DELETE FROM example WHERE id =9;")
con.commit()

cursor.close()
con.close()

help()

#tipos de comentarios

# comentario tipo 1
""" comentario tipo 2
puede usarse para más de una linea"""


