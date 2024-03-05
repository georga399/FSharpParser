from FVisitor import FVisitor
from TokenizeLexer import TokenizeLexer
from TokenizeParser import TokenizeParser
from antlr4 import InputStream, CommonTokenStream
import typing

class FParserTable:

    def __init__(self):
        self._operators = {}
        self._operands = {}

    def SetText(self, text:str):
        self.text = text
        in_stream = InputStream(text)
        lexer = TokenizeLexer(in_stream)
        stream = CommonTokenStream(lexer)
        parser = TokenizeParser(stream)
        tree = parser.exprs()
        visitor = FVisitor(self._operators, self._operands)
        visitor.visit(tree)

    def GetOperators(self) -> dict:     
        return self._operators

    def GetOperands(self) -> dict:
        return self._operands