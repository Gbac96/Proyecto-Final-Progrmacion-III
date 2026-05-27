# -*- coding: utf-8 -*-
"""
Implementación de Lista Enlazada Simple
Sin usar list[] de Python - estructura propia
"""

class Nodo:
    """Nodo individual de la lista enlazada"""
    
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    """Lista enlazada simple implementada desde cero"""
    
    def __init__(self):
        self.cabeza = None
        self.tamano = 0
    
    def agregar(self, dato):
        """Agregar elemento al final de la lista"""
        nuevo_nodo = Nodo(dato)
        
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        
        self.tamano += 1
    
    def agregar_al_inicio(self, dato):
        """Agregar elemento al inicio de la lista"""
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        self.tamano += 1
    
    def obtener(self, indice):
        """Obtener elemento en la posición indicada"""
        if indice < 0 or indice >= self.tamano:
            return None
        
        actual = self.cabeza
        for _ in range(indice):
            actual = actual.siguiente
        
        return actual.dato
    
    def eliminar(self, indice):
        """Eliminar elemento en la posición indicada"""
        if indice < 0 or indice >= self.tamano:
            return False
        
        if indice == 0:
            self.cabeza = self.cabeza.siguiente
            self.tamano -= 1
            return True
        
        actual = self.cabeza
        for _ in range(indice - 1):
            actual = actual.siguiente
        
        actual.siguiente = actual.siguiente.siguiente
        self.tamano -= 1
        return True
    
    def buscar(self, dato):
        """Buscar la primera ocurrencia de un dato"""
        actual = self.cabeza
        indice = 0
        
        while actual is not None:
            if actual.dato == dato:
                return indice
            actual = actual.siguiente
            indice += 1
        
        return -1
    
    def esta_vacia(self):
        """Verificar si la lista está vacía"""
        return self.cabeza is None
    
    def obtener_tamano(self):
        """Obtener el tamaño de la lista"""
        return self.tamano
    
    def limpiar(self):
        """Limpiar toda la lista"""
        self.cabeza = None
        self.tamano = 0
    
    def a_lista_python(self):
        """Convertir a lista de Python para facilitar iteración (solo para visualización)"""
        resultado = []
        actual = self.cabeza
        while actual is not None:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado
    
    def __str__(self):
        """Representación en string de la lista"""
        if self.cabeza is None:
            return "[]"
        
        elementos = []
        actual = self.cabeza
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        
        return "[" + " -> ".join(elementos) + "]"
