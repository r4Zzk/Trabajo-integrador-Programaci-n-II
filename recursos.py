#Resource es la clase base para definir recursos (entidades o endpoints)
#que exponen métodos HTTP
from flask_restful import Resource
#request permite acceder a datos enviados por el cliente, como parámetros
#en la URL (query parameters) o datos del cuerpo de una solicitud.
from flask import request

import json


from modelos.bodega import Bodega
from modelos.cepa import Cepa
from modelos.vino import Vino
from vinoteca import Vinoteca

#define un recurso RESTful para una bodega específica
class RecursoBodega(Resource):
    #Implementa el método HTTP GET. Permite al cliente
    #solicitar información de una bodega por su id.
    def get(self, id):
        #Llama al método buscarBodega de Vinoteca
        #para buscar la bodega con el id proporcionado.
        bodega = Vinoteca.buscarBodega(id)
        #Verifica si se encontró una bodega válida.
        if isinstance(bodega, Bodega):
            #Convierte la bodega a un formato JSON completo usando
            #convertirAJSONFull, y responde con un código HTTP 200 (éxito).
            return json.loads(json.dumps(bodega.convertirAJSONFull())), 200
        else:
            #Si no se encuentra, devuelve un mensaje de error
            #con un código HTTP 404 (no encontrado).
            return {"error": "Bodega no encontrada"}, 404

#Define un recurso RESTful para listar todas las bodegas.
class RecursoBodegas(Resource):

    def get(self):
        #Lee el parámetro orden de la URL para determinar el criterio de ordenamiento.
        orden = request.args.get("orden")
        if orden:
            #Lee el parámetro reverso para decidir si el orden es descendente (si) o ascendente.
            reverso = request.args.get("reverso")
            #Llama al método obtenerBodegas de Vinoteca para obtener una lista de bodegas,
            #aplicando los criterios de orden si están presentes.
            bodegas = Vinoteca.obtenerBodegas(
                orden=orden, reverso=reverso == "si"
            )
        else:
            bodegas = Vinoteca.obtenerBodegas()
        return (
            #Si bodegas contiene objetos, convierte cada uno a JSON usando su método convertirAJSON.
            #Devuelve la lista de bodegas en formato JSON y un código HTTP 200
            json.loads(json.dumps(bodegas, default=lambda o: o.convertirAJSON())),
            200,
        )

#similar a RecursoBodega pero con cepa
class RecursoCepa(Resource):

    def get(self, id):
        cepa = Vinoteca.buscarCepa(id)
        if isinstance(cepa, Cepa):
            return json.loads(json.dumps(cepa.convertirAJSONFull())), 200
        else:
            return {"error": "Cepa no encontrada"}, 404

#similar a RecursoBodegas pero con cepas
class RecursoCepas(Resource):

    def get(self):
        orden = request.args.get("orden")
        if orden:
            reverso = request.args.get("reverso")
            cepas = Vinoteca.obtenerCepas(orden=orden, reverso=reverso == "si")
        else:
            cepas = Vinoteca.obtenerCepas()
        return (
            json.loads(json.dumps(cepas, default=lambda o: o.convertirAJSONFull())),
            200,
        )

#Define un recurso RESTful para un vino específico.
class RecursoVino(Resource):

    def get(self, id):
        #Busca un vino por su id en Vinoteca.
        vino = Vinoteca.buscarVino(id)
        if isinstance(vino, Vino):
            #Convierte el vino encontrado en una representación JSON completa.
            return json.loads(json.dumps(vino.convertirAJSONFull())), 200
        else:
            #Devuelve un error 404 si no se encuentra el vino.
            return {"error": "Vino no encontrado"}, 404


class RecursoVinos(Resource):

    def get(self):
        #Lee el parámetro anio para filtrar los vinos por un año específico.
        anio = request.args.get("anio")
        if anio:
            anio = int(anio)
        orden = request.args.get("orden")
        if orden:
            reverso = request.args.get("reverso")
            #Obtiene la lista de vinos desde Vinoteca, aplicando
            #los filtros y criterios de ordenamiento.
            vinos = Vinoteca.obtenerVinos(
                anio, orden=orden, reverso=reverso == "si"
            )
        else:
            vinos = Vinoteca.obtenerVinos(anio)
            #Devuelve la lista de vinos en formato JSON.
        return json.loads(json.dumps(vinos, default=lambda o: o.convertirAJSON())), 200
