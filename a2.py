def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    if len(dna1) > len(dna2):
        return True



def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """


    num_occurrences = 0

    for char in dna:
        if char in nucleotide:
            num_occurrences = num_occurrences + 1

    return num_occurrences
        


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    if dna2 in dna1:
        return True
    else:
        return False


def is_valid_sequence(dna):
    """ (str) -> int

    Return True if and only if the DNA sequence is valid(that is, it contains no characters other than 'A', 'T', 'C' and 'G')

    >>> is_valid_sequence('AGTCTGCGGG')
    True
    >>> is_valid_sequence('ACXGATCG')
    False
    >>> is_valid_sequence('FfFff')
    False
    >>> is_valid_sequence('AAA')
    True
    >>> is_valid_sequence('agtc')
    False
    """

    for char in dna:
        if char not in 'ATCG':
            return False
        else:
            return True



def insert_sequence(dna1, dna2, i):
    """ (str, str, int) -> str

    Return the DNA sequence obtained by inserting the second DNA sequence into the first DNA sequence at the given index.

    >>>insert_sequence('GATCGG', 'AA', 2)
    'GAAATCGG'
    >>>insert_sequence('ATC', 'TATCG', -1)
    'ATCTATCG'
    >>>insert_sequence('CGATATCAGG', 'G', 0)
    'GCGATATCAGG'
    """


    if i == 0:
        return dna2 + dna1
    else:
        return dna1[:i] + dna2 + dna1[i:]


def get_complement(nucleotide):
    """(str) -> str

    For the complement nucleotide for the given nucleotide.
    
    >>>get_complement('A')
    T
    >>>get_complement('T')
    A
    >>>get_complement('C')
    G
    >>>get_complement('G')
    C
    """


    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'


def get_complementary_sequence(dna):
    """(str) -> str

    Returns the DNA sequence complementary to the given DNA sequence.

    >>>get_complementary_sequence('ATG')
    'TAC'
    >>>get_complementary_sequence('CTAGGC')
    'GATCCG'
    >>get_complementary_sequence('CG')
    'GC'
    """

    new_sequence = ''

    for char in dna:
        if char in 'ATCG':
            new_sequence = new_sequence + get_complement(char)

    return new_sequence
    
    
    


    

