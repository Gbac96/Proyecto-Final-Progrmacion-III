# -*- coding: utf-8 -*-
"""
MAIN - TIC TAC TOE CON APRENDIZAJE SUPERVISADO
Punto de entrada principal de la aplicación
"""

import tkinter as tk
from tkinter import messagebox
import config
from juego.movimientos import GestorMovimientos
from juego.ia import IA, Entrenador
from historial.gestor import GestorHistorial
from visualizacion.graphviz_exporter import GraphvizExporter
from interfaz.menu_principal import MenuPrincipal
from interfaz.pantalla_juego import PantallaJuego
from interfaz.pantalla_historial import PantallaHistorial
from interfaz.pantalla_entrenamiento import PantallaEntrenamiento
from interfaz.pantalla_visualizaciones import PantallaVisualizaciones
from interfaz.ventana_creditos import VentanaCreditos, mostrar_estadisticas


class GestorJuego:
    """
    Gestor principal del juego
    Coordina todas las componentes del sistema
    """
    
    def __init__(self, root):
        """Inicializar el gestor de juego"""
        self.root = root
        
        # Inicializar estructuras de datos
        self.gestor_movimientos = GestorMovimientos()
        self.gestor_historial = GestorHistorial(grado=config.GRADO_ARBOL_B)
        
        # Inicializar IA y entrenador
        self.ia = IA(self.gestor_movimientos)
        self.entrenador = Entrenador(self.ia)
        
        # Inicializar exportador de visualizaciones
        self.exporter = GraphvizExporter()
        
        # Inicializar pantallas
        self.menu_principal = MenuPrincipal(root, self)
        self.pantalla_juego = None
        self.pantalla_historial = None
        self.pantalla_entrenamiento = None
        self.pantalla_visualizaciones = None
        self.ventana_creditos = VentanaCreditos(root)
    
    def iniciar(self):
        """Iniciar la aplicación mostrando el menú principal"""
        self.menu_principal.mostrar()
    
    def volver_menu(self):
        """Volver al menú principal"""
        self.menu_principal.mostrar()
    
    def iniciar_juego_manual(self):
        """Iniciar una partida manual contra la IA"""
        self.pantalla_juego = PantallaJuego(self.root, self)
        self.pantalla_juego.mostrar()
    
    def iniciar_entrenamiento_manual(self):
        """Iniciar entrenamiento manual (igual que juego manual)"""
        messagebox.showinfo(
            "Entrenamiento Manual",
            "En el modo de entrenamiento manual, juega partidas normales.\n"
            "Cada partida ayudará a la IA a mejorar su estrategia."
        )
        self.iniciar_juego_manual()
    
    def mostrar_pantalla_entrenamiento(self):
        """Mostrar la pantalla de entrenamiento automático"""
        self.pantalla_entrenamiento = PantallaEntrenamiento(self.root, self)
        self.pantalla_entrenamiento.mostrar()
    
    def mostrar_historial(self):
        """Mostrar el historial de partidas"""
        self.pantalla_historial = PantallaHistorial(self.root, self)
        self.pantalla_historial.mostrar()
    
    def mostrar_estadisticas(self):
        """Mostrar estadísticas generales"""
        mostrar_estadisticas(self.root, self)
    
    def mostrar_visualizaciones(self):
        """Mostrar la pantalla de visualizaciones"""
        self.pantalla_visualizaciones = PantallaVisualizaciones(self.root, self)
        self.pantalla_visualizaciones.mostrar()
    
    def mostrar_creditos(self):
        """Mostrar ventana de créditos"""
        self.ventana_creditos.mostrar()
    
    def limpiar_sistema(self):
        """Limpiar todo el sistema (reiniciar)"""
        respuesta = messagebox.askyesno(
            "Confirmar",
            "¿Estás seguro de que deseas limpiar todo el sistema?\n\n"
            "Esto borrará:\n"
            "- Todos los pesos aprendidos\n"
            "- Todo el historial de partidas\n"
            "- Todas las estadísticas\n\n"
            "Esta acción no se puede deshacer."
        )
        
        if respuesta:
            self.gestor_movimientos.limpiar()
            self.gestor_historial.limpiar()
            self.ia.reiniciar_estadisticas()
            
            messagebox.showinfo(
                "Sistema Limpiado",
                "El sistema ha sido reiniciado exitosamente.\n"
                "Todos los datos han sido borrados."
            )
            
            self.volver_menu()


def main():
    """Función principal"""
    # Crear ventana principal
    root = tk.Tk()
    root.title("Tic Tac Toe - Aprendizaje Supervisado")
    root.geometry("900x700")
    root.config(bg="#34495e")
    root.resizable(False, False)
    
    # Centrar ventana en la pantalla
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    # Crear gestor de juego e iniciar
    gestor = GestorJuego(root)
    gestor.iniciar()
    
    # Mensaje de bienvenida
    messagebox.showinfo(
        "Bienvenido",
        "Bienvenido a Tic Tac Toe con Aprendizaje Supervisado\n\n"
        "La IA aprenderá a jugar mejor a medida que juegues más partidas.\n\n"
        "¡Diviértete!"
    )
    
    # Iniciar loop principal
    root.mainloop()


if __name__ == "__main__":
    main()
