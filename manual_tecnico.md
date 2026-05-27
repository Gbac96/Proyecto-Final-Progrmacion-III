# Manual Técnico
## Tic Tac Toe con Aprendizaje Supervisado

---

## 1. Esquema Conceptual del Sistema

### Visión General

El sistema implementa un juego de Tic Tac Toe con una IA que aprende mediante ajuste de pesos. La arquitectura se divide en capas modulares:

```
┌─────────────────────────────────────────┐
│         INTERFAZ GRÁFICA (Tkinter)       │
│  Menu │ Juego │ Historial │ Entrenamiento│
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│         GESTOR PRINCIPAL (main.py)       │
│  Coordina todas las componentes          │
└──────┬────────┬────────┬────────┬───────┘
       │        │        │        │
   ┌───▼──┐ ┌──▼──┐ ┌───▼───┐ ┌─▼────┐
   │  IA  │ │Juego│ │Historial│ │Visual│
   └───┬──┘ └──┬──┘ └───┬───┘ └──────┘
       │       │        │
   ┌───▼───────▼────────▼───────────┐
   │ ESTRUCTURAS DE DATOS PROPIAS   │
   │ Lista Enlazada │ Árbol B        │
   └────────────────────────────────┘
```

### Flujo de Datos

1. **Usuario** → **Interfaz** → **Gestor Principal**
2. **Gestor** → **IA** → **Gestor Movimientos** (pesos)
3. **Resultados** → **Historial** (Árbol B)
4. **Estructuras** → **Visualización** (Graphviz)

---

## 2. Arquitectura del Sistema

### Componentes Principales

#### 2.1. Capa de Presentación (Interfaz)
- **Responsabilidad:** Interacción con el usuario
- **Tecnología:** Tkinter
- **Módulos:**
  - `menu_principal.py` - Menú de navegación
  - `pantalla_juego.py` - Tablero interactivo
  - `pantalla_historial.py` - Visualización de partidas
  - `pantalla_entrenamiento.py` - Configuración de entrenamiento
  - `ventana_creditos.py` - Información del equipo

#### 2.2. Capa de Lógica de Negocio
- **Responsabilidad:** Reglas del juego y aprendizaje
- **Módulos:**
  - `tablero.py` - Estado del juego, validación, detección de victoria
  - `movimientos.py` - Sistema de pesos y estados
  - `ia.py` - Selección de movimientos y ajuste de pesos
  - `partida.py` - Representación de partidas individuales
  - `gestor.py` - Gestión del historial con Árbol B

#### 2.3. Capa de Estructuras de Datos
- **Responsabilidad:** Almacenamiento eficiente sin usar estructuras nativas
- **Módulos:**
  - `lista_enlazada.py` - Implementación de lista enlazada simple
  - `arbol_b.py` - Implementación de Árbol B

#### 2.4. Capa de Visualización
- **Responsabilidad:** Exportación a Graphviz
- **Módulos:**
  - `graphviz_exporter.py` - Generación de archivos .dot

#### 2.5. Coordinación Global
- **Archivo:** `main.py`
- **Clase:** `GestorJuego`
- **Responsabilidad:** Inicialización y coordinación de todas las componentes

---

## 3. Diagrama de Clases

### 3.1. Estructuras de Datos Base

```
┌─────────────────────┐
│       Nodo          │
├─────────────────────┤
│ - dato: any         │
│ - siguiente: Nodo   │
├─────────────────────┤
│ + __init__(dato)    │
└─────────────────────┘
         △
         │ usa
         │
┌─────────────────────────────┐
│     ListaEnlazada           │
├─────────────────────────────┤
│ - cabeza: Nodo              │
│ - tamano: int               │
├─────────────────────────────┤
│ + agregar(dato)             │
│ + obtener(indice): any      │
│ + buscar(dato): int         │
│ + eliminar(indice): bool    │
│ + limpiar()                 │
└─────────────────────────────┘

┌─────────────────────────────┐
│        NodoB                │
├─────────────────────────────┤
│ - claves: ListaEnlazada     │
│ - valores: ListaEnlazada    │
│ - hijos: ListaEnlazada      │
│ - es_hoja: bool             │
├─────────────────────────────┤
│ + obtener_num_claves(): int │
│ + obtener_clave(i): any     │
│ + insertar_clave_valor(...)  │
└─────────────────────────────┘
         △
         │ usa
         │
┌─────────────────────────────┐
│        ArbolB               │
├─────────────────────────────┤
│ - raiz: NodoB               │
│ - grado: int                │
│ - num_partidas: int         │
├─────────────────────────────┤
│ + insertar(clave, valor)    │
│ + buscar(clave): any        │
│ + obtener_todas_partidas()  │
│ + limpiar()                 │
└─────────────────────────────┘
```

