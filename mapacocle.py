#Rogelio trujillo, Geeremith Lopez
import networkx as nx # Importa la librería networkx para trabajar con grafos
import matplotlib.pyplot as plt # Importa la librería matplotlib para visualización

# Crea una figura con tamaño de 12x12 pulgadas para el gráfico
fig = plt.figure(figsize=(12,12))
# Agrega un subplot en la posición (1, 1, 1) en la figura
ax = plt.subplot(111)

# Define nombres de distritos como variables
Aguadulce = "Aguadulce"
Anton = "Antón"
La_Pintada = "La Pintada"
Nata = "Natá"
Ola = "Olá"
Penonome = "Penonomé"


Grafo = nx.Graph() # Crea un objeto de tipo Grafo usando la librería networkx
# Agrega nodos al grafo, que representan dsitritos
Grafo.add_node(Aguadulce)      
Grafo.add_node(Anton)
Grafo.add_node(La_Pintada)
Grafo.add_node(Nata)
Grafo.add_node(Ola)
Grafo.add_node(Penonome)

# Agrega aristas (con pesos) que conectan las ciudades, creando una red de conexiones
Grafo.add_edge(Aguadulce,Ola,weight=35)  
Grafo.add_edge(Aguadulce,Nata,weight=19)
Grafo.add_edge(Penonome,La_Pintada,weight=18)
Grafo.add_edge(Penonome,Anton,weight=18)
Grafo.add_edge(Ola,Nata,weight=38)
Grafo.add_edge(Ola,La_Pintada,weight=45)
Grafo.add_edge(Anton,Nata,weight=65)


pos = nx.spring_layout(Grafo) # Calcula la posición de los nodos en el grafo utilizando un algoritmo de disposición (para posicionar los nodos en un gráfico o red de manera visualmente agradable y comprensible)
# Dibuja el grafo con los nodos y las conexiones, personalizando su apariencia
nx.draw(Grafo, pos, node_size=1300, node_color='red', font_size=8, font_weight='bold', with_labels=True)

weights = nx.get_edge_attributes(Grafo, "weight")# Obtiene los pesos de las aristas del grafo
nx.draw_networkx_edge_labels(Grafo, pos, edge_labels=weights) # Agrega etiquetas de peso a las aristas del grafo

inicio = input("Ingresa el lugar de partida -> ")# Solicita al usuario el lugar de partida
destino = input("Ingresa el lugar de llegada: -> ") # Solicita al usuario el lugar de llegada

# Encuentra el camino más corto y su longitud entre el lugar de inicio y destino en el grafo
camino_corto = nx.shortest_path(Grafo, inicio, destino, weight='weight')
longitud = nx.shortest_path_length(Grafo, inicio, destino, weight='weight')
leyenda = "El Camino Corto es: " + str(camino_corto) + " con una distancia de: " + str(longitud) + " km"
ax.set_title(leyenda, fontsize=10)  # Establece el título del gráfico con información sobre el camino más corto encontrado
print(camino_corto)  # Imprime el camino más corto en la consola

plt.tight_layout() # Ajusta el diseño del gráfico para una presentación más clara
plt.savefig("Graph.png", format="PNG")  # Guarda el gráfico como una imagen PNG
plt.show()  # Muestra el gráfico
