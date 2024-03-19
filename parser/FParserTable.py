from FVisitor import FVisitor
from FSharpGrammar.FSharpLexer import FSharpLexer
from FSharpGrammar.FSharpParser import FSharpParser
from antlr4 import InputStream, CommonTokenStream

class FParserTable:
    """Class to get dictionary of operators and operands of F# code."""
    def __init__(self):
        self._rules = {}
        self._operators = {}
        self._rem_list = ['exprs', 'expression', 
                          'string', 'dotIentifier', 
                          'interpolated_string', 
                          'char', 'int', 'float', 'dot']
        self._operands = {}


    def SetText(self, text:str):
        """Set text for parsing."""
        self.text = text
        in_stream = InputStream(text)
        lexer = FSharpLexer(in_stream)
        stream = CommonTokenStream(lexer)
        parser = FSharpParser(stream)
        tree = parser.exprs()
        indexMap = parser.ruleNames
        visitor = FVisitor(self._rules, self._operands, indexMap)
        visitor.visit(tree)
        self._operators = {key: self._rules[key] 
             for key in self._rules if key not in self._rem_list}

    def getRules(self) -> dict:
        """Get dictionary of rules"""
        return self._rules

    def GetOperators(self) -> dict:   
        """Get dictionary of operators."""  
        return self._operators

    def GetOperands(self) -> dict:
        """Get dictionary of operands."""
        return self._operands