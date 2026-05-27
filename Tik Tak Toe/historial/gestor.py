# -*- coding: utf-8 -*-
"""
Gestor de Historial usando Árbol B
"""

import config
from estructuras.arbol_b import ArbolB
from historial.partida import Partida


class GestorHistorial:
    """
    Gestiona el historial de partidas usando un Árbol B
    """
    
    def __init__(self, grado=None):
        """
        Inicializar gestor de historial
        grado: grado del árbol B (usa config.GRADO_ARBOL_B por defecto)
        """
        if grado is None:
            grado = config.GRADO_ARBOL_B
        
        self.arbol = ArbolB(grado=grado)
        self.contador_partidas = 0
    
    def registrar_partida(self, ganador, estado_tablero, es_entrenamiento=False):
        """
        Registrar una nueva partida en el historial
        Retorna el ID de la partida registrada
        """
        self.contador_partidas += 1
        partida = Partida(self.contador_partidas, ganador, estado_tablero, es_entrenamiento)
        
        self.arbol.insertar(self.contador_partidas, partida)
        
        return self.contador_partidas
    
    def buscar_partida(self, id_partida):
        """
        Buscar una partida por su ID
        Retorna objeto Partida o None si no existe
        """
        return self.arbol.buscar(id_partida)
    
    def obtener_todas_partidas(self):
        """
        Obtener todas las partidas en orden
        Retorna ListaEnlazada de objetos Partida
        """
        return self.arbol.obtener_todas_partidas()
    
    def obtener_num_partidas(self):
        """Obtener número total de partidas registradas"""
        return self.arbol.obtener_num_partidas()
    
    def obtener_estadisticas(self):
        """Obtener estadísticas del historial"""
        todas = self.obtener_todas_partidas()
        
        victorias_x = 0
        victorias_o = 0
        empates = 0
        entrenamientos = 0
        manuales = 0
        
        for i in range(todas.obtener_tamano()):
            partida = todas.obtener(i)
            
            if partida.ganador == config.JUGADOR_X:
                victorias_x += 1
            elif partida.ganador == config.JUGADOR_O:
                victorias_o += 1
            else:
                empates += 1
            
            if partida.es_entrenamiento:
                entrenamientos += 1
            else:
                manuales += 1
        
        total = todas.obtener_tamano()
        
        return {
            'total_partidas': total,
            'victorias_x': victorias_x,
            'victorias_o': victorias_o,
            'empates': empates,
            'partidas_entrenamiento': entrenamientos,
            'partidas_manuales': manuales,
            'porcentaje_victorias_x': victorias_x / total * 100 if total > 0 else 0,
            'porcentaje_victorias_o': victorias_o / total * 100 if total > 0 else 0,
            'porcentaje_empates': empates / total * 100 if total > 0 else 0
        }
    
    def limpiar(self):
        """Limpiar todo el historial"""
        self.arbol.limpiar()
        self.contador_partidas = 0