### 3.2. Lógica del Juego

```
┌─────────────────────────────┐
│        Tablero              │
├─────────────────────────────┤
│ - celdas: list[int]         │
│ - movimientos_realizados    │
├─────────────────────────────┤
│ + realizar_movimiento(...)  │
│ + verificar_victoria(): bool│
│ + obtener_ganador(): int    │
│ + obtener_estado_tupla()    │
└─────────────────────────────┘

┌─────────────────────────────┐
│   MovimientoConPeso         │
├─────────────────────────────┤
│ - posicion: int             │
│ - peso: float               │
├─────────────────────────────┤
│ + ajustar_peso(ajuste)      │
└─────────────────────────────┘
         △
         │ gestiona
         │
┌─────────────────────────────────────┐
│      GestorMovimientos              │
├─────────────────────────────────────┤
│ - estados_movimientos: dict         │
│ - num_estados: int                  │
├─────────────────────────────────────┤
│ + obtener_movimientos(estado)       │
│ + registrar_movimiento(...)         │
│ + obtener_mejor_movimiento(...)     │
│ + ajustar_pesos_secuencia(...)      │
└─────────────────────────────────────┘
         △
         │ usa
         │
┌─────────────────────────────────────┐
│            IA                       │
├─────────────────────────────────────┤
│ - gestor_movimientos                │
│ - secuencia_actual: list            │
│ - victorias, derrotas, empates      │
├─────────────────────────────────────┤
│ + seleccionar_movimiento(tablero)   │
│ + registrar_movimiento(...)         │
│ + finalizar_partida(resultado)      │
│ + obtener_estadisticas(): dict      │
└─────────────────────────────────────┘
         △
         │ entrena
         │
┌─────────────────────────────────────┐
│         Entrenador                  │
├─────────────────────────────────────┤
│ - ia: IA                            │
├─────────────────────────────────────┤
│ + entrenar_automatico(num_partidas) │
│ - _simular_partida(): int           │
└─────────────────────────────────────┘
```

### 3.3. Historial

```
┌─────────────────────────────┐
│        Partida              │
├─────────────────────────────┤
│ - id_partida: int           │
│ - ganador: int              │
│ - estado_tablero: list      │
│ - es_entrenamiento: bool    │
│ - timestamp: datetime       │
├─────────────────────────────┤
│ + obtener_resultado_texto() │
│ + obtener_resumen(): str    │
│ + obtener_tablero_visual()  │
└─────────────────────────────┘
         △
         │ almacena
         │
┌─────────────────────────────────────┐
│      GestorHistorial                │
├─────────────────────────────────────┤
│ - arbol: ArbolB                     │
│ - contador_partidas: int            │
├─────────────────────────────────────┤
│ + registrar_partida(...): int       │
│ + buscar_partida(id): Partida       │
│ + obtener_todas_partidas()          │
│ + obtener_estadisticas(): dict      │
│ + limpiar()                         │
└─────────────────────────────────────┘
```

---

## 4. Descripción de Clases Principales

### 4.1. ListaEnlazada
**Responsabilidad:** Estructura de datos dinámica para almacenar colecciones sin usar list[] de Python.

**Atributos:**
- `cabeza: Nodo` - Primer nodo de la lista
- `tamano: int` - Número de elementos

