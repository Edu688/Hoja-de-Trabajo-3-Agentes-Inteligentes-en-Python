import random
import time

class AgenteExplorador:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.posicion_actual = (0, 0)  # Comienza en la esquina superior izquierda
        self.visitados = set()  # Almacena posiciones visitadas
        self.direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Derecha, Abajo, Izquierda, Arriba

    def moverse(self):
        """Elige una dirección no visitada y mueve al agente."""
        random.shuffle(self.direcciones)  # Mezcla direcciones para exploración aleatoria
        for dx, dy in self.direcciones:
            nueva_pos = (self.posicion_actual[0] + dx, self.posicion_actual[1] + dy)
            if self.es_valido(nueva_pos):
                self.posicion_actual = nueva_pos
                self.visitados.add(nueva_pos)
                return nueva_pos
        return None  

    def es_valido(self, posicion):
        """Verifica si la posición está dentro de los límites y no ha sido visitada."""
        x, y = posicion
        return 0 <= x < self.filas and 0 <= y < self.columnas and posicion not in self.visitados

    def explorar(self):
        """Ejecuta el proceso de exploración de la cuadrícula."""
        self.visitados.add(self.posicion_actual)
        while True:
            print(f"Agente en: {self.posicion_actual}")
            if not self.moverse():
                print("✔️ Exploración completada. No hay más movimientos posibles.")
                break
            time.sleep(1)  # Simula el tiempo entre movimientos

# Configuración del entorno de 5x5
filas, columnas = 5, 5

# Crear y ejecutar el agente explorador
agente = AgenteExplorador(filas, columnas)
agente.explorar()
