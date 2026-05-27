# -*- coding: utf-8 -*-
"""
Exportador de estructuras de datos a formato Graphviz (.dot)
"""

import os
import config


class GraphvizExporter:
    """Clase para exportar estructuras a formato Graphviz"""
    
    def __init__(self):
        """Inicializar exportador"""
        # Crear carpeta de visualizaciones si no existe
        if not os.path.exists(config.CARPETA_VISUALIZACIONES):
            os.makedirs(config.CARPETA_VISUALIZACIONES)
    
    def exportar_arbol_movimientos(self, gestor_movimientos, id_partida):
        """
        Exportar el árbol de movimientos con pesos a formato .dot
        gestor_movimientos: instancia de GestorMovimientos
        id_partida: ID de la partida para nombrar el archivo
        """
        nombre_archivo = os.path.join(
            config.CARPETA_VISUALIZACIONES,
            f"movimientos_partida_{id_partida}.dot"
        )
        
        try:
            with open(nombre_archivo, 'w', encoding='utf-8') as f:
                f.write("digraph MovimientosConPesos {\n")
                f.write("    rankdir=TB;\n")
                f.write("    node [shape=box, style=rounded];\n\n")
                
                # Contador para nodos únicos
                contador_nodos = 0
                estado_a_nodo = {}
                
                # Iterar sobre todos los estados
                for estado_tupla, movimientos in gestor_movimientos.estados_movimientos.items():
                    if movimientos.obtener_tamano() == 0:
                        continue
                    
                    # Crear nodo para el estado si no existe
                    if estado_tupla not in estado_a_nodo:
                        estado_a_nodo[estado_tupla] = f"estado_{contador_nodos}"
                        contador_nodos += 1
                        
                        # Formatear estado para visualización
                        estado_visual = self._formatear_estado(estado_tupla)
                        f.write(f'    {estado_a_nodo[estado_tupla]} [label="{estado_visual}"];\n')
                    
                    # Agregar movimientos con pesos
                    for i in range(movimientos.obtener_tamano()):
                        mov = movimientos.obtener(i)
                        
                        # Simular el estado resultante (simplificado)
                        nuevo_estado = list(estado_tupla)
                        nuevo_estado[mov.posicion] = config.JUGADOR_O
                        nuevo_estado_tupla = tuple(nuevo_estado)
                        
                        # Crear nodo destino si no existe
                        if nuevo_estado_tupla not in estado_a_nodo:
                            estado_a_nodo[nuevo_estado_tupla] = f"estado_{contador_nodos}"
                            contador_nodos += 1
                            estado_visual = self._formatear_estado(nuevo_estado_tupla)
                            f.write(f'    {estado_a_nodo[nuevo_estado_tupla]} [label="{estado_visual}"];\n')
                        
                        # Crear arista con peso
                        color = self._obtener_color_peso(mov.peso)
                        f.write(f'    {estado_a_nodo[estado_tupla]} -> {estado_a_nodo[nuevo_estado_tupla]} ')
                        f.write(f'[label="Pos {mov.posicion}\\nPeso: {mov.peso:.2f}", color="{color}", penwidth=2.0];\n')
                
                f.write("}\n")
            
            return nombre_archivo
        except Exception as e:
            print(f"Error al exportar árbol de movimientos: {e}")
            return None
    
    def exportar_arbol_b(self, gestor_historial, nombre_base="historial"):
        """
        Exportar el árbol B del historial a formato .dot
        gestor_historial: instancia de GestorHistorial
        """
        nombre_archivo = os.path.join(
            config.CARPETA_VISUALIZACIONES,
            f"{nombre_base}.dot"
        )
        
        try:
            with open(nombre_archivo, 'w', encoding='utf-8') as f:
                f.write("digraph ArbolB {\n")
                f.write("    rankdir=TB;\n")
                f.write("    node [shape=record];\n\n")
                
                if gestor_historial.arbol.raiz is not None:
                    self._exportar_nodo_arbol_b(f, gestor_historial.arbol.raiz, 0)
                
                f.write("}\n")
            
            return nombre_archivo
        except Exception as e:
            print(f"Error al exportar árbol B: {e}")
            return None
    
    def _exportar_nodo_arbol_b(self, archivo, nodo, id_nodo, padre_id=None, contador=[0]):
        """
        Exportar un nodo del árbol B recursivamente
        """
        nodo_actual = f"nodo_{id_nodo}"
        
        # Construir label del nodo con todas sus claves
        claves_texto = []
        for i in range(nodo.obtener_num_claves()):
            clave = nodo.obtener_clave(i)
            valor = nodo.obtener_valor(i)
            resultado_corto = "X" if valor.ganador == config.JUGADOR_X else ("O" if valor.ganador == config.JUGADOR_O else "E")
            claves_texto.append(f"ID:{clave}({resultado_corto})")
        
        label = "|".join([f"<f{i}> {claves_texto[i]}" for i in range(len(claves_texto))])
        
        color = "lightblue" if nodo.es_hoja else "lightgreen"
        archivo.write(f'    {nodo_actual} [label="{label}", fillcolor={color}, style=filled];\n')
        
        # Si tiene padre, crear arista
        if padre_id is not None:
            archivo.write(f'    nodo_{padre_id} -> {nodo_actual};\n')
        
        # Exportar hijos recursivamente
        if not nodo.es_hoja:
            for i in range(nodo.hijos.obtener_tamano()):
                hijo = nodo.obtener_hijo(i)
                if hijo is not None:
                    contador[0] += 1
                    self._exportar_nodo_arbol_b(archivo, hijo, contador[0], id_nodo, contador)
    
    def _formatear_estado(self, estado_tupla):
        """Formatear un estado del tablero para visualización"""
        simbolos = {
            config.VACIO: "_",
            config.JUGADOR_X: "X",
            config.JUGADOR_O: "O"
        }
        
        lineas = []
        for fila in range(3):
            inicio = fila * 3
            celdas = [simbolos[estado_tupla[i]] for i in range(inicio, inicio + 3)]
            lineas.append(" ".join(celdas))
        
        return "\\n".join(lineas)
    
    def _obtener_color_peso(self, peso):
        """Obtener color según el valor del peso"""
        if peso >= 2.0:
            return "green"
        elif peso >= 1.0:
            return "blue"
        elif peso >= 0.5:
            return "orange"
        else:
            return "red"
    
    def generar_reporte_visualizacion(self, gestor_movimientos, gestor_historial):
        """
        Generar un reporte con estadísticas de las visualizaciones
        """
        nombre_archivo = os.path.join(
            config.CARPETA_VISUALIZACIONES,
            "reporte.txt"
        )
        
        try:
            with open(nombre_archivo, 'w', encoding='utf-8') as f:
                f.write("=" * 60 + "\n")
                f.write("REPORTE DE VISUALIZACIONES\n")
                f.write("=" * 60 + "\n\n")
                
                # Estadísticas de movimientos
                stats_mov = gestor_movimientos.obtener_estadisticas()
                f.write("ESTADÍSTICAS DE MOVIMIENTOS:\n")
                f.write(f"  - Estados únicos visitados: {stats_mov['num_estados']}\n")
                f.write(f"  - Total de movimientos registrados: {stats_mov['total_movimientos']}\n")
                f.write(f"  - Promedio movimientos por estado: {stats_mov['promedio_movimientos_por_estado']:.2f}\n\n")
                
                # Estadísticas de historial
                stats_hist = gestor_historial.obtener_estadisticas()
                f.write("ESTADÍSTICAS DE HISTORIAL:\n")
                f.write(f"  - Total de partidas: {stats_hist['total_partidas']}\n")
                f.write(f"  - Victorias Jugador X: {stats_hist['victorias_x']} ({stats_hist['porcentaje_victorias_x']:.1f}%)\n")
                f.write(f"  - Victorias IA (O): {stats_hist['victorias_o']} ({stats_hist['porcentaje_victorias_o']:.1f}%)\n")
                f.write(f"  - Empates: {stats_hist['empates']} ({stats_hist['porcentaje_empates']:.1f}%)\n")
                f.write(f"  - Partidas manuales: {stats_hist['partidas_manuales']}\n")
                f.write(f"  - Partidas entrenamiento: {stats_hist['partidas_entrenamiento']}\n\n")
                
                f.write("ARCHIVOS GENERADOS:\n")
                f.write(f"  - Carpeta: {config.CARPETA_VISUALIZACIONES}\n")
                f.write("  - Archivos .dot pueden ser convertidos a imágenes usando:\n")
                f.write("    dot -Tpng archivo.dot -o archivo.png\n\n")
                
                f.write("=" * 60 + "\n")
            
            return nombre_archivo
        except Exception as e:
            print(f"Error al generar reporte: {e}")
            return None