**Métodos principales:**
- `agregar(dato)` - Agregar al final O(n)
- `obtener(indice)` - Obtener elemento O(n)
- `buscar(dato)` - Buscar primera ocurrencia O(n)
- `eliminar(indice)` - Eliminar elemento O(n)

### 4.2. ArbolB
**Responsabilidad:** Árbol balanceado para almacenar historial de partidas con búsqueda eficiente.

**Atributos:**
- `raiz: NodoB` - Nodo raíz del árbol
- `grado: int` - Grado del árbol (mínimo de claves, defecto 5)
- `num_partidas: int` - Total de partidas almacenadas

**Métodos principales:**
- `insertar(clave, valor)` - Insertar partida O(log n)
- `buscar(clave)` - Buscar partida O(log n)
- `obtener_todas_partidas()` - Recorrido inorden O(n)

**Justificación:** El Árbol B permite búsqueda e inserción eficientes (O(log n)), ideal para historial que crece dinámicamente.

### 4.3. GestorMovimientos
**Responsabilidad:** Almacenar y gestionar pesos de movimientos para cada estado del juego.

**Atributos:**
- `estados_movimientos: dict` - Diccionario de estado → ListaEnlazada de MovimientoConPeso
- `num_estados: int` - Total de estados únicos visitados

**Métodos principales:**
- `obtener_mejor_movimiento(estado, disponibles)` - Seleccionar movimiento con mayor peso
- `ajustar_pesos_secuencia(secuencia, ajuste)` - Actualizar pesos después de partida

**Justificación:** Usa diccionario interno (permitido para índice rápido) pero almacena valores en ListaEnlazada propia.

### 4.4. IA
**Responsabilidad:** Seleccionar movimientos y aprender de resultados.

**Atributos:**
- `gestor_movimientos: GestorMovimientos` - Referencia compartida
- `secuencia_actual: list` - Movimientos de la partida en curso
- `victorias, derrotas, empates: int` - Estadísticas

**Métodos principales:**
- `seleccionar_movimiento(tablero)` - Elegir mejor jugada según pesos
- `finalizar_partida(resultado)` - Ajustar pesos según resultado

**Lógica de aprendizaje:**
```python
if ganador == IA:
    ajuste = +1.0  # Reforzar movimientos ganadores
elif ganador == Humano:
    ajuste = -0.5  # Penalizar movimientos perdedores
else:
    ajuste = +0.2  # Pequeño refuerzo por empate
```

### 4.5. GestorHistorial
**Responsabilidad:** Gestionar almacenamiento y consulta de partidas usando Árbol B.

**Atributos:**
- `arbol: ArbolB` - Árbol B con partidas
- `contador_partidas: int` - ID incremental

**Métodos principales:**
- `registrar_partida(...)` - Insertar nueva partida y retornar ID
- `obtener_estadisticas()` - Calcular victorias, derrotas, empates, porcentajes

---

## 5. Estructuras de Datos Implementadas

### 5.1. Lista Enlazada Simple

**Propósito:** Almacenar colecciones dinámicas sin usar estructuras nativas de Python.

**Implementación:**
- Cada nodo contiene `dato` y `siguiente`
- Operaciones básicas: agregar, obtener, buscar, eliminar
- Complejidad temporal: O(n) para la mayoría de operaciones

**Uso en el sistema:**
- Claves y valores en NodoB del Árbol B
- Almacenar MovimientoConPeso para cada estado
- Colecciones generales donde no se requiere acceso aleatorio constante

**Justificación:** Cumple requisito de no usar listas nativas. Suficiente para colecciones pequeñas (3-9 movimientos por estado).

### 5.2. Árbol B (Grado 5)

**Propósito:** Almacenar historial de partidas con búsqueda e inserción eficientes.

**Forma de implementación:**
- Cada nodo contiene múltiples claves (IDs de partidas) y valores (objetos Partida)
- Grado 5: mínimo 4 claves, máximo 5 claves por nodo (excepto raíz)
- Auto-balanceo mediante división de nodos llenos
- Búsqueda: O(log n), Inserción: O(log n)

