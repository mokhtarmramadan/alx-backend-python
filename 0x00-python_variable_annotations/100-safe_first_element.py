#!/usr/bin/env python3
''' 'duck-typed '''
import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) -> typing.Union[
        typing.Any, None]:
    ''' fun '''
    if lst:
        return lst[0]
    else:
        return None
