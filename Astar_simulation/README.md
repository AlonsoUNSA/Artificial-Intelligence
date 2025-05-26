# simulación del algoritmo A\*

Este proyecto es una simulación del algoritmo A\* (Astar), un algoritmo de búsqueda utilizado para encontrar el camino más corto en un grafo. Esta implementación permite visualizar cómo funciona el algoritmo en un entorno gráfico.

## Tabla de Contenidos

- [Características](#características)
- [Instalación](#instalación)
- [Uso](#uso)
- [Ejemplo](#ejemplo)

## Características

- Visualización del proceso de búsqueda del algoritmo A\*.
- Soporte para diferentes heurísticas (por ejemplo, distancia Manhattan).
- Interfaz gráfica simple para interactuar con el entorno de simulación.

## Explicación

En este apartado vamos a ver cómo es que funciona el algoritmo A\* siguiendo la función principal `astar`

- `open_set`
  - Una cola de prioridad hecha para poder ordenar los nodos que hace falta visitar donde se prioriza aquellos que tengan un score general mejor
- `g_score`
  - El costo real (pasos desde el inicio hasta el nodo en cuestión)
- `f_score`
  - Diccionario con el costo total lo que implica g_socre + heurística
- `open_set_hash`
  - Un conjunto que refleja `open_set` pero este es de acceso rápido
- Bucle _while_ principal
  - Almacenamos el mejor nodo de la cola de prioridad en `current`
  - Se marca de amarillo
  - Condicional si se ha llegado a la meta `current == end`
    - Recorre `came_from` un mapa que define de dódne viene cada nodo de modo que hace backtracking y colorea de azul
  - Marcado como ya evaluado y se colorea de gris
    -Exploración de vecinos
    - Sacamos los vecinos de `current`
    - Si el vecino ya fue evaluado se omite, usando el conjunto `closed_set`
      - Si el vecino no ha calculado su g_score o el g_score de `current` mas 1 es menor a gscore del vecino en cuestion
        - Definimos o actualizamos el `g_score` del vecino en cuestión y también su f_score
        - Si el vecino en cuestión no está en open_set_hash (open_set)
          - Se le añade al open set basado con su `f_score` y se colorea de cyan

## Instalación

Para instalar y ejecutar este proyecto, sigue estos pasos:

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/simulacion_astar.git
   cd simulacion_astar
   ```
2. Crea un entorno virtual (opcional)

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa: venv\Scripts\activate
   ```

3. Instala dependencias
   Siendo un proyecto en python es necesario tener instalado python.
   Además instala pygame con pip:

   ```bash
   pip install --upgrade pip
   pip install pygame
   ```

## Uso

Ejecuta el comando: `python main.py`

Pasos:

- clic: una vez para definir la partida, una segunda vez para definir la meta
- spacebar: aplicar el algoritmo y ver simulación

## Ejemplo

![Ejemplo](images/Example.jpg)