**Características:**
```
Nodo Interno:
┌───┬───┬───┬───┬───┐
│ 10│ 25│ 38│ 52│ 67│  Claves (IDs)
└─┬─┴─┬─┴─┬─┴─┬─┴─┬─┘
  │   │   │   │   │
 Hijos (punteros a sub-árboles)
```

**Uso en el sistema:**
- Clave: ID de partida (entero incremental)
- Valor: objeto Partida completo
- Permite búsqueda rápida por ID
- Recorrido inorden para listar todas las partidas

**Justificación:** Árbol B mantiene balance automático, ideal para inserciones frecuentes. Grado 5 es suficiente para ~1000 partidas sin excesiva profundidad.

### 5.3. Diccionario de Estados (estructura auxiliar)

**Propósito:** Índice rápido de estado → movimientos con pesos.

**Implementación:**
- Diccionario Python nativo como índice (permitido por simplicidad)
- Valores son ListaEnlazada de MovimientoConPeso (estructura propia)
- Clave: tupla de 9 elementos representando tablero

**Justificación:** El diccionario interno es una optimización permitida (no se almacenan datos de usuario directamente). Las colecciones de valores usan ListaEnlazada propia.

---

## 6. Lógica del Aprendizaje Implementado

### 6.1. Fundamento del Aprendizaje Supervisado

**Tipo:** Aprendizaje por refuerzo con ajuste de pesos

**Principio:** Los movimientos que conducen a victorias incrementan su peso, los que conducen a derrotas lo disminuyen.

### 6.2. Representación de Estados

Cada estado del tablero se representa como tupla de 9 elementos:
```python
(0, 1, 0, 2, 0, 1, 0, 0, 2)
# 0 = vacío, 1 = X, 2 = O

Visualizado:
  | X |  
---------
O |   | X
---------
  |   | O
```

### 6.3. Sistema de Pesos

**Peso Inicial:** 1.0 para todos los movimientos

**Ajustes por Resultado:**
- **Victoria IA:** +1.0 a todos los movimientos de la secuencia
- **Derrota IA:** -0.5 a todos los movimientos de la secuencia
- **Empate:** +0.2 a todos los movimientos (refuerzo pequeño)

**Límite Inferior:** Peso mínimo 0.1 (evitar pesos negativos o cero)

### 6.4. Algoritmo de Selección de Movimiento

```python
def seleccionar_movimiento(estado, movimientos_disponibles):
    pesos = obtener_pesos_para_estado(estado)
    
    mejor_movimiento = None
    mejor_peso = -infinito
    
    for movimiento in movimientos_disponibles:
        if pesos[movimiento] > mejor_peso:
            mejor_peso = pesos[movimiento]
            mejor_movimiento = movimiento
    
    return mejor_movimiento
```

### 6.5. Proceso de Aprendizaje en una Partida

1. **Durante el juego:**
   - IA registra cada (estado, movimiento) en secuencia_actual
   
2. **Al finalizar partida:**
   - Determinar resultado (victoria, derrota, empate)
   - Calcular ajuste según resultado
   - Aplicar ajuste a TODOS los movimientos de la secuencia
   
3. **Evolución:**
   - Movimientos exitosos acumulan peso positivo
   - Movimientos malos acumulan peso negativo
   - Con suficientes partidas, emergenmovimientos óptimos naturalmente

### 6.6. Entrenamiento Automático

**Estrategia:**
- Simular partidas IA vs. oponente aleatorio
- Oponente aleatorio no usa pesos (exploración pura)
- Permite que IA aprenda contra comportamiento impredecible

**Convergencia:**
- 0-50 partidas: IA juega casi aleatoriamente
- 50-200 partidas: IA empieza a evitar errores obvios
- 200-500 partidas: IA juega defensiva y ofensivamente
- 500+ partidas: IA juega casi óptimamente

### 6.7. Limitaciones del Enfoque

**Ventajas:**
- Simple de implementar y entender
- No requiere algoritmos complejos (minimax, Q-learning)
- Aprende progresivamente de la experiencia

**Desventajas:**
- No garantiza estrategia óptima (solo aproximación)
- Requiere muchas partidas para convergencia
- No prevé movimientos futuros (no hay lookahead)

