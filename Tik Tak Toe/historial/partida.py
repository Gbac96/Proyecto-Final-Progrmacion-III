# -*- coding: utf-8 -*-
"""
Clase Partida para representar una partida individual
"""

from datetime import datetime
import config


class Partida:
    """Representa una partida jugada"""
    
    def __init__(self, id_partida, ganador, estado_tablero, es_entrenamiento=False):
        """
        Inicializar partida
        id_partida: identificador único de la partida
        ganador: config.JUGADOR_X, config.JUGADOR_O, o 0 (empate)
        estado_tablero: estado final del tablero (lista de 9 elementos)
        es_entrenamiento: True si es partida de entrenamiento automático
        """
        self.id_partida = id_partida
        self.ganador = ganador
        self.estado_tablero = estado_tablero[:]  # Copiar estado
        self.es_entrenamiento = es_entrenamiento
        self.timestamp = datetime.now()
    
    def obtener_resultado_texto(self):
        """Obtener el resultado como texto"""
        if self.ganador == config.JUGADOR_X:
            return "Victoria Jugador X"
        elif self.ganador == config.JUGADOR_O:
            return "Victoria IA (O)"
        else:
            return "Empate"
    
    def obtener_resumen(self):
        """Obtener resumen breve de la partida"""
        tipo = "Entrenamiento" if self.es_entrenamiento else "Manual"
        resultado = self.obtener_resultado_texto()
        fecha = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        return f"ID: {self.id_partida} | {tipo} | {resultado} | {fecha}"
    
    def obtener_tablero_visual(self):
        """Obtener representación visual del tablero final"""
        simbolos = {
            config.VACIO: config.SIMBOLO_VACIO,
            config.JUGADOR_X: config.SIMBOLO_X,
            config.JUGADOR_O: config.SIMBOLO_O
        }
        
        lineas = []
        for fila in range(3):
            inicio = fila * 3
            celdas_fila = [simbolos[self.estado_tablero[i]] for i in range(inicio, inicio + 3)]
            lineas.append(" | ".join(celdas_fila))
        
        return "\n---------\n".join(lineas)
    
    def __str__(self):
        return self.obtener_resumen()
