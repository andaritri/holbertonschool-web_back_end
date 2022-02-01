#!/usr/bin/env python3
"""File that contains zoom_array function"""
from typing import List, Tuple


def zoom_array(
    lst: Tuple,
    factor: int = 2
) -> List:
    """Put type annotations for a function"""
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), int(3.0))
