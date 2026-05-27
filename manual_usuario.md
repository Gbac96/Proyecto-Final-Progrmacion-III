# Manual de Usuario
## Tic Tac Toe con Aprendizaje Supervisado

---

## 1. Introducción

Bienvenido al juego de **Tic Tac Toe con Aprendizaje Supervisado**. Esta aplicación no es un simple juego de Tres en Raya, sino un sistema inteligente donde la computadora (IA) aprende a jugar mejor con cada partida.

### ¿Qué hace especial a este juego?

- La IA **empieza sin saber jugar** (movimientos aleatorios)
- **Aprende de cada partida** ajustando su estrategia
- Después de **entrenar**, la IA se vuelve un oponente formidable
- Puedes ver **cómo aprende** a través de estadísticas y visualizaciones

---

## 2. Requisitos del Sistema

### Software Necesario

#### ✅ Obligatorios

1. **Python 3.8 o superior**
   - Descargar desde: https://www.python.org/downloads/
   - Durante instalación: ✅ Marcar "Add Python to PATH"

2. **Tkinter** (interfaz gráfica)
   - Viene incluido con Python en Windows y macOS
   - En Linux Ubuntu/Debian: `sudo apt-get install python3-tk`

#### 📦 Opcionales

3. **Graphviz** (para visualizaciones)
   - **No es obligatorio**, el juego funciona sin él
   - Sirve para generar diagramas de las estructuras de datos
   
   **Instalación Windows:**
   1. Descargar desde: https://graphviz.org/download/
   2. Ejecutar instalador
   3. ✅ Marcar "Add Graphviz to system PATH"
   4. Reiniciar computadora

   **Instalación Linux:**
   ```bash
   sudo apt-get install graphviz
   ```

   **Verificar instalación:**
   ```bash
   dot -V
   ```
   Debe mostrar: `dot - graphviz version...`

### Hardware Mínimo

- **RAM:** 512 MB disponible
- **Disco:** 50 MB de espacio libre
- **Pantalla:** Resolución mínima 800x600

---

## 3. Instalación y Ejecución

### Paso 1: Obtener el Programa

**Opción A: Descargar ZIP**
1. Descargar archivo ZIP del repositorio
2. Extraer en una carpeta 

**Opción B: Clonar con Git**
```bash
git clone <URL_DEL_REPOSITORIO>
cd FInal
```

### Paso 2: Verificar Archivos

Asegurarse de tener esta estructura:

```
FInal/
├── main.py          ← Archivo principal
├── config.py
├── README.md
├── estructuras/
├── juego/
├── historial/
├── visualizacion/
├── interfaz/
└── docs/
```

### Paso 3: Ejecutar el Programa

#### En Windows:

1. Abrir **PowerShell** o **CMD**
2. Navegar a la carpeta:
   ```bash
   cd C:\Users\TuUsuario\Desktop\FInal
   ```
3. Ejecutar:
   ```bash
   python main.py
   ```

#### En Linux/macOS:

1. Abrir **Terminal**
2. Navegar a la carpeta:
   ```bash
   cd ~/Desktop/FInal
   ```
3. Ejecutar:
   ```bash
   python3 main.py
   ```

### ¿Problemas al ejecutar?

**Error: "python no se reconoce"**
- Python no está en PATH
- Solución: Reinstalar Python y marcar "Add to PATH"

**Error: "No module named 'tkinter'"**
- Tkinter no está instalado
- Solución Linux: `sudo apt-get install python3-tk`
- Solución Windows: Reinstalar Python con "tcl/tk" habilitado

---

## 4. Descripción del Menú Principal

Al iniciar, verás la pantalla principal con 8 opciones:

```
╔═══════════════════════════════════════════╗
║   TIC TAC TOE                             ║
║   con Aprendizaje Supervisado             ║
╠═══════════════════════════════════════════╣
║                                           ║
║   [1. Jugar contra IA]                    ║
║   [2. Entrenar Manualmente]               ║
║   [3. Entrenar Automáticamente]           ║
║   [4. Ver Historial]                      ║
║   [5. Ver Estadísticas]                   ║
║   [6. Limpiar Sistema]                    ║
║   [7. Créditos]                           ║
║   [Salir]                                 ║
║                                           ║
╠═══════════════════════════════════════════╣
║  Partidas: 0 | IA: 0V-0D-0E | Estados: 0 ║
╚═══════════════════════════════════════════╝
```

### Barra de Estado (abajo)

- **Partidas totales:** Número de juegos jugados
- **IA:** Victorias-Derrotas-Empates de la computadora
- **Estados:** Cuántos tableros diferentes ha aprendido la IA

---

## 5. Guía de Uso Paso a Paso

### 5.1. Jugar tu Primera Partida

#### Paso 1: Seleccionar "Jugar contra IA"

Hacer clic en el botón **"1. Jugar contra IA"**

#### Paso 2: Entender el Tablero

Verás un tablero 3x3 con celdas vacías:

```
┌───┬───┬───┐
│   │   │   │
├───┼───┼───┤
│   │   │   │
├───┼───┼───┤
│   │   │   │
└───┴───┴───┘
```

- **Tú juegas con:** X (color azul)
- **IA juega con:** O (color rojo)
- **Tu objetivo:** Conseguir 3 X en línea (horizontal, vertical o diagonal)

#### Paso 3: Hacer tu Movimiento

1. Hacer clic en cualquier celda vacía
2. Aparecerá tu símbolo **X** en azul
3. La IA responderá automáticamente (medio segundo después)

#### Paso 4: Continuar Jugando

- Alterna turnos con la IA
- Las celdas ocupadas no se pueden usar
- El juego detecta automáticamente cuando alguien gana o hay empate

#### Paso 5: Fin del Juego

Cuando termine, verás un mensaje:
- **"¡Felicidades! Has ganado"** → Tú ganaste
- **"La IA ha ganado"** → La computadora ganó
- **"Empate"** → Tablero lleno sin ganador

Hacer clic en **"OK"** y luego en **"Volver al Menú"**

#### 📝 Nota Importante

En tu **primera partida**, la IA juega casi aleatoriamente porque aún no ha aprendido. ¡Esto es normal!

---

### 5.2. Entrenar a la IA

La IA necesita **aprender** para jugar bien. Hay dos formas:

#### Opción A: Entrenamiento Manual

**Cuándo usar:** Quieres ver cómo aprende jugando contra ella

1. Seleccionar **"2. Entrenar Manualmente"**
2. Jugar normalmente (igual que la opción 1)
3. Cada partida que juegues entrena a la IA
4. Después de **10-20 partidas**, notarás mejoras

**Ventaja:** Ves el aprendizaje en acción  
**Desventaja:** Lento si quieres una IA fuerte

#### Opción B: Entrenamiento Automático ⚡ (Recomendado)

**Cuándo usar:** Quieres una IA fuerte rápidamente

1. Seleccionar **"3. Entrenar Automáticamente"**
2. Verás esta pantalla:

```
╔════════════════════════════════════════╗
║   Entrenamiento Automático             ║
╠════════════════════════════════════════╣
║  La IA jugará contra un oponente       ║
║  aleatorio para mejorar su estrategia  ║
║                                        ║
║  Número de partidas a simular:         ║
║  ┌──────────┐                          ║
║  │   100    │  ← Cambiar este número   ║
║  └──────────┘                          ║
║                                        ║
║  [Iniciar Entrenamiento]               ║
║                                        ║
║  Progreso: ▓▓▓▓░░░░░░ 40%             ║
║                                        ║
║  Resultados:                           ║
║  Lote 1: 3V - 5D - 2E                  ║
║  Lote 2: 4V - 4D - 2E                  ║
║  ...                                   ║
╚════════════════════════════════════════╝
```

