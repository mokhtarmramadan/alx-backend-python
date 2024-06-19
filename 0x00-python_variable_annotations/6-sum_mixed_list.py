#!/usr/bin/env python3
''' sum mixed list'''
from typing import Union, List


def sum_mixed_list(mxd_lst: Union[List[int], List[float]]) -> float:
    ''' takes a list mxd_lst of integers and floats and
    returns their sum as a float '''
    sum_float: float = sum([i for i in mxd_lst])
    return sum_float
