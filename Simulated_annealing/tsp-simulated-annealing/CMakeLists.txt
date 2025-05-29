cmake_minimum_required(VERSION 3.10)

project(TSPSimulatedAnnealing)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Incluye los headers de la carpeta include/
include_directories(include)

# Busca todos los archivos fuente en src/
file(GLOB SOURCES
    src/*.cpp
)

# Crea el ejecutable principal
add_executable(tsp_simulated_annealing ${SOURCES})

# Si tienes tests, descomenta estas líneas:
# enable_testing()
# add_subdirectory(tests)