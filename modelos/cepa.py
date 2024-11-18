import json
from .entidadvineria import EntidadVineria

#hija/hereda de EntidadVineria
class Cepa(EntidadVineria):
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
que se ofrecen en la cepa en cuestión.
        """

    def obtenerVinos(self):
        from vinoteca import Vinoteca
        todos_vinos = Vinoteca.obtenerVinos(None, None, None)
        return [vino for vino in todos_vinos if self._id in vino._cepas]

    def __repr__(self):
        return json.dumps({"nombre": self.obtenerNombre()})
    
    def __eq__(self, otro):
        if not isinstance(otro, Cepa):
            return False
        return self._id == otro._id
    
    def convertirAJSON(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "vinos": len(self.obtenerVinos()),
        }

    def convertirAJSONFull(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "vinos": self.__mapearVinos(),
        }

    def __mapearVinos(self):
        vinos = self.obtenerVinos()
        vinosMapa = map(
            lambda a: a.obtenerNombre()
            + " ("
            + a.obtenerBodega().obtenerNombre()
            + ")",
            vinos,
        )
        return list(vinosMapa)
