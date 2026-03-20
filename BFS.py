from collections import deque

grafo = {
    "CDMX": ["Morelos", "Hidalgo", "Qro", "Zacatecas", "Tamaulipas", "Monterrey"],
    "Morelos": ["CDMX", "Hidalgo"],
    "Hidalgo": ["Morelos", "CDMX"],
    "Qro": ["CDMX", "SLP", "Jiloyork"],
    "SLP": ["Qro", "Zacatecas"],
    "Zacatecas": ["SLP", "CDMX", "GDL"],
    "GDL": ["Zacatecas", "Tamaulipas"],
    "Tamaulipas": ["GDL", "CDMX"],
    "Monterrey": ["CDMX"],
    "Jiloyork": ["Qro"]
}

def buscar_solucion_BFS(inicio, objetivo):
    cola = deque([[inicio]])
    visitados = set()

    while cola:
        ruta = cola.popleft()
        nodo = ruta[-1]

        if nodo == objetivo:
            return ruta

        if nodo not in visitados:
            visitados.add(nodo)

            for vecino in grafo.get(nodo, []):
                nueva_ruta = list(ruta)
                nueva_ruta.append(vecino)
                cola.append(nueva_ruta)

    return None