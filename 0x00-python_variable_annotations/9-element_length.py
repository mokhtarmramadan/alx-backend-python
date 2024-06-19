#!/usr/bin/env python3
''' Annotate the below function’s parameters '''
import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> typing.List[
        typing.Tuple[typing.Sequence, int]]:
    ''' fun '''
    return [(i, len(i)) for i in lst]
