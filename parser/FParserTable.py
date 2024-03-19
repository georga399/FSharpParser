from parser.FVisitor import FVisitor
from parser.FSharpGrammar.FSharpLexer import FSharpLexer
from parser.FSharpGrammar.FSharpParser import FSharpParser
from antlr4 import InputStream, CommonTokenStream


class FParserTable:
    """Class to get dictionary of operators and operands of F# code."""

    def __init__(self):
        self._operators = {}
        self._operands = {}

    def SetText(self, text: str):
        """Set text for parsing."""
        self.text = text
        in_stream = InputStream(text)
        lexer = FSharpLexer(in_stream)
        stream = CommonTokenStream(lexer)
        parser = FSharpParser(stream)
        tree = parser.exprs()
        indexMap = parser.ruleNames
        visitor = FVisitor(self._operators, self._operands, indexMap)
        visitor.visit(tree)

    def GetOperators(self) -> dict:
        """Get dictionary of operators."""
        return self._operators

    def GetOperands(self) -> dict:
        """Get dictionary of type of rules (operands)."""
        return self._operands
