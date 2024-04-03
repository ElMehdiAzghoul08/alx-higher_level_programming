#!/usr/bin/python3

"""Lazy matrix multiplication"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """function that multiplies two matrices
    """

    return (np.matmul(m_a, m_b))