---

## 7. Flujo del Sistema

### 7.1. Inicio de la Aplicación

```
1. main.py ejecutado
2. Crear ventana Tkinter 700x600
3. Inicializar GestorJuego:
   - GestorMovimientos (vacío, sin estados)
   - GestorHistorial con ArbolB(grado=5)
   - IA con referencia a GestorMovimientos
   - Entrenador con referencia a IA
   - GraphvizExporter
4. Mostrar MenuPrincipal
5. Mensaje de bienvenida
6. Loop principal Tkinter
```

### 7.2. Flujo de una Partida Manual

```
1. Usuario selecciona "Jugar contra IA"
2. PantallaJuego.mostrar():
   - Crear tablero 3x3 con botones
   - Inicializar Tablero (todas celdas vacías)
3. Turno Jugador:
   - Usuario hace clic en celda
   - Validar movimiento
   - Actualizar Tablero y botón visual
   - Verificar victoria/empate → FIN
   - Cambiar turno a IA
4. Turno IA:
   - IA.seleccionar_movimiento(tablero)
     • Obtener estado actual
     • Obtener movimientos disponibles
     • Consultar pesos en GestorMovimientos
     • Seleccionar movimiento con mayor peso
   - IA.registrar_movimiento(estado, movimiento)
   - Actualizar Tablero y botón visual
   - Verificar victoria/empate → FIN
   - Cambiar turno a Jugador
5. Fin del Juego:
   - IA.finalizar_partida(resultado)
     • Ajustar pesos de toda la secuencia
   - GestorHistorial.registrar_partida(...)
   - Exportar visualización Graphviz
   - Mostrar mensaje con ganador
   - Botón "Volver al Menú"
```

### 7.3. Flujo de Entrenamiento Automático

```
1. Usuario selecciona "Entrenar Automáticamente"
2. PantallaEntrenamiento.mostrar()
3. Usuario ingresa N (número de partidas)
4. Click "Iniciar Entrenamiento"
5. Para i = 1 to N:
   - Entrenador._simular_partida():
     • Crear tablero vacío
     • Turno alternado: Aleatorio vs. IA
     • IA registra sus movimientos
     • Determinar ganador
     • IA.finalizar_partida(ganador)
       → Ajustar pesos
     • GestorHistorial.registrar_partida(...)
   - Actualizar barra de progreso
   - Mostrar resultado en pantalla
6. Fin del entrenamiento:
   - Exportar visualización del ArbolB
   - Generar reporte con estadísticas
   - Mostrar resumen
```

### 7.4. Flujo de Consulta de Historial

```
1. Usuario selecciona "Ver Historial"
2. PantallaHistorial.mostrar():
   - GestorHistorial.obtener_todas_partidas()
     • ArbolB.recorrido_inorden()
     • Retornar ListaEnlazada de Partidas
3. Para cada Partida:
   - Mostrar item visual con resumen
   - Botón "Ver Tablero" → Mostrar detalles en popup
4. Botón "Volver al Menú"
```

---

## 8. Tecnologías y Herramientas

### 8.1. Lenguaje
- **Python 3.8+**
- Tipado dinámico
- Orientado a objetos

### 8.2. Interfaz Gráfica
- **Tkinter** (incluido con Python)
- Widgets: Button, Label, Frame, Entry, Text, Scrollbar, Progressbar

### 8.3. Visualización
- **Graphviz** (opcional)
- Generación de archivos .dot
- Conversión manual a PNG/SVG

### 8.4. Estructuras Internas
- **Sin dependencias externas**
- Implementación pura de Python para listas y árboles

---

## 9. Rendimiento y Escalabilidad

### 9.1. Complejidad Temporal

| Operación | Complejidad |
|-----------|-------------|
| Insertar en ListaEnlazada | O(n) |
| Buscar en ListaEnlazada | O(n) |
| Insertar en ArbolB | O(log n) |
| Buscar en ArbolB | O(log n) |
| Seleccionar movimiento IA | O(m) donde m ≤ 9 |
| Simular partida | O(k) donde k ≤ 9 turnos |

