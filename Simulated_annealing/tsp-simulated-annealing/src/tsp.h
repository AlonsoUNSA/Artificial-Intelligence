#pragma once
#include <vector>

class TSP {
public:
    // Constructor: recibe la matriz de distancias
    TSP(const std::vector<std::vector<double>>& distanceMatrix);

    // Calcula la distancia total de un recorrido (tour)
    double calculateTotalDistance(const std::vector<int>& tour) const;

    // Devuelve el número de ciudades
    int getNumCities() const;

private:
    std::vector<std::vector<double>> distances;
};