3. **Cambiar el número** de partidas (recomendado: 100-500)
4. Hacer clic en **"Iniciar Entrenamiento"**
5. Esperar a que termine (100 partidas ≈ 10-15 segundos)
6. Ver el **reporte final** con estadísticas

**Recomendaciones de entrenamiento:**

| Partidas | Nivel de la IA | Tiempo aprox |
|----------|----------------|--------------|
| 50       | Principiante   | 5 segundos   |
| 100      | Intermedio     | 10 segundos  |
| 500      | Avanzado       | 1 minuto     |
| 1000     | Experto        | 2 minutos    |

---

### 5.3. Ver Historial de Partidas

**Para qué sirve:** Ver todas las partidas jugadas (manuales y automáticas)

1. Seleccionar **"4. Ver Historial"**
2. Verás una lista de partidas:

```
╔════════════════════════════════════════════════════╗
║           Historial de Partidas                    ║
╠════════════════════════════════════════════════════╣
║                                                    ║
║  ┌──────────────────────────────────────────────┐ ║
║  │ ID: 1 | Manual | Victoria Jugador X          │ ║
║  │ 2026-05-25 14:30:15          [Ver Tablero]   │ ║
║  └──────────────────────────────────────────────┘ ║
║                                                    ║
║  ┌──────────────────────────────────────────────┐ ║
║  │ ID: 2 | Entrenamiento | Victoria IA (O)      │ ║
║  │ 2026-05-25 14:31:22          [Ver Tablero]   │ ║
║  └──────────────────────────────────────────────┘ ║
║                                                    ║
║  ...                                               ║
║                                                    ║
║  [Volver al Menú]                                  ║
╚════════════════════════════════════════════════════╝
```

3. Hacer clic en **"Ver Tablero"** para ver detalles:
   - Resultado de la partida
   - Tipo (manual o entrenamiento)
   - Fecha y hora
   - Tablero final

**Dato útil:** Cada partida tiene un **ID único** que se puede usar para buscarla

---

### 5.4. Ver Estadísticas

**Para qué sirve:** Ver el rendimiento general del sistema

1. Seleccionar **"5. Ver Estadísticas"**
2. Aparecerá una ventana emergente:

```
═══════════════════════════════════════
         ESTADÍSTICAS GENERALES
═══════════════════════════════════════

HISTORIAL DE PARTIDAS:
  Total: 156
  Victorias Jugador X: 52 (33.3%)
  Victorias IA (O): 89 (57.1%)
  Empates: 15 (9.6%)
  Manuales: 6
  Entrenamiento: 150

RENDIMIENTO DE LA IA:
  Partidas jugadas: 156
  Victorias: 89 (57.1%)
  Derrotas: 52 (33.3%)
  Empates: 15 (9.6%)

APRENDIZAJE:
  Estados únicos aprendidos: 187
  Total movimientos registrados: 842
  Promedio por estado: 4.50
```

**Interpretación:**
- **Tasa de victoria IA > 50%:** La IA está jugando bien
- **Estados aprendidos:** Más estados = más experiencia
- **Promedio por estado:** Indica cuántas opciones conoce por situación

---

### 5.5. Limpiar el Sistema

**⚠️ PRECAUCIÓN:** Esta opción **borra todo**

**Para qué sirve:** Reiniciar el sistema desde cero

**¿Cuándo usar?**
- Quieres empezar de nuevo
- La IA aprendió mal (poco probable)
- Experimentar con diferentes configuraciones

**Cómo hacerlo:**
1. Seleccionar **"6. Limpiar Sistema"**
2. Aparecerá confirmación:

```
┌────────────────────────────────────┐
│          ¿Confirmar?               │
├────────────────────────────────────┤
│ ¿Estás seguro de que deseas        │
│ limpiar todo el sistema?           │
│                                    │
│ Esto borrará:                      │
│ • Todos los pesos aprendidos       │
│ • Todo el historial de partidas    │
│ • Todas las estadísticas           │
│                                    │
│ Esta acción no se puede deshacer.  │
│                                    │
│      [Sí]          [No]            │
└────────────────────────────────────┘
```

