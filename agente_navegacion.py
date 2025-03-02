from collections import deque
import time

class AgenteNavegacion:
    def __init__(self, laberinto, inicio, meta):
        self.laberinto = laberinto
        self.inicio = inicio
        self.meta = meta
        self.movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Derecha, Abajo, Izquierda, Arriba

    def buscar_salida(self):
        """Encuentra la ruta más corta usando Búsqueda en Anchura (BFS)."""
        fila_inicio, col_inicio = self.inicio
        fila_meta, col_meta = self.meta

        # Cola para BFS (posiciones y ruta acumulada)
        cola = deque([(fila_inicio, col_inicio, [])])
        visitados = set()
        
        while cola:
            fila, col, ruta = cola.popleft()
            ruta.append((fila, col))

            print(f"Agente en: {fila, col}")
            time.sleep(0.5)  # Simula el tiempo de búsqueda
            
            if (fila, col) == (fila_meta, col_meta):
                print("🎯 Meta alcanzada. Ruta óptima encontrada:")
                print(ruta)
                return ruta
            
            visitados.add((fila, col))

            for df, dc in self.movimientos:
                nueva_fila, nueva_col = fila + df, col + dc
                if self.es_valido(nueva_fila, nueva_col, visitados):
                    cola.append((nueva_fila, nueva_col, ruta.copy()))
        
        print("🚫 No se encontró una ruta a la meta.")
        return None

    def es_valido(self, fila, col, visitados):
        """Verifica si la celda está dentro del laberinto y no es una pared."""
        return (0 <= fila < len(self.laberinto) and
                0 <= col < len(self.laberinto[0]) and
                self.laberinto[fila][col] == 0 and
                (fila, col) not in visitados)

# Representación del laberinto (0 = camino, 1 = pared)
laberinto_5x5 = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

inicio = (0, 0) 
meta = (4, 4)  # Posición de la salida

# Crear y ejecutar el agente de navegación
agente = AgenteNavegacion(laberinto_5x5, inicio, meta)
ruta_optima = agente.buscar_salida()
