def dist_estaciones(est1, est2, comunidad):
    estacion1 = comunidad.busca_estacion(est1, tipo_busqueda='id')
    if estacion1 is None:
        return "ERROR: Estación 1 no encontrada"
    estacion2 = comunidad.busca_estacion(est2, tipo_busqueda='id')
    if estacion2 is None:
        return "ERROR: Estación 2 no encontrada"
    
    distancia = estacion1.distancia(estacion2.longitude, estacion2.latitude)
    return distancia