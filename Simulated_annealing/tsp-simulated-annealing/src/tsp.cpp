#include "tsp.h"

TSP::TSP(const std::vector<std::vector<double>>& distanceMatrix)
    : distances(distanceMatrix) {}

double TSP::calculateTotalDistance(const std::vector<int>& tour) const {
    double total = 0.0;
    for (std::size_t i = 0; i < tour.size() - 1; ++i) {
        total += distances[tour[i]][tour[i+1]];
    }
    // Regresa al inicio
    total += distances[tour.back()][tour[0]];
    return total;
}

int TSP::getNumCities() const {
    return distances.size();
}