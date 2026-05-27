# -*- coding: utf-8 -*-
"""
Ventana de Créditos
"""

import tkinter as tk
from tkinter import messagebox


class VentanaCreditos:
    """Ventana para mostrar créditos del equipo"""
    
    def __init__(self, root):
        """
        Inicializar ventana de créditos
        root: ventana raíz de Tkinter
        """
        self.root = root
    
    def mostrar(self):
        """Mostrar la ventana de créditos"""
        # Crear ventana emergente
        ventana = tk.Toplevel(self.root)
        ventana.title("Créditos")
        ventana.geometry("500x400")
        ventana.config(bg="#34495e")
        ventana.resizable(False, False)
        
        # Centrar ventana
        ventana.transient(self.root)
        ventana.grab_set()
        
        # Título
        titulo = tk.Label(
            ventana,
            text="Créditos del Proyecto",
            font=("Arial", 20, "bold"),
            bg="#34495e",
            fg="white",
            pady=20
        )
        titulo.pack()
        
        # Frame de información
        frame_info = tk.Frame(ventana, bg="#2c3e50", relief=tk.RAISED, bd=2)
        frame_info.pack(padx=30, pady=20, fill=tk.BOTH, expand=True)
        
        # Información del proyecto
        info_proyecto = tk.Label(
            frame_info,
            text="TIC TAC TOE CON APRENDIZAJE SUPERVISADO",
            font=("Arial", 12, "bold"),
            bg="#2c3e50",
            fg="#3498db"
        )
        info_proyecto.pack(pady=10)
        
        # Separador
        separador1 = tk.Frame(frame_info, height=2, bg="#3498db")
        separador1.pack(fill=tk.X, padx=50, pady=10)
        
        # Integrantes del grupo
        label_integrantes = tk.Label(
            frame_info,
            text="Integrantes del Grupo:",
            font=("Arial", 11, "bold"),
            bg="#2c3e50",
            fg="white"
        )
        label_integrantes.pack(pady=5)
        
        # Lista de integrantes
        integrantes = [
            ("Nelson Ramirez", "9490-23-17-12237", "100%"),
            ("Moises Galicia", "9490-23-9112", "100%"),
            ("Gerson Bac",  "9490-17-22584","100% ")
        ]
        
        frame_integrantes = tk.Frame(frame_info, bg="#2c3e50")
        frame_integrantes.pack(pady=10)
        
        for nombre, carnet, participacion in integrantes:
            texto = f"{nombre} - Carnet: {carnet} - {participacion}"
            label = tk.Label(
                frame_integrantes,
                text=texto,
                font=("Arial", 10),
                bg="#2c3e50",
                fg="white"
            )
            label.pack(pady=3)
        
        # Separador
        separador2 = tk.Frame(frame_info, height=2, bg="#3498db")
        separador2.pack(fill=tk.X, padx=50, pady=10)
        
        # Sección
        seccion = tk.Label(
            frame_info,
            text="Sección: A",
            font=("Arial", 11),
            bg="#2c3e50",
            fg="white"
        )
        seccion.pack(pady=5)
        
        # Curso
        curso = tk.Label(
            frame_info,
            text="Programación III - 2026",
            font=("Arial", 10, "italic"),
            bg="#2c3e50",
            fg="#95a5a6"
        )
        curso.pack(pady=5)
        
        # Botón cerrar
        btn_cerrar = tk.Button(
            ventana,
            text="Cerrar",
            font=("Arial", 11),
            command=ventana.destroy,
            bg="#3498db",
            fg="white",
            padx=30,
            pady=8
        )
        btn_cerrar.pack(pady=15)


def mostrar_estadisticas(root, gestor_juego):
    """Función auxiliar para mostrar estadísticas generales"""
    stats_ia = gestor_juego.ia.obtener_estadisticas()
    stats_hist = gestor_juego.gestor_historial.obtener_estadisticas()
    stats_mov = gestor_juego.gestor_movimientos.obtener_estadisticas()
    
    mensaje = "ESTADÍSTICAS GENERALES\n"
    mensaje += "=" * 40 + "\n\n"
    
    mensaje += "HISTORIAL DE PARTIDAS:\n"
    mensaje += f"  Total: {stats_hist['total_partidas']}\n"
    mensaje += f"  Victorias Jugador X: {stats_hist['victorias_x']} ({stats_hist['porcentaje_victorias_x']:.1f}%)\n"
    mensaje += f"  Victorias IA (O): {stats_hist['victorias_o']} ({stats_hist['porcentaje_victorias_o']:.1f}%)\n"
    mensaje += f"  Empates: {stats_hist['empates']} ({stats_hist['porcentaje_empates']:.1f}%)\n"
    mensaje += f"  Manuales: {stats_hist['partidas_manuales']}\n"
    mensaje += f"  Entrenamiento: {stats_hist['partidas_entrenamiento']}\n\n"
    
    mensaje += "RENDIMIENTO DE LA IA:\n"
    mensaje += f"  Partidas jugadas: {stats_ia['partidas_jugadas']}\n"
    mensaje += f"  Victorias: {stats_ia['victorias']} ({stats_ia['tasa_victoria']:.1f}%)\n"
    mensaje += f"  Derrotas: {stats_ia['derrotas']} ({stats_ia['tasa_derrota']:.1f}%)\n"
    mensaje += f"  Empates: {stats_ia['empates']} ({stats_ia['tasa_empate']:.1f}%)\n\n"
    
    mensaje += "APRENDIZAJE:\n"
    mensaje += f"  Estados únicos aprendidos: {stats_mov['num_estados']}\n"
    mensaje += f"  Total movimientos registrados: {stats_mov['total_movimientos']}\n"
    mensaje += f"  Promedio por estado: {stats_mov['promedio_movimientos_por_estado']:.2f}\n"
    
    messagebox.showinfo("Estadísticas", mensaje)
