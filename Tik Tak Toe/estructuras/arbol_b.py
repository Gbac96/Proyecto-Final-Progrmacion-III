# -*- coding: utf-8 -*-
"""
Implementación de Árbol B
Árbol balanceado de búsqueda con múltiples claves por nodo
"""

from estructuras.lista_enlazada import ListaEnlazada


class NodoB:
    """Nodo del árbol B con múltiples claves y referencias a hijos"""
    
    def __init__(self, es_hoja=True):
        self.claves = ListaEnlazada()  # Lista de claves (IDs de partidas)
        self.valores = ListaEnlazada()  # Lista de valores (objetos Partida)
        self.hijos = ListaEnlazada()  # Lista de nodos hijos
        self.es_hoja = es_hoja
    
    def obtener_num_claves(self):
        """Obtener número de claves en el nodo"""
        return self.claves.obtener_tamano()
    
    def obtener_clave(self, indice):
        """Obtener clave en posición específica"""
        return self.claves.obtener(indice)
    
    def obtener_valor(self, indice):
        """Obtener valor en posición específica"""
        return self.valores.obtener(indice)
    
    def obtener_hijo(self, indice):
        """Obtener hijo en posición específica"""
        return self.hijos.obtener(indice)
    
    def insertar_clave_valor(self, indice, clave, valor):
        """Insertar clave y valor en posición específica"""
        # Insertar en listas enlazadas requiere reconstruir
        claves_temp = []
        valores_temp = []
        
        for i in range(self.claves.obtener_tamano()):
            if i == indice:
                claves_temp.append(clave)
                valores_temp.append(valor)
            claves_temp.append(self.claves.obtener(i))
            valores_temp.append(self.valores.obtener(i))
        
        if indice == self.claves.obtener_tamano():
            claves_temp.append(clave)
            valores_temp.append(valor)
        
        self.claves.limpiar()
        self.valores.limpiar()
        
        for c in claves_temp:
            self.claves.agregar(c)
        for v in valores_temp:
            self.valores.agregar(v)
    
    def insertar_hijo(self, indice, hijo):
        """Insertar hijo en posición específica"""
        hijos_temp = []
        
        for i in range(self.hijos.obtener_tamano()):
            if i == indice:
                hijos_temp.append(hijo)
            hijos_temp.append(self.hijos.obtener(i))
        
        if indice == self.hijos.obtener_tamano():
            hijos_temp.append(hijo)
        
        self.hijos.limpiar()
        for h in hijos_temp:
            self.hijos.agregar(h)


