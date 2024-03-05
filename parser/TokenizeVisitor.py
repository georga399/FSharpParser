# Generated from Tokenize.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TokenizeParser import TokenizeParser
else:
    from TokenizeParser import TokenizeParser

# This class defines a complete generic visitor for a parse tree produced by TokenizeParser.

class TokenizeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TokenizeParser#dotIentifier.
    def visitDotIentifier(self, ctx:TokenizeParser.DotIentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#int.
    def visitInt(self, ctx:TokenizeParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#float.
    def visitFloat(self, ctx:TokenizeParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#unit.
    def visitUnit(self, ctx:TokenizeParser.UnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#bool.
    def visitBool(self, ctx:TokenizeParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#char.
    def visitChar(self, ctx:TokenizeParser.CharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#missing_arg.
    def visitMissing_arg(self, ctx:TokenizeParser.Missing_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#interpolationSign.
    def visitInterpolationSign(self, ctx:TokenizeParser.InterpolationSignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#dollar.
    def visitDollar(self, ctx:TokenizeParser.DollarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#string.
    def visitString(self, ctx:TokenizeParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#attribute.
    def visitAttribute(self, ctx:TokenizeParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#round_brackets.
    def visitRound_brackets(self, ctx:TokenizeParser.Round_bracketsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#rec.
    def visitRec(self, ctx:TokenizeParser.RecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#public.
    def visitPublic(self, ctx:TokenizeParser.PublicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#private.
    def visitPrivate(self, ctx:TokenizeParser.PrivateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#internal.
    def visitInternal(self, ctx:TokenizeParser.InternalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#mutable.
    def visitMutable(self, ctx:TokenizeParser.MutableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#let.
    def visitLet(self, ctx:TokenizeParser.LetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#fun.
    def visitFun(self, ctx:TokenizeParser.FunContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#typezation.
    def visitTypezation(self, ctx:TokenizeParser.TypezationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#if_then_elif_else.
    def visitIf_then_elif_else(self, ctx:TokenizeParser.If_then_elif_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#add.
    def visitAdd(self, ctx:TokenizeParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#mul.
    def visitMul(self, ctx:TokenizeParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#div.
    def visitDiv(self, ctx:TokenizeParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#minus.
    def visitMinus(self, ctx:TokenizeParser.MinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#pow.
    def visitPow(self, ctx:TokenizeParser.PowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#mod.
    def visitMod(self, ctx:TokenizeParser.ModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#equal.
    def visitEqual(self, ctx:TokenizeParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#expression.
    def visitExpression(self, ctx:TokenizeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#exprs.
    def visitExprs(self, ctx:TokenizeParser.ExprsContext):
        return self.visitChildren(ctx)



del TokenizeParser