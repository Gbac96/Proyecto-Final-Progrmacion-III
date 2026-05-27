# -*- coding: utf-8 -*-
"""
Implementación de la IA con aprendizaje supervisado
Aprende ajustando pesos según resultados de partidas
"""

import config
from juego.tablero import Tablero
from juego.movimientos import GestorMovimientos
import random


class IA:
    """
    Inteligencia Artificial que aprende mediante ajuste de pesos
    """
    
    def __init__(self, gestor_movimientos):
        """
        Inicializar IA
        gestor_movimientos: instancia de GestorMovimientos compartida
        """
        self.gestor_movimientos = gestor_movimientos
        self.jugador = config.JUGADOR_O
        self.secuencia_actual = []  # Lista de (estado, movimiento) de la partida actual
        self.partidas_jugadas = 0
        self.victorias = 0
        self.derrotas = 0
        self.empates = 0
    
    def seleccionar_movimiento(self, tablero, aleatorio=False):
        """
        Seleccionar el mejor movimiento para el estado actual del tablero
        Si aleatorio=True, selecciona aleatoriamente (útil para exploración inicial)
        """
        posiciones_disponibles = tablero.obtener_movimientos_disponibles()
        
        if not posiciones_disponibles:
            return None
        
        # Modo aleatorio para exploración
        if aleatorio:
            return random.choice(posiciones_disponibles)
        
        # Modo inteligente: usar pesos
        estado_actual = tablero.obtener_estado_tupla()
        mejor_posicion = self.gestor_movimientos.obtener_mejor_movimiento(
            estado_actual, posiciones_disponibles
        )
        
        return mejor_posicion
    
    def registrar_movimiento(self, tablero, posicion):
        """
        Registrar un movimiento realizado en la secuencia actual
        """
        estado = tablero.obtener_estado_tupla()
        self.secuencia_actual.append((estado, posicion))
        
        # Asegurar que el movimiento esté registrado en el gestor
        self.gestor_movimientos.registrar_movimiento(estado, posicion)
    
    def finalizar_partida(self, resultado):
        """
        Finalizar partida y ajustar pesos según el resultado
        resultado: config.JUGADOR_X (derrota), config.JUGADOR_O (victoria), 0 (empate)
        """
        self.partidas_jugadas += 1
        
        if resultado == config.JUGADOR_O:
            # Victoria de la IA
            self.victorias += 1
            ajuste = config.AJUSTE_VICTORIA
        elif resultado == config.JUGADOR_X:
            # Derrota de la IA
            self.derrotas += 1
            ajuste = config.AJUSTE_DERROTA
        else:
            # Empate
            self.empates += 1
            ajuste = config.AJUSTE_EMPATE
        
        # Ajustar pesos de toda la secuencia
        self.gestor_movimientos.ajustar_pesos_secuencia(self.secuencia_actual, ajuste)
        
        # Limpiar secuencia para la próxima partida
        self.secuencia_actual = []
    
    def reiniciar_estadisticas(self):
        """Reiniciar estadísticas de partidas"""
        self.partidas_jugadas = 0
        self.victorias = 0
        self.derrotas = 0
        self.empates = 0
    
    def obtener_estadisticas(self):
        """Obtener estadísticas de la IA"""
        return {
            'partidas_jugadas': self.partidas_jugadas,
            'victorias': self.victorias,
            'derrotas': self.derrotas,
            'empates': self.empates,
            'tasa_victoria': self.victorias / self.partidas_jugadas * 100 if self.partidas_jugadas > 0 else 0,
            'tasa_derrota': self.derrotas / self.partidas_jugadas * 100 if self.partidas_jugadas > 0 else 0,
            'tasa_empate': self.empates / self.partidas_jugadas * 100 if self.partidas_jugadas > 0 else 0
        }


class Entrenador:
    """
    Clase para entrenar la IA automáticamente mediante simulación de partidas
    """
    
    def __init__(self, ia):
        """
        Inicializar entrenador
        ia: instancia de IA a entrenar
        """
        self.ia = ia
    
    def entrenar_automatico(self, num_partidas, callback_progreso=None):
        """
        Entrenar la IA mediante simulación de partidas
        num_partidas: número de partidas a simular
        callback_progreso: función opcional para reportar progreso (recibe i, resultado)
        """
        resultados = []
        
        for i in range(num_partidas):
            resultado = self._simular_partida()
            resultados.append(resultado)
            
            if callback_progreso:
                callback_progreso(i + 1, resultado)
        
        return resultados
    
    def _simular_partida(self):
        """
        Simular una partida completa entre la IA y un oponente aleatorio
        """
        tablero = Tablero()
        turno = config.JUGADOR_X  # El humano (oponente aleatorio) empieza
        
        while True:
            if turno == config.JUGADOR_X:
                # Turno del oponente (aleatorio)
                posiciones = tablero.obtener_movimientos_disponibles()
                if not posiciones:
                    break
                posicion = random.choice(posiciones)
                tablero.realizar_movimiento(posicion, config.JUGADOR_X)
            else:
                # Turno de la IA
                posicion = self.ia.seleccionar_movimiento(tablero)
                if posicion is None:
                    break
                
                # Registrar movimiento antes de realizarlo
                self.ia.registrar_movimiento(tablero, posicion)
                tablero.realizar_movimiento(posicion, config.JUGADOR_O)
            
            # Verificar fin del juego
            ganador = tablero.obtener_ganador()
            if ganador is not None:
                self.ia.finalizar_partida(ganador)
                return ganador
            
            # Cambiar turno
            turno = config.JUGADOR_O if turno == config.JUGADOR_X else config.JUGADOR_X
        
        # Si llegamos aquí, es empate
        self.ia.finalizar_partida(0)
        return 0
