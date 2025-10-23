# INF8175 - Artificial Intelligence Course Projects

This repository contains coursework for **INF8175 - Artificial Intelligence** at Polytechnique Montréal, covering various AI topics including search algorithms, constraint programming, neural networks, and game AI.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Devoir 1: Search Algorithms](#devoir-1-search-algorithms)
- [Devoir 2: Constraint Programming & Local Search](#devoir-2-constraint-programming--local-search)
- [Devoir 3: Neural Networks](#devoir-3-neural-networks)
- [Final Project: Divercite Game AI](#final-project-divercite-game-ai)
- [Requirements](#requirements)
- [Usage](#usage)

## Overview

This repository contains four main components:
1. **Devoir 1**: Pacman search algorithms (BFS, DFS, UCS, A*)
2. **Devoir 2**: Constraint programming with MiniZinc and local search for scheduling
3. **Devoir 3**: Neural network implementations from scratch
4. **Final Project**: Divercite game AI using minimax algorithm

## Project Structure

```
PolyMTL_INF8175/
├── Devoir1_INF8175_A2024/          # Search algorithms
│   ├── code/                        # Main implementation
│   └── INF8175_A24_TP1.pdf         # Project description
├── Devoir2_INF8175_A24/            # Constraint programming & local search
│   ├── ProgrammationParContraintes/ # MiniZinc files
│   ├── RechercheLocale/            # Local search implementations
│   └── Sujet_Devoir_2_INF8175_A24.pdf
├── Devoir3_INF8175_A24/            # Neural networks
│   ├── students/                    # Implementation files
│   └── INF8175_A24_Devoir3.pdf
└── Projet_Divercite_A2024/          # Game AI project
    ├── Divercite/                   # Game implementation
    └── Projet_Divercite_A2024.pdf
```

## Devoir 1: Search Algorithms

**Location**: `Devoir1_INF8175_A2024/`

### Description
Implementation of classic graph search algorithms for Pacman AI, based on UC Berkeley's CS188 course materials.

### Algorithms Implemented
- **Depth-First Search (DFS)**: Explores deepest nodes first using a stack
- **Breadth-First Search (BFS)**: Explores shallowest nodes first using a queue
- **Uniform Cost Search (UCS)**: Finds optimal path considering step costs
- **A* Search**: Optimal pathfinding with heuristic functions

### Key Files
- `search.py`: Core search algorithm implementations
- `searchAgents.py`: Pacman agents using search algorithms
- `test_cases/`: Automated test cases for each algorithm

### Running Tests
```bash
cd Devoir1_INF8175_A2024/code
python autograder.py -q q1  # Test DFS
python autograder.py -q q2  # Test BFS
python autograder.py -q q3  # Test UCS
python autograder.py -q q4  # Test A*
```

### Running Pacman
```bash
cd Devoir1_INF8175_A2024/code
python pacman.py -p SearchAgent -a fn=depthFirstSearch
python pacman.py -p SearchAgent -a fn=breadthFirstSearch
python pacman.py -p SearchAgent -a fn=uniformCostSearch
python pacman.py -p SearchAgent -a fn=aStarSearch
```

## Devoir 2: Constraint Programming & Local Search

**Location**: `Devoir2_INF8175_A24/`

### Part 1: Constraint Programming (MiniZinc)

**Location**: `ProgrammationParContraintes/`

#### Description
Implementation of constraint satisfaction problems using MiniZinc modeling language.

#### Problems Solved
1. **Easy**: Actor-role assignment with costume constraints
2. **Normal**: Extended constraint problem
3. **Hard**: Complex constraint satisfaction

#### Key Files
- `1_Easy.mzn`, `2_Normal.mzn`, `3_Hard.mzn`: MiniZinc model files
- `*_Data_*.dzn`: Data files for testing

#### Constraints Implemented
- All actors must have different roles
- Each costume used only once
- Neighboring actors cannot have adjacent roles
- No two actors can have same role and costume

#### Running
```bash
cd Devoir2_INF8175_A24/ProgrammationParContraintes
minizinc 1_Easy.mzn 1_Easy_Data_1.dzn
```

### Part 2: Local Search

**Location**: `RechercheLocale/code/`

#### Description
Solving academic course scheduling problems using local search algorithms to minimize time slot conflicts.

#### Algorithms Implemented
- **Naive Solver**: Assigns different time slot to each course
- **Advanced Solver**: Iterative improvement local search to minimize conflicts

#### Key Files
- `main.py`: Main execution script
- `schedule.py`: Schedule data structure and utilities
- `solver_naive.py`: Basic solver implementation
- `solver_advanced.py`: Optimized local search solver

#### Running
```bash
cd Devoir2_INF8175_A24/RechercheLocale/code
python main.py --agent=naive --infile=instances/medium.txt --outfile=output.txt
python main.py --agent=advanced --infile=instances/medium.txt --outfile=output.txt
```

## Devoir 3: Neural Networks

**Location**: `Devoir3_INF8175_A24/students/`

### Description
Implementation of neural networks from scratch, including:
- Perceptron for binary classification
- Neural network for regression (sin(x) approximation)
- Neural network for digit classification (MNIST)

### Components Implemented

#### 1. Perceptron (`models.py`)
- Binary classification using linear decision boundary
- Training via perceptron learning algorithm

#### 2. Regression Model (`models.py`)
- Two-layer neural network with ReLU activation
- Approximates sin(x) function on [-2π, 2π]
- Architecture: 1 → 50 → 1

#### 3. Digit Classification Model (`models.py`)
- Two-layer neural network for MNIST digit classification
- Architecture: 784 (28×28) → 256 → 10
- Uses Softmax loss for multi-class classification

#### Key Files
- `models.py`: Model implementations (PerceptronModel, RegressionModel, DigitClassificationModel)
- `nn.py`: Neural network framework with backward propagation
- `backend.py`: Dataset classes and training utilities
- `data/`: MNIST and language identification datasets

#### Running
```bash
cd Devoir3_INF8175_A24/students
python autograder.py
```

## Final Project: Divercite Game AI

**Location**: `Projet_Divercite_A2024/Divercite/`

### Description
Implementation of an AI agent for the **Divercite** board game using the minimax algorithm with alpha-beta pruning.

### Game Overview
Divercite is a strategic board game where players place colored pieces (city and resource pieces) on a 9×9 grid to maximize diversity and score points.

### AI Implementation

#### Algorithm
- **Minimax with Alpha-Beta Pruning**: Searches game tree to optimal depth
- **Heuristic Function**: Evaluates game states based on score difference
- **Adaptive Depth**: Dynamic depth adjustment based on game progress

#### Key Features
- Custom heuristic evaluation function
- Efficient action generation (light and heavy actions)
- Optimized minimax implementation with alpha-beta pruning

#### Key Files
- `my_player.py`: Main AI player implementation
- `game_state_divercite.py`: Game state representation
- `board_divercite.py`: Board management
- `main_divercite.py`: Game execution script
- `GUI/`: Web-based graphical interface

#### Running the Game

**Local Game** (two AI players):
```bash
cd Projet_Divercite_A2024/Divercite
python main_divercite.py local my_player.py my_player.py
```

**Human vs Computer**:
```bash
python main_divercite.py human_vs_computer my_player.py
```

**Human vs Human**:
```bash
python main_divercite.py human_vs_human
```

**Network Game** (host):
```bash
python main_divercite.py host_game my_player.py -a YOUR_IP
```

**Network Game** (connect):
```bash
python main_divercite.py connect my_player.py -a HOST_IP
```

## Requirements

### Devoir 1
- Python 3.x
- No external dependencies beyond standard library

### Devoir 2
- **Constraint Programming**: MiniZinc compiler
- **Local Search**: Python 3.x, NetworkX, Matplotlib

### Devoir 3
- Python 3.x
- NumPy
- Matplotlib

### Final Project
- Python 3.x
- Seahorse framework (included)
- NetworkX
- Loguru

## Usage

### Setting Up Environment

1. Clone the repository:
```bash
git clone <repository-url>
cd PolyMTL_INF8175
```

2. Ensure Python 3.x is installed:
```bash
python3 --version
```

3. Install dependencies (if needed):
```bash
pip install numpy matplotlib networkx loguru
```

### Running Individual Components

Each component is self-contained and can be run independently. Navigate to the respective directory and follow the usage instructions above.

## Authors

- **LUCET Alistair** 
- **DELFORGE Raphaël**

## Academic Disclaimer

This work is submitted as coursework for INF8175 - Artificial Intelligence at Polytechnique Montréal. The code is provided for educational purposes only.

## License

Educational use only. See individual project PDFs for specific licensing information.

