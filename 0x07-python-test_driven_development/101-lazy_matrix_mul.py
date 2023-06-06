#!/usr/bin/python3
# 101-lazy_matrix_mul.py
""" defines a matrix mult function using Numpy. """
import numpy as n
def lazy_matrix_mul(m_a, m_b):
    """
    return the mult of two matrices
    """
    return (n.matmul(m_a, m_b))
