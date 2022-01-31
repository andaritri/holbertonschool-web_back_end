#!/usr/bin/env python3
"""File that contains to_kv function"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple with v argument at the begining and the second
    position the square of v.
    """
    return (k, v**2)
