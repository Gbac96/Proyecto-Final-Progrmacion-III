# -*- coding: utf-8 -*-
"""
Archivo de configuración global del proyecto
Tic Tac Toe con Aprendizaje Supervisado
"""

# Configuración del Árbol B
GRADO_ARBOL_B = 5  # Grado del árbol B (mínimo 4-5 claves por nodo)

# Configuración del sistema de aprendizaje
PESO_INICIAL = 1.0  # Peso inicial para todos los movimientos
AJUSTE_VICTORIA = 1.0  # Incremento de peso cuando la IA gana
AJUSTE_DERROTA = -0.5  # Decremento de peso cuando la IA pierde
AJUSTE_EMPATE = 0.2  # Pequeño incremento en empates

# Representación del tablero
VACIO = 0
JUGADOR_X = 1  # Humano
JUGADOR_O = 2  # IA

# Símbolos para visualización
SIMBOLO_VACIO = " "
SIMBOLO_X = "X"
SIMBOLO_O = "O"

# Configuración de interfaz
TAMANO_CELDA = 100  # Tamaño en píxeles de cada celda del tablero
COLOR_X = "#3498db"  # Azul para X
COLOR_O = "#e74c3c"  # Rojo para O
COLOR_VACIO = "#ecf0f1"  # Gris claro para vacío
COLOR_FONDO = "#2c3e50"  # Fondo oscuro

# Configuración de visualización Graphviz
CARPETA_VISUALIZACIONES = "visualizaciones"
EXPORTAR_CADA_N_PARTIDAS = 1  # Exportar árbol B cada N partidas
