#!/usr/bin/env python

class Dialog:
    name = ''
    text = ''

    def __init__(self, name, text) -> None:
        self.name = name
        self.text = text

    def __str__(self) -> str:
        return f'{self.name}: {self.text}'
