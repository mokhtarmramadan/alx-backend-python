#!/usr/bin/env python3
'''  type-annotated list '''
from typing import List


def sum_list(input_list: List[float]) -> float:
    ''' which takes a list input_list of floats as argument
    and returns their sum as a float '''
    sum_float: float = 0.0
    sum_float = sum([i for i in input_list])
    return sum_float
