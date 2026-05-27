# -*- coding: utf-8 -*-
"""
Menú Principal de la aplicación
"""

import tkinter as tk
from tkinter import ttk
import config


class MenuPrincipal:
    """Ventana principal del menú"""
    
    def __init__(self, root, gestor_juego):
        """
        Inicializar menú principal
        root: ventana raíz de Tkinter
        gestor_juego: instancia del gestor de juego principal
        """
        self.root = root
        self.gestor_juego = gestor_juego
        self.ventana = None
    
    def mostrar(self):
        """Mostrar el menú principal"""
        # Limpiar ventana
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Título
        titulo = tk.Label(
            self.root,
            text="TIC TAC TOE\ncon Aprendizaje Supervisado",
            font=("Arial", 24, "bold"),
            bg="#34495e",
            fg="white",
            pady=20
        )
        titulo.pack(fill=tk.X)
        
        # Frame para botones
        frame_botones = tk.Frame(self.root, bg="#34495e", pady=20)
        frame_botones.pack(expand=True)
        
        # Estilo de botones
        estilo_boton = {
            'font': ("Arial", 12),
            'width': 30,
            'height': 2,
            'bg': "#3498db",
            'fg': "white",
            'activebackground': "#2980b9",
            'activeforeground': "white",
            'relief': tk.RAISED,
            'bd': 3
        }
        
        # Botones del menú
        botones = [
            ("1. Jugar contra IA", self.gestor_juego.iniciar_juego_manual),
            ("2. Entrenar Manualmente", self.gestor_juego.iniciar_entrenamiento_manual),
            ("3. Entrenar Automáticamente", self.gestor_juego.mostrar_pantalla_entrenamiento),
            ("4. Ver Historial", self.gestor_juego.mostrar_historial),
            ("5. Ver Estadísticas", self.gestor_juego.mostrar_estadisticas),
            ("6. Ver Visualizaciones", self.gestor_juego.mostrar_visualizaciones),
            ("7. Limpiar Sistema", self.gestor_juego.limpiar_sistema),
            ("8. Créditos", self.gestor_juego.mostrar_creditos),
            ("Salir", self.root.quit)
        ]
        
        for texto, comando in botones:
            btn = tk.Button(frame_botones, text=texto, command=comando, **estilo_boton)
            btn.pack(pady=5)
        
        # Información de estado
        self.actualizar_estado()
    
    def actualizar_estado(self):
        """Actualizar información de estado en la parte inferior"""
        # Limpiar estado anterior si existe
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame) and widget != self.root.winfo_children()[0]:
                # Verificar si es el frame de estado
                if hasattr(widget, 'es_estado'):
                    widget.destroy()
        
        # Frame de estado
        frame_estado = tk.Frame(self.root, bg="#2c3e50", pady=10)
        frame_estado.es_estado = True
        frame_estado.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Obtener estadísticas
        stats_ia = self.gestor_juego.ia.obtener_estadisticas()
        stats_hist = self.gestor_juego.gestor_historial.obtener_estadisticas()
        
        texto_estado = f"Partidas totales: {stats_hist['total_partidas']} | "
        texto_estado += f"IA: {stats_ia['victorias']}V-{stats_ia['derrotas']}D-{stats_ia['empates']}E | "
        texto_estado += f"Estados aprendidos: {self.gestor_juego.gestor_movimientos.obtener_num_estados()}"
        
        label_estado = tk.Label(
            frame_estado,
            text=texto_estado,
            font=("Arial", 10),
            bg="#2c3e50",
            fg="white"
        )
        label_estado.pack()
