"""Library for flattening nested instances of container types.

Python library for common functionalities related to flattening
nested instances of container types.
"""
from types import GeneratorType
import doctest

def _is_container(instance):
    return isinstance(instance, (
        tuple, list, set, frozenset,
        GeneratorType
    ))

def flats(xss, depth=1):
    """
    Flatten an instance that consists of nested values
    of a container type.

    >>> list(flats([[1,2,3],[4,5,6,7]]))
    [1, 2, 3, 4, 5, 6, 7]
    >>> list(flats([(1,2,3), (4,5,6,7)]))
    [1, 2, 3, 4, 5, 6, 7]
    >>> list(flats([[[1,2],3],[4,5,6,7]], depth=2))
    [1, 2, 3, 4, 5, 6, 7]
    >>> list(flats([[[1,2],[3]],[[4,5],[6,7]]], depth=2))
    [1, 2, 3, 4, 5, 6, 7]
    >>> list(flats([[[1,2],3],[4,5,6,7]], depth=1))
    [[1, 2], 3, 4, 5, 6, 7]
    >>> list(flats([[[1,2],3],[4,5,6,7]], depth=0))
    [[[1, 2], 3], [4, 5, 6, 7]]
    >>> list(flats([[[1,[2]],3],[4,[[[5]]],6,7]], depth=float('inf')))
    [1, 2, 3, 4, 5, 6, 7]
    """
    if depth == 1: # Most common case is first for efficiency.
        for xs in xss:
            if _is_container(xs):
                for x in xs:
                    yield x
            else:
                yield xs
    elif depth == 0: # For consistency, base case is also a generator.
        for xs in xss:
            yield xs
    else: # General recursive case.
        for xs in xss:
            if isinstance(depth, int) and depth >= 1:
                if _is_container(xs):
                    for x in flats(xs, depth=(depth - 1)):
                        yield x
                else:
                    yield xs
            elif depth == float('inf'):
                if _is_container(xs):
                    for x in flats(xs, depth=float('inf')):
                        yield x
                else:
                    yield xs
            elif not isinstance(depth, int) and depth == float('inf'):
                raise TypeError('depth must be an integer or infinity')
            elif isinstance(depth, int) and depth < 0:
                raise ValueError('depth must be a non-negative integer or infinity')
            else:
                raise ValueError('depth value is invalid')

if __name__ == "__main__": 
    doctest.testmod()
