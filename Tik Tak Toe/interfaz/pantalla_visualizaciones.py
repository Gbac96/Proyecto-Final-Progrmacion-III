# -*- coding: utf-8 -*-
"""
Pantalla de Visualizaciones
Permite ver y convertir archivos .dot generados por el sistema
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import os
import subprocess
import config


class PantallaVisualizaciones:
    """Pantalla para visualizar archivos .dot del sistema"""
    
    def __init__(self, root, gestor_juego):
        """
        Inicializar pantalla de visualizaciones
        root: ventana raíz de Tkinter
        gestor_juego: instancia del gestor de juego principal
        """
        self.root = root
        self.gestor_juego = gestor_juego
    
    def mostrar(self):
        """Mostrar la pantalla de visualizaciones"""
        # Limpiar ventana
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Título
        titulo = tk.Label(
            self.root,
            text="📊 Visualizaciones Graphviz",
            font=("Arial", 20, "bold"),
            bg="#34495e",
            fg="white",
            pady=15
        )
        titulo.pack(fill=tk.X)
        
        # Frame principal
        frame_principal = tk.Frame(self.root, bg="#2c3e50", pady=10)
        frame_principal.pack(fill=tk.BOTH, expand=True, padx=20)
        
        # Descripción
        descripcion = tk.Label(
            frame_principal,
            text="Archivos de visualización generados automáticamente\n"
                 "Puedes ver el contenido o convertirlos a imágenes",
            font=("Arial", 11),
            bg="#2c3e50",
            fg="#ecf0f1",
            justify=tk.CENTER
        )
        descripcion.pack(pady=10)
        
        # Verificar si Graphviz está instalado
        graphviz_instalado = self._verificar_graphviz()
        
        # Frame de estado de Graphviz
        frame_graphviz = tk.Frame(frame_principal, bg="#34495e", relief=tk.RAISED, bd=2)
        frame_graphviz.pack(pady=10, padx=50, fill=tk.X)
        
        if graphviz_instalado:
            label_graphviz = tk.Label(
                frame_graphviz,
                text="✓ Graphviz instalado - Puedes convertir a imágenes",
                font=("Arial", 10, "bold"),
                bg="#27ae60",
                fg="white",
                pady=8
            )
        else:
            label_graphviz = tk.Label(
                frame_graphviz,
                text="⚠ Graphviz no instalado - Solo puedes ver el contenido como texto",
                font=("Arial", 10, "bold"),
                bg="#e67e22",
                fg="white",
                pady=8
            )
        label_graphviz.pack(fill=tk.X)
        
        # Frame de lista de archivos
        frame_lista = tk.Frame(frame_principal, bg="#34495e", relief=tk.RAISED, bd=3)
        frame_lista.pack(pady=15, padx=50, fill=tk.BOTH, expand=True)
        
        # Label de lista
        label_lista = tk.Label(
            frame_lista,
            text="📁 Archivos de Visualización:",
            font=("Arial", 12, "bold"),
            bg="#34495e",
            fg="white"
        )
        label_lista.pack(pady=10)
        
        # Listbox con scrollbar
        frame_listbox = tk.Frame(frame_lista, bg="#34495e")
        frame_listbox.pack(pady=5, padx=20, fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(frame_listbox)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.listbox_archivos = tk.Listbox(
            frame_listbox,
            font=("Courier", 10),
            bg="#2c3e50",
            fg="white",
            selectbackground="#3498db",
            selectforeground="white",
            yscrollcommand=scrollbar.set,
            height=10
        )
        self.listbox_archivos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.listbox_archivos.yview)
        
        # Cargar archivos .dot
        self._cargar_archivos()
        
        # Frame de botones de acción
        frame_botones_accion = tk.Frame(frame_lista, bg="#34495e")
        frame_botones_accion.pack(pady=15)
        
        # Botón para ver contenido
        btn_ver = tk.Button(
            frame_botones_accion,
            text="👁 Ver Contenido",
            font=("Arial", 11, "bold"),
            command=self._ver_contenido,
            bg="#3498db",
            fg="white",
            padx=20,
            pady=10,
            relief=tk.RAISED,
            bd=3,
            cursor="hand2"
        )
        btn_ver.pack(side=tk.LEFT, padx=10)
        
        # Botón para convertir y abrir (solo si Graphviz está instalado)
        if graphviz_instalado:
            btn_convertir = tk.Button(
                frame_botones_accion,
                text="🖼 Convertir y Abrir",
                font=("Arial", 11, "bold"),
                command=self._convertir_y_abrir,
                bg="#27ae60",
                fg="white",
                padx=20,
                pady=10,
                relief=tk.RAISED,
                bd=3,
                cursor="hand2"
            )
            btn_convertir.pack(side=tk.LEFT, padx=10)
        else:
            btn_ayuda = tk.Button(
                frame_botones_accion,
                text="❓ Cómo Instalar Graphviz",
                font=("Arial", 11, "bold"),
                command=self._mostrar_ayuda_graphviz,
                bg="#e67e22",
                fg="white",
                padx=20,
                pady=10,
                relief=tk.RAISED,
                bd=3,
                cursor="hand2"
            )
            btn_ayuda.pack(side=tk.LEFT, padx=10)
        
        # Botón para actualizar lista
        btn_actualizar = tk.Button(
            frame_botones_accion,
            text="🔄 Actualizar",
            font=("Arial", 11, "bold"),
            command=self._cargar_archivos,
            bg="#9b59b6",
            fg="white",
            padx=20,
            pady=10,
            relief=tk.RAISED,
            bd=3,
            cursor="hand2"
        )
        btn_actualizar.pack(side=tk.LEFT, padx=10)
        
        # Botón de volver
        btn_volver = tk.Button(
            self.root,
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
        btn_volver.pack(pady=20)
    
    def _verificar_graphviz(self):
        """Verificar si Graphviz está instalado"""
        try:
            result = subprocess.run(
                ['dot', '-V'],
                capture_output=True,
                text=True,
                timeout=5
            )
            return result.returncode == 0
        except:
            return False
    
    def _cargar_archivos(self):
        """Cargar la lista de archivos .dot"""
        self.listbox_archivos.delete(0, tk.END)
        
        # Verificar que existe la carpeta
        if not os.path.exists(config.CARPETA_VISUALIZACIONES):
            self.listbox_archivos.insert(tk.END, "No hay archivos de visualización")
            return
        
        # Obtener archivos .dot
        archivos = [f for f in os.listdir(config.CARPETA_VISUALIZACIONES) 
                   if f.endswith('.dot')]
        
        if not archivos:
            self.listbox_archivos.insert(tk.END, "No hay archivos .dot generados")
            self.listbox_archivos.insert(tk.END, "")
            self.listbox_archivos.insert(tk.END, "Juega partidas para generar visualizaciones")
        else:
            # Ordenar archivos
            archivos.sort()
            for archivo in archivos:
                ruta_completa = os.path.join(config.CARPETA_VISUALIZACIONES, archivo)
                tamaño = os.path.getsize(ruta_completa)
                tamaño_kb = tamaño / 1024
                self.listbox_archivos.insert(tk.END, f"{archivo} ({tamaño_kb:.1f} KB)")
    
    def _ver_contenido(self):
        """Ver el contenido del archivo .dot seleccionado"""
        seleccion = self.listbox_archivos.curselection()
        
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona un archivo para ver")
            return
        
        # Obtener nombre del archivo (sin el tamaño)
        texto = self.listbox_archivos.get(seleccion[0])
        if "No hay" in texto or "Juega" in texto:
            return
        
        nombre_archivo = texto.split(" (")[0]
        ruta_archivo = os.path.join(config.CARPETA_VISUALIZACIONES, nombre_archivo)
        
        if not os.path.exists(ruta_archivo):
            messagebox.showerror("Error", "El archivo no existe")
            return
        
        # Crear ventana para mostrar contenido
        ventana_contenido = tk.Toplevel(self.root)
        ventana_contenido.title(f"Contenido: {nombre_archivo}")
        ventana_contenido.geometry("800x600")
        ventana_contenido.config(bg="#2c3e50")
        
        # Título
        titulo = tk.Label(
            ventana_contenido,
            text=f"📄 {nombre_archivo}",
            font=("Arial", 14, "bold"),
            bg="#34495e",
            fg="white",
            pady=10
        )
        titulo.pack(fill=tk.X)
        
        # Área de texto con scroll
        text_widget = scrolledtext.ScrolledText(
            ventana_contenido,
            font=("Courier", 10),
            bg="#2c3e50",
            fg="#ecf0f1",
            wrap=tk.WORD,
            padx=10,
            pady=10
        )
        text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Leer y mostrar contenido
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                contenido = f.read()
                text_widget.insert(1.0, contenido)
                text_widget.config(state=tk.DISABLED)
        except Exception as e:
            text_widget.insert(1.0, f"Error al leer archivo: {e}")
            text_widget.config(state=tk.DISABLED)
        
        # Botón cerrar
        btn_cerrar = tk.Button(
            ventana_contenido,
            text="Cerrar",
            font=("Arial", 12, "bold"),
            command=ventana_contenido.destroy,
            bg="#e74c3c",
            fg="white",
            padx=30,
            pady=10,
            cursor="hand2"
        )
        btn_cerrar.pack(pady=10)
    
    def _convertir_y_abrir(self):
        """Convertir archivo .dot a PNG y abrirlo"""
        seleccion = self.listbox_archivos.curselection()
        
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona un archivo para convertir")
            return
        
        # Obtener nombre del archivo
        texto = self.listbox_archivos.get(seleccion[0])
        if "No hay" in texto or "Juega" in texto:
            return
        
        nombre_archivo = texto.split(" (")[0]
        ruta_dot = os.path.join(config.CARPETA_VISUALIZACIONES, nombre_archivo)
        ruta_png = ruta_dot.replace('.dot', '.png')
        
        if not os.path.exists(ruta_dot):
            messagebox.showerror("Error", "El archivo no existe")
            return
        
        try:
            # Convertir .dot a .png usando Graphviz
            messagebox.showinfo("Convirtiendo", f"Convirtiendo {nombre_archivo} a PNG...\nEsto puede tardar unos segundos.")
            
            result = subprocess.run(
                ['dot', '-Tpng', ruta_dot, '-o', ruta_png],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode != 0:
                messagebox.showerror(
                    "Error de Conversión",
                    f"No se pudo convertir el archivo:\n{result.stderr}"
                )
                return
            
            # Abrir imagen con el visor predeterminado
            if os.name == 'nt':  # Windows
                os.startfile(ruta_png)
            elif os.name == 'posix':  # Linux/Mac
                subprocess.run(['xdg-open', ruta_png])
            
            messagebox.showinfo(
                "Éxito",
                f"Archivo convertido exitosamente:\n{ruta_png}\n\n"
                f"La imagen se ha abierto con el visor predeterminado."
            )
            
        except subprocess.TimeoutExpired:
            messagebox.showerror(
                "Error",
                "La conversión tardó demasiado tiempo.\n"
                "El archivo puede ser muy grande."
            )
        except Exception as e:
            messagebox.showerror("Error", f"Error al convertir archivo:\n{e}")
    
    def _mostrar_ayuda_graphviz(self):
        """Mostrar ayuda para instalar Graphviz"""
        ayuda = (
            "📥 Cómo Instalar Graphviz en Windows:\n\n"
            "1. Descargar desde:\n"
            "   https://graphviz.org/download/#windows\n\n"
            "2. Ejecutar el instalador descargado\n\n"
            "3. Durante la instalación, MARCAR:\n"
            "   ☑ Add Graphviz to the system PATH\n\n"
            "4. Completar instalación\n\n"
            "5. REINICIAR Windows\n\n"
            "6. Verificar ejecutando en CMD:\n"
            "   dot -V\n\n"
            "Una vez instalado, podrás convertir\n"
            "los archivos .dot a imágenes PNG.\n\n"
            "Consulta docs/guia_graphviz.md\n"
            "para más información."
        )
        
        messagebox.showinfo("Instalar Graphviz", ayuda)
