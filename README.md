# Quantum Computing with Qiskit

A comprehensive collection of quantum computing algorithms and tutorials implemented using IBM's Qiskit framework. This repository demonstrates fundamental and advanced quantum algorithms with practical implementations.

## Overview

This repository contains hands-on implementations of key quantum algorithms that showcase the power of quantum computing. Each implementation includes detailed explanations and visualizations to help understand quantum mechanics principles.

## Implemented Algorithms

### 1. Shor's Algorithm 🔐
**Location:** `Shor's Algorithm/`

Shor's algorithm is a quantum algorithm for integer factorization that runs exponentially faster than the best known classical algorithms. This implementation demonstrates:
- Quantum Fourier Transform (QFT)
- Period finding using quantum phase estimation
- Factorization of composite numbers
- Statistical analysis of measurement outcomes

**Significance:** This algorithm famously threatens RSA encryption by efficiently factoring large numbers.

**Complexity:** Classical O(exp(n^1/3)), Quantum O(n^3)

### 2. Grover's Search Algorithm 🔍
**Location:** `Grover's Algorithm/`

Grover's algorithm provides quadratic speedup for searching unstructured databases:
- Oracle function for marking target states
- Amplitude amplification through Grover diffusion operator
- Optimal iteration count calculation
- Demonstration of quantum speedup

**Significance:** Searches N items in O(√N) time vs classical O(N).

**Speedup:** Quadratic advantage over classical search

### 3. Deutsch-Jozsa Algorithm ⚡
**Location:** `Deutsch-Jozsa Algorithm/`

Determines whether a function is constant or balanced with a single query:
- Oracle construction for different function types
- Quantum parallelism demonstration
- Single-query solution vs exponential classical queries

**Significance:** First algorithm to show quantum advantage over classical computing.

**Complexity:** Classical O(2^(n-1)), Quantum O(1)

### 4. Bernstein-Vazirani Algorithm 🎯
**Location:** `Bernstein-Vazirani Algorithm/`

Finds a hidden binary string in a single query:
- Secret string encoding in oracle
- Parallel information extraction
- Direct readout of hidden string

**Significance:** Demonstrates quantum parallelism in extracting global properties.

**Queries:** Classical n queries, Quantum 1 query

### 5. Quantum Teleportation 📡
**Location:** `Quantum Teleportation Algorithm/`

Implementation of the quantum teleportation protocol that transfers quantum states between qubits using:
- Quantum entanglement (Bell pair creation)
- Bell state measurements
- Controlled operations for state reconstruction

**Key Concept:** Demonstrates how quantum information can be transmitted using classical communication and pre-shared entanglement.

### 6. Basic Quantum Gates ⚙️
**Location:** `X gate Representation/`

Exploration of fundamental quantum gates including:
- Pauli-X gate (quantum NOT gate)
- Statevector visualization
- Bloch sphere representation
- Unitary matrix representation

### 7. Bell States and Entanglement 🔗
**Location:** `QIskit tutorial #1/`

Introduction to quantum entanglement through Bell state creation:
- Hadamard and CNOT gate operations
- Quantum circuit construction
- Simulation and execution on real IBM quantum hardware
- Measurement statistics analysis

## Requirements

- Python 3.7+
- Qiskit
- Qiskit-Aer (simulators)
- Matplotlib (visualization)
- NumPy
- Jupyter Notebook

Install dependencies:
```bash
pip install -r requirements.txt
```

## Getting Started

1. Clone this repository
2. Install the required dependencies
3. Open any of the Jupyter notebooks in the algorithm directories
4. Run the cells sequentially to see the algorithms in action

## Project Structure

```
Qiskit-projects/
├── Shor's Algorithm/                    # Integer factorization (exponential speedup)
├── Grover's Algorithm/                  # Quantum search (quadratic speedup)
├── Deutsch-Jozsa Algorithm/             # Constant vs balanced function detection
├── Bernstein-Vazirani Algorithm/        # Hidden string finding
├── Quantum Teleportation Algorithm/     # State transfer protocol
├── X gate Representation/               # Basic quantum gates
├── QIskit tutorial #1/                  # Bell states and entanglement
├── requirements.txt                     # Python dependencies
├── .gitignore                          # Git ignore rules
└── README.md                           # This file
```

## Quantum Computing Concepts Demonstrated

- **Superposition**: Qubits existing in multiple states simultaneously
- **Entanglement**: Correlation between qubits stronger than classical physics allows
- **Quantum Interference**: Amplifying correct answers and canceling wrong ones
- **Measurement**: Collapsing quantum states to classical bits
- **Quantum Gates**: Operations that manipulate quantum states

## Algorithm Comparison

| Algorithm | Problem | Classical Complexity | Quantum Complexity | Speedup |
|-----------|---------|---------------------|-------------------|---------|
| Shor's Algorithm | Factorization | O(exp(n^1/3)) | O(n^3) | Exponential |
| Grover's Algorithm | Search | O(N) | O(√N) | Quadratic |
| Deutsch-Jozsa | Function Type | O(2^(n-1)) | O(1) | Exponential |
| Bernstein-Vazirani | Hidden String | O(n) | O(1) | Linear |

## Future Enhancements

Planned additions to this repository:
- Variational Quantum Eigensolver (VQE)
- Quantum Approximate Optimization Algorithm (QAOA)
- Simon's Algorithm
- Additional quantum cryptography protocols (BB84, E91)

## Resources

- [Qiskit Documentation](https://qiskit.org/documentation/)
- [IBM Quantum Experience](https://quantum-computing.ibm.com/)
- [Qiskit Textbook](https://qiskit.org/textbook/)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

Built with IBM Qiskit, the open-source quantum computing framework.
