import json
from .entidadvineria import EntidadVineria


#hija/hereda de EntidadVineria  
class Vino(EntidadVineria):
    #constructor
    def __init__(self, id: str, nombre: str, bodega: str, cepas: list, partidas: list):
        super().__init__(id, nombre)
        #atributos de instancia        
        self._bodega = bodega
        self._cepas = cepas
        self._partidas = partidas

#comandos
    def establecerBodega(self, bodega: str):
        self._bodega = bodega
    
    def establecerCepas(self, cepas: list):
        self._cepas = cepas
    
    def establecerPartidas(self, partidas: list):
        self._partidas = partidas

#consultas  
    def obtenerId(self):
        return super().obtenerId()
    
    def obtenerNombre(self):
        return super().obtenerNombre()
    
        """
B. La consulta obtenerBodega debe hacer uso del servicio buscarBodega de la clase Vinoteca 
para recuperar el objeto de tipo Bodega asociado al vino. 
        """

    def obtenerBodega(self):
        from vinoteca import Vinoteca
        return Vinoteca.buscarBodega(self._bodega)
    
        """
C. La consulta obtenerCepas puede hacer uso de los servicios buscarCepa u obtenerCepas de la clase Vinoteca 
para recuperar los objetos de tipo Cepa para las cepas en las que se ofrece el vino en cuestión. 
        """

    def obtenerCepas(self):
        from vinoteca import Vinoteca
        return [Vinoteca.buscarCepa(cepa_id) for cepa_id in self._cepas]
    
    
    def obtenerPartidas(self) -> list:
        return self._partidas

    def __repr__(self):
        return json.dumps({"nombre": self.obtenerNombre()})

    def convertirAJSON(self)-> dict:
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "bodega": self.obtenerBodega().obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "partidas": self._partidas,
        }

    def convertirAJSONFull(self)-> dict:
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "bodega": self.obtenerBodega().obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "partidas": self._partidas,
        }

    def __mapearCepas(self):
        cepas = self.obtenerCepas()
        cepasMapa = map(lambda a: a.obtenerNombre(), cepas)
        return list(cepasMapa)
