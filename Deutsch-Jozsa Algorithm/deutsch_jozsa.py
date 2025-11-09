"""
Deutsch-Jozsa Algorithm
Determines whether a function is constant or balanced with a single query
Demonstrates quantum advantage over classical algorithms
"""

from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import numpy as np

def deutsch_jozsa_oracle(case, n):
    """
    Create an oracle for the Deutsch-Jozsa algorithm

    Args:
        case: 'balanced' or 'constant'
        n: number of qubits (excluding ancilla)

    Returns:
        QuantumCircuit representing the oracle
    """
    oracle_qc = QuantumCircuit(n + 1)

    if case == 'balanced':
        # Balanced function: f(x) returns 0 for half inputs, 1 for other half
        # Simple balanced oracle: output depends on the first qubit
        for i in range(n):
            oracle_qc.cx(i, n)
    else:
        # Constant function: f(x) = 0 for all inputs (do nothing)
        # or f(x) = 1 for all inputs (flip the output qubit)
        if np.random.randint(2) == 1:
            oracle_qc.x(n)

    oracle_gate = oracle_qc.to_gate()
    oracle_gate.name = "Oracle"
    return oracle_gate

def deutsch_jozsa_circuit(oracle, n):
    """
    Create the complete Deutsch-Jozsa circuit

    Args:
        oracle: Oracle gate
        n: number of qubits (excluding ancilla)

    Returns:
        QuantumCircuit
    """
    qc = QuantumCircuit(n + 1, n)

    # Initialize ancilla qubit in |1⟩ state
    qc.x(n)

    # Apply Hadamard gates to all qubits
    for i in range(n + 1):
        qc.h(i)

    qc.barrier()

    # Apply oracle
    qc.append(oracle, range(n + 1))

    qc.barrier()

    # Apply Hadamard gates to input qubits
    for i in range(n):
        qc.h(i)

    # Measure input qubits
    qc.measure(range(n), range(n))

    return qc

def run_deutsch_jozsa(case='balanced', n=3):
    """
    Execute the Deutsch-Jozsa algorithm

    Args:
        case: 'balanced' or 'constant'
        n: number of qubits (excluding ancilla)

    Returns:
        measurement results
    """
    # Create oracle
    oracle = deutsch_jozsa_oracle(case, n)

    # Create circuit
    qc = deutsch_jozsa_circuit(oracle, n)

    # Execute
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, backend=simulator, shots=1024).result()
    counts = result.get_counts()

    return qc, counts

if __name__ == "__main__":
    print("Deutsch-Jozsa Algorithm")
    print("=" * 60)
    print("This algorithm determines if a function is constant or balanced")
    print("Classical algorithms need 2^(n-1) + 1 queries in worst case")
    print("Quantum algorithm needs only 1 query!\n")

    n_qubits = 3

    # Test balanced case
    print(f"\nTest Case 1: BALANCED function ({n_qubits} qubits)")
    print("-" * 60)
    qc_balanced, counts_balanced = run_deutsch_jozsa('balanced', n_qubits)

    all_zeros = '0' * n_qubits
    if all_zeros in counts_balanced and counts_balanced[all_zeros] > 900:
        result = "CONSTANT"
    else:
        result = "BALANCED"

    print(f"Measurement results: {counts_balanced}")
    print(f"Algorithm output: {result}")
    print(f"✓ Correct!" if result == "BALANCED" else "✗ Incorrect")

    # Test constant case
    print(f"\nTest Case 2: CONSTANT function ({n_qubits} qubits)")
    print("-" * 60)
    qc_constant, counts_constant = run_deutsch_jozsa('constant', n_qubits)

    all_zeros = '0' * n_qubits
    if all_zeros in counts_constant and counts_constant[all_zeros] > 900:
        result = "CONSTANT"
    else:
        result = "BALANCED"

    print(f"Measurement results: {counts_constant}")
    print(f"Algorithm output: {result}")
    print(f"✓ Correct!" if result == "CONSTANT" else "✗ Incorrect")

    # Visualize circuit
    print("\nCircuit structure (balanced case):")
    print(qc_balanced.draw(output='text'))

    # Create comparison plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

    # Plot balanced results
    ax1.bar(counts_balanced.keys(), counts_balanced.values())
    ax1.set_title('Balanced Function')
    ax1.set_xlabel('Measurement Outcome')
    ax1.set_ylabel('Counts')

    # Plot constant results
    ax2.bar(counts_constant.keys(), counts_constant.values())
    ax2.set_title('Constant Function')
    ax2.set_xlabel('Measurement Outcome')
    ax2.set_ylabel('Counts')

    plt.tight_layout()
    plt.savefig("Deutsch-Jozsa Algorithm/deutsch_jozsa_results.png", dpi=300, bbox_inches='tight')
    print("\nResults visualization saved as 'deutsch_jozsa_results.png'")

    print("\n" + "=" * 60)
    print("Key Insight:")
    print("If we measure all 0s → function is CONSTANT")
    print("If we measure anything else → function is BALANCED")
    print("=" * 60)
