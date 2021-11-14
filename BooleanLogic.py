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

        # Process lines and save to output variables
        inputs = [None] * len(self.inVars)
        for line in lines:
            cells = BooleanLogic._lineToArray(line)
            for i in range(len(self.inVars)):
                inputs[i] = cells[i]
            for i in range(len(self.inVars)-1, len(self.outVars) + len(self.inVars)):
                if cells[i].strip() == '1':
                   self.outVars[i-len(self.inVars)][1].append(copy.deepcopy(inputs))
        print(self.outVars)
        print(self.inVars)

    def getMinimal(self) -> str:
        X = ttvars('x', len(self.inVars))
        ret = ""
        for i in range(len(self.outVars)):
            ret += self.outVars[i][0] + " "
            arrayAsString = ""
            for j in self.outTable[i]:
                arrayAsString += j
            ret += self.pyedaToTex(str(espresso_tts(truthtable(X, arrayAsString))[0]))
            ret += "\n"
        return ret

    def getUnminimalised(self) -> str:
        ret = ""
        for i in self.outVars:
            ret += "| "
            ret += i[0]
            ret += " | $"
            for j in i[1]:
                ret += self.getTex(j)
                ret += " + "
            ret = ret[:-3] + "$ |\n"
        return ret
        
    def pyedaToTex(self, s: str) -> str:
        s = s.replace("Or", "")
        s = s.replace("And", "")
        s = s.replace(",", "")
        s = s.replace(") (", "+")
        s = s.replace("((", "")
        s = s.replace("))", "")
        s = s.replace(" ", "")
        for i in range(len(self.inVars)):
            s = s.replace("x[" + str(i) + "]", self.inVars[i])
        for i in range(len(self.inVars)):
            s = s.replace("~" + self.inVars[i], "\\bar{" + self.inVars[i] + "}")
        s = s.replace("+", " + ")
        return "$" + s + "$"

    def getTex(self, arr: list) -> str:
        ret = ""
        for i in range(len(arr)):
            if arr[i] == '1':
                ret += self.inVars[i]
            else:
                ret += "\\bar{" + self.inVars[i] + "}"
        return ret
