#!/usr/bin/env python3
''' to kv '''
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    ''' eturns a tuple. The first element of the tuple is the string k '''
    square_v: float = v ** 2
    return (k, square_v)
