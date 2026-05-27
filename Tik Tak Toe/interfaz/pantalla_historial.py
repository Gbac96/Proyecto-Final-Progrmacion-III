# -*- coding: utf-8 -*-
"""
Pantalla de Historial - Lista de partidas
"""

import tkinter as tk
from tkinter import ttk, messagebox
import config


class PantallaHistorial:
    """Pantalla para ver el historial de partidas"""
    
    def __init__(self, root, gestor_juego):
        """
        Inicializar pantalla de historial
        root: ventana raíz de Tkinter
        gestor_juego: instancia del gestor de juego principal
        """
        self.root = root
        self.gestor_juego = gestor_juego
    
    def mostrar(self):
        """Mostrar la pantalla de historial"""
        # Limpiar ventana
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Título
        titulo = tk.Label(
            self.root,
            text="Historial de Partidas",
            font=("Arial", 20, "bold"),
            bg="#34495e",
            fg="white",
            pady=15
        )
        titulo.pack(fill=tk.X)
        
        # Frame principal con scroll
        frame_principal = tk.Frame(self.root, bg="#2c3e50")
        frame_principal.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Canvas y scrollbar
        canvas = tk.Canvas(frame_principal, bg="#2c3e50", highlightthickness=0)
        scrollbar = ttk.Scrollbar(frame_principal, orient="vertical", command=canvas.yview)
        frame_scroll = tk.Frame(canvas, bg="#2c3e50")
        
        frame_scroll.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=frame_scroll, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Obtener todas las partidas
        todas_partidas = self.gestor_juego.gestor_historial.obtener_todas_partidas()
        
        if todas_partidas.obtener_tamano() == 0:
            label_vacio = tk.Label(
                frame_scroll,
                text="No hay partidas registradas",
                font=("Arial", 14),
                bg="#2c3e50",
                fg="white"
            )
            label_vacio.pack(pady=50)
        else:
            # Mostrar cada partida
            for i in range(todas_partidas.obtener_tamano()):
                partida = todas_partidas.obtener(i)
                self.crear_item_partida(frame_scroll, partida)
        
        # Botón de volver
        btn_volver = tk.Button(
            self.root,
            text="Volver al Menú",
            font=("Arial", 12),
            command=self.gestor_juego.volver_menu,
            bg="#3498db",
            fg="white",
            padx=20,
            pady=10
        )
        btn_volver.pack(pady=15)
    
    def crear_item_partida(self, parent, partida):
        """Crear un item visual para una partida"""
        # Frame para la partida
        frame_partida = tk.Frame(parent, bg="#34495e", relief=tk.RAISED, bd=2)
        frame_partida.pack(fill=tk.X, padx=10, pady=5)
        
        # Resumen
        label_resumen = tk.Label(
            frame_partida,
            text=partida.obtener_resumen(),
            font=("Arial", 11),
            bg="#34495e",
            fg="white",
            anchor="w"
        )
        label_resumen.pack(fill=tk.X, padx=10, pady=5)
        
        # Botón para ver detalles
        btn_detalles = tk.Button(
            frame_partida,
            text="Ver Tablero",
            font=("Arial", 9),
            command=lambda p=partida: self.mostrar_detalles(p),
            bg="#3498db",
            fg="white"
        )
        btn_detalles.pack(side=tk.RIGHT, padx=10, pady=5)
    
    def mostrar_detalles(self, partida):
        """Mostrar detalles de una partida específica"""
        detalles = f"Partida ID: {partida.id_partida}\n\n"
        detalles += f"Resultado: {partida.obtener_resultado_texto()}\n"
        detalles += f"Tipo: {'Entrenamiento' if partida.es_entrenamiento else 'Manual'}\n"
        detalles += f"Fecha: {partida.timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        detalles += "Tablero Final:\n\n"
        detalles += partida.obtener_tablero_visual()
        
        messagebox.showinfo(f"Detalles Partida {partida.id_partida}", detalles)
