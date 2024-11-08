"""
simulacion_propagacion.py

Este módulo realiza la simulación de propagación de información en la red social usando un algoritmo de 
Búsqueda en Anchura (BFS) modificado. La probabilidad de propagación entre nodos depende de atributos como 
la tasa de interacción, similitud de intereses, y coincidencias demográficas.

Funciones:
    - similitud_intereses: Calcula la similitud entre intereses de dos usuarios.
    - propagar_informacion: Realiza la propagación de información en el grafo usando BFS y ajustando la probabilidad 
      según los atributos de usuario y tipo de información.
"""
import random
from generador_informacion import FACTORES_PROPAGACION

def similitud_intereses(interes1, interes2):
    return len(set(interes1) & set(interes2)) / max(len(set(interes1) | set(interes2)), 1)

def propagar_informacion(grafo, perfiles, informacion, nodo_inicial):
    cola = [(nodo_inicial, 0)]
    visitados = {nodo_inicial: 0}

    while cola:
        nodo_actual, tiempo_actual = cola.pop(0)

        for vecino in grafo.neighbors(nodo_actual):
            if vecino not in visitados:
                similitud = similitud_intereses(perfiles[nodo_actual]['intereses'], perfiles[vecino]['intereses'])
                factor_propagacion = FACTORES_PROPAGACION[informacion['categoria']]
                factor_demografico = 1.0

                if perfiles[vecino]['pais'] == perfiles[nodo_actual]['pais']:
                    factor_demografico += 0.1
                if perfiles[vecino]['genero'] == perfiles[nodo_actual]['genero']:
                    factor_demografico += 0.1

                probabilidad_propagacion = perfiles[vecino]['tasa_interaccion'] * similitud * factor_propagacion * factor_demografico

                if random.random() < probabilidad_propagacion:
                    tiempo_llegada = tiempo_actual + 1 / (perfiles[vecino]['tiempo_uso'] * informacion['popularidad_inicial'])
                    visitados[vecino] = tiempo_llegada
                    cola.append((vecino, tiempo_llegada))

    return visitados
