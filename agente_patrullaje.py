import random
import time

class AgentePatrullaje:
    def __init__(self, ruta):
        self.ruta = ruta  # Lista de posiciones [(x, y)]
        self.posicion_actual = 0  # Índice en la ruta
        self.direccion = 1  # 1 = Avanza, -1 = Retrocede
    
    def detectar_obstaculo(self):
        """ Simula la detección de un obstáculo con un 20% de probabilidad. """
        return random.random() < 0.2

    def patrullar(self):
        """ Realiza el patrullaje siguiendo la ruta. """
        while True:
            posicion = self.ruta[self.posicion_actual]
            print(f"Agente en posición: {posicion}")

            if self.detectar_obstaculo():
                print("⚠️ Obstáculo detectado. Cambiando dirección.")
                self.direccion = random.choice([-1, 1])

            self.posicion_actual += self.direccion

            # Evitar salir del rango de la ruta
            if self.posicion_actual >= len(self.ruta):
                self.posicion_actual = len(self.ruta) - 2
                self.direccion = -1
            elif self.posicion_actual < 0:
                self.posicion_actual = 1
                self.direccion = 1
            
            time.sleep(1) 

# Definir una ruta de patrullaje
ruta_definida = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0)]

# Crear y ejecutar el agente de patrullaje
agente = AgentePatrullaje(ruta_definida)
agente.patrullar()