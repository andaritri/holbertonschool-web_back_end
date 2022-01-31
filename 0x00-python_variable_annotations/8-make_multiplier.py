#!/usr/bin/env python3
"""File that contains make_multiplier function"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return multiplier by other float number"""
    return lambda n: n * multiplier
