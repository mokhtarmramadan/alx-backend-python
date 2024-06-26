#!/usr/bin/env python3
''' make multiplier '''
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    ''' takes a float multiplier as argument and returns a function
    that multiplies a float by multiplier '''
    return lambda x: x * multiplier
