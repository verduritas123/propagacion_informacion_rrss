"""
generador_informacion.py

Este módulo define las categorías de información que pueden propagarse en la red social y genera 
un tipo de información basado en una categoría seleccionada. Cada categoría tiene un factor de 
propagación asociado, lo que influye en la rapidez y alcance de su difusión en la red.

Categorías de Información:
    Noticias de Actualidad, Deportes, Entretenimiento, Cotilleos, Política, Economía y Finanzas, Tecnología, Ciencia y Salud, Cultura y Espectáculos, Viajes y Turismo, Educación, Medio Ambiente. Opinión y Blogs, Activismo Social

Factores de Propagación:
    Cada categoría de información tiene un factor de propagación que determina la rapidez y 
    facilidad con que la información se transmite. Las categorías más virales (como Cotilleos) 
    tienen factores de propagación más altos que otras (como Medio Ambiente).

Funciones:
    - generar_informacion: Genera un diccionario con el tipo de información seleccionada y 
      su factor de popularidad inicial.
"""
import random

CATEGORIAS_INFORMACION = [
    'Noticias de Actualidad', 'Deportes', 'Entretenimiento', 'Cotilleos',
    'Política', 'Economía y Finanzas', 'Tecnología', 'Ciencia y Salud',
    'Cultura y Espectáculos', 'Viajes y Turismo', 'Educación', 'Medio Ambiente',
    'Opinión y Blogs', 'Activismo Social'
]

FACTORES_PROPAGACION = {
    'Noticias de Actualidad': 1.5,
    'Deportes': 1.3,
    'Entretenimiento': 1.4,
    'Cotilleos': 1.7,
    'Política': 1.6,
    'Economía y Finanzas': 1.2,
    'Tecnología': 1.0,
    'Ciencia y Salud': 0.9,
    'Cultura y Espectáculos': 1.1,
    'Viajes y Turismo': 1.0,
    'Educación': 0.8,
    'Medio Ambiente': 0.7,
    'Opinión y Blogs': 0.6,
    'Activismo Social': 1.3,
}


def generar_informacion(categoria):
    return {
        'categoria': categoria,
        'popularidad_inicial': random.uniform(0.5, 1.5),
        'es_viral': random.choice([True, False])
    }
