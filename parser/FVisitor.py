from TokenizeLexer import TokenizeLexer
from TokenizeParser import TokenizeParser
from TokenizeVisitor import TokenizeVisitor

class FVisitor(TokenizeVisitor):

    def __init__(self, operators:dict, operands: dict):
        self._operators = operators
        self._operands = operands

    def visitAttribute(self, ctx: TokenizeParser.AttributeContext):
        val = self._operators.get('[<..>]')
        if val is None:
            self._operators['[<..>]'] = 1
        else:
            self._operators['[<..>]'] += 1 
        return super().visitAttribute(ctx)

    def visitDotIentifier(self, ctx: TokenizeParser.DotIentifierContext):
        name = ctx.getText()
        val = self._operands.get(name)
        if val is None:
            self._operands[name] = 1
        else:
            self._operands[name] += 1 
        return super().visitDotIentifier(ctx)