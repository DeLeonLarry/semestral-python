import networkx as nx
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(12, 12))
ax = plt.subplot(111)

#Definiendo arreglos. (variables)
penonome = "penonome"
aguadulce = "aguadulce"
anton = "anton"
nata = "nata"
la_pintada = "la_pintada"
ola = "ola"


#Añadiendo variables al grafo.
Grafo = nx.Graph()
Grafo.add_node(penonome)
Grafo.add_node(aguadulce)
Grafo.add_node(la_pintada)
Grafo.add_node(nata)
Grafo.add_node(anton)
Grafo.add_node(ola)


#Se indica el inicio, final y peso de cada ruta que en este caso es en minutos.
Grafo.add_edge(penonome, la_pintada, weight=18)
Grafo.add_edge(penonome, anton, weight=22)
Grafo.add_edge(la_pintada, ola, weight=52)
Grafo.add_edge(ola, nata, weight=38)
Grafo.add_edge(aguadulce, ola, weight=36)
Grafo.add_edge(aguadulce, nata, weight=19)
Grafo.add_edge(anton, nata, weight=65)



#Se añaden las medicionbes para el grafo y sus caracteristicas.
#se puede cambiar color, tamaño de letra y fuente. 
pos = nx.spring_layout(Grafo)
nx.draw(Grafo, pos, node_size=1300, node_color='yellow', font_size=10, font_weight='bold', with_labels=True)

#Atributos del grafo, caracteristicas. Se le envia el parametro, grafo y peso.
weights = nx.get_edge_attributes(Grafo, "weight")
nx.draw_networkx_edge_labels(Grafo, pos, edge_labels=weights)

#Imprimir en pantalla y lo guarda en la variable inicio y destino.
inicio = input("Ingrese la ruta de inicio: ")
destino = input("Ingrese la ruta de destino: ")


#Funcion de algoritmo de Dijkstra que pasa por parametros los datos previamente añadidos
camino_corto = nx.shortest_path(Grafo, inicio, destino, weight='weight')
distancia = nx.shortest_path_length(Grafo, inicio, destino, weight='weight')

#Titulo del grafo.
leyenda = f"El Camino más corto es: {camino_corto} y con distancia de {distancia} km"
ax.set_title(leyenda, fontsize=10)

#Sirve para mostrar el grafo en formato PNG.
plt.tight_layout()
plt.savefig("Graph.png", format="PNG")
plt.show()


