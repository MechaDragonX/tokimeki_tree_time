#!/usr/bin/env python

from tri import Tri
from dialog import Dialog

class TextParser:
    def import_all_dialog(path) -> Tri[Dialog]:
        file = open(path, 'r')
        lines = file.readlines()
        i = 0
        while i < len(lines):
            lines[i] = lines[i][:-1]
            i += 1

        currentName = ''
        tri = Tri()
        for line in lines:
            if line.find('@') == 0 and len(line) != 0:
                currentName = line[1:len(line)]
            elif line != '@':
                tri.add(Dialog(currentName, line))
        
        return tri