3. Hacer clic en **"Sí"** para confirmar
4. El sistema se reiniciará completamente

**Resultado:** Todo vuelve a 0, como si nunca hubieras jugado

---

### 5.6. Créditos

**Para qué sirve:** Ver información del equipo

1. Seleccionar **"7. Créditos"**
2. Verás una ventana con:
   - Nombre del proyecto
   - Integrantes del grupo
   - Carnets
   - Porcentaje de participación
   - Sección

3. Hacer clic en **"Cerrar"** cuando termines

---

## 6. Capturas de Pantalla Explicadas

### Captura 1: Menú Principal

![Menú Principal - Placeholder]

**Descripción:**
- Título del proyecto en la parte superior
- 8 botones de opciones en el centro
- Barra de estado con estadísticas en la parte inferior
- Colores: Fondo oscuro, botones azules

**Elementos clave:**
- Barra de estado muestra progreso del aprendizaje

---

### Captura 2: Pantalla de Juego

![Pantalla de Juego - Placeholder]

**Descripción:**
- Tablero 3x3 en el centro
- Indicador de turno arriba ("Tu turno (X)" o "Turno de IA (O)")
- Botón "Volver al Menú" abajo
- Celdas vacías en gris, X en azul, O en rojo

**Elementos clave:**
- Las celdas ocupadas se deshabilitan (no se pueden hacer clic)
- El turno cambia automáticamente

---

### Captura 3: Entrenamiento Automático

![Entrenamiento - Placeholder]

**Descripción:**
- Input para número de partidas
- Botón "Iniciar Entrenamiento"
- Barra de progreso animada
- Área de texto con resultados en tiempo real

**Elementos clave:**
- El progreso se actualiza cada 10 partidas
- Los resultados se muestran en formato "Lote X: YV - ZD - WE"

---

### Captura 4: Historial de Partidas

![Historial - Placeholder]

**Descripción:**
- Lista scrollable de partidas
- Cada item muestra: ID, tipo, resultado, fecha
- Botón "Ver Tablero" por partida
- Botón "Volver al Menú" abajo

**Elementos clave:**
- Si no hay partidas, muestra "No hay partidas registradas"
- Partidas ordenadas por ID (las más recientes abajo)

---

### Captura 5: Ventana de Estadísticas

![Estadísticas - Placeholder]

**Descripción:**
- Ventana emergente pequeña
- Texto con estadísticas formateadas
- Dividido en 3 secciones: Historial, Rendimiento, Aprendizaje
- Botón "OK" para cerrar

**Elementos clave:**
- Los porcentajes se calculan automáticamente
- Muestra tanto partidas manuales como de entrenamiento

---

## 7. Ejemplo de Uso Completo

### Escenario: Entrenar y jugar contra una IA competente

#### Paso 1: Inicio
```
1. Ejecutar: python main.py
2. Ver mensaje de bienvenida → Click OK
3. Estás en el Menú Principal
```

#### Paso 2: Primera partida (IA débil)
```
1. Click "Jugar contra IA"
2. Jugar una partida (probablemente ganes fácil)
3. Observar que IA juega casi aleatoriamente
4. Volver al menú
```

#### Paso 3: Entrenar la IA
```
1. Click "Entrenar Automáticamente"
2. Cambiar número a 200
3. Click "Iniciar Entrenamiento"
4. Esperar ~20 segundos
5. Ver reporte:
   - Victorias IA: ~90 (45%)
   - Derrotas IA: ~90 (45%)
   - Empates: ~20 (10%)
6. Volver al menú
```

#### Paso 4: Ver progreso
```
1. Click "Ver Estadísticas"
2. Verificar:
   - Total partidas: 201 (1 manual + 200 entrenamiento)
   - Estados aprendidos: ~150
3. Click OK
```

