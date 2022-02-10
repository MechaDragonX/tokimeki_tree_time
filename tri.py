#!/usr/bin/env python

from typing import TypeVar, Generic

T = TypeVar('T')

class TriNode(Generic[T]):
    value = ''
    left = None
    middle = None
    right = None
    
    def __init__(self, val) -> None:
        self.value = val

class Tri(Generic[T]):
    __root = None

    def __init__(self, value) -> None:
        self.__root = TriNode[T](value)

    def contains(self, value) -> bool:
        return self.__contains(self.__root, value)
    def __contains(self, current, value) -> bool:
        if (current.value == value):
            return True
        else:
            self.__contains(self, current.left, value)
            self.__contains(self, current.right, value)
            self.__contains(self, current.middle, value)
        return False
    
    def add(self, value) -> None:
        return self.__add(self.__root, value)

    def __add(self, current, value) -> None:
        if current == None:
            return

        if current.left == None:
            current.left = TriNode[T](value)
            return
        elif current.middle == None:
            current.middle = TriNode[T](value)
            return
        elif current.right == None:
            current.right = TriNode[T](value)
            return
        else:
            self.add(current.left, value)
            self.add(current.right, value)
            self.add(current.middle, value)
