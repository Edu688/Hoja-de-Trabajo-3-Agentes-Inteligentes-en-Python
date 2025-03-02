import numpy as np

class AgenteSeleccionRutas:
    def __init__(self, matriz_recompensas, inicio, meta):
        self.matriz = matriz_recompensas
        self.inicio = inicio
        self.meta = meta
        self.movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Derecha, Abajo, Izquierda, Arriba

    def buscar_mejor_ruta(self):
        """Encuentra la ruta con mayor recompensa usando búsqueda por maximización."""
        mejor_ruta = []
        mejor_puntaje = -np.inf
        cola = [(self.inicio, [], 0)]  # (posición, ruta, puntaje acumulado)

        while cola:
            (fila, col), ruta, puntaje = cola.pop(0)
            ruta.append((fila, col))
            puntaje += self.matriz[fila][col]

            if (fila, col) == self.meta:
                if puntaje > mejor_puntaje:
                    mejor_puntaje = puntaje
                    mejor_ruta = ruta
                continue

            for df, dc in self.movimientos:
                nueva_fila, nueva_col = fila + df, col + dc
                if self.es_valido(nueva_fila, nueva_col, ruta):
                    cola.append(((nueva_fila, nueva_col), ruta.copy(), puntaje))

        print(f"🔝 Mejor ruta encontrada con utilidad {mejor_puntaje}: {mejor_ruta}")
        return mejor_ruta

    def es_valido(self, fila, col, ruta):
        """Verifica si la celda está dentro de la matriz y no ha sido visitada."""
        return 0 <= fila < len(self.matriz) and 0 <= col < len(self.matriz[0]) and (fila, col) not in ruta

# Matriz de recompensas (valores más altos = mejor recompensa)
matriz_recompensas = np.array([
    [3, 2, 4, 1, 5],
    [1, 5, 2, 8, 3],
    [4, 3, 6, 2, 4],
    [2, 8, 3, 7, 1],
    [3, 6, 5, 2, 9]
])

inicio = (0, 0)  # Posición inicial
meta = (4, 4)  # Destino

# Crear y ejecutar el agente de selección de rutas
agente = AgenteSeleccionRutas(matriz_recompensas, inicio, meta)
mejor_ruta = agente.buscar_mejor_ruta()