#### Paso 5: Jugar contra IA entrenada
```
1. Click "Jugar contra IA"
2. Jugar una partida
3. Observar que IA juega MUCHO mejor
4. Probablemente pierdas o empates
5. Volver al menú
```

#### Paso 6: Ver historial
```
1. Click "Ver Historial"
2. Scroll hasta el final
3. Ver las últimas partidas
4. Click "Ver Tablero" en alguna para ver detalles
5. Volver al menú
```

#### Paso 7: Más entrenamiento (opcional)
```
1. Click "Entrenar Automáticamente"
2. Cambiar a 300 partidas
3. Entrenar nuevamente
4. IA será aún más fuerte (>60% victorias)
```

**Resultado final:**
- IA ha jugado 501 partidas (1+200+300)
- Conoce ~250 estados diferentes
- Tasa de victoria ~60-65%
- Es un oponente muy difícil de vencer

---

## 8. Visualizaciones Graphviz (Opcional)

### ¿Qué son?

Las visualizaciones son **diagramas** que muestran cómo funciona internamente el sistema:

- **Árbol de movimientos:** Muestra estados del juego y pesos
- **Árbol B del historial:** Muestra cómo se organizan las partidas

### ¿Cómo generarlas?

**Automáticamente:**
- Después de cada partida manual → `movimientos_partida_X.dot`
- Después de entrenamiento automático → `historial.dot`
- Se guardan en carpeta `visualizaciones/`

**⚠️ Requisito:** Tener Graphviz instalado

### ¿Cómo verlas?

#### Opción 1: Convertir a imagen (Recomendado)

```bash
cd visualizaciones
dot -Tpng historial.dot -o historial.png
```

Luego abrir `historial.png` con cualquier visor de imágenes

#### Opción 2: Ver .dot en editor de texto

Abrir con Notepad++, VSCode, etc. (menos visual pero funciona)

### Ejemplo de contenido

**Archivo: movimientos_partida_1.dot**
```dot
digraph MovimientosConPesos {
    estado_0 [label="_ _ _\n_ _ _\n_ _ _"];
    estado_1 [label="X _ _\n_ _ _\n_ _ _"];
    estado_0 -> estado_1 [label="Pos 0\nPeso: 1.00"];
    ...
}
```

**Interpretación:**
- Cada caja = un estado del tablero
- Flechas = movimientos posibles
- Pesos = qué tan bueno es ese movimiento según lo aprendido

---

## 9. Preguntas Frecuentes (FAQ)

### ❓ ¿Por qué la IA juega mal al inicio?

**Respuesta:** La IA **no tiene conocimiento previo**. Empieza con todos los movimientos en peso 1.0 (neutral). Solo aprende de la experiencia.

**Solución:** Entrenar con al menos 100 partidas automáticas.

---

### ❓ ¿Se guarda el aprendizaje cuando cierro el programa?

**Respuesta:** **NO**. Los datos se pierden al cerrar. Esto es una limitación del proyecto (no implementa persistencia).

**Workaround:** No cerrar el programa mientras lo uses. Si cierras, deberás entrenar de nuevo.

---

### ❓ ¿Cuántas partidas necesito para que la IA sea "buena"?

**Respuesta:**
- **100 partidas:** IA decente (50% victorias)
- **300 partidas:** IA buena (60% victorias)
- **500+ partidas:** IA muy buena (65-70% victorias)

**Nota:** En Tic Tac Toe, con juego perfecto de ambos lados, siempre hay empate. Una IA con 70% de victorias contra oponente aleatorio es excelente.

---

### ❓ ¿Puedo jugar 2 humanos? (Sin IA)

**Respuesta:** **NO**. El proyecto está diseñado para humano vs. IA. No hay modo multijugador local.

---

### ❓ ¿Qué pasa si entreno 10,000 partidas?

