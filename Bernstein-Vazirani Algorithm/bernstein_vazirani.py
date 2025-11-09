"""
Bernstein-Vazirani Algorithm
Finds a hidden binary string in a single query
Classical approach requires n queries, quantum needs only 1
"""

from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram, circuit_drawer
import matplotlib.pyplot as plt

def bv_oracle(secret_string):
    """
    Create an oracle that encodes a secret string

    The oracle implements f(x) = s·x (mod 2)
    where s is the secret string and · is the dot product

    Args:
        secret_string: binary string to encode (e.g., '101')

    Returns:
        QuantumCircuit representing the oracle
    """
    n = len(secret_string)
    oracle_qc = QuantumCircuit(n + 1)

    # Reverse the secret string to match Qiskit's qubit ordering
    secret_string = secret_string[::-1]

    for i, bit in enumerate(secret_string):
        if bit == '1':
            oracle_qc.cx(i, n)

    oracle_gate = oracle_qc.to_gate()
    oracle_gate.name = f"Oracle: {secret_string[::-1]}"
    return oracle_gate

def bernstein_vazirani_circuit(secret_string):
    """
    Create the Bernstein-Vazirani circuit

    Args:
        secret_string: binary string to find

    Returns:
        QuantumCircuit
    """
    n = len(secret_string)
    qc = QuantumCircuit(n + 1, n)

    # Initialize ancilla qubit in |1⟩
    qc.x(n)

    # Apply Hadamard gates to all qubits
    for i in range(n + 1):
        qc.h(i)

    qc.barrier()

    # Apply oracle
    oracle = bv_oracle(secret_string)
    qc.append(oracle, range(n + 1))

    qc.barrier()

    # Apply Hadamard gates to input qubits
    for i in range(n):
        qc.h(i)

    # Measure
    qc.measure(range(n), range(n))

    return qc

def run_bernstein_vazirani(secret_string):
    """
    Execute the Bernstein-Vazirani algorithm

    Args:
        secret_string: binary string to find

    Returns:
        circuit and measurement results
    """
    qc = bernstein_vazirani_circuit(secret_string)

    # Execute
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, backend=simulator, shots=1024).result()
    counts = result.get_counts()

    return qc, counts

if __name__ == "__main__":
    print("Bernstein-Vazirani Algorithm")
    print("=" * 60)
    print("This algorithm finds a hidden binary string in a single query")
    print("Classical algorithm needs n queries")
    print("Quantum algorithm needs only 1 query!\n")

    # Test with different secret strings
    test_cases = ['101', '1101', '10101', '11111']

    for secret in test_cases:
        print(f"\nFinding secret string: {secret}")
        print("-" * 60)

        qc, counts = run_bernstein_vazirani(secret)

        # The measurement should give us the secret string
        measured = max(counts, key=counts.get)

        print(f"Secret string:   {secret}")
        print(f"Measured string: {measured}")
        print(f"Match: {'✓ YES!' if measured == secret else '✗ NO'}")
        print(f"Measurement counts: {counts}")

        # For the first test case, show the circuit
        if secret == test_cases[0]:
            print("\nCircuit structure:")
            print(qc.draw(output='text'))

    # Visualize results for a specific case
    print(f"\nGenerating visualization for secret string '{test_cases[1]}'...")
    qc, counts = run_bernstein_vazirani(test_cases[1])

    plt.figure(figsize=(10, 5))
    plot_histogram(counts)
    plt.title(f"Bernstein-Vazirani Algorithm Results\nSecret String: {test_cases[1]}")
    plt.savefig("Bernstein-Vazirani Algorithm/bv_results.png", dpi=300, bbox_inches='tight')
    print("Histogram saved as 'bv_results.png'")

    print("\n" + "=" * 60)
    print("Key Insight:")
    print("The algorithm finds the entire secret string with just 1 query!")
    print("Classically, you would need to query the oracle n times,")
    print("once for each bit of the secret string.")
    print("=" * 60)
