import re
from FSharpGrammar.FSharpLexer import FSharpLexer
from FSharpGrammar.FSharpParser import FSharpParser
from antlr4 import InputStream, CommonTokenStream
from FSharpGrammar.FSharpParserVisitor import FSharpParserVisitor

class FVisitor(FSharpParserVisitor):
    """Class to define behavior of visit tree."""

    def __init__(self, operators: dict, operands: dict, indexMap: list):
        self._operators = operators
        self._operands = operands
        self._indexMap = indexMap

    def visitChildren(self, node):
        name = self._indexMap[node.getRuleIndex()]
        self.addNameOperator(name)
        return super().visitChildren(node)

    def addNameOperand(self, name:str, count = 1):
        if count == 0:
            return
        val = self._operands.get(name)
        if val is None:
            self._operands[name] = count
        else:
            self._operands[name] += count 

    def addNameOperator(self, name:str, count = 1):
        if count == 0:
            return
        val = self._operators.get(name)
        if val is None:
            self._operators[name] = count
        else:
            self._operators[name] += count
        
    # def visitDotIentifier(self, ctx: FSharpParser.DotIentifierContext):
    #     name = ctx.getText()
    #     self.addNameOperand(name)
    #     return super().visitDotIentifier(ctx)
    
    def visitIdentifier(self, ctx: FSharpParser.IdentifierContext):
        name = ctx.getText()
        self.addNameOperand(name)
        return super().visitIdentifier(ctx)

    def visitString(self, ctx: FSharpParser.StringContext): 
        name = ctx.getText()
        self.addNameOperand(name)
        interpolationSign_s = len(re.findall('%s', name))
        interpolationSign_d = len(re.findall('%d', name))
        interpolationSign_f = len(re.findall('%f', name))
        interpolationSign_c = len(re.findall('%c', name))
        interpolationSign_i = len(re.findall('%i', name))
        self.addNameOperator('%s', interpolationSign_s)
        self.addNameOperator('%d', interpolationSign_d)
        self.addNameOperator('%f', interpolationSign_f)
        self.addNameOperator('%c', interpolationSign_c)
        self.addNameOperator('%i', interpolationSign_i)
        return super().visitString(ctx)

    def visitInterpolated_string(self, ctx: FSharpParser.Interpolated_stringContext):  
        name = ctx.getText()
        self.addNameOperand(name)
        self.addNameOperator('$')
        pattern = re.compile(r'{.*}')
        for m in re.finditer(pattern, name):
            self.addNameOperator('{..}') 
            childOperators = {}
            childOperands = {}
            text = m.group(0)[1:-1]
            in_stream = InputStream(text)
            lexer = FSharpLexer(in_stream)
            stream = CommonTokenStream(lexer)
            parser = FSharpParser(stream)
            tree = parser.exprs()
            indexMap = parser.ruleNames
            childVisitor = FVisitor(childOperators, childOperands, indexMap) 
            childVisitor.visit(tree)
            for key, val in childOperands.items():
                self.addNameOperand(key, val)
            for key, val in childOperators.items():
                self.addNameOperator(key, val)
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
