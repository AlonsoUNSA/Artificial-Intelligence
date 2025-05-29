#include "simulated_annealing.h"
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>

SimulatedAnnealing::SimulatedAnnealing(const TSP& tspInstance, double initialTemp, double coolingRate, int maxIterations)
    : tsp(tspInstance), initialTemperature(initialTemp), coolingRate(coolingRate), maxIterations(maxIterations) {
    std::srand(static_cast<unsigned int>(std::time(nullptr)));
}

double SimulatedAnnealing::evaluateCost(const std::vector<int>& solution) const {
    return tsp.calculateTotalDistance(solution);
}

std::vector<int> SimulatedAnnealing::generateNeighbor(const std::vector<int>& solution) const {
    std::vector<int> neighbor = solution;
    int i = std::rand() % neighbor.size();
    int j = std::rand() % neighbor.size();
    std::swap(neighbor[i], neighbor[j]);
    return neighbor;
}

void SimulatedAnnealing::run() {
    // Inicialización con una solución secuencial
    currentSolution.resize(tsp.getNumCities());
    for (int i = 0; i < tsp.getNumCities(); ++i) currentSolution[i] = i;
    bestSolution = currentSolution;
    bestCost = evaluateCost(currentSolution);

    double temperature = initialTemperature;

    for (int iteration = 0; iteration < maxIterations; ++iteration) {
        std::vector<int> newSolution = generateNeighbor(currentSolution);
        double currentCost = evaluateCost(currentSolution);
        double newCost = evaluateCost(newSolution);

        if (newCost < currentCost ||
            (std::exp((currentCost - newCost) / temperature) > (std::rand() / (RAND_MAX + 1.0)))) {
            currentSolution = newSolution;
            if (newCost < bestCost) {
                bestCost = newCost;
                bestSolution = newSolution;
            }
        }
        temperature *= coolingRate;
    }
}

std::vector<int> SimulatedAnnealing::getBestSolution() const {
    return bestSolution;
}

double SimulatedAnnealing::getBestCost() const {
    return bestCost;
}