def extract_minterms_from_truth_table(truth_table, num_state_bits):
    """
    Extracts minterms from the state machine's truth table.

    :param truth_table: The truth table as a list of tuples (current state, input, next state, output).
    :param num_state_bits: Number of bits used to represent the state.
    :return: A list of minterms where the output is 1.
    """
    minterms = []
    for row in truth_table:
        state, input_signal, _, output = row
        if output == 1:
            state_val = ord(state) - 65  # Convert state character to number (A=0, B=1, ...)
            minterm = (state_val << 1) + input_signal  # Combine state and input signal to form a minterm
            minterms.append(minterm)
    return minterms

from src.algorithms.quine_mccluskey import hamming_distance

def calculate_hamming_distances(states):
    """
    Calculates the Hamming distance between all pairs of states.

    :param states: List of states in the state machine.
    :return: Dictionary of Hamming distances between state pairs.
    """
    distances = {}
    for i, state1 in enumerate(states):
        for j, state2 in enumerate(states):
            if i < j:
                key = (state1, state2)
                distances[key] = hamming_distance(ord(state1) - 65, ord(state2) - 65)
    return distances
