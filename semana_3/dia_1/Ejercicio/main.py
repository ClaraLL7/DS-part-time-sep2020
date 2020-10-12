from clases import Estacion, ComunidadMadrid
from funciones import dist_estaciones

import pandas as pd

dic = pd.read_excel("2018_Julio_Bases_Bicimad_EMT.xlsx").to_dict()

# Define (e importa) antes la clase Estacion!!!

tot_est = []
for i in range(len(dic['name'].values())):
    estacion = Estacion(dic['name'][i], dic['id'][i], dic['total_bases'][i],
                        dic['address'][i], dic['longitude'][i], 
                        dic['latitude'][i])
    tot_est.append(estacion)
    
comunidad = ComunidadMadrid(tot_est)


    
print("Bienvenido a BiciMAD Search")

print("¿Qué deseas hacer?")

msg = """
Escoge una opción:
    1. Busca estación (nombre)
    2. Calcula distancia (entre ids)
    3. Salir del programa
"""


while True:
    entrada = input(msg)
    
    if entrada == '3':
        break
    
    elif entrada == '2':
        id1 = input("Introduce id 1a estación: ")
        id2 = input("Introduce id 2a estación: ")
        try:
            id1 = int(id1)
            id2 = int(id2)
            ids_estaciones = comunidad.get_ids()
            if id1 in ids_estaciones and id2 in ids_estaciones:
                distancia = dist_estaciones(id1, id2, comunidad)
                print(f"La distancia entre las estaciones {id1} y {id2} es {distancia} km")
                print("¿Qué más deseas hacer?")
            else:
                print("ERROR: IDs no encontrados.\nVolviendo al menú principal...")
        except:
            print("Has introducido mal algún id ¡¡Eso no son números enteros!!")
            
    elif entrada == '1':
        name1 = input("Introduce el nombre que quieres buscar: ")
        est_found = comunidad.busca_estacion(name1, tipo_busqueda='name')
        if est_found == None:
            print("Estación no encontrada")
        else:
            print(est_found.name)
            
        

