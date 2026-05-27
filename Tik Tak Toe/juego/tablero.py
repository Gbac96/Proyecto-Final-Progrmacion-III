# -*- coding: utf-8 -*-
"""
Implementación del Tablero de Tic Tac Toe
Incluye validación de movimientos y detección de victoria
"""

import config


class Tablero:
    """Tablero de 3x3 para el juego de Tic Tac Toe"""
    
    def __init__(self):
        """Inicializar tablero vacío"""
        # Crear tablero 3x3 sin usar matriz de Python
        self.celdas = [config.VACIO] * 9  # Usamos lista simple como array
        self.movimientos_realizados = 0
    
    def realizar_movimiento(self, posicion, jugador):
        """
        Realizar un movimiento en el tablero
        posicion: 0-8 (fila*3 + columna)
        jugador: config.JUGADOR_X o config.JUGADOR_O
        Retorna True si el movimiento es válido, False si no
        """
        if posicion < 0 or posicion > 8:
            return False
        
        if self.celdas[posicion] != config.VACIO:
            return False
        
        self.celdas[posicion] = jugador
        self.movimientos_realizados += 1
        return True
    
    def deshacer_movimiento(self, posicion):
        """Deshacer un movimiento (útil para simulaciones)"""
        if posicion < 0 or posicion > 8:
            return False
        
        if self.celdas[posicion] == config.VACIO:
            return False
        
        self.celdas[posicion] = config.VACIO
        self.movimientos_realizados -= 1
        return True
    
    def obtener_movimientos_disponibles(self):
        """Obtener lista de posiciones disponibles"""
        disponibles = []
        for i in range(9):
            if self.celdas[i] == config.VACIO:
                disponibles.append(i)
        return disponibles
    
    def esta_lleno(self):
        """Verificar si el tablero está lleno"""
        return self.movimientos_realizados >= 9
    
    def verificar_victoria(self, jugador):
        """
        Verificar si un jugador ha ganado
        Retorna True si el jugador tiene 3 en línea
        """
        # Combinaciones ganadoras (filas, columnas, diagonales)
        combinaciones = [
            [0, 1, 2],  # Fila 1
            [3, 4, 5],  # Fila 2
            [6, 7, 8],  # Fila 3
            [0, 3, 6],  # Columna 1
            [1, 4, 7],  # Columna 2
            [2, 5, 8],  # Columna 3
            [0, 4, 8],  # Diagonal principal
            [2, 4, 6]   # Diagonal secundaria
        ]
        
        for combo in combinaciones:
            if (self.celdas[combo[0]] == jugador and 
                self.celdas[combo[1]] == jugador and 
                self.celdas[combo[2]] == jugador):
                return True
        
        return False
    
    def obtener_ganador(self):
        """
        Obtener el ganador del juego
        Retorna: config.JUGADOR_X, config.JUGADOR_O, 0 (empate), o None (juego en curso)
        """
        if self.verificar_victoria(config.JUGADOR_X):
            return config.JUGADOR_X
        
        if self.verificar_victoria(config.JUGADOR_O):
            return config.JUGADOR_O
        
        if self.esta_lleno():
            return 0  # Empate
        
        return None  # Juego en curso
    
    def obtener_estado_tupla(self):
        """
        Obtener el estado del tablero como tupla (para usar como clave en diccionario)
        """
        return tuple(self.celdas)
    
    def establecer_desde_tupla(self, estado):
        """Establecer el tablero desde una tupla de estado"""
        self.celdas = list(estado)
        self.movimientos_realizados = sum(1 for c in self.celdas if c != config.VACIO)
    
    def copiar(self):
        """Crear una copia del tablero"""
        nuevo_tablero = Tablero()
        nuevo_tablero.celdas = self.celdas[:]
        nuevo_tablero.movimientos_realizados = self.movimientos_realizados
        return nuevo_tablero
    
    def obtener_celda(self, posicion):
        """Obtener el valor de una celda específica"""
        if posicion < 0 or posicion > 8:
            return None
        return self.celdas[posicion]
    
    def limpiar(self):
        """Limpiar el tablero"""
        self.celdas = [config.VACIO] * 9
        self.movimientos_realizados = 0
    
    def __str__(self):
        """Representación en string del tablero"""
        simbolos = {
            config.VACIO: config.SIMBOLO_VACIO,
            config.JUGADOR_X: config.SIMBOLO_X,
            config.JUGADOR_O: config.SIMBOLO_O
        }
        
        lineas = []
        for fila in range(3):
            inicio = fila * 3
            celdas_fila = [simbolos[self.celdas[i]] for i in range(inicio, inicio + 3)]
            lineas.append(" | ".join(celdas_fila))
        
        return "\n---------\n".join(lineas)
