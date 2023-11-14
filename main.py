from src.models.state_machine import AsynchronousStateMachine
from src.utils.utils import extract_minterms_from_truth_table, calculate_hamming_distances
from src.algorithms.quine_mccluskey import quine_mccluskey
from src.visualization.circuit_diagram import draw_circuit_diagrams

def create_state_machine(num_states=2):
    """
    Creates an asynchronous state machine, generates and prints the truth table,
    calculates and prints Hamming distances, minterms, maxterms, and draws circuit diagrams.

    :param num_states: Number of states in the state machine.
    """
    # Create an instance of AsynchronousStateMachine with a specified number of states
    sm = AsynchronousStateMachine(num_states)

    # Generate the truth table for the state machine
    truth_table = sm.truth_table()

    # Calculate the number of bits needed to represent the state
    num_state_bits = len(bin(num_states - 1)) - 2

    # Extract minterms from the truth table
    minterms = extract_minterms_from_truth_table(truth_table, num_state_bits)

    # Define the number of variables for the Quine-McCluskey algorithm
    num_vars = num_state_bits + 1

    # Apply the Quine-McCluskey algorithm to simplify the minterms
    simplified = quine_mccluskey(minterms, num_vars)
    
    # Calculate and print Hamming distances between all state pairs
    hamming_distances = calculate_hamming_distances(sm.states)
    print("Hamming Distances:")
    for pair, distance in hamming_distances.items():
        print(f"{pair}: {distance}")

    # Print the truth table
    print("\nTruth Table:")
    for row in truth_table:
        print(row)

    # Print minterms and maxterms
    maxterms = sm.maxterms()
    print("\nMinterms:", minterms)
    print("\nMaxterms:", maxterms)
    print("\nsimplified", simplified)

    # Draw the circuit diagrams based on the test inputs
    test_inputs = [0, 1, 0, 1, 0, 1, 0, 0, 1]
    draw_circuit_diagrams(sm, test_inputs)

if __name__ == "__main__":
    # Create and test the state machine with a specified number of states
    create_state_machine(4)
