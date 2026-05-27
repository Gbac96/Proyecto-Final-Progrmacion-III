# -*- coding: utf-8 -*-
"""
Pantalla de Entrenamiento Automático
"""

import tkinter as tk
from tkinter import ttk, messagebox
import config


class PantallaEntrenamiento:
    """Pantalla para configurar y ejecutar entrenamiento automático"""
    
    def __init__(self, root, gestor_juego):
        """
        Inicializar pantalla de entrenamiento
        root: ventana raíz de Tkinter
        gestor_juego: instancia del gestor de juego principal
        """
        self.root = root
        self.gestor_juego = gestor_juego
        self.entrenando = False
    
    def mostrar(self):
        """Mostrar la pantalla de entrenamiento"""
        # Limpiar ventana
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Título
        titulo = tk.Label(
            self.root,
            text="Entrenamiento Automático de IA",
            font=("Arial", 20, "bold"),
            bg="#34495e",
            fg="white",
            pady=15
        )
        titulo.pack(fill=tk.X)
        
        # Frame principal (SIN expand para que el botón sea visible)
        frame_principal = tk.Frame(self.root, bg="#2c3e50", pady=10)
        frame_principal.pack(fill=tk.X, padx=20)
        
        # Descripción
        descripcion = tk.Label(
            frame_principal,
            text="La IA jugará múltiples partidas contra un oponente aleatorio\n"
                 "para mejorar su estrategia mediante aprendizaje supervisado.",
            font=("Arial", 11),
            bg="#2c3e50",
            fg="#ecf0f1",
            justify=tk.CENTER
        )
        descripcion.pack(pady=10)
        
        # Frame de configuración
        frame_config = tk.Frame(frame_principal, bg="#34495e", relief=tk.RAISED, bd=3)
        frame_config.pack(pady=10, padx=50, fill=tk.X)
        
        # Label y entrada para número de partidas
        label_num = tk.Label(
            frame_config,
            text="🎯 Número de partidas a simular:",
            font=("Arial", 12, "bold"),
            bg="#34495e",
            fg="white"
        )
        label_num.pack(pady=8)
        
        self.entry_num_partidas = tk.Entry(
            frame_config,
            font=("Arial", 16, "bold"),
            width=12,
            justify=tk.CENTER,
            relief=tk.SUNKEN,
            bd=2
        )
        self.entry_num_partidas.insert(0, "100")
        self.entry_num_partidas.pack(pady=8)
        
        # Botón de iniciar entrenamiento (mejorado)
        self.btn_iniciar = tk.Button(
            frame_principal,
            text="▶ Iniciar Entrenamiento",
            font=("Arial", 14, "bold"),
            command=self.iniciar_entrenamiento,
            bg="#27ae60",
            fg="white",
            padx=35,
            pady=15,
            relief=tk.RAISED,
            bd=3,
            cursor="hand2"
        )
        self.btn_iniciar.pack(pady=15)
        
        # Barra de progreso
        self.progreso = ttk.Progressbar(
            frame_principal,
            length=600,
            mode='determinate'
        )
        self.progreso.pack(pady=8)
        
        # Label de estado (mejorado)
        self.label_estado = tk.Label(
            frame_principal,
            text="Esperando inicio...",
            font=("Arial", 11, "bold"),
            bg="#2c3e50",
            fg="#3498db"
        )
        self.label_estado.pack(pady=5)
        
        # Área de resultados (Text widget) - Reducido para ver el botón
        label_resultados = tk.Label(
            frame_principal,
            text="📊 Resultados del Entrenamiento:",
            font=("Arial", 11, "bold"),
            bg="#2c3e50",
            fg="white"
        )
        label_resultados.pack(pady=(5, 3))
        
        frame_resultados = tk.Frame(frame_principal, bg="#2c3e50")
        frame_resultados.pack(pady=3, fill=tk.X, padx=60)
        
        scroll_resultados = tk.Scrollbar(frame_resultados)
        scroll_resultados.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.text_resultados = tk.Text(
            frame_resultados,
            font=("Courier", 10),
            bg="#34495e",
            fg="white",
            height=6,
            width=80,
            yscrollcommand=scroll_resultados.set,
            wrap=tk.WORD,
            relief=tk.SUNKEN,
            bd=2
        )
        self.text_resultados.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll_resultados.config(command=self.text_resultados.yview)
        
        # Frame para botones inferiores (dentro de frame_principal)
        frame_botones = tk.Frame(frame_principal, bg="#2c3e50")
        frame_botones.pack(pady=10)
        
        # Botón de volver al menú (más grande y visible)
        btn_volver = tk.Button(
            frame_botones,
            text="◀ Volver al Menú",
            font=("Arial", 14, "bold"),
            command=self.gestor_juego.volver_menu,
            bg="#e74c3c",
            fg="white",
            padx=40,
            pady=15,
            relief=tk.RAISED,
            bd=4,
            cursor="hand2"
        )
        btn_volver.pack()
        
        # Botón ADICIONAL fuera del frame principal (siempre visible)
        btn_volver_fijo = tk.Button(
            self.root,
            text="◀ VOLVER AL MENÚ",
            font=("Arial", 16, "bold"),
            command=self.gestor_juego.volver_menu,
            bg="#c0392b",
            fg="white",
            padx=50,
            pady=18,
            relief=tk.RAISED,
            bd=5,
            cursor="hand2"
        )
        btn_volver_fijo.pack(pady=20)
    
    def iniciar_entrenamiento(self):
        """Iniciar el entrenamiento automático"""
        if self.entrenando:
            messagebox.showwarning("Espera", "Ya hay un entrenamiento en curso")
            return
        
        try:
            num_partidas = int(self.entry_num_partidas.get())
            if num_partidas <= 0:
                raise ValueError()
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido de partidas")
            return
        
        # Deshabilitar botón
        self.btn_iniciar.config(state=tk.DISABLED)
        self.entrenando = True
        
        # Limpiar resultados
        self.text_resultados.delete(1.0, tk.END)
        self.progreso['value'] = 0
        self.progreso['maximum'] = num_partidas
        
        # Iniciar entrenamiento
        self.entrenar_progresivo(num_partidas, 0)
    
    def entrenar_progresivo(self, total, actual):
        """Entrenar de forma progresiva para no bloquear la UI"""
        if actual >= total:
            self.finalizar_entrenamiento()
            return
        
        # Entrenar un lote pequeño (10 partidas a la vez)
        lote = min(10, total - actual)
        
        victorias_ia = 0
        derrotas_ia = 0
        empates = 0
        
        for i in range(lote):
            resultado = self.gestor_juego.entrenador._simular_partida()
            
            # Registrar en historial
            # Obtener el tablero final (no disponible fácilmente, usar placeholder)
            self.gestor_juego.gestor_historial.registrar_partida(
                resultado,
                [0] * 9,  # Tablero placeholder
                es_entrenamiento=True
            )
            
            if resultado == config.JUGADOR_O:
                victorias_ia += 1
            elif resultado == config.JUGADOR_X:
                derrotas_ia += 1
            else:
                empates += 1
            
            actual += 1
            self.progreso['value'] = actual
            self.label_estado.config(text=f"Progreso: {actual}/{total} partidas")
        
        # Agregar resultado al text widget
        texto = f"Lote {actual//10}: {victorias_ia}V - {derrotas_ia}D - {empates}E\n"
        self.text_resultados.insert(tk.END, texto)
        self.text_resultados.see(tk.END)
        
        # Continuar con el siguiente lote
        self.root.after(10, lambda: self.entrenar_progresivo(total, actual))
    
    def finalizar_entrenamiento(self):
        """Finalizar el entrenamiento y mostrar resumen"""
        self.entrenando = False
        self.btn_iniciar.config(state=tk.NORMAL)
        
        # Obtener estadísticas finales
        stats_ia = self.gestor_juego.ia.obtener_estadisticas()
        
        # Mostrar resumen
        resumen = "\n" + "="*50 + "\n"
        resumen += "ENTRENAMIENTO COMPLETADO\n"
        resumen += "="*50 + "\n"
        resumen += f"Total partidas: {stats_ia['partidas_jugadas']}\n"
        resumen += f"Victorias IA: {stats_ia['victorias']} ({stats_ia['tasa_victoria']:.1f}%)\n"
        resumen += f"Derrotas IA: {stats_ia['derrotas']} ({stats_ia['tasa_derrota']:.1f}%)\n"
        resumen += f"Empates: {stats_ia['empates']} ({stats_ia['tasa_empate']:.1f}%)\n"
        resumen += f"Estados aprendidos: {self.gestor_juego.gestor_movimientos.obtener_num_estados()}\n"
        resumen += "="*50 + "\n"
        
        self.text_resultados.insert(tk.END, resumen)
        self.text_resultados.see(tk.END)
        
        self.label_estado.config(text="¡Entrenamiento completado!")
        
        # Exportar visualización del árbol B
        self.gestor_juego.exporter.exportar_arbol_b(self.gestor_juego.gestor_historial)
        
        messagebox.showinfo(
            "Completado",
            f"Entrenamiento finalizado\n\n"
            f"La IA ha jugado {stats_ia['partidas_jugadas']} partidas\n"
            f"Tasa de victoria: {stats_ia['tasa_victoria']:.1f}%"
        )