**Respuesta:** 
- **Ventaja:** IA será casi imbatible
- **Desventaja:** Tomará varios minutos (5-10 min)
- **Problema:** El programa puede ralentizarse por la cantidad de estados en memoria

**Recomendación:** Máximo 2000 partidas para balance entre rendimiento y aprendizaje.

---

### ❓ ¿Para qué sirve el ID de partida?

**Respuesta:** Identificación única de cada partida. Útil para:
- Buscar una partida específica en el historial
- Nombrar archivos de visualización
- Rastrear progreso del aprendizaje

---

### ❓ ¿Qué significa "Estados aprendidos"?

**Respuesta:** Número de **configuraciones diferentes del tablero** que la IA ha visto y registrado.

**Ejemplo:**
```
Estado 1:        Estado 2:        Estado 3:
X |   |          X | O |          X | O | X
---------        ---------        ---------
  |   |            |   |            | O |
---------        ---------        ---------
  |   |            |   |            |   |
```

Cada configuración única es un "estado". Con 200 partidas, la IA puede conocer ~150-250 estados diferentes.

---

### ❓ Error: "La ventana no responde"

**Respuesta:** Durante entrenamiento automático, la interfaz puede parecer congelada. Esto es normal si entrenas muchas partidas (>500).

**Solución:** Esperar a que termine. La barra de progreso se actualiza cada 10 partidas.

---

### ❓ ¿Puedo cambiar los colores de la interfaz?

**Respuesta:** **SÍ**, pero requiere editar código.

**Archivo:** `config.py`

```python
# Cambiar estos valores
COLOR_X = "#3498db"  # Azul → Cambiar a otro color hex
COLOR_O = "#e74c3c"  # Rojo → Cambiar a otro color hex
COLOR_VACIO = "#ecf0f1"  # Gris → Cambiar a otro
```

**Ejemplo:** Para X verde y O morado:
```python
COLOR_X = "#27ae60"  # Verde
COLOR_O = "#9b59b6"  # Morado
```

---

## 10. Solución de Problemas Comunes

### Problema 1: "El programa se cierra inmediatamente"

**Posibles causas:**
- Error de sintaxis en Python
- Falta algún archivo

**Solución:**
1. Abrir terminal/CMD en la carpeta del proyecto
2. Ejecutar: `python main.py`
3. Leer el error que aparece
4. Si dice "No such file", verificar estructura de carpetas
5. Si dice "SyntaxError", reinstalar los archivos originales

---

### Problema 2: "No se generan visualizaciones"

**Causa:** Graphviz no está instalado o no está en PATH

**Verificar:**
```bash
dot -V
```

**Si no funciona:**
1. Instalar Graphviz (ver sección 2)
2. Agregar a PATH:
   - Windows: Variables de entorno → PATH → Agregar `C:\Program Files\Graphviz\bin`
   - Linux/Mac: Debería funcionar automáticamente tras `apt-get install`
3. Reiniciar terminal/computadora

**Alternativa:** Usar el programa sin visualizaciones (funciona igual)

---

### Problema 3: "La IA sigue jugando mal después de entrenar"

**Posibles causas:**
- No se entrenó suficiente (menos de 50 partidas)
- Se limpió el sistema accidentalmente
- Bug en el código

**Solución:**
1. Ver estadísticas (opción 5)
2. Verificar "Estados aprendidos":
   - Si es 0 → No hay aprendizaje, entrenar de nuevo
   - Si es >100 → Debe jugar bien
3. Si el problema persiste, limpiar sistema y volver a entrenar con 300 partidas

---

### Problema 4: "El entrenamiento tarda mucho"

**Causa:** Entrenaste con demasiadas partidas (>2000)

**Solución:**
- Esperar a que termine (puede tomar 5-10 minutos)
- Para futuras sesiones, usar máximo 1000 partidas

**Prevención:**
- 100-500 partidas es el rango ideal
- Si necesitas más, entrenar en bloques de 500

---

