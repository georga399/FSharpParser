import re
from FSharpGrammar.FSharpParser import FSharpParser
from FSharpGrammar.FSharpParserVisitor import FSharpParserVisitor 

class FVisitor(FSharpParserVisitor):
    """Class to define behavior of visit tree."""
    def __init__(self, operators:dict, operands: dict, indexMap:list):
        self._operators = operators
        self._operands = operands
        self._indexMap = indexMap

    def visitChildren(self, node):
        name = self._indexMap[node.getRuleIndex()]
        val = self._operators.get(name)
        if val is None:
            self._operators[name] = 1
        else:
            self._operators[name] += 1
        return super().visitChildren(node)

    def addNameOperand(self, name:str, count = 1):
        val = self._operands.get(name)
        if val is None:
            self._operands[name] = count
        else:
            self._operands[name] += count 

    def visitDotIentifier(self, ctx: FSharpParser.DotIentifierContext):
        name = ctx.getText()
        self.addNameOperand(name)
        return super().visitDotIentifier(ctx)
    
    def visitString(self, ctx: FSharpParser.StringContext): 
        name = ctx.getText()
        self.addNameOperand(name)
        interpolationSign_s = len(re.findall('%s', name))
        interpolationSign_d = len(re.findall('%d', name))
        interpolationSign_f = len(re.findall('%f', name))
        interpolationSign_c = len(re.findall('%c', name))
        self.addNameOperand('%s', interpolationSign_s)
        self.addNameOperand('%d', interpolationSign_d)
        self.addNameOperand('%f', interpolationSign_f)
        self.addNameOperand('%c', interpolationSign_c)
        return super().visitString(ctx)
    
    def visitInterpolated_string(self, ctx: FSharpParser.Interpolated_stringContext): #TODO FIND brackets
        name = ctx.getText()
        self.addNameOperand(name)
        return super().visitInterpolated_string(ctx)

    def visitChar(self, ctx: FSharpParser.CharContext):
        name = ctx.getText()
        self.addNameOperand(name)
        return super().visitChar(ctx)
    
    def visitInt(self, ctx: FSharpParser.IntContext):
        name = ctx.getText()
        self.addNameOperand(name)
        return super().visitInt(ctx)
    
    def visitFloat(self, ctx: FSharpParser.FloatContext):
        name = ctx.getText()
        self.addNameOperand(name)
        return super().visitFloat(ctx)