# Problema del Viajante (TSP) - Recocido Simulado

Este proyecto implementa una solución al Problema del Viajante (Traveling Salesman Problem, TSP) utilizando el algoritmo de Recocido Simulado (Simulated Annealing). El objetivo es encontrar la ruta más corta que visite todas las ciudades exactamente una vez y regrese al punto de inicio.

## Estructura del Proyecto

```
tsp-simulated-annealing
├── src
│   ├── main.cpp
│   ├── simulated_annealing.cpp
│   ├── simulated_annealing.h
│   ├── tsp.cpp
│   └── tsp.h
├── include
│   └── utils.h
├── CMakeLists.txt
└── README.md
```

## Descripción de Archivos

- **src/main.cpp**: Punto de entrada de la aplicación. Inicializa el problema y ejecuta el algoritmo.
- **src/simulated_annealing.cpp / .h**: Implementación y declaración de la clase que resuelve el TSP mediante recocido simulado.
- **src/tsp.cpp / .h**: Implementación y declaración de la clase que representa el problema del viajante.
- **include/utils.h**: Funciones utilitarias (puede estar vacío si no se usan).
- **CMakeLists.txt**: Archivo de configuración para compilar el proyecto con CMake.

## Compilación

Asegúrate de tener CMake instalado. Luego, ejecuta:

```bash
mkdir build
cd build
cmake ..
make
```

Esto generará el ejecutable en la carpeta `build/`.

## Ejecución

Después de compilar, ejecuta el programa con:

```bash
./tsp_simulated_annealing
```

## Uso

El programa ejecuta el algoritmo de recocido simulado para resolver el TSP con una matriz de distancias definida en `main.cpp`.  
Puedes modificar los parámetros del algoritmo (temperatura inicial, tasa de enfriamiento, iteraciones) y la matriz de distancias para probar diferentes escenarios.

## Descripción Algorítmica

La clase `TSP` (definida en [`src/tsp.cpp`](src/tsp.cpp)) representa el problema del viajante de la siguiente manera:

- **Matriz de distancias:** Se almacena como un `std::vector<std::vector<double>>`, donde cada elemento `[i][j]` indica la distancia entre la ciudad `i` y la ciudad `j`.
- **Cálculo de la distancia total:** El método `calculateTotalDistance` recibe un recorrido (vector de índices de ciudades) y suma las distancias entre ciudades consecutivas, incluyendo el regreso a la ciudad de origen.
- **Supuestos:** La matriz de distancias es simétrica y el recorrido siempre regresa al punto de inicio.

## Método principal

La clase `SimulatedAnnealing` (definida en [`src/simulated_annealing.cpp`](src/simulated_annealing.cpp)) implementa el algoritmo de recocido simulado para encontrar una solución aproximada al TSP:

- **Inicialización:** Comienza con una solución inicial (por ejemplo, el recorrido secuencial de las ciudades).
- **Vecindario:** En cada iteración, genera una solución vecina intercambiando dos ciudades del recorrido.
- **Criterio de aceptación:** Si la nueva solución es mejor, se acepta. Si es peor, se acepta con una probabilidad que depende de la diferencia de costo y la temperatura actual.
- **Enfriamiento:** La temperatura disminuye gradualmente según la tasa de enfriamiento.
- **Mejor solución:** Se guarda la mejor solución encontrada durante el proceso.

**Parámetros principales:**

- Temperatura inicial (`initialTemp`)
- Tasa de enfriamiento (`coolingRate`)
- Número máximo de iteraciones (`maxIterations`)

Puedes modificar estos parámetros en el constructor de la clase para experimentar con diferentes comportamientos del algoritmo.

### Detalle del método `SimulatedAnnealing::run()`

Este método ejecuta el algoritmo de recocido simulado para aproximar la solución óptima al TSP. El proceso es el siguiente:

1. **Inicialización:**  
   Se parte de una solución inicial (por ejemplo, visitar las ciudades en orden).
2. **Iteraciones:**  
   En cada iteración:
   - Se genera una solución vecina intercambiando dos ciudades al azar.
   - Se calcula el costo (distancia total) de la solución actual y de la vecina.
   - Si la vecina es mejor, se acepta como nueva solución actual.
   - Si la vecina es peor, se acepta con una probabilidad que depende de la diferencia de costos y la temperatura actual (criterio de Metropolis).
   - Si la nueva solución es la mejor encontrada, se actualiza el registro de la mejor solución.
   - La temperatura se reduce multiplicándola por el factor de enfriamiento.
3. **Finalización:**  
   Tras todas las iteraciones, la mejor solución encontrada queda almacenada y puede consultarse mediante los métodos `getBestSolution()` y `getBestCost()`.

Este método permite escapar de óptimos locales y encontrar soluciones cercanas al óptimo global para el TSP.
