import math

class Estacion:
    
    def __init__(self, name, identificador, num_bicis, address, longitude, latitude):
        self.name = name
        self.id = identificador
        self.num_bicis = num_bicis
        self.address = address
        self.longitude = longitude
        self.latitude = latitude
    
    def distancia(self, longitude, latitude):

        lat1, lon1 = self.latitude, self.longitude
        lat2, lon2 = latitude, longitude
        radius = 6371  # km

        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
             math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
             math.sin(dlon / 2) * math.sin(dlon / 2))
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d = radius * c

        return d
    

    
class ComunidadMadrid:
    
    def __init__(self, estaciones):
        self.estaciones = estaciones
        
    def get_ids(self):
        ids = []
        for estacion in self.estaciones:
            ids.append(estacion.id)
        return ids
    
    def busca_estacion(self, buscado, tipo_busqueda='id'):
        if tipo_busqueda == 'id':
            for est in self.estaciones:
                if est.id == buscado:
                    return est
            return None
        elif tipo_busqueda == 'name':
            for est in self.estaciones:
                if est.name == buscado:
                    return est
            return None
        return None