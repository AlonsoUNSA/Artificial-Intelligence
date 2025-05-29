#include <iostream>
#include <vector>
#include "tsp.h"
#include "simulated_annealing.h"

int main() {
    // Matriz de distancias para 4 ciudades (simétrica)
    std::vector<std::vector<double>> distanceMatrix = {
        {0, 10, 15, 20},
        {10, 0, 35, 25},
        {15, 35, 0, 30},
        {20, 25, 30, 0}
    };

    TSP tsp(distanceMatrix);

    // Crear instancia de SimulatedAnnealing
    SimulatedAnnealing sa(tsp, 1000, 0.995, 10000);
    sa.run();

    std::vector<int> bestTour = sa.getBestSolution();
    double bestCost = sa.getBestCost();

    std::cout << "Mejor recorrido encontrado: ";
    for (int city : bestTour) std::cout << city << " ";
    std::cout << bestTour[0] << std::endl; // Regresa al inicio

    std::cout << "Distancia total: " << bestCost << std::endl;

    return 0;
}