from abc import ABC, abstractmethod
import json

'''
# 1.c. definición de clase abstracta
'''

class EntidadVineria(ABC):
    #constructor
    def __init__(self, id: str, nombre: str):
        #atributos de instancia protegidos
        self._id = id
        self._nombre = nombre

#consultas    
    def obtenerNombre(self) -> str:
        return self._nombre
        
    def obtenerId(self) -> str:
        return self._id

#comandos 
    def establecerNombre(self, nombre: str):
        self._nombre = nombre

    '''
1.b. __eq__ compara dos objetos con operador == basándose en sus ids
    '''

    def __eq__(self, otro):
        #Verifica si el objeto otro es una instancia
        #de EntidadVineria o de una clase derivada. Sino retorna False
        if not isinstance(otro, EntidadVineria):
            return False
        #si son iguales los ids los considera equivalentes
        return self._id == otro.obtenerId()
    

    @abstractmethod
    #debe ser implementada la personalización por las clases hijas
    #devuelve un dic con la representación completa de la entidad
    def convertirAJSONFull(self) -> dict:
        
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "bodega": self.obtenerBodega().obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "partidas": self.__partidas,
        }

    def __repr__(self) -> str:
        
        return json.dumps({"nombre": self.obtenerNombre()})