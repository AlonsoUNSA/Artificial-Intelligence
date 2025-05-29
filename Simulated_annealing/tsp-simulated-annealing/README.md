# Traveling Salesman Problem - Simulated Annealing

This project implements a solution to the Traveling Salesman Problem (TSP) using the simulated annealing algorithm. The goal is to find the shortest possible route that visits each city exactly once and returns to the origin city.

## Project Structure

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
├── tests
│   └── test_simulated_annealing.cpp
├── CMakeLists.txt
└── README.md
```

## Files Overview

- **src/main.cpp**: Entry point of the application. Initializes the program and starts the simulated annealing process.
- **src/simulated_annealing.cpp**: Contains the implementation of the simulated annealing algorithm, including solution initialization and cost evaluation.
- **src/simulated_annealing.h**: Header file for the `SimulatedAnnealing` class, declaring its methods and constants.
- **src/tsp.cpp**: Implements functions related to TSP, such as distance calculations and route evaluations.
- **src/tsp.h**: Header file declaring functions and types related to TSP.
- **include/utils.h**: Contains utility functions for random number generation and logging.
- **tests/test_simulated_annealing.cpp**: Unit tests for the simulated annealing implementation.
- **CMakeLists.txt**: Configuration file for CMake, specifying project structure and build instructions.

## Building the Project

To build the project, ensure you have CMake installed. Navigate to the project directory and run the following commands:

```bash
mkdir build
cd build
cmake ..
make
```

## Running the Project

After building, you can run the application using:

```bash
./tsp-simulated-annealing
```

## Usage

The application will execute the simulated annealing algorithm to solve the TSP. You can modify the input parameters in `main.cpp` to test different scenarios.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.