def count_ones(num):
    """
    Counts the number of ones in the binary representation of a number.

    :param num: Integer to count the ones in.
    :return: Number of ones in the binary representation of num.
    """
    return bin(num).count('1')

def hamming_distance(a, b):
    """
    Calculates the Hamming distance between two binary numbers.
    
    :param a: First binary number.
    :param b: Second binary number.
    :return: Hamming distance between a and b.
    """
    xor_result = a ^ b
    return count_ones(xor_result)

def merge_minterms(a, b, num_vars):
    """
    Merges two minterms if they differ by exactly one bit.

    :param a: First minterm.
    :param b: Second minterm.
    :param num_vars: Number of variables in the minterms.
    :return: Merged minterm or None if they differ by more than one bit.
    """
    if hamming_distance(a, b) == 1:
        return a ^ (a & -a)
    return None

def quine_mccluskey(minterms, num_vars):
    """
    Implements the Quine-McCluskey algorithm for Boolean minimization.

    :param minterms: List of minterms to minimize.
    :param num_vars: Number of variables in the minterms.
    :return: List of simplified minterms.
    """
    groups = {}
    for minterm in minterms:
        ones_count = count_ones(minterm)
        if ones_count not in groups:
            groups[ones_count] = []
        groups[ones_count].append(minterm)
        
    new_minterms = set(minterms)
    while True:
        new_groups = {}
        visited = set()
        for ones_count in groups:
            if ones_count + 1 in groups:
                for minterm1 in groups[ones_count]:
                    for minterm2 in groups[ones_count + 1]:
                        merged = merge_minterms(minterm1, minterm2, num_vars)
                        if merged is not None:
                            if ones_count not in new_groups:
                                new_groups[ones_count] = []
                            new_groups[ones_count].append(merged)
                            visited.add(minterm1)
                            visited.add(minterm2)
                            new_minterms.add(merged)
                            
        if len(new_groups) == 0:
            break
        groups = new_groups
        
    primes = new_minterms - visited
    return list(primes)
