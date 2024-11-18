import os
import json

# modelos
from modelos.bodega import Bodega
from modelos.cepa import Cepa
from modelos.vino import Vino

#motor de consultas
class Vinoteca:
#atributos de clase
    __archivoDeDatos = os.path.join(os.path.dirname(__file__), 'vinoteca.json') #"vinoteca.json"
    #listas privadas para almacenar instancias de bodegas, cepas y vinos
    __bodegas = []
    __cepas = []
    __vinos = []

#comandos
    #carga los datos desde el JSON y los convierte en instancias de las clases correspondientes
    def inicializar():
        datos = Vinoteca.__parsearArchivoDeDatos()
        Vinoteca.__convertirJsonAListas(datos)

#consultas

    '''
b. i. ii. obtener bodegas,cepas y vinos si se pasa orden se utiliza sorted() para ordenar las bodegas, cepas o vinos 
según el criterio indicado. sino devuelve colección sin alterar el orden
    '''

    def obtenerBodegas( orden: str = None, reverso: bool = False) -> list[Bodega]:
        
        if orden:
            if orden == "nombre":
                return sorted(Vinoteca.__bodegas.copy(), key=lambda b: b.nombre, reverse=reverso)
            elif orden == "vinos":
                return sorted(Vinoteca.__bodegas.copy(), key=lambda b: len(b.obtenerVinos()), reverse=reverso)
        return Vinoteca.__bodegas

    
    def obtenerCepas( orden: str = None, reverso: bool = False) -> list[Cepa]:
        
        if orden == "nombre":
            return sorted(Vinoteca.__cepas.copy(), key=lambda c: c.nombre, reverse=reverso)
        return Vinoteca.__cepas

    
    def obtenerVinos( anio: int = None, orden: str = None, reverso: bool = False) -> list[Vino]:
        
        vinos_filtrados = Vinoteca.__vinos
        
        #c. Filtrar por año si se proporciona
        if anio is not None:
            vinos_filtrados = [vino for vino in vinos_filtrados if anio in vino.obtenerPartidas()]
        
        #ordena según el parámetro orden y reverso
        if orden:
            if orden == "nombre":
                #lambda es como def obtener_nombre(b): return b.nombre
                vinos_filtrados.sort(key=lambda v: v.obtenerNombre(), reverse=reverso)
            elif orden == "bodega":
                vinos_filtrados.sort(key=lambda v: v.obtenerBodega().nombre, reverse=reverso)
            elif orden == "cepas":
                vinos_filtrados.sort(key=lambda v: len(v.obtenerCepas()), reverse=reverso)
        
        return vinos_filtrados
    
    '''
d. todos los buscar recorren las listas privadas, devuelve instancia que coincide con el ID, sino None
    '''
    
    def buscarBodega(id: str):
        for bodega in Vinoteca.__bodegas:
            if bodega.obtenerId() == id:
                return bodega
        return None
    
    def buscarCepa(id: str):
        for cepa in Vinoteca.__cepas:
            if cepa.obtenerId() == id:
                return cepa
        return None
    
    def buscarVino(id: str):
        for vino in Vinoteca.__vinos:
            if vino.obtenerId() == id:
                return vino
        return None

    #e. abre JSON, lo carga como diccionarios, cierra y lo retorna 
    def __parsearArchivoDeDatos():
        with open (Vinoteca.__archivoDeDatos, "r", encoding= "utf-8") as archivo:
            datos = json.load(archivo)
            return datos

    '''
f. operador ** desempaqueta diccionarios. Toma un dicc, pasa sus claves y valores como
argumentos nombrados a una función o constructor.
    '''
    
    def __convertirJsonAListas(lista):
        Vinoteca.__vinos = []
        for vino in lista ["vinos"]:
            Vinoteca.__vinos.append (Vino(**vino))
        
        Vinoteca.__bodegas = []
        for bodega in lista ["bodegas"]:
            Vinoteca.__bodegas.append (Bodega(**bodega))

        Vinoteca.__cepas = []
        for cepa in lista ["cepas"]:
            Vinoteca.__cepas.append (Cepa(**cepa))

'''
sin ** sería:
Vinoteca.__vinos = [
Vino(
    nombre=vino["nombre"],
    anio=vino["anio"],
    bodega=vino["bodega"]
    ) 
for vino in lista["vinos"]
]
'''




