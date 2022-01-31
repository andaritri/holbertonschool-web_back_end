#!/usr/bin/env python3
"""File that contains element_lengh function"""


from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples"""
    return [(i, len(i)) for i in lst]
