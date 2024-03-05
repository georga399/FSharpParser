# Generated from Tokenize.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TokenizeParser import TokenizeParser
else:
    from TokenizeParser import TokenizeParser

# This class defines a complete listener for a parse tree produced by TokenizeParser.
class TokenizeListener(ParseTreeListener):

    # Enter a parse tree produced by TokenizeParser#dotIentifier.
    def enterDotIentifier(self, ctx:TokenizeParser.DotIentifierContext):
        pass

    # Exit a parse tree produced by TokenizeParser#dotIentifier.
    def exitDotIentifier(self, ctx:TokenizeParser.DotIentifierContext):
        pass


    # Enter a parse tree produced by TokenizeParser#int.
    def enterInt(self, ctx:TokenizeParser.IntContext):
        pass

    # Exit a parse tree produced by TokenizeParser#int.
    def exitInt(self, ctx:TokenizeParser.IntContext):
        pass


    # Enter a parse tree produced by TokenizeParser#float.
    def enterFloat(self, ctx:TokenizeParser.FloatContext):
        pass

    # Exit a parse tree produced by TokenizeParser#float.
    def exitFloat(self, ctx:TokenizeParser.FloatContext):
        pass


    # Enter a parse tree produced by TokenizeParser#unit.
    def enterUnit(self, ctx:TokenizeParser.UnitContext):
        pass

    # Exit a parse tree produced by TokenizeParser#unit.
    def exitUnit(self, ctx:TokenizeParser.UnitContext):
        pass


    # Enter a parse tree produced by TokenizeParser#bool.
    def enterBool(self, ctx:TokenizeParser.BoolContext):
        pass

    # Exit a parse tree produced by TokenizeParser#bool.
    def exitBool(self, ctx:TokenizeParser.BoolContext):
        pass


    # Enter a parse tree produced by TokenizeParser#char.
    def enterChar(self, ctx:TokenizeParser.CharContext):
        pass

    # Exit a parse tree produced by TokenizeParser#char.
    def exitChar(self, ctx:TokenizeParser.CharContext):
        pass


    # Enter a parse tree produced by TokenizeParser#missing_arg.
    def enterMissing_arg(self, ctx:TokenizeParser.Missing_argContext):
        pass

    # Exit a parse tree produced by TokenizeParser#missing_arg.
    def exitMissing_arg(self, ctx:TokenizeParser.Missing_argContext):
        pass


    # Enter a parse tree produced by TokenizeParser#interpolationSign.
    def enterInterpolationSign(self, ctx:TokenizeParser.InterpolationSignContext):
        pass

    # Exit a parse tree produced by TokenizeParser#interpolationSign.
    def exitInterpolationSign(self, ctx:TokenizeParser.InterpolationSignContext):
        pass


    # Enter a parse tree produced by TokenizeParser#dollar.
    def enterDollar(self, ctx:TokenizeParser.DollarContext):
        pass

    # Exit a parse tree produced by TokenizeParser#dollar.
    def exitDollar(self, ctx:TokenizeParser.DollarContext):
        pass


    # Enter a parse tree produced by TokenizeParser#string.
    def enterString(self, ctx:TokenizeParser.StringContext):
        pass

    # Exit a parse tree produced by TokenizeParser#string.
    def exitString(self, ctx:TokenizeParser.StringContext):
        pass


    # Enter a parse tree produced by TokenizeParser#attribute.
    def enterAttribute(self, ctx:TokenizeParser.AttributeContext):
        pass

    # Exit a parse tree produced by TokenizeParser#attribute.
    def exitAttribute(self, ctx:TokenizeParser.AttributeContext):
        pass


    # Enter a parse tree produced by TokenizeParser#round_brackets.
    def enterRound_brackets(self, ctx:TokenizeParser.Round_bracketsContext):
        pass

    # Exit a parse tree produced by TokenizeParser#round_brackets.
    def exitRound_brackets(self, ctx:TokenizeParser.Round_bracketsContext):
        pass


    # Enter a parse tree produced by TokenizeParser#rec.
    def enterRec(self, ctx:TokenizeParser.RecContext):
        pass

    # Exit a parse tree produced by TokenizeParser#rec.
    def exitRec(self, ctx:TokenizeParser.RecContext):
        pass


    # Enter a parse tree produced by TokenizeParser#public.
    def enterPublic(self, ctx:TokenizeParser.PublicContext):
        pass

    # Exit a parse tree produced by TokenizeParser#public.
    def exitPublic(self, ctx:TokenizeParser.PublicContext):
        pass


    # Enter a parse tree produced by TokenizeParser#private.
    def enterPrivate(self, ctx:TokenizeParser.PrivateContext):
        pass

    # Exit a parse tree produced by TokenizeParser#private.
    def exitPrivate(self, ctx:TokenizeParser.PrivateContext):
        pass


    # Enter a parse tree produced by TokenizeParser#internal.
    def enterInternal(self, ctx:TokenizeParser.InternalContext):
        pass

    # Exit a parse tree produced by TokenizeParser#internal.
    def exitInternal(self, ctx:TokenizeParser.InternalContext):
        pass


    # Enter a parse tree produced by TokenizeParser#mutable.
    def enterMutable(self, ctx:TokenizeParser.MutableContext):
        pass

    # Exit a parse tree produced by TokenizeParser#mutable.
    def exitMutable(self, ctx:TokenizeParser.MutableContext):
        pass


    # Enter a parse tree produced by TokenizeParser#let.
    def enterLet(self, ctx:TokenizeParser.LetContext):
        pass

    # Exit a parse tree produced by TokenizeParser#let.
    def exitLet(self, ctx:TokenizeParser.LetContext):
        pass


    # Enter a parse tree produced by TokenizeParser#fun.
    def enterFun(self, ctx:TokenizeParser.FunContext):
        pass

    # Exit a parse tree produced by TokenizeParser#fun.
    def exitFun(self, ctx:TokenizeParser.FunContext):
        pass


    # Enter a parse tree produced by TokenizeParser#typezation.
    def enterTypezation(self, ctx:TokenizeParser.TypezationContext):
        pass

    # Exit a parse tree produced by TokenizeParser#typezation.
    def exitTypezation(self, ctx:TokenizeParser.TypezationContext):
        pass


    # Enter a parse tree produced by TokenizeParser#if_then_elif_else.
    def enterIf_then_elif_else(self, ctx:TokenizeParser.If_then_elif_elseContext):
        pass

    # Exit a parse tree produced by TokenizeParser#if_then_elif_else.
    def exitIf_then_elif_else(self, ctx:TokenizeParser.If_then_elif_elseContext):
        pass


    # Enter a parse tree produced by TokenizeParser#add.
    def enterAdd(self, ctx:TokenizeParser.AddContext):
        pass

    # Exit a parse tree produced by TokenizeParser#add.
    def exitAdd(self, ctx:TokenizeParser.AddContext):
        pass


    # Enter a parse tree produced by TokenizeParser#mul.
    def enterMul(self, ctx:TokenizeParser.MulContext):
        pass

    # Exit a parse tree produced by TokenizeParser#mul.
    def exitMul(self, ctx:TokenizeParser.MulContext):
        pass


    # Enter a parse tree produced by TokenizeParser#div.
    def enterDiv(self, ctx:TokenizeParser.DivContext):
        pass

    # Exit a parse tree produced by TokenizeParser#div.
    def exitDiv(self, ctx:TokenizeParser.DivContext):
        pass


    # Enter a parse tree produced by TokenizeParser#minus.
    def enterMinus(self, ctx:TokenizeParser.MinusContext):
        pass

    # Exit a parse tree produced by TokenizeParser#minus.
    def exitMinus(self, ctx:TokenizeParser.MinusContext):
        pass


    # Enter a parse tree produced by TokenizeParser#pow.
    def enterPow(self, ctx:TokenizeParser.PowContext):
        pass

    # Exit a parse tree produced by TokenizeParser#pow.
    def exitPow(self, ctx:TokenizeParser.PowContext):
        pass


    # Enter a parse tree produced by TokenizeParser#mod.
    def enterMod(self, ctx:TokenizeParser.ModContext):
        pass

    # Exit a parse tree produced by TokenizeParser#mod.
    def exitMod(self, ctx:TokenizeParser.ModContext):
        pass


    # Enter a parse tree produced by TokenizeParser#equal.
    def enterEqual(self, ctx:TokenizeParser.EqualContext):
        pass

    # Exit a parse tree produced by TokenizeParser#equal.
    def exitEqual(self, ctx:TokenizeParser.EqualContext):
        pass


    # Enter a parse tree produced by TokenizeParser#expression.
    def enterExpression(self, ctx:TokenizeParser.ExpressionContext):
        pass

    # Exit a parse tree produced by TokenizeParser#expression.
    def exitExpression(self, ctx:TokenizeParser.ExpressionContext):
        pass


    # Enter a parse tree produced by TokenizeParser#exprs.
    def enterExprs(self, ctx:TokenizeParser.ExprsContext):
        pass

    # Exit a parse tree produced by TokenizeParser#exprs.
    def exitExprs(self, ctx:TokenizeParser.ExprsContext):
        pass



del TokenizeParser