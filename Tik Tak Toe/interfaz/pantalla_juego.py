# -*- coding: utf-8 -*-
"""
Pantalla de Juego - Tablero interactivo
"""

import tkinter as tk
from tkinter import messagebox
import config
from juego.tablero import Tablero


class PantallaJuego:
    """Pantalla con el tablero de juego interactivo"""
    
    def __init__(self, root, gestor_juego):
        """
        Inicializar pantalla de juego
        root: ventana raíz de Tkinter
        gestor_juego: instancia del gestor de juego principal
        """
        self.root = root
        self.gestor_juego = gestor_juego
        self.tablero = Tablero()
        self.botones = []
        self.turno_jugador = True  # True = jugador X, False = IA
        self.juego_activo = True
    
    def mostrar(self):
        """Mostrar la pantalla de juego"""
        # Limpiar ventana
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Título
        self.label_turno = tk.Label(
            self.root,
            text="Tu turno (X)",
            font=("Arial", 18, "bold"),
            bg="#34495e",
            fg="white",
            pady=15
        )
        self.label_turno.pack(fill=tk.X)
        
        # Frame para el tablero
        frame_tablero = tk.Frame(self.root, bg="#2c3e50", pady=20)
        frame_tablero.pack(expand=True)
        
        # Crear botones del tablero 3x3
        self.botones = []
        for i in range(9):
            fila = i // 3
            columna = i % 3
            
            btn = tk.Button(
                frame_tablero,
                text="",
                font=("Arial", 32, "bold"),
                width=4,
                height=2,
                bg=config.COLOR_VACIO,
                command=lambda pos=i: self.hacer_movimiento(pos)
            )
            btn.grid(row=fila, column=columna, padx=5, pady=5)
            self.botones.append(btn)
        
        # Frame para botones de control
        self.frame_botones = tk.Frame(self.root, bg="#34495e")
        self.frame_botones.pack(pady=20)
        
        # Botón de jugar de nuevo (inicialmente oculto)
        self.btn_jugar_nuevo = tk.Button(
            self.frame_botones,
            text="🔄 Jugar de Nuevo",
            font=("Arial", 12, "bold"),
            command=self.reiniciar_juego,
            bg="#27ae60",
            fg="white",
            padx=25,
            pady=12,
            relief=tk.RAISED,
            bd=3,
            cursor="hand2"
        )
        
        # Botón de volver al menú
        self.btn_volver = tk.Button(
            self.frame_botones,
            text="◀ Volver al Menú",
            font=("Arial", 12),
            command=self.volver_menu,
            bg="#3498db",
            fg="white",
            padx=25,
            pady=12,
            relief=tk.RAISED,
            bd=3,
            cursor="hand2"
        )
        self.btn_volver.pack(side=tk.LEFT, padx=10)
    
    def hacer_movimiento(self, posicion):
        """Manejar un movimiento del jugador"""
        if not self.juego_activo:
            return
        
        if not self.turno_jugador:
            messagebox.showwarning("Espera", "Es el turno de la IA")
            return
        
        # Realizar movimiento del jugador
        if self.tablero.realizar_movimiento(posicion, config.JUGADOR_X):
            self.actualizar_boton(posicion, config.JUGADOR_X)
            
            # Verificar fin del juego
            if self.verificar_fin_juego():
                return
            
            # Turno de la IA
            self.turno_jugador = False
            self.label_turno.config(text="Turno de IA (O)")
            self.root.update()
            
            # IA realiza movimiento
            self.root.after(500, self.movimiento_ia)
    
    def movimiento_ia(self):
        """Realizar movimiento de la IA"""
        if not self.juego_activo:
            return
        
        # IA selecciona movimiento
        posicion = self.gestor_juego.ia.seleccionar_movimiento(self.tablero)
        
        if posicion is not None:
            # Registrar movimiento para aprendizaje
            self.gestor_juego.ia.registrar_movimiento(self.tablero, posicion)
            
            # Realizar movimiento
            self.tablero.realizar_movimiento(posicion, config.JUGADOR_O)
            self.actualizar_boton(posicion, config.JUGADOR_O)
            
            # Verificar fin del juego
            if self.verificar_fin_juego():
                return
            
            # Turno del jugador
            self.turno_jugador = True
            self.label_turno.config(text="Tu turno (X)")
    
    def actualizar_boton(self, posicion, jugador):
        """Actualizar visual de un botón"""
        simbolo = config.SIMBOLO_X if jugador == config.JUGADOR_X else config.SIMBOLO_O
        color = config.COLOR_X if jugador == config.JUGADOR_X else config.COLOR_O
        
        self.botones[posicion].config(text=simbolo, bg=color, state=tk.DISABLED)
    
    def verificar_fin_juego(self):
        """Verificar si el juego ha terminado"""
        ganador = self.tablero.obtener_ganador()
        
        if ganador is not None:
            self.juego_activo = False
            
            # Finalizar partida de la IA (para aprendizaje)
            self.gestor_juego.ia.finalizar_partida(ganador)
            
            # Registrar en historial
            self.gestor_juego.gestor_historial.registrar_partida(
                ganador,
                self.tablero.celdas,
                es_entrenamiento=False
            )
            
            # Exportar visualización
            id_partida = self.gestor_juego.gestor_historial.contador_partidas
            self.gestor_juego.exporter.exportar_arbol_movimientos(
                self.gestor_juego.gestor_movimientos,
                id_partida
            )
            
            # Mostrar resultado
            if ganador == config.JUGADOR_X:
                mensaje = "¡Felicidades! Has ganado"
                self.label_turno.config(text="¡Ganaste!", fg="#2ecc71")
            elif ganador == config.JUGADOR_O:
                mensaje = "La IA ha ganado"
                self.label_turno.config(text="IA ganó", fg="#e74c3c")
            else:
                mensaje = "Empate"
                self.label_turno.config(text="Empate", fg="#f39c12")
            
            # Mostrar botón de jugar de nuevo
            self.btn_jugar_nuevo.pack(side=tk.LEFT, padx=10)
            
            messagebox.showinfo("Fin del Juego", mensaje)
            return True
        
        return False
    
    def reiniciar_juego(self):
        """Reiniciar el juego para una nueva partida"""
        # Reiniciar variables
        self.tablero = Tablero()
        self.turno_jugador = True
        self.juego_activo = True
        
        # Limpiar y reactivar botones del tablero
        for btn in self.botones:
            btn.config(
                text="",
                bg=config.COLOR_VACIO,
                state=tk.NORMAL
            )
        
        # Restaurar label de turno
        self.label_turno.config(
            text="Tu turno (X)",
            fg="white"
        )
        
        # Ocultar botón de jugar de nuevo
        self.btn_jugar_nuevo.pack_forget()
    
    def volver_menu(self):
        """Volver al menú principal"""
        self.gestor_juego.volver_menu()
