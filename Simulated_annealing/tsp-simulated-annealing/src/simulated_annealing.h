#pragma once
#include <vector>
#include "tsp.h"

class SimulatedAnnealing {
public:
    SimulatedAnnealing(const TSP& tspInstance, double initialTemp = 1000, double coolingRate = 0.995, int maxIterations = 10000);
    void run();
    std::vector<int> getBestSolution() const;
    double getBestCost() const;

private:
    const TSP& tsp;
    double initialTemperature;
    double coolingRate;
    int maxIterations;

    std::vector<int> currentSolution;
    std::vector<int> bestSolution;
    double bestCost;

    double evaluateCost(const std::vector<int>& solution) const;
    std::vector<int> generateNeighbor(const std::vector<int>& solution) const;
};