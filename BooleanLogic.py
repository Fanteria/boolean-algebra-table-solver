import os
import copy
from pyeda.inter import *

class BooleanLogic:
    def __init__(self, table: str, letter: str, bonusLines: int = 1) -> None:
        self.inVars = []
        self.outVars = []
        self.outTable = []
        self.processLines(table, letter, bonusLines)

    @staticmethod
    def _lineToArray(line: str) -> list:
        return [l.strip() for l in line.split('|') if l.strip()]

    @staticmethod
    def _BoolArrayToNumber(arr: list) -> int:
        ret = 0
        powNumber = 0
        for i in reversed(arr):
            if i == "1":
                ret += pow(2, powNumber)
            powNumber += 1
        return ret

    def processLines(self, table:str, lastIn:str, bonusLines:int) -> None:
        # Remove empty lines in table
        lines = [s for s in table.splitlines() if s]
        end = False

        # Read line with variables
        BooleanLogic._lineToArray(lines[0])
        for i in BooleanLogic._lineToArray(lines[0]):
            if not end:
                self.inVars.append(i)
            else:
                self.outVars.append((i, []))
                continue
            if i == lastIn:
                end = True
        
        # Remove line with variables and unnessesery lines
        for i in range(bonusLines + 1):
            del lines[0]

        inputs = [None] * len(self.inVars)
        for line in lines:
            cells = BooleanLogic._lineToArray(line)
            for i in range(len(self.inVars)):
                inputs[i] = cells[i]
            number = BooleanLogic._BoolArrayToNumber(inputs)
            for i in range(len(self.inVars)-1, len(self.outVars) + len(self.inVars)):
                if cells[i].strip() == '1':
                   self.outVars[i-len(self.inVars)][1].append(number)
        print(self.outVars)
        print(self.inVars)