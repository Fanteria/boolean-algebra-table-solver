import os
import copy
from pyeda.inter import *

class BooleanLogic:
    texOutput: bool = True

    def __init__(self, table: str, letter: str, bonusLines: int = 1) -> None:
        self.inVars = []
        self.outVars = {}
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
        outVarsTable = []

        # Read line with variables
        BooleanLogic._lineToArray(lines[0])
        for i in BooleanLogic._lineToArray(lines[0]):
            if not end:
                self.inVars.append(i)
            else:
                outVarsTable.append((i, []))
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
            for i in range(len(self.inVars), len(outVarsTable) + len(self.inVars)):
                if cells[i].strip() == '1':
                   outVarsTable[i-len(self.inVars)][1].append(copy.deepcopy(inputs))
        self.outVars = dict((x, y) for x, y in outVarsTable)

    def getLine(self, outVar: str, outVarFunction) -> str:
        return "| " + outVar + " | " + outVarFunction(outVar) + " |\n"
    
    def getAll(self, minimal: bool = True):
        ret = ""
        func = self.getMinimal if minimal else self.getUnminimalised
        for i in self.outVars:
            ret += self.getLine(i, func) 
        return ret

    def getUnminimalised(self, outVar: str) -> str:
        ret = ""
        if self.texOutput:
            ret += "$"
        for i in self.outVars[outVar]:
            ret += self._getProductFromArray(i)
            ret += " + "
        ret = ret[:-3]
        if self.texOutput:
            ret += "$"
        return ret
    
    def getMinimal(self, outVar: str) -> str:
        # Create input variables for minimalization
        X = ttvars('x', len(self.inVars))

        # Create string of output values
        trueNumbers = []
        for i in self.outVars[outVar]:
            trueNumbers.append(BooleanLogic._BoolArrayToNumber(i))
        # if all is zero
        trueNumbers.sort()
        arrayAsString = ""
        for i in range(0, len(self.inVars) * len(self.inVars)):
            if i in trueNumbers:
                arrayAsString += "1"
            else:
                arrayAsString += "0"
        return self._pyedaToTex(str(espresso_tts(truthtable(X, arrayAsString))[0]))
        
    def _pyedaToTex(self, s: str) -> str:
        s = s.replace("Or", "")
        s = s.replace("And", "")
        s = s.replace(",", "")
        s = s.replace(") (", "+")
        s = s.replace("((", "")
        s = s.replace("))", "")
        s = s.replace(" ", "")
        for i in range(len(self.inVars)):
            s = s.replace("x[" + str(i) + "]", self.inVars[i])
        if self.texOutput:
            for i in range(len(self.inVars)):
                s = s.replace("~" + self.inVars[i], "\\bar{" + self.inVars[i] + "}")
        s = s.replace("+", " + ")
        if self.texOutput:
            return "$" + s + "$"
        return s

    def _getProductFromArray(self, arr: list) -> str:
        ret = ""
        for i in range(len(arr)):
            if arr[i] == '1':
                ret += self.inVars[i]
            else:
                if self.texOutput:
                    ret += "\\bar{" + self.inVars[i] + "}"
                else:
                    ret += '~' + self.inVars[i]
        return ret