"""
main.py

Archivo principal para ejecutar la simulación de propagación de información en redes sociales.

Este archivo coordina la generación de perfiles, selección de categoría de información, 
ejecución de la propagación y visualización de los resultados.

Pasos:
    1. Crear red social como grafo.
    2. Generar perfiles de usuario.
    3. Solicitar al usuario una categoría de información.
    4. Ejecutar la simulación de propagación.
    5. Visualizar los resultados de propagación en la red.

"""
import networkx as nx
from generador_perfiles import generar_perfiles_usuarios
from generador_informacion import generar_informacion, CATEGORIAS_INFORMACION
from simulacion_propagacion import propagar_informacion
from visualizacion import visualizar_propagacion

def main():
    num_usuarios = 1000
    probabilidad_conexion = 0.05

    # Crear la red social como un grafo
    G = nx.erdos_renyi_graph(num_usuarios, probabilidad_conexion)

    # Generar perfiles de usuarios
    perfiles = generar_perfiles_usuarios(num_usuarios)

    # Solicitar al usuario que elija la categoría de información
    print("Seleccione la categoría de información para la propagación:")
    for i, categoria in enumerate(CATEGORIAS_INFORMACION, start=1):
        print(f"{i}. {categoria}")
    seleccion = int(input("Ingrese el número de la categoría: "))
    categoria_informacion = CATEGORIAS_INFORMACION[seleccion - 1]

    # Generar información con la categoría seleccionada
    informacion = generar_informacion(categoria_informacion)

    # Nodo inicial de propagación
    nodo_inicial = 0

    # Ejecutar simulación de propagación
    tiempos_llegada = propagar_informacion(G, perfiles, informacion, nodo_inicial)

    # Visualizar la propagación
    visualizar_propagacion(G, perfiles, tiempos_llegada, categoria_informacion)

if __name__ == "__main__":
    main()
