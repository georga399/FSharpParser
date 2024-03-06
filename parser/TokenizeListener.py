# Generated from Tokenize.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TokenizeParser import TokenizeParser
else:
    from TokenizeParser import TokenizeParser

# This class defines a complete listener for a parse tree produced by TokenizeParser.
class TokenizeListener(ParseTreeListener):

    # Enter a parse tree produced by TokenizeParser#dot.
    def enterDot(self, ctx:TokenizeParser.DotContext):
        pass

    # Exit a parse tree produced by TokenizeParser#dot.
    def exitDot(self, ctx:TokenizeParser.DotContext):
        pass


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


    # Enter a parse tree produced by TokenizeParser#fun_type.
    def enterFun_type(self, ctx:TokenizeParser.Fun_typeContext):
        pass

    # Exit a parse tree produced by TokenizeParser#fun_type.
    def exitFun_type(self, ctx:TokenizeParser.Fun_typeContext):
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


    # Enter a parse tree produced by TokenizeParser#while_do.
    def enterWhile_do(self, ctx:TokenizeParser.While_doContext):
        pass

    # Exit a parse tree produced by TokenizeParser#while_do.
    def exitWhile_do(self, ctx:TokenizeParser.While_doContext):
        pass


    # Enter a parse tree produced by TokenizeParser#for.
    def enterFor(self, ctx:TokenizeParser.ForContext):
        pass

    # Exit a parse tree produced by TokenizeParser#for.
    def exitFor(self, ctx:TokenizeParser.ForContext):
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


    # Enter a parse tree produced by TokenizeParser#not_equal.
    def enterNot_equal(self, ctx:TokenizeParser.Not_equalContext):
        pass

    # Exit a parse tree produced by TokenizeParser#not_equal.
    def exitNot_equal(self, ctx:TokenizeParser.Not_equalContext):
        pass


    # Enter a parse tree produced by TokenizeParser#less.
    def enterLess(self, ctx:TokenizeParser.LessContext):
        pass

    # Exit a parse tree produced by TokenizeParser#less.
    def exitLess(self, ctx:TokenizeParser.LessContext):
        pass


    # Enter a parse tree produced by TokenizeParser#less_equal.
    def enterLess_equal(self, ctx:TokenizeParser.Less_equalContext):
        pass

    # Exit a parse tree produced by TokenizeParser#less_equal.
    def exitLess_equal(self, ctx:TokenizeParser.Less_equalContext):
        pass


    # Enter a parse tree produced by TokenizeParser#greater.
    def enterGreater(self, ctx:TokenizeParser.GreaterContext):
        pass

    # Exit a parse tree produced by TokenizeParser#greater.
    def exitGreater(self, ctx:TokenizeParser.GreaterContext):
        pass


    # Enter a parse tree produced by TokenizeParser#greater_equal.
    def enterGreater_equal(self, ctx:TokenizeParser.Greater_equalContext):
        pass

    # Exit a parse tree produced by TokenizeParser#greater_equal.
    def exitGreater_equal(self, ctx:TokenizeParser.Greater_equalContext):
        pass


    # Enter a parse tree produced by TokenizeParser#equal.
    def enterEqual(self, ctx:TokenizeParser.EqualContext):
        pass

    # Exit a parse tree produced by TokenizeParser#equal.
    def exitEqual(self, ctx:TokenizeParser.EqualContext):
        pass


    # Enter a parse tree produced by TokenizeParser#and.
    def enterAnd(self, ctx:TokenizeParser.AndContext):
        pass

    # Exit a parse tree produced by TokenizeParser#and.
    def exitAnd(self, ctx:TokenizeParser.AndContext):
        pass


    # Enter a parse tree produced by TokenizeParser#or.
    def enterOr(self, ctx:TokenizeParser.OrContext):
        pass

    # Exit a parse tree produced by TokenizeParser#or.
    def exitOr(self, ctx:TokenizeParser.OrContext):
        pass


    # Enter a parse tree produced by TokenizeParser#lshift.
    def enterLshift(self, ctx:TokenizeParser.LshiftContext):
        pass

    # Exit a parse tree produced by TokenizeParser#lshift.
    def exitLshift(self, ctx:TokenizeParser.LshiftContext):
        pass


    # Enter a parse tree produced by TokenizeParser#rshift.
    def enterRshift(self, ctx:TokenizeParser.RshiftContext):
        pass

    # Exit a parse tree produced by TokenizeParser#rshift.
    def exitRshift(self, ctx:TokenizeParser.RshiftContext):
        pass


    # Enter a parse tree produced by TokenizeParser#log_mul.
    def enterLog_mul(self, ctx:TokenizeParser.Log_mulContext):
        pass

    # Exit a parse tree produced by TokenizeParser#log_mul.
    def exitLog_mul(self, ctx:TokenizeParser.Log_mulContext):
        pass


    # Enter a parse tree produced by TokenizeParser#log_add.
    def enterLog_add(self, ctx:TokenizeParser.Log_addContext):
        pass

    # Exit a parse tree produced by TokenizeParser#log_add.
    def exitLog_add(self, ctx:TokenizeParser.Log_addContext):
        pass


    # Enter a parse tree produced by TokenizeParser#log_xor.
    def enterLog_xor(self, ctx:TokenizeParser.Log_xorContext):
        pass

    # Exit a parse tree produced by TokenizeParser#log_xor.
    def exitLog_xor(self, ctx:TokenizeParser.Log_xorContext):
        pass


    # Enter a parse tree produced by TokenizeParser#log_not.
    def enterLog_not(self, ctx:TokenizeParser.Log_notContext):
        pass

    # Exit a parse tree produced by TokenizeParser#log_not.
    def exitLog_not(self, ctx:TokenizeParser.Log_notContext):
        pass


    # Enter a parse tree produced by TokenizeParser#not.
    def enterNot(self, ctx:TokenizeParser.NotContext):
        pass

    # Exit a parse tree produced by TokenizeParser#not.
    def exitNot(self, ctx:TokenizeParser.NotContext):
        pass


    # Enter a parse tree produced by TokenizeParser#pipe.
    def enterPipe(self, ctx:TokenizeParser.PipeContext):
        pass

    # Exit a parse tree produced by TokenizeParser#pipe.
    def exitPipe(self, ctx:TokenizeParser.PipeContext):
        pass


    # Enter a parse tree produced by TokenizeParser#compos.
    def enterCompos(self, ctx:TokenizeParser.ComposContext):
        pass

    # Exit a parse tree produced by TokenizeParser#compos.
    def exitCompos(self, ctx:TokenizeParser.ComposContext):
        pass


    # Enter a parse tree produced by TokenizeParser#assign.
    def enterAssign(self, ctx:TokenizeParser.AssignContext):
        pass

    # Exit a parse tree produced by TokenizeParser#assign.
    def exitAssign(self, ctx:TokenizeParser.AssignContext):
        pass


    # Enter a parse tree produced by TokenizeParser#type.
    def enterType(self, ctx:TokenizeParser.TypeContext):
        pass

    # Exit a parse tree produced by TokenizeParser#type.
    def exitType(self, ctx:TokenizeParser.TypeContext):
        pass


    # Enter a parse tree produced by TokenizeParser#module.
    def enterModule(self, ctx:TokenizeParser.ModuleContext):
        pass

    # Exit a parse tree produced by TokenizeParser#module.
    def exitModule(self, ctx:TokenizeParser.ModuleContext):
        pass


    # Enter a parse tree produced by TokenizeParser#open.
    def enterOpen(self, ctx:TokenizeParser.OpenContext):
        pass

    # Exit a parse tree produced by TokenizeParser#open.
    def exitOpen(self, ctx:TokenizeParser.OpenContext):
        pass


    # Enter a parse tree produced by TokenizeParser#namespace.
    def enterNamespace(self, ctx:TokenizeParser.NamespaceContext):
        pass

    # Exit a parse tree produced by TokenizeParser#namespace.
    def exitNamespace(self, ctx:TokenizeParser.NamespaceContext):
        pass


    # Enter a parse tree produced by TokenizeParser#class.
    def enterClass(self, ctx:TokenizeParser.ClassContext):
        pass

    # Exit a parse tree produced by TokenizeParser#class.
    def exitClass(self, ctx:TokenizeParser.ClassContext):
        pass


    # Enter a parse tree produced by TokenizeParser#do.
    def enterDo(self, ctx:TokenizeParser.DoContext):
        pass

    # Exit a parse tree produced by TokenizeParser#do.
    def exitDo(self, ctx:TokenizeParser.DoContext):
        pass


    # Enter a parse tree produced by TokenizeParser#new.
    def enterNew(self, ctx:TokenizeParser.NewContext):
        pass

    # Exit a parse tree produced by TokenizeParser#new.
    def exitNew(self, ctx:TokenizeParser.NewContext):
        pass


    # Enter a parse tree produced by TokenizeParser#then.
    def enterThen(self, ctx:TokenizeParser.ThenContext):
        pass

    # Exit a parse tree produced by TokenizeParser#then.
    def exitThen(self, ctx:TokenizeParser.ThenContext):
        pass


    # Enter a parse tree produced by TokenizeParser#seq.
    def enterSeq(self, ctx:TokenizeParser.SeqContext):
        pass

    # Exit a parse tree produced by TokenizeParser#seq.
    def exitSeq(self, ctx:TokenizeParser.SeqContext):
        pass


    # Enter a parse tree produced by TokenizeParser#list.
    def enterList(self, ctx:TokenizeParser.ListContext):
        pass

    # Exit a parse tree produced by TokenizeParser#list.
    def exitList(self, ctx:TokenizeParser.ListContext):
        pass


    # Enter a parse tree produced by TokenizeParser#array.
    def enterArray(self, ctx:TokenizeParser.ArrayContext):
        pass

    # Exit a parse tree produced by TokenizeParser#array.
    def exitArray(self, ctx:TokenizeParser.ArrayContext):
        pass


    # Enter a parse tree produced by TokenizeParser#map.
    def enterMap(self, ctx:TokenizeParser.MapContext):
        pass

    # Exit a parse tree produced by TokenizeParser#map.
    def exitMap(self, ctx:TokenizeParser.MapContext):
        pass


    # Enter a parse tree produced by TokenizeParser#generator.
    def enterGenerator(self, ctx:TokenizeParser.GeneratorContext):
        pass

    # Exit a parse tree produced by TokenizeParser#generator.
    def exitGenerator(self, ctx:TokenizeParser.GeneratorContext):
        pass


    # Enter a parse tree produced by TokenizeParser#set.
    def enterSet(self, ctx:TokenizeParser.SetContext):
        pass

    # Exit a parse tree produced by TokenizeParser#set.
    def exitSet(self, ctx:TokenizeParser.SetContext):
        pass


    # Enter a parse tree produced by TokenizeParser#async_rule.
    def enterAsync_rule(self, ctx:TokenizeParser.Async_ruleContext):
        pass

    # Exit a parse tree produced by TokenizeParser#async_rule.
    def exitAsync_rule(self, ctx:TokenizeParser.Async_ruleContext):
        pass


    # Enter a parse tree produced by TokenizeParser#task.
    def enterTask(self, ctx:TokenizeParser.TaskContext):
        pass

    # Exit a parse tree produced by TokenizeParser#task.
    def exitTask(self, ctx:TokenizeParser.TaskContext):
        pass


    # Enter a parse tree produced by TokenizeParser#exclamation_mark.
    def enterExclamation_mark(self, ctx:TokenizeParser.Exclamation_markContext):
        pass

    # Exit a parse tree produced by TokenizeParser#exclamation_mark.
    def exitExclamation_mark(self, ctx:TokenizeParser.Exclamation_markContext):
        pass


    # Enter a parse tree produced by TokenizeParser#match_with.
    def enterMatch_with(self, ctx:TokenizeParser.Match_withContext):
        pass

    # Exit a parse tree produced by TokenizeParser#match_with.
    def exitMatch_with(self, ctx:TokenizeParser.Match_withContext):
        pass


    # Enter a parse tree produced by TokenizeParser#try_with_finally.
    def enterTry_with_finally(self, ctx:TokenizeParser.Try_with_finallyContext):
        pass

    # Exit a parse tree produced by TokenizeParser#try_with_finally.
    def exitTry_with_finally(self, ctx:TokenizeParser.Try_with_finallyContext):
        pass


    # Enter a parse tree produced by TokenizeParser#use.
    def enterUse(self, ctx:TokenizeParser.UseContext):
        pass

    # Exit a parse tree produced by TokenizeParser#use.
    def exitUse(self, ctx:TokenizeParser.UseContext):
        pass


    # Enter a parse tree produced by TokenizeParser#using.
    def enterUsing(self, ctx:TokenizeParser.UsingContext):
        pass

    # Exit a parse tree produced by TokenizeParser#using.
    def exitUsing(self, ctx:TokenizeParser.UsingContext):
        pass


    # Enter a parse tree produced by TokenizeParser#raise.
    def enterRaise(self, ctx:TokenizeParser.RaiseContext):
        pass

    # Exit a parse tree produced by TokenizeParser#raise.
    def exitRaise(self, ctx:TokenizeParser.RaiseContext):
        pass


    # Enter a parse tree produced by TokenizeParser#reraise.
    def enterReraise(self, ctx:TokenizeParser.ReraiseContext):
        pass

    # Exit a parse tree produced by TokenizeParser#reraise.
    def exitReraise(self, ctx:TokenizeParser.ReraiseContext):
        pass


    # Enter a parse tree produced by TokenizeParser#failwith.
    def enterFailwith(self, ctx:TokenizeParser.FailwithContext):
        pass

    # Exit a parse tree produced by TokenizeParser#failwith.
    def exitFailwith(self, ctx:TokenizeParser.FailwithContext):
        pass


    # Enter a parse tree produced by TokenizeParser#invalidArg.
    def enterInvalidArg(self, ctx:TokenizeParser.InvalidArgContext):
        pass

    # Exit a parse tree produced by TokenizeParser#invalidArg.
    def exitInvalidArg(self, ctx:TokenizeParser.InvalidArgContext):
        pass


    # Enter a parse tree produced by TokenizeParser#exception_of.
    def enterException_of(self, ctx:TokenizeParser.Exception_ofContext):
        pass

    # Exit a parse tree produced by TokenizeParser#exception_of.
    def exitException_of(self, ctx:TokenizeParser.Exception_ofContext):
        pass


    # Enter a parse tree produced by TokenizeParser#member.
    def enterMember(self, ctx:TokenizeParser.MemberContext):
        pass

    # Exit a parse tree produced by TokenizeParser#member.
    def exitMember(self, ctx:TokenizeParser.MemberContext):
        pass


    # Enter a parse tree produced by TokenizeParser#val.
    def enterVal(self, ctx:TokenizeParser.ValContext):
        pass

    # Exit a parse tree produced by TokenizeParser#val.
    def exitVal(self, ctx:TokenizeParser.ValContext):
        pass


    # Enter a parse tree produced by TokenizeParser#struct.
    def enterStruct(self, ctx:TokenizeParser.StructContext):
        pass

    # Exit a parse tree produced by TokenizeParser#struct.
    def exitStruct(self, ctx:TokenizeParser.StructContext):
        pass


    # Enter a parse tree produced by TokenizeParser#with_get_set.
    def enterWith_get_set(self, ctx:TokenizeParser.With_get_setContext):
        pass

    # Exit a parse tree produced by TokenizeParser#with_get_set.
    def exitWith_get_set(self, ctx:TokenizeParser.With_get_setContext):
        pass


    # Enter a parse tree produced by TokenizeParser#tuple.
    def enterTuple(self, ctx:TokenizeParser.TupleContext):
        pass

    # Exit a parse tree produced by TokenizeParser#tuple.
    def exitTuple(self, ctx:TokenizeParser.TupleContext):
        pass


    # Enter a parse tree produced by TokenizeParser#with.
    def enterWith(self, ctx:TokenizeParser.WithContext):
        pass

    # Exit a parse tree produced by TokenizeParser#with.
    def exitWith(self, ctx:TokenizeParser.WithContext):
        pass


    # Enter a parse tree produced by TokenizeParser#record.
    def enterRecord(self, ctx:TokenizeParser.RecordContext):
        pass

    # Exit a parse tree produced by TokenizeParser#record.
    def exitRecord(self, ctx:TokenizeParser.RecordContext):
        pass


    # Enter a parse tree produced by TokenizeParser#of.
    def enterOf(self, ctx:TokenizeParser.OfContext):
        pass

    # Exit a parse tree produced by TokenizeParser#of.
    def exitOf(self, ctx:TokenizeParser.OfContext):
        pass


    # Enter a parse tree produced by TokenizeParser#enum.
    def enterEnum(self, ctx:TokenizeParser.EnumContext):
        pass

    # Exit a parse tree produced by TokenizeParser#enum.
    def exitEnum(self, ctx:TokenizeParser.EnumContext):
        pass


    # Enter a parse tree produced by TokenizeParser#inherit.
    def enterInherit(self, ctx:TokenizeParser.InheritContext):
        pass

    # Exit a parse tree produced by TokenizeParser#inherit.
    def exitInherit(self, ctx:TokenizeParser.InheritContext):
        pass


    # Enter a parse tree produced by TokenizeParser#default.
    def enterDefault(self, ctx:TokenizeParser.DefaultContext):
        pass

    # Exit a parse tree produced by TokenizeParser#default.
    def exitDefault(self, ctx:TokenizeParser.DefaultContext):
        pass


    # Enter a parse tree produced by TokenizeParser#override.
    def enterOverride(self, ctx:TokenizeParser.OverrideContext):
        pass

    # Exit a parse tree produced by TokenizeParser#override.
    def exitOverride(self, ctx:TokenizeParser.OverrideContext):
        pass


    # Enter a parse tree produced by TokenizeParser#abstract.
    def enterAbstract(self, ctx:TokenizeParser.AbstractContext):
        pass

    # Exit a parse tree produced by TokenizeParser#abstract.
    def exitAbstract(self, ctx:TokenizeParser.AbstractContext):
        pass


    # Enter a parse tree produced by TokenizeParser#base.
    def enterBase(self, ctx:TokenizeParser.BaseContext):
        pass

    # Exit a parse tree produced by TokenizeParser#base.
    def exitBase(self, ctx:TokenizeParser.BaseContext):
        pass


    # Enter a parse tree produced by TokenizeParser#colon_q.
    def enterColon_q(self, ctx:TokenizeParser.Colon_qContext):
        pass

    # Exit a parse tree produced by TokenizeParser#colon_q.
    def exitColon_q(self, ctx:TokenizeParser.Colon_qContext):
        pass


    # Enter a parse tree produced by TokenizeParser#interface.
    def enterInterface(self, ctx:TokenizeParser.InterfaceContext):
        pass

    # Exit a parse tree produced by TokenizeParser#interface.
    def exitInterface(self, ctx:TokenizeParser.InterfaceContext):
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