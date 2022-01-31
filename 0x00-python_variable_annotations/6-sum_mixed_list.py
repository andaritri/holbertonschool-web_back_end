#!/usr/bin/env python3
"""File that contains sum_mixed_list functions"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sums a list of integer and floats"""
    return sum(mxd_lst)
