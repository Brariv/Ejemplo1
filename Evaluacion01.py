#---------------------------------------------------------------
# Universudad del valle guatemala
# Facultad de ingenieria
# Departamento de ciencia en la computacion
# Algoritmos y programacion Basica
# Seccion 180
#
# Descripcion: EVALUACION INDIVIDUAL #1
# Brandon Werner Rivera Cabrera 23088
#---------------------------------------------------------------
from turtle import *
from Evaluacion01_modulo import *
from collections import Counter
import time
import random
hideturtle()
speed(11)
setup(500, 530, -100, 100)

canciones = {}
cancionesordenadas = {}
artistas = []

print("Bienvenido a Spotify UVG")
interfaz1()
print("*"*60)
opcion = 0
print("1. Agregar nueva canción \n 2. Eliminar canción \n 3. Ver canciones guardadas \n 4. Ver artistas guardados \n 5. Eliminar todas las canciones \n 6. Salir")
opcion = input("Ingrese una opcion: ")
v = True
while (v == True):
    try:
        int(opcion)
        if(int(opcion) <= 6):
            v = False
        else:
            print("Error!, Ingrese una opcion valida")
            opcion = input("Ingrese una opcion: ")
    except:
        print("Error!, Ingrese un numero valido")
        opcion = input("Ingrese una opcion: ")
    print("*"*60)

    while (int(opcion) != 6):
        if (int(opcion) == 1):
            cancion = input("Ingrese el nombre de la cancion deseada: ")
            if (cancion in canciones): # (Python Check If Key Exists in Dictionary, 2023)
                cancion = cancion + str(2) # (Python Insert a Number in String, 2019)
            artista = input("Ingrese el nombre del artista al cual pertenece: ")
            album = input("Ingrese el nombre del album al cual pertenece: ")
            duracion = input("Ingrese la duracion de la cancion (:): ").split(":")
            canciones.update({cancion:[album,artista,duracion[0],duracion[1]]}) #(Python - Add Dictionary Items, 2023)
        elif (int(opcion) == 2):
            print("Ingrese el nombre de la cancion que desea eliminar \n presione q para cancelar")
            eliminar = input("Ingrese el nombre: ")
            a = True
            while(a == True):
                if (eliminar == "q"):
                    a = False
                elif (eliminar in canciones):
                    canciones.pop(eliminar)
                    print("Cancion eliminada exitosamente!")
                    a = False
                else:
                    eliminar = input("Ingrese una opcion o el nombre de una cancion valida: ")
        elif (int(opcion) == 3):
            largo = len(canciones)
            orden = sorted(canciones)
            for key in orden:
                cancionesordenadas[key] = canciones[key] # (Bala Priya C, 2022)
            interfaz2(largo, cancionesordenadas)
            salir = input("Presione enter para salir: ")
        elif (int(opcion) == 4):
            largo = len(canciones)
            for i in range(largo):
                key, value = list(canciones.items())[i]
                artistas.append(value[1])
            conteo = dict(Counter(artistas)) # (Nik, 2021)
            cantart = {key:value for key, value in conteo.items()}
            interfaz3(len(cantart),cantart)
            salir = input("Presione enter para salir: ")
        elif (int(opcion) == 5):
            print("Esta a punto de eliminar todas las canciones")
            seguro = input("esta seguro que desea hacerlo? (si o no): ")
            s = seguro.lower()
            if (s == "si"):
                canciones.clear()
                print("Canciones eliminadas exitosamente!")
            else:
                continue
        time.sleep(2)
        interfaz1()
        print("*"*60)
        print("1. Agregar nueva canción \n 2. Eliminar canción \n 3. Ver canciones guardadas \n 4. Ver artistas guardados \n 5. Eliminar todas las canciones \n 6. Salir")
        opcion = input("Ingrese una opcion: ")
        v = True
        while (v == True):
            try:
                int(opcion)
                if(int(opcion) <= 6):
                    v = False
                else:
                    print("Error!, Ingrese una opcion valida")
                    opcion = input("Ingrese una opcion: ")
            except:
                print("Error!, Ingrese un numero valido")
                opcion = input("Ingrese una opcion: ")
            print("*"*60)
print("Saliendo del programa!")