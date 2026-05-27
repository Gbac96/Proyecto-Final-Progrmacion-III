# -*- coding: utf-8 -*-
"""
Sistema de movimientos con pesos para aprendizaje supervisado
Almacena estados del juego y sus pesos asociados
"""

import config
from estructuras.lista_enlazada import ListaEnlazada


class MovimientoConPeso:
    """Representa un movimiento con su peso asociado"""
    
    def __init__(self, posicion, peso=None):
        self.posicion = posicion
        self.peso = peso if peso is not None else config.PESO_INICIAL
    
    def ajustar_peso(self, ajuste):
        """Ajustar el peso del movimiento"""
        self.peso += ajuste
        # Evitar pesos negativos muy bajos
        if self.peso < 0.1:
            self.peso = 0.1
    
    def __str__(self):
        return f"Mov({self.posicion}, peso={self.peso:.2f})"


class GestorMovimientos:
    """
    Gestor de movimientos con pesos
    Almacena estados del juego y los movimientos posibles desde cada estado
    """
    
    def __init__(self):
        # Diccionario simple de Python para estados (permitido para estructuras internas simples)
        # Clave: tupla de estado del tablero
        # Valor: ListaEnlazada de MovimientoConPeso
        self.estados_movimientos = {}
        self.num_estados = 0
    
    def obtener_movimientos(self, estado_tablero):
        """
        Obtener los movimientos disponibles para un estado del tablero
        Retorna una ListaEnlazada de MovimientoConPeso
        """
        estado_tupla = tuple(estado_tablero)
        
        if estado_tupla not in self.estados_movimientos:
            # Crear nueva lista de movimientos para este estado
            self.estados_movimientos[estado_tupla] = ListaEnlazada()
            self.num_estados += 1
        
        return self.estados_movimientos[estado_tupla]
    
    def registrar_movimiento(self, estado_tablero, posicion, peso=None):
        """
        Registrar un movimiento para un estado específico
        Si el movimiento ya existe, no hace nada
        """
        movimientos = self.obtener_movimientos(estado_tablero)
        
        # Verificar si el movimiento ya existe
        for i in range(movimientos.obtener_tamano()):
            mov = movimientos.obtener(i)
            if mov.posicion == posicion:
                return mov
        
        # Agregar nuevo movimiento
        nuevo_mov = MovimientoConPeso(posicion, peso)
        movimientos.agregar(nuevo_mov)
        return nuevo_mov
    
    def actualizar_peso_movimiento(self, estado_tablero, posicion, ajuste):
        """
        Actualizar el peso de un movimiento específico
        """
        movimientos = self.obtener_movimientos(estado_tablero)
        
        for i in range(movimientos.obtener_tamano()):
            mov = movimientos.obtener(i)
            if mov.posicion == posicion:
                mov.ajustar_peso(ajuste)
                return True
        
        return False
    
    def obtener_mejor_movimiento(self, estado_tablero, posiciones_disponibles):
        """
        Obtener el mejor movimiento (mayor peso) entre las posiciones disponibles
        Si no hay movimientos registrados, retorna el primero disponible
        """
        movimientos = self.obtener_movimientos(estado_tablero)
        
        # Si no hay movimientos registrados para este estado, registrar todos los disponibles
        if movimientos.obtener_tamano() == 0:
            for pos in posiciones_disponibles:
                self.registrar_movimiento(estado_tablero, pos)
            movimientos = self.obtener_movimientos(estado_tablero)
        
        # Encontrar el movimiento con mayor peso entre los disponibles
        mejor_movimiento = None
        mejor_peso = -999999
        
        for i in range(movimientos.obtener_tamano()):
            mov = movimientos.obtener(i)
            if mov.posicion in posiciones_disponibles:
                if mov.peso > mejor_peso:
                    mejor_peso = mov.peso
                    mejor_movimiento = mov.posicion
        
        return mejor_movimiento if mejor_movimiento is not None else posiciones_disponibles[0]
    
    def ajustar_pesos_secuencia(self, secuencia_movimientos, ajuste):
        """
        Ajustar los pesos de una secuencia completa de movimientos
        secuencia_movimientos: lista de tuplas (estado_tablero, posicion)
        """
        for estado, posicion in secuencia_movimientos:
            self.actualizar_peso_movimiento(estado, posicion, ajuste)
    
    def obtener_num_estados(self):
        """Obtener el número de estados únicos visitados"""
        return self.num_estados
    
    def limpiar(self):
        """Limpiar todos los estados y reiniciar"""
        self.estados_movimientos = {}
        self.num_estados = 0
    
    def obtener_estadisticas(self):
        """Obtener estadísticas del gestor de movimientos"""
        total_movimientos = 0
        for estado in self.estados_movimientos:
            movimientos = self.estados_movimientos[estado]
            total_movimientos += movimientos.obtener_tamano()
        
        return {
            'num_estados': self.num_estados,
            'total_movimientos': total_movimientos,
            'promedio_movimientos_por_estado': total_movimientos / self.num_estados if self.num_estados > 0 else 0
        }