### 9.2. Complejidad Espacial

- **GestorMovimientos:** O(e × m) donde e = estados únicos, m ≈ 5 movimientos promedio
- **ArbolB:** O(p) donde p = número de partidas
- **Total:** O(e × m + p)

Con 500 estados y 1000 partidas: ~3MB en memoria (estimado)

### 9.3. Escalabilidad

**Límites prácticos:**
- Hasta ~10,000 estados sin problemas de rendimiento
- Hasta ~5,000 partidas en ArbolB mantiene buen rendimiento
- Entrenamiento de 1000 partidas: ~30-60 segundos

**Cuellos de botella:**
- ListaEnlazada para búsqueda lineal (pequeña pero frecuente)
- Recorrido completo de ArbolB para estadísticas

---

## 10. Pruebas y Validación

### 10.1. Pruebas Unitarias Sugeridas

```python
# Test ListaEnlazada
def test_lista_enlazada():
    lista = ListaEnlazada()
    lista.agregar(1)
    lista.agregar(2)
    assert lista.obtener_tamano() == 2
    assert lista.obtener(0) == 1

# Test ArbolB
def test_arbol_b():
    arbol = ArbolB(grado=3)
    for i in range(20):
        arbol.insertar(i, f"Valor{i}")
    assert arbol.buscar(10) == "Valor10"
    assert arbol.obtener_num_partidas() == 20

# Test Tablero
def test_tablero():
    tablero = Tablero()
    assert tablero.realizar_movimiento(0, JUGADOR_X)
    assert not tablero.verificar_victoria(JUGADOR_X)
```

### 10.2. Pruebas de Integración

1. **Partida completa manual**
   - Verificar que el ganador se detecta correctamente
   - Verificar que se registra en historial
   - Verificar que se ajustan pesos

2. **Entrenamiento automático**
   - Ejecutar 100 partidas
   - Verificar que stats_ia.partidas_jugadas == 100
   - Verificar que num_estados > 50

3. **Persistencia de datos durante sesión**
   - Jugar → Ver historial → Debe mostrar partida
   - Entrenar → Ver estadísticas → Debe reflejar aprendizaje

---

## 11. Mantenimiento y Extensibilidad

### 11.1. Modificaciones Comunes

**Cambiar ajustes de aprendizaje:**
```python
# En config.py
AJUSTE_VICTORIA = 1.5  # Incrementar refuerzo
AJUSTE_DERROTA = -0.7  # Incrementar penalización
```

**Cambiar grado del Árbol B:**
```python
# En config.py
GRADO_ARBOL_B = 7  # Mayor grado = menos profundidad
```

**Agregar persistencia:**
```python
# En GestorJuego.__init__()
self.cargar_desde_archivo("datos.pkl")

# En GestorJuego al cerrar
self.guardar_a_archivo("datos.pkl")
```

### 11.2. Extensiones Posibles

1. **Guardar/Cargar estado:**
   - Serializar GestorMovimientos y GestorHistorial con pickle

2. **Algoritmos más avanzados:**
   - Implementar Minimax con poda alfa-beta
   - Usar Q-Learning con tabla Q

3. **Tableros más grandes:**
   - Generalizar a N×N (requiere ajustar detección de victoria)

4. **Multijugador en red:**
   - Usar sockets para conectar 2 clientes

---

## 12. Conclusión Técnica

El sistema implementa exitosamente un Tic Tac Toe con aprendizaje supervisado usando estructuras de datos propias y una arquitectura modular. El diseño permite extensibilidad y cumple con todos los requisitos del proyecto.

**Fortalezas:**
- Código modular y bien organizado
- Estructuras de datos propias funcionales
- Aprendizaje observable en tiempo real
- Interfaz simple pero completa

**Áreas de mejora:**
- Persistencia de datos entre sesiones
- Algoritmos de IA más sofisticados
- Optimización de búsquedas en ListaEnlazada

---

**Documento preparado para:**  
Proyecto Final - Programación III  
Universidad Mariano Gálvez de Guatemala - 2026
