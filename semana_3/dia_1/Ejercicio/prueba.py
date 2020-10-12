from clases import Estacion, ComunidadMadrid
from funciones import dist_estaciones

import pandas as pd

dic = pd.read_excel("2018_Julio_Bases_Bicimad_EMT.xlsx").to_dict()

# Define (e importa) antes la clase Estacion!!!

tot_est = []
for i in range(len(dic['name'].values())):
    estacion = Estacion(dic['name'][i], dic['id'][i], dic['total_bases'][i], dic['address'][i], dic['longitude'][i], 
                        dic['latitude'][i])
    tot_est.append(estacion)
    
comunidad = ComunidadMadrid(tot_est)


while True:
    opcion = input("""Escoge una opcion:
        1. Busca estacion (nombre)
        2. Calcula distancia (entre ids)
        3. Salir del programa
        
                   """)
    if opcion == '3':
        break
    elif opcion == '2':
        print("Soy opción 2")
    elif opcion == '1':
        a = input("Nº 1"))
        if a == True:
            print("Hola")
            continue
            print("HOLAAAA SOY B")            
            
        else:
            print("Es falso")
        
        
        
        print("Soy opción 1")
    else:
        print("No es un número válido!!")
                   
                   
