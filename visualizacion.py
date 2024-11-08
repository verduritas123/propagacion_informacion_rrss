"""
visualizacion.py

Este módulo genera una visualización interactiva de la propagación de información en la red social.
La visualización se realiza utilizando `Plotly`, y permite ver el tiempo de llegada de la información 
a cada nodo (usuario) en función del camino más corto.

Funciones:
    - visualizar_propagacion: Crea un gráfico interactivo de la red mostrando el tiempo de llegada 
      de la información a cada usuario.
"""
import plotly.graph_objects as go
import networkx as nx

def visualizar_propagacion(grafo, perfiles, tiempos_llegada, categoria_informacion):
    pos = nx.spring_layout(grafo)
    edge_x = []
    edge_y = []
    for edge in grafo.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]

    edge_trace = go.Scatter(x=edge_x, y=edge_y, line=dict(width=0.5, color='#888'), hoverinfo='none', mode='lines')

    node_x = []
    node_y = []
    node_color = []
    node_text = []

    for nodo in grafo.nodes():
        x, y = pos[nodo]
        node_x.append(x)
        node_y.append(y)
        tiempo = tiempos_llegada.get(nodo, float('inf'))
        color = tiempo if tiempo != float('inf') else 0
        node_color.append(color)
        perfil = perfiles[nodo]
        node_text.append(f"Usuario {nodo}<br>País: {perfil['pais']}<br>Género: {perfil['genero']}<br>Tiempo de llegada: {color:.2f}")

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        text=node_text,
        marker=dict(
            showscale=True,
            colorscale='Viridis',
            size=10,
            color=node_color,
            colorbar=dict(title="Tiempo de llegada")
        )
    )

    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        title=f"Propagación de Información: {categoria_informacion}",
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20, l=5, r=5, t=40),
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                    )
    fig.show()
