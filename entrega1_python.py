#Instalamos el paquete necesario para cargar los datos de pinguinos
!pip install palmerpenguins

#importamos las librerias necesarias
import pandas as pd
import numpy as np
from palmerpenguins import load_penguins

################################################################################
#Ejercicio 1
print("EJERCICIO 1")
print("_"*80)
#Cargamos el conjunto de datos
penguins = load_penguins()

#Sabemos que el numero de observaciones es el numero de filas de nuestro dataframe
#Mostraremos el resultado con un print
print(f'El numero de observaciones es: {penguins.shape[0]} \n')

#Las columnas seran las caracteristicas que estudiaremos de los pinguinos
#Miramos el tipo de dato de cada una de ellas y sus nombres
print(penguins.info())

#Comprovamos si tiene valores NA
print(f"\n El conjunto penguins tiene valores NA en las columnas: \n{penguins.isna().any()}")
print("_"*80)

################################################################################
#Ejercicio 2
print("EJERCICIO 2")
print("_"*80)
#Eliminamos las observaciones que contienen NA
penguins_nona=penguins.dropna()

#Comprovamos si queda algun NA
print(f"\n El conjunto penguins_nona tiene valores NA en las columnas: \n{penguins_nona.isna().any()}")
print("_"*80)

################################################################################
#Ejercicio 3
print("EJERCICIO 3")
print("_"*80)
#Agrupamos los individuos por sexo con la funcion groupby
penguins_bysex=penguins_nona.groupby("sex")

#Usamos la funcion len para saber cuantos hay de cada sexo, descontando los que tenian NA
n_female = len(penguins_bysex.groups["female"])
n_male = len(penguins_bysex.groups["male"])

print(f"El numero de hembras es: {n_female}\nEl numero de machos es: {n_male}")

#Podemos obtener la longitud media del pico segun sexo mediante la funcion aggregate y la funcion mean de numpy
mean_bill_len_bysex = penguins_nona.groupby("sex").aggregate({"bill_length_mm": np.mean})
print("\nA continuacion presentamos la longitud media del pico segun el sexo:")
print(mean_bill_len_bysex)
print("_"*80)

################################################################################
#Ejercicio 4
print("EJERCICIO 4")
print("_"*80)
#Creamos una lista que contiene para cada pinguino el producto de la longitud y la profundidad del pico
bill_area = penguins_nona.bill_length_mm * penguins_nona.bill_depth_mm

#Añadimos esa lista en el dataframe usando la funcion insert
penguins_nona.insert(loc=penguins_nona.shape[1], column="bill_area", value=bill_area)

#Verificamos que es correcto
print(penguins_nona)
print("_"*80)

################################################################################
#Ejercicio 5
print("EJERCICIO 5")
print("_"*80)
#Agrupamos en función de sexo y especie con groupby
penguins_bysex_byspecie=penguins_nona.groupby(["sex", "species"])

#Imprimimos la informacion por especies de los pinguinos hembra
for name, group in penguins_bysex_byspecie:
  if name[0]=="female":
    print(name[1])
    print(group)
    print("\n")
print("_"*80)

################################################################################
#Ejercicio 6
print("EJERCICIO 6")
print("_"*80)
#Creamos una lista que contenga el peso de los pinguinos en kg
body_mass_kg= penguins_nona.body_mass_g / 1000

#Añadimos esta columna en la posicion de de body_mass_g
penguins_nona.insert(loc=5, column="body_mass_kg", value=body_mass_kg)

#Eliminamos la columna body_mass_g
penguins_nona.drop(columns=["body_mass_g"])
print(penguins_nona)