class ArbolB:
    """Árbol B para almacenar historial de partidas"""
    
    def __init__(self, grado=5):
        """
        Inicializar árbol B
        grado: número mínimo de claves por nodo (excepto raíz)
        """
        self.raiz = None
        self.grado = grado  # Mínimo de claves
        self.max_claves = grado  # Máximo de claves
        self.num_partidas = 0
    
    def buscar(self, clave):
        """Buscar una clave en el árbol"""
        if self.raiz is None:
            return None
        return self._buscar_recursivo(self.raiz, clave)
    
    def _buscar_recursivo(self, nodo, clave):
        """Búsqueda recursiva en el árbol"""
        i = 0
        num_claves = nodo.obtener_num_claves()
        
        # Encontrar la posición de la clave
        while i < num_claves and clave > nodo.obtener_clave(i):
            i += 1
        
        # Si encontramos la clave
        if i < num_claves and clave == nodo.obtener_clave(i):
            return nodo.obtener_valor(i)
        
        # Si es hoja y no encontramos, no existe
        if nodo.es_hoja:
            return None
        
        # Buscar en el hijo correspondiente
        return self._buscar_recursivo(nodo.obtener_hijo(i), clave)
    
    def insertar(self, clave, valor):
        """Insertar una clave-valor en el árbol"""
        # Si el árbol está vacío
        if self.raiz is None:
            self.raiz = NodoB(es_hoja=True)
            self.raiz.claves.agregar(clave)
            self.raiz.valores.agregar(valor)
            self.num_partidas += 1
            return
        
        # Si la raíz está llena, dividirla
        if self.raiz.obtener_num_claves() >= self.max_claves:
            nueva_raiz = NodoB(es_hoja=False)
            nueva_raiz.hijos.agregar(self.raiz)
            self._dividir_hijo(nueva_raiz, 0)
            self.raiz = nueva_raiz
        
        self._insertar_no_lleno(self.raiz, clave, valor)
        self.num_partidas += 1
    
    def _insertar_no_lleno(self, nodo, clave, valor):
        """Insertar en un nodo que no está lleno"""
        i = nodo.obtener_num_claves() - 1
        
        if nodo.es_hoja:
            # Encontrar posición e insertar
            while i >= 0 and clave < nodo.obtener_clave(i):
                i -= 1
            nodo.insertar_clave_valor(i + 1, clave, valor)
        else:
            # Encontrar hijo donde insertar
            while i >= 0 and clave < nodo.obtener_clave(i):
                i -= 1
            i += 1
            
            hijo = nodo.obtener_hijo(i)
            
            # Si el hijo está lleno, dividirlo
            if hijo.obtener_num_claves() >= self.max_claves:
                self._dividir_hijo(nodo, i)
                
                # Después de dividir, decidir a qué hijo ir
                if clave > nodo.obtener_clave(i):
                    i += 1
                    hijo = nodo.obtener_hijo(i)
                else:
                    hijo = nodo.obtener_hijo(i)
            
            self._insertar_no_lleno(hijo, clave, valor)
    
    def _dividir_hijo(self, padre, indice):
        """Dividir un hijo lleno"""
        hijo_lleno = padre.obtener_hijo(indice)
        nuevo_nodo = NodoB(es_hoja=hijo_lleno.es_hoja)
        
        # Punto medio para dividir
        medio = self.grado // 2
        
        # Mover la segunda mitad de claves al nuevo nodo
        for i in range(medio, hijo_lleno.obtener_num_claves()):
            nuevo_nodo.claves.agregar(hijo_lleno.obtener_clave(i))
            nuevo_nodo.valores.agregar(hijo_lleno.obtener_valor(i))
        
        # Mover hijos si no es hoja
        if not hijo_lleno.es_hoja:
            for i in range(medio, hijo_lleno.hijos.obtener_tamano()):
                nuevo_nodo.hijos.agregar(hijo_lleno.obtener_hijo(i))
        
        # Reducir el tamaño del hijo lleno
        claves_temp = []
        valores_temp = []
        hijos_temp = []
        
        for i in range(medio):
            claves_temp.append(hijo_lleno.obtener_clave(i))
            valores_temp.append(hijo_lleno.obtener_valor(i))
        
        if not hijo_lleno.es_hoja:
            for i in range(medio):
                hijos_temp.append(hijo_lleno.obtener_hijo(i))
        
        hijo_lleno.claves.limpiar()
        hijo_lleno.valores.limpiar()
        hijo_lleno.hijos.limpiar()
        
        for c in claves_temp:
            hijo_lleno.claves.agregar(c)
        for v in valores_temp:
            hijo_lleno.valores.agregar(v)
        for h in hijos_temp:
            hijo_lleno.hijos.agregar(h)
        
        # Subir la clave del medio al padre
        clave_medio = claves_temp[-1] if claves_temp else 0
        valor_medio = valores_temp[-1] if valores_temp else None
        
        # Insertar la clave del medio en el padre
        padre.insertar_clave_valor(indice, clave_medio, valor_medio)
        
        # Insertar el nuevo nodo como hijo
        padre.insertar_hijo(indice + 1, nuevo_nodo)
    
    def obtener_todas_partidas(self):
        """Obtener todas las partidas en orden"""
        resultado = ListaEnlazada()
        if self.raiz is not None:
            self._recorrido_inorden(self.raiz, resultado)
        return resultado
    
    def _recorrido_inorden(self, nodo, resultado):
        """Recorrido inorden del árbol"""
        if nodo is None:
            return
        
        i = 0
        num_claves = nodo.obtener_num_claves()
        
        while i < num_claves:
            # Visitar hijo izquierdo
            if not nodo.es_hoja:
                self._recorrido_inorden(nodo.obtener_hijo(i), resultado)
            
            # Visitar clave actual
            resultado.agregar(nodo.obtener_valor(i))
            i += 1
        
        # Visitar último hijo
        if not nodo.es_hoja:
            self._recorrido_inorden(nodo.obtener_hijo(i), resultado)
    
    def limpiar(self):
        """Limpiar todo el árbol"""
        self.raiz = None
        self.num_partidas = 0
    
    def obtener_num_partidas(self):
        """Obtener número total de partidas"""
        return self.num_partidas
