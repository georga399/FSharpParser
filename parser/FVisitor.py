from TokenizeLexer import TokenizeLexer
from TokenizeParser import TokenizeParser
from TokenizeVisitor import TokenizeVisitor

class FVisitor(TokenizeVisitor):

    def __init__(self, operators:dict, operands: dict, indexMap:list):
        self._operators = operators
        self._operands = operands
        self._indexMap = indexMap

    def visitChildren(self, node):
        # print(type(node))
        
        name = self._indexMap[node.getRuleIndex()]
        val = self._operators.get(name)
        if val is None:
            self._operators[name] = 1
        else:
            self._operators[name] += 1
        return super().visitChildren(node)

    # def visitAttribute(self, ctx: TokenizeParser.AttributeContext):
    #     # print(ctx.getRuleIndex)
    #     val = self._operators.get('[<..>]')
    #     if val is None:
    #         self._operators['[<..>]'] = 1
    #     else:
    #         self._operators['[<..>]'] += 1 
    #     return super().visitAttribute(ctx)
    def addNameOperand(self, name:str):
        val = self._operands.get(name)
        if val is None:
            self._operands[name] = 1
        else:
            self._operands[name] += 1 

    def visitDotIentifier(self, ctx: TokenizeParser.DotIentifierContext):
        name = ctx.getText()
        self.addNameOperand(name)
        return super().visitDotIentifier(ctx)
    
    def visitString(self, ctx: TokenizeParser.StringContext):
        name = ctx.getText()
        self.addNameOperand(name)
        return super().visitString(ctx)
    
    def visitChar(self, ctx: TokenizeParser.CharContext):
        name = ctx.getText()
        self.addNameOperand(name)
        return super().visitChar(ctx)
    
    def visitInt(self, ctx: TokenizeParser.IntContext):
        name = ctx.getText()
        self.addNameOperand(name)
        return super().visitInt(ctx)
    
    def visitFloat(self, ctx: TokenizeParser.FloatContext):
        name = ctx.getText()
        self.addNameOperand(name)
        return super().visitFloat(ctx)