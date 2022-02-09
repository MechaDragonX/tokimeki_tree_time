#!/usr/bin/env python

from typing import TypeVar, Generic

T = TypeVar('T')

class TriNode(Generic[T]):
    __value = ""
    __left = None
    __middle = None
    __right = None
    
    def __init__(self, value) -> None:
        __value = value

class Tri(Generic[T]):
    __root = None

    def __init__(self, value) -> None:
        _root = TriNode[T](value)