### Problema 5: "No puedo hacer clic en las celdas"

**Posibles causas:**
- Es el turno de la IA (esperar 0.5 segundos)
- La celda ya está ocupada
- El juego ya terminó

**Solución:**
- Verificar el indicador de turno arriba
- Solo hacer clic en celdas vacías (grises)
- Si el juego terminó, cerrar el mensaje y volver al menú

---

## 11. Consejos y Trucos

### 💡 Consejo 1: Entrenamiento eficiente

**No entrenar de más al inicio:**
- Primeras sesión: 100 partidas
- Ver rendimiento (estadísticas)
- Si IA < 50% victorias → Entrenar 200 más
- Si IA > 60% victorias → Suficiente para jugar

### 💡 Consejo 2: Aprender de las derrotas

**Cuando la IA te gane:**
- Hacer clic en "Ver Historial"
- Buscar tu partida perdida
- Ver el tablero final
- Analizar qué movimiento te costó el juego

### 💡 Consejo 3: Experimentar con configuración

**Editar `config.py` para experimentar:**

```python
# Hacer que IA aprenda más rápido
AJUSTE_VICTORIA = 2.0  # En vez de 1.0
AJUSTE_DERROTA = -1.0  # En vez de -0.5

# Entrenar de nuevo y ver diferencia
```

### 💡 Consejo 4: Guardar estadísticas manualmente

**Dado que no hay persistencia, tomar captura:**
1. Ver estadísticas
2. Tomar screenshot de la ventana
3. Guardar imagen para comparar después

### 💡 Consejo 5: Usar el historial para comparar

**Antes y después de entrenar:**
- Jugar 1 partida manual (antes)
- Entrenar 200 partidas
- Jugar 1 partida manual (después)
- Comparar en el historial cuál fue más difícil

---

## 12. Glosario de Términos

**IA (Inteligencia Artificial):** La computadora que juega contra ti

**Estado:** Una configuración específica del tablero (qué celdas tienen X, O, o están vacías)

**Peso:** Valor numérico que indica qué tan "bueno" es un movimiento según lo aprendido

**Aprendizaje Supervisado:** Técnica donde la IA aprende ajustando pesos según resultados

**Historial:** Registro de todas las partidas jugadas (manuales y automáticas)

**Árbol B:** Estructura de datos que organiza el historial de forma eficiente

**Graphviz:** Herramienta opcional para crear diagramas de las estructuras

**Entrenamiento:** Proceso de hacer que la IA juegue muchas partidas para mejorar

**Secuencia:** Serie de movimientos en una partida (ejemplo: pos 0, pos 4, pos 8)

---

## 13. Contacto y Soporte

Para preguntas, problemas o sugerencias sobre el proyecto:

**Integrantes del Equipo:**
- [Ver opción "7. Créditos" en el menú principal]

**Repositorio:**
- [URL del repositorio si aplica]

**Curso:**
- Programación III
- Universidad Mariano Gálvez de Guatemala
- Sección A - 2026

---

## 14. Conclusión

¡Felicidades! Ahora sabes cómo usar completamente el sistema de Tic Tac Toe con Aprendizaje Supervisado.

### Resumen de flujo recomendado:

1. ✅ Ejecutar programa
2. ✅ Jugar 1 partida (ver IA débil)
3. ✅ Entrenar 200 partidas automáticas
4. ✅ Ver estadísticas (verificar mejora)
5. ✅ Jugar varias partidas (disfrutar del desafío)
6. ✅ Ver historial (analizar partidas)

### Siguiente nivel:

- Entrenar hasta 500+ partidas
- Intentar ganarle a la IA entrenada (¡difícil!)
- Experimentar con configuraciones
- Generar visualizaciones Graphviz

**¡Diviértete y aprende cómo funciona el aprendizaje automático! 🎮🤖**

---

**Documento preparado para:**  
Proyecto Final - Programación III  
Universidad Mariano Gálvez de Guatemala - 2026
