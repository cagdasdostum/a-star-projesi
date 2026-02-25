# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 21:01:37 2026

@author: cagda
"""

import networkx as nx
import matplotlib.pyplot as plt

# Graf verilerimiz
graph_data = {
    'Balçova Barajı': {'Mithatpaşa': 15},
    'Bornova': {'Buca Su Pompaları': 18, 'Konak Merkez': 15, 'Kemalpaşa': 20},
    'Buca Su Pompaları': {'Tahtalı Barajı': 40, 'Bornova': 18},
    'Güzelbahçe': {'Mithatpaşa': 22},
    'Güzelhisar Barajı': {'Menemen Kuyuları': 25},
    'Gördes Barajı': {'Sarıkız Kuyuları': 65},
    'Kemalpaşa': {'Bornova': 20, 'Sarıkız Kuyuları': 20},
    'Konak Merkez': {},
    'Menemen Çıkış': {'Konak Merkez': 10, 'Menemen Kuyuları': 12},
    'Menemen Kuyuları': {'Güzelhisar Barajı': 25, 'Menemen Çıkış': 12},
    'Mithatpaşa': {'Balçova Barajı': 15, 'Güzelbahçe': 22, 'Konak Merkez': 12},
    'Sarıkız Kuyuları': {'Gördes Barajı': 65, 'Menemen Kuyuları': 15, 'Kemalpaşa': 20},
    'Tahtalı Barajı': {'Buca Su Pompaları': 40, 'Mithatpaşa': 30}
}

# Algoritmanın bulduğu en iyi rota
best_path = ['Tahtalı Barajı', 'Mithatpaşa', 'Konak Merkez']

# Graf nesnesini oluştur ve kenarları ekle
G = nx.Graph()
for u, edges in graph_data.items():
    for v, weight in edges.items():
        G.add_edge(u, v, weight=weight)

# Düğümlerin ekrandaki yerleşimini raporundaki haritaya benzer şekilde koordinatlıyoruz
pos = {
    'Gördes Barajı': (10, 10),
    'Sarıkız Kuyuları': (8, 8),
    'Güzelhisar Barajı': (4, 10),
    'Menemen Kuyuları': (5, 7),
    'Menemen Çıkış': (4, 5),
    'Kemalpaşa': (9, 4),
    'Bornova': (7, 3),
    'Buca Su Pompaları': (7, 0),
    'Konak Merkez': (4, 3),
    'Mithatpaşa': (2, 2),
    'Balçova Barajı': (1, 0),
    'Güzelbahçe': (0, 3),
    'Tahtalı Barajı': (5, -2)
}

plt.figure(figsize=(12, 8))

# Genel haritayı çizdirme işlemleri
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, 
        font_size=10, font_weight='bold', edge_color='gray', width=1.5)

# Maliyetleri çizgilerin üzerine yazdırma
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, font_color='red')

# Bulunan optimum rotayı yeşil renk ve kalın çizgi ile vurgulama
path_edges = list(zip(best_path, best_path[1:]))
nx.draw_networkx_nodes(G, pos, nodelist=best_path, node_color='lightgreen', node_size=3000)
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='green', width=4)

plt.title("İzmir Su Dağıtım Ağı ve Optimum Rota (Tahtalı Barajı -> Konak Merkez)", fontsize=16)
plt.show()