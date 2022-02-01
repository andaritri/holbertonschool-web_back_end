#!/usr/bin/env python3
"""File that contains zoom_array function"""
from typing import List, Any, Sequence, Union


def zoom_array(
    lst: Sequence[Any],
    factor: Union[int, float] = 2
) -> Sequence[Any]:
    """Put type annotations for a function"""
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
