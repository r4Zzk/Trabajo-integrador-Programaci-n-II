import json
from .entidadvineria import EntidadVineria

#hija/hereda de EntidadVineria
class Bodega(EntidadVineria):
    #constructor
    def __init__(self, id: str, nombre: str):
        super().__init__(id, nombre)


#consultas
    def obtenerId(self):
        return super().obtenerId()
    
    def obtenerNombre(self):
        return super().obtenerNombre()

        """
B. La consulta obtenerVinos debe hacer uso del servicio obtenerVinos de la clase Vinoteca para recuperar 
todos los vinos contenidos en el archivo json. Sobre dicha lista se debe iterar hasta encontrar los vinos 
que pertenecen a la bodega en cuestión. 
        """

    def obtenerVinos(self) -> list:
        from vinoteca import Vinoteca
        todos_vinos = Vinoteca.obtenerVinos(None, None, None)
        #filtro vinos que obtenerBodega().obtenerId() coincida
        #con el id de la bodega actual (self._id)
        return [vino for vino in todos_vinos if vino.obtenerBodega().obtenerId() == self._id]
    
        """
C. La consulta obtenerCepas debe seguir la misma impronta que el punto anterior para intentar encontrar 
aquellos vinos que pertenecen a la bodega, recuperando únicamente las cepas en los que se ofrecen estos. 
        """

    def obtenerCepas(self):
        #obtiene todos los vinos de la bodega pasada x parámetro
        vinos_bodega = self.obtenerVinos()
        cepas = []
        #itera sobre cada vino y después sobre cada cepa asociada al vino
        for vino in vinos_bodega:
            for cepa in vino.obtenerCepas():
                #__eq__ ( de la clase Cepas) para comparar correctamente los objetos
                if cepa not in cepas:  
                    cepas.append(cepa)
        return cepas
        
    def __repr__(self):
        #convierte conjunto de objetos en cadena JSON
        return json.dumps(self.convertirAJSON())
    
    def convertirAJSON(self):
        #convierte la instancia en dic JSON
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            #lista de nombres
            "cepas": self.__mapearCepas(),
            #total de vinos
            "vinos": len(self.obtenerVinos()),
        }

    def convertirAJSONFull(self):
        #convierte la instancia en dic JSON completo
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "vinos": self.__mapearVinos(),
        }

    def __mapearCepas(self):
        cepas = self.obtenerCepas()
        #map itera para aplicar la función en cada cepa
        #lambda a: a.obtenerNombre() toma cada elemento a (una cepa)
        #y llama al método obtenerNombre() para obtener el nom de la cepa
        cepasMapa = map(lambda a: a.obtenerNombre(), cepas)
        #map es iterador, se convierte a lista y la retorna
        return list(cepasMapa)

    def __mapearVinos(self):
        vinos = self.obtenerVinos()
        #mismo funcionamiento que __mapearCepas pero con objetos vino
        vinosMapa = map(lambda a: a.obtenerNombre(), vinos)
        return list(vinosMapa)

