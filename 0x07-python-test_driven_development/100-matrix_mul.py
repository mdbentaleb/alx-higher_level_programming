#!/usr/bin/python3
""" matrix multiplication function """


def matrix_mul(m_a, m_b):
    """ multiply two matrices

    Args:
        m_a: first matrix
        m_b: second matrix
    Raises:
        TypeError: If either m_a or m_b isnot a list of lists of ints/floats
        TypeError: If either m_a or m_b isempty.
        TypeError: If either m_a or m_b hasdifferent-sized rows.
        ValueError: If m_a and m_b cannot bemultiplied.
    Returns:
        A new matrix representingthemultiplication of m_a by m_b.
    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inverted_b = []
    for k in range(len(m_b[0])):
        new_row = []
        for u in range(len(m_b)):
            new_row.append(m_b[u][k])
        inverted_b.append(new_row)

    new_matrix = []
    for rw in m_a:
        new_row = []
        for cl in inverted_b:
            prd = 0
            for p in range(len(inverted_b[0])):
                prd += rw[p] * cl[p]
            new_row.append(prd)
        new_matrix.append(new_row)

    return new_matrix
