"""
generador_perfiles.py

Este módulo crea los perfiles de usuario en la red social. Cada usuario es representado como un nodo en el grafo, 
con atributos personalizados que influyen en su comportamiento y en la propagación de información.

Atributos de Usuario:
    - seguidores: Número de conexiones salientes de un usuario (influencia en la red).
    - tiempo_uso: Tiempo que el usuario pasa en la red, influye en la probabilidad de propagación.
    - intereses: Lista de categorías de interés, utilizada para calcular similitudes con otros usuarios.
    - tasa_interaccion: Frecuencia con la que un usuario interactúa, ajusta la probabilidad de propagación.
    - genero: Género del usuario.
    - pais: País de origen del usuario, afecta la probabilidad de propagación en función de coincidencias demográficas.

Funciones:
    - generar_perfiles_usuarios: Genera una cantidad especificada de perfiles de usuario con atributos aleatorios.
"""
import random

GENEROS = ['Masculino', 'Femenino', 'No Binario']
PAISES = ['EE.UU.', 'México', 'España', 'Brasil', 'India', 'Argentina', 'Chile', 'Colombia', 'Reino Unido', 'Francia']

def generar_perfiles_usuarios(num_usuarios):
    perfiles = {}
    for i in range(num_usuarios):
        perfiles[i] = {
            'seguidores': random.randint(10, 1000),
            'tiempo_uso': random.uniform(0.5, 24),  # Horas de uso diario
            'intereses': random.sample(range(10), 3),  # Ejemplo de 10 categorías de interés
            'tasa_interaccion': random.uniform(0.1, 1),  # Tasa de interacción
            'genero': random.choice(GENEROS),
            'pais': random.choice(PAISES)
        }
    return perfiles
