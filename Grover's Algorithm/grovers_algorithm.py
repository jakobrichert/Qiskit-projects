"""
Grover's Algorithm - Quantum Search Algorithm
Provides quadratic speedup for unstructured search problems
"""

from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram, plot_bloch_multivector
import matplotlib.pyplot as plt
import numpy as np

def initialize_s(qc, qubits):
    """Apply Hadamard gates to create superposition"""
    for q in qubits:
        qc.h(q)
    return qc

def oracle(qc, qubits, target):
    """
    Oracle function that marks the target state
    For a 2-qubit system searching for |11⟩
    """
    if target == '11':
        # Multi-controlled Z gate (CZ for 2 qubits)
        qc.cz(qubits[0], qubits[1])
    elif target == '10':
        qc.x(qubits[1])
        qc.cz(qubits[0], qubits[1])
        qc.x(qubits[1])
    elif target == '01':
        qc.x(qubits[0])
        qc.cz(qubits[0], qubits[1])
        qc.x(qubits[0])
    elif target == '00':
        qc.x(qubits[0])
        qc.x(qubits[1])
        qc.cz(qubits[0], qubits[1])
        qc.x(qubits[0])
        qc.x(qubits[1])
    return qc

def diffuser(qc, qubits):
    """
    Grover diffusion operator - amplifies the amplitude of the target state
    Also known as inversion about average
    """
    # Apply Hadamard gates
    for q in qubits:
        qc.h(q)

    # Apply X gates
    for q in qubits:
        qc.x(q)

    # Multi-controlled Z
    qc.h(qubits[-1])
    qc.mct(qubits[:-1], qubits[-1])  # multi-controlled Toffoli
    qc.h(qubits[-1])

    # Apply X gates
    for q in qubits:
        qc.x(q)

    # Apply Hadamard gates
    for q in qubits:
        qc.h(q)

    return qc

def grover_algorithm(target='11', n_qubits=2):
    """
    Execute Grover's algorithm to search for a target state

    Args:
        target: Binary string representing the target state
        n_qubits: Number of qubits
    """
    # Calculate optimal number of iterations
    # For N=4 states, optimal is pi/4 * sqrt(N) ≈ 1 iteration
    n_iterations = int(np.pi/4 * np.sqrt(2**n_qubits))

    # Create quantum circuit
    qc = QuantumCircuit(n_qubits, n_qubits)
    qubits = list(range(n_qubits))

    # Initialize superposition
    qc = initialize_s(qc, qubits)
    qc.barrier()

    # Apply Grover iteration
    for _ in range(n_iterations):
        qc = oracle(qc, qubits, target)
        qc.barrier()
        qc = diffuser(qc, qubits)
        qc.barrier()

    # Measure
    qc.measure(qubits, qubits)

    return qc

if __name__ == "__main__":
    # Search for state |11⟩
    print("Grover's Algorithm - Searching for state |11⟩")
    print("=" * 50)

    target = '11'
    qc = grover_algorithm(target=target, n_qubits=2)

    # Draw circuit
    print("\nQuantum Circuit:")
    print(qc.draw(output='text'))

    # Execute on simulator
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, backend=simulator, shots=1024).result()
    counts = result.get_counts()

    print(f"\nMeasurement Results:")
    print(f"Target state |{target}⟩ was found with probability: {counts.get(target, 0)/1024:.2%}")
    print(f"\nAll results: {counts}")

    # Visualize
    print("\nGenerating histogram...")
    plot_histogram(counts)
    plt.title(f"Grover's Algorithm Results - Searching for |{target}⟩")
    plt.savefig("Grover's Algorithm/grovers_results.png", dpi=300, bbox_inches='tight')
    print("Histogram saved as 'grovers_results.png'")
