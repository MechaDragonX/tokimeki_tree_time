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
    root = None

    def __init__(self) -> None:
        self.root = None
    # def __init__(self, value) -> None:
    #     self.root = TriNode[T](value)

    def contains(self, value) -> bool:
        return self.__contains(self.root, value)
    def __contains(self, current, value) -> bool:
        if (current.value == value):
            return True
        else:
            self.__contains(self, current.left, value)
            self.__contains(self, current.right, value)
            self.__contains(self, current.middle, value)
        return False
    
    def add(self, value) -> None:
        return self.__add(self.root, value)

    def __add(self, current, value) -> None:
        if current == None and self.root == None:
            self.root = TriNode[T](value)
            return
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
            self.__add(current.left, value)
            self.__add(current.right, value)
            self.__add(current.middle, value)
    
    def printNodes(self) -> None:
        self.printNodes(self.root)
    def __printNodes(self, current) -> None:
        if current == None:
            return
        
        print(current.value)
        self.__printNodes(current.left)
        self.__printNodes(current.middle)
        self.__printNodes(current.right)
