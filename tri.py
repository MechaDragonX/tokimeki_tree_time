#!/usr/bin/env python

from typing import TypeVar, Generic

T = TypeVar('T')

class TriNode(Generic[T]):
    value = ""
    left = None
    middle = None
    right = None
    
    def __init__(self, val) -> None:
        value = val

class Tri(Generic[T]):
    __root = None

    def __init__(self, value) -> None:
        _root = TriNode[T](value)

    def contains(self, value) -> bool:
        return self.__contains(self.__root, value)
    def __contains(self, current, value) -> bool:
        if (current.value == value):
            return True
        else :
            self.__contains(self, current.left, value)
            self.__contains(self, current.right, value)
            self.__contains(self, current.middle, value)
        return False
