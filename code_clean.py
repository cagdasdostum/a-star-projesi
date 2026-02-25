import heapq
from typing import Dict, List, Tuple, Optional

class WaterNetworkOptimizer:
    """İzmir su dağıtım ağı optimizasyonu için A* algoritması sınıfı."""

    def __init__(self, graph: Dict[str, Dict[str, int]], heuristics: Dict[str, int]):
        self.graph = graph
        self.heuristics = heuristics

    def find_shortest_path(self, start_node: str, goal_node: str) -> Optional[Tuple[int, List[str]]]:
        """
        A* algoritmasını kullanarak başlangıç düğümünden hedefe en düşük maliyetli rotayı bulur.
        """
        priority_queue = [(self.heuristics.get(start_node, 0), 0, start_node, [start_node])]
        g_scores = {start_node: 0}
        visited = set()

        while priority_queue:
            current_f, current_g, current_node, path = heapq.heappop(priority_queue)

            if current_node == goal_node:
                return current_g, path

            if current_node in visited:
                continue

            visited.add(current_node)

            for neighbor, weight in self.graph.get(current_node, {}).items():
                tentative_g_score = current_g + weight

                if neighbor not in g_scores or tentative_g_score < g_scores[neighbor]:
                    g_scores[neighbor] = tentative_g_score
                    f_score = tentative_g_score + self.heuristics.get(neighbor, 0)
                    new_path = path + [neighbor]
                    
                    heapq.heappush(priority_queue, (f_score, tentative_g_score, neighbor, new_path))

        return None


if __name__ == '__main__':
    # GRAPH TANIMLAMASI
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

    # SEZGİSEL DEĞERLER
    heuristics_data = {
        'Balçova Barajı': 25, 'Bornova': 9, 'Buca Su Pompaları': 15, 'Güzelbahçe': 32,
        'Güzelhisar Barajı': 40, 'Gördes Barajı': 60, 'Kemalpaşa': 30, 'Konak Merkez': 0,
        'Menemen Çıkış': 10, 'Menemen Kuyuları': 22, 'Mithatpaşa': 8, 'Sarıkız Kuyuları': 35,
        'Tahtalı Barajı': 40
    }

    optimizer = WaterNetworkOptimizer(graph_data, heuristics_data)
    hedef = 'Konak Merkez'
    test_noktalari = ['Tahtalı Barajı', 'Gördes Barajı']
    
    sonuclar = []
    
    # Tüm test noktaları için algoritmayı çalıştır ve sonuçları kaydet
    for baslangic in test_noktalari:
        sonuc = optimizer.find_shortest_path(baslangic, hedef)
        if sonuc:
            mesafe, rota = sonuc
            sonuclar.append({'kaynak': baslangic, 'maliyet': mesafe, 'rota': rota})
        else:
            print(f"{baslangic} ile {hedef} arasında ulaşım yok.\n")

    # Sonuçları yüksek maliyetliden düşük maliyetliye doğru sırala (az maliyetli en sonda kalacak)
    if sonuclar:
        sonuclar.sort(key=lambda x: x['maliyet'], reverse=True)
        
        print("--- SENARYO KARŞILAŞTIRMALARI ---\n")
        
        for s in sonuclar:
            print(f"Kaynak: {s['kaynak']}")
            print(f"Toplam Maliyet: {s['maliyet']}")
            print(f"Oluşan Rota: {' -> '.join(s['rota'])}\n")
            print("-" * 40 + "\n")
            
        en_iyi_senaryo = sonuclar[-1]
        print(f">>> KARAR: En uygun maliyetli kaynak {en_iyi_senaryo['maliyet']} birim ile '{en_iyi_senaryo['kaynak']}' olarak belirlenmiştir. <<<")