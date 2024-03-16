# Generated from FSharpGrammar/FSharpParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .FSharpParser import FSharpParser
else:
    from FSharpParser import FSharpParser

# This class defines a complete listener for a parse tree produced by FSharpParser.
class FSharpParserListener(ParseTreeListener):

    # Enter a parse tree produced by FSharpParser#dot.
    def enterDot(self, ctx:FSharpParser.DotContext):
        pass

    # Exit a parse tree produced by FSharpParser#dot.
    def exitDot(self, ctx:FSharpParser.DotContext):
        pass


    # Enter a parse tree produced by FSharpParser#dotIentifier.
    def enterDotIentifier(self, ctx:FSharpParser.DotIentifierContext):
        pass

    # Exit a parse tree produced by FSharpParser#dotIentifier.
    def exitDotIentifier(self, ctx:FSharpParser.DotIentifierContext):
        pass


    # Enter a parse tree produced by FSharpParser#int.
    def enterInt(self, ctx:FSharpParser.IntContext):
        pass

    # Exit a parse tree produced by FSharpParser#int.
    def exitInt(self, ctx:FSharpParser.IntContext):
        pass


    # Enter a parse tree produced by FSharpParser#float.
    def enterFloat(self, ctx:FSharpParser.FloatContext):
        pass

    # Exit a parse tree produced by FSharpParser#float.
    def exitFloat(self, ctx:FSharpParser.FloatContext):
        pass


    # Enter a parse tree produced by FSharpParser#unit.
    def enterUnit(self, ctx:FSharpParser.UnitContext):
        pass

    # Exit a parse tree produced by FSharpParser#unit.
    def exitUnit(self, ctx:FSharpParser.UnitContext):
        pass


    # Enter a parse tree produced by FSharpParser#bool.
    def enterBool(self, ctx:FSharpParser.BoolContext):
        pass

    # Exit a parse tree produced by FSharpParser#bool.
    def exitBool(self, ctx:FSharpParser.BoolContext):
        pass


    # Enter a parse tree produced by FSharpParser#char.
    def enterChar(self, ctx:FSharpParser.CharContext):
        pass

    # Exit a parse tree produced by FSharpParser#char.
    def exitChar(self, ctx:FSharpParser.CharContext):
        pass


    # Enter a parse tree produced by FSharpParser#missing_arg.
    def enterMissing_arg(self, ctx:FSharpParser.Missing_argContext):
        pass

    # Exit a parse tree produced by FSharpParser#missing_arg.
    def exitMissing_arg(self, ctx:FSharpParser.Missing_argContext):
        pass


    # Enter a parse tree produced by FSharpParser#interpolationSign.
    def enterInterpolationSign(self, ctx:FSharpParser.InterpolationSignContext):
        pass

    # Exit a parse tree produced by FSharpParser#interpolationSign.
    def exitInterpolationSign(self, ctx:FSharpParser.InterpolationSignContext):
        pass


    # Enter a parse tree produced by FSharpParser#dollar.
    def enterDollar(self, ctx:FSharpParser.DollarContext):
        pass

    # Exit a parse tree produced by FSharpParser#dollar.
    def exitDollar(self, ctx:FSharpParser.DollarContext):
        pass


    # Enter a parse tree produced by FSharpParser#string.
    def enterString(self, ctx:FSharpParser.StringContext):
        pass

    # Exit a parse tree produced by FSharpParser#string.
    def exitString(self, ctx:FSharpParser.StringContext):
        pass


    # Enter a parse tree produced by FSharpParser#interpolated_string.
    def enterInterpolated_string(self, ctx:FSharpParser.Interpolated_stringContext):
        pass

    # Exit a parse tree produced by FSharpParser#interpolated_string.
    def exitInterpolated_string(self, ctx:FSharpParser.Interpolated_stringContext):
        pass


    # Enter a parse tree produced by FSharpParser#attribute.
    def enterAttribute(self, ctx:FSharpParser.AttributeContext):
        pass

    # Exit a parse tree produced by FSharpParser#attribute.
    def exitAttribute(self, ctx:FSharpParser.AttributeContext):
        pass


    # Enter a parse tree produced by FSharpParser#round_brackets.
    def enterRound_brackets(self, ctx:FSharpParser.Round_bracketsContext):
        pass

    # Exit a parse tree produced by FSharpParser#round_brackets.
    def exitRound_brackets(self, ctx:FSharpParser.Round_bracketsContext):
        pass


    # Enter a parse tree produced by FSharpParser#rec.
    def enterRec(self, ctx:FSharpParser.RecContext):
        pass

    # Exit a parse tree produced by FSharpParser#rec.
    def exitRec(self, ctx:FSharpParser.RecContext):
        pass


    # Enter a parse tree produced by FSharpParser#public.
    def enterPublic(self, ctx:FSharpParser.PublicContext):
        pass

    # Exit a parse tree produced by FSharpParser#public.
    def exitPublic(self, ctx:FSharpParser.PublicContext):
        pass


    # Enter a parse tree produced by FSharpParser#private.
    def enterPrivate(self, ctx:FSharpParser.PrivateContext):
        pass

    # Exit a parse tree produced by FSharpParser#private.
    def exitPrivate(self, ctx:FSharpParser.PrivateContext):
        pass


    # Enter a parse tree produced by FSharpParser#internal.
    def enterInternal(self, ctx:FSharpParser.InternalContext):
        pass

    # Exit a parse tree produced by FSharpParser#internal.
    def exitInternal(self, ctx:FSharpParser.InternalContext):
        pass


    # Enter a parse tree produced by FSharpParser#mutable.
    def enterMutable(self, ctx:FSharpParser.MutableContext):
        pass

    # Exit a parse tree produced by FSharpParser#mutable.
    def exitMutable(self, ctx:FSharpParser.MutableContext):
        pass


    # Enter a parse tree produced by FSharpParser#let.
    def enterLet(self, ctx:FSharpParser.LetContext):
        pass

    # Exit a parse tree produced by FSharpParser#let.
    def exitLet(self, ctx:FSharpParser.LetContext):
        pass


    # Enter a parse tree produced by FSharpParser#fun.
    def enterFun(self, ctx:FSharpParser.FunContext):
        pass

    # Exit a parse tree produced by FSharpParser#fun.
    def exitFun(self, ctx:FSharpParser.FunContext):
        pass


    # Enter a parse tree produced by FSharpParser#fun_type.
    def enterFun_type(self, ctx:FSharpParser.Fun_typeContext):
        pass

    # Exit a parse tree produced by FSharpParser#fun_type.
    def exitFun_type(self, ctx:FSharpParser.Fun_typeContext):
        pass


    # Enter a parse tree produced by FSharpParser#typezation.
    def enterTypezation(self, ctx:FSharpParser.TypezationContext):
        pass

    # Exit a parse tree produced by FSharpParser#typezation.
    def exitTypezation(self, ctx:FSharpParser.TypezationContext):
        pass


    # Enter a parse tree produced by FSharpParser#if_then_elif_else.
    def enterIf_then_elif_else(self, ctx:FSharpParser.If_then_elif_elseContext):
        pass

    # Exit a parse tree produced by FSharpParser#if_then_elif_else.
    def exitIf_then_elif_else(self, ctx:FSharpParser.If_then_elif_elseContext):
        pass


    # Enter a parse tree produced by FSharpParser#while_do.
    def enterWhile_do(self, ctx:FSharpParser.While_doContext):
        pass

    # Exit a parse tree produced by FSharpParser#while_do.
    def exitWhile_do(self, ctx:FSharpParser.While_doContext):
        pass


    # Enter a parse tree produced by FSharpParser#for.
    def enterFor(self, ctx:FSharpParser.ForContext):
        pass

    # Exit a parse tree produced by FSharpParser#for.
    def exitFor(self, ctx:FSharpParser.ForContext):
        pass


    # Enter a parse tree produced by FSharpParser#add.
    def enterAdd(self, ctx:FSharpParser.AddContext):
        pass

    # Exit a parse tree produced by FSharpParser#add.
    def exitAdd(self, ctx:FSharpParser.AddContext):
        pass


    # Enter a parse tree produced by FSharpParser#mul.
    def enterMul(self, ctx:FSharpParser.MulContext):
        pass

    # Exit a parse tree produced by FSharpParser#mul.
    def exitMul(self, ctx:FSharpParser.MulContext):
        pass


    # Enter a parse tree produced by FSharpParser#div.
    def enterDiv(self, ctx:FSharpParser.DivContext):
        pass

    # Exit a parse tree produced by FSharpParser#div.
    def exitDiv(self, ctx:FSharpParser.DivContext):
        pass


    # Enter a parse tree produced by FSharpParser#minus.
    def enterMinus(self, ctx:FSharpParser.MinusContext):
        pass

    # Exit a parse tree produced by FSharpParser#minus.
    def exitMinus(self, ctx:FSharpParser.MinusContext):
        pass


    # Enter a parse tree produced by FSharpParser#pow.
    def enterPow(self, ctx:FSharpParser.PowContext):
        pass

    # Exit a parse tree produced by FSharpParser#pow.
    def exitPow(self, ctx:FSharpParser.PowContext):
        pass


    # Enter a parse tree produced by FSharpParser#mod.
    def enterMod(self, ctx:FSharpParser.ModContext):
        pass

    # Exit a parse tree produced by FSharpParser#mod.
    def exitMod(self, ctx:FSharpParser.ModContext):
        pass


    # Enter a parse tree produced by FSharpParser#not_equal.
    def enterNot_equal(self, ctx:FSharpParser.Not_equalContext):
        pass

    # Exit a parse tree produced by FSharpParser#not_equal.
    def exitNot_equal(self, ctx:FSharpParser.Not_equalContext):
        pass


    # Enter a parse tree produced by FSharpParser#less.
    def enterLess(self, ctx:FSharpParser.LessContext):
        pass

    # Exit a parse tree produced by FSharpParser#less.
    def exitLess(self, ctx:FSharpParser.LessContext):
        pass


    # Enter a parse tree produced by FSharpParser#less_equal.
    def enterLess_equal(self, ctx:FSharpParser.Less_equalContext):
        pass

    # Exit a parse tree produced by FSharpParser#less_equal.
    def exitLess_equal(self, ctx:FSharpParser.Less_equalContext):
        pass


    # Enter a parse tree produced by FSharpParser#greater.
    def enterGreater(self, ctx:FSharpParser.GreaterContext):
        pass

    # Exit a parse tree produced by FSharpParser#greater.
    def exitGreater(self, ctx:FSharpParser.GreaterContext):
        pass


    # Enter a parse tree produced by FSharpParser#greater_equal.
    def enterGreater_equal(self, ctx:FSharpParser.Greater_equalContext):
        pass

    # Exit a parse tree produced by FSharpParser#greater_equal.
    def exitGreater_equal(self, ctx:FSharpParser.Greater_equalContext):
        pass


    # Enter a parse tree produced by FSharpParser#equal.
    def enterEqual(self, ctx:FSharpParser.EqualContext):
        pass

    # Exit a parse tree produced by FSharpParser#equal.
    def exitEqual(self, ctx:FSharpParser.EqualContext):
        pass


    # Enter a parse tree produced by FSharpParser#and.
    def enterAnd(self, ctx:FSharpParser.AndContext):
        pass

    # Exit a parse tree produced by FSharpParser#and.
    def exitAnd(self, ctx:FSharpParser.AndContext):
        pass


    # Enter a parse tree produced by FSharpParser#or.
    def enterOr(self, ctx:FSharpParser.OrContext):
        pass

    # Exit a parse tree produced by FSharpParser#or.
    def exitOr(self, ctx:FSharpParser.OrContext):
        pass


    # Enter a parse tree produced by FSharpParser#lshift.
    def enterLshift(self, ctx:FSharpParser.LshiftContext):
        pass

    # Exit a parse tree produced by FSharpParser#lshift.
    def exitLshift(self, ctx:FSharpParser.LshiftContext):
        pass


    # Enter a parse tree produced by FSharpParser#rshift.
    def enterRshift(self, ctx:FSharpParser.RshiftContext):
        pass

    # Exit a parse tree produced by FSharpParser#rshift.
    def exitRshift(self, ctx:FSharpParser.RshiftContext):
        pass


    # Enter a parse tree produced by FSharpParser#log_mul.
    def enterLog_mul(self, ctx:FSharpParser.Log_mulContext):
        pass

    # Exit a parse tree produced by FSharpParser#log_mul.
    def exitLog_mul(self, ctx:FSharpParser.Log_mulContext):
        pass


    # Enter a parse tree produced by FSharpParser#log_add.
    def enterLog_add(self, ctx:FSharpParser.Log_addContext):
        pass

    # Exit a parse tree produced by FSharpParser#log_add.
    def exitLog_add(self, ctx:FSharpParser.Log_addContext):
        pass


    # Enter a parse tree produced by FSharpParser#log_xor.
    def enterLog_xor(self, ctx:FSharpParser.Log_xorContext):
        pass

    # Exit a parse tree produced by FSharpParser#log_xor.
    def exitLog_xor(self, ctx:FSharpParser.Log_xorContext):
        pass


    # Enter a parse tree produced by FSharpParser#log_not.
    def enterLog_not(self, ctx:FSharpParser.Log_notContext):
        pass

    # Exit a parse tree produced by FSharpParser#log_not.
    def exitLog_not(self, ctx:FSharpParser.Log_notContext):
        pass


    # Enter a parse tree produced by FSharpParser#not.
    def enterNot(self, ctx:FSharpParser.NotContext):
        pass

    # Exit a parse tree produced by FSharpParser#not.
    def exitNot(self, ctx:FSharpParser.NotContext):
        pass


    # Enter a parse tree produced by FSharpParser#pipe.
    def enterPipe(self, ctx:FSharpParser.PipeContext):
        pass

    # Exit a parse tree produced by FSharpParser#pipe.
    def exitPipe(self, ctx:FSharpParser.PipeContext):
        pass


    # Enter a parse tree produced by FSharpParser#compos.
    def enterCompos(self, ctx:FSharpParser.ComposContext):
        pass

    # Exit a parse tree produced by FSharpParser#compos.
    def exitCompos(self, ctx:FSharpParser.ComposContext):
        pass


    # Enter a parse tree produced by FSharpParser#assign.
    def enterAssign(self, ctx:FSharpParser.AssignContext):
        pass

    # Exit a parse tree produced by FSharpParser#assign.
    def exitAssign(self, ctx:FSharpParser.AssignContext):
        pass


    # Enter a parse tree produced by FSharpParser#type.
    def enterType(self, ctx:FSharpParser.TypeContext):
        pass

    # Exit a parse tree produced by FSharpParser#type.
    def exitType(self, ctx:FSharpParser.TypeContext):
        pass


    # Enter a parse tree produced by FSharpParser#module.
    def enterModule(self, ctx:FSharpParser.ModuleContext):
        pass

    # Exit a parse tree produced by FSharpParser#module.
    def exitModule(self, ctx:FSharpParser.ModuleContext):
        pass


    # Enter a parse tree produced by FSharpParser#open.
    def enterOpen(self, ctx:FSharpParser.OpenContext):
        pass

    # Exit a parse tree produced by FSharpParser#open.
    def exitOpen(self, ctx:FSharpParser.OpenContext):
        pass


    # Enter a parse tree produced by FSharpParser#namespace.
    def enterNamespace(self, ctx:FSharpParser.NamespaceContext):
        pass

    # Exit a parse tree produced by FSharpParser#namespace.
    def exitNamespace(self, ctx:FSharpParser.NamespaceContext):
        pass


    # Enter a parse tree produced by FSharpParser#class.
    def enterClass(self, ctx:FSharpParser.ClassContext):
        pass

    # Exit a parse tree produced by FSharpParser#class.
    def exitClass(self, ctx:FSharpParser.ClassContext):
        pass


    # Enter a parse tree produced by FSharpParser#do.
    def enterDo(self, ctx:FSharpParser.DoContext):
        pass

    # Exit a parse tree produced by FSharpParser#do.
    def exitDo(self, ctx:FSharpParser.DoContext):
        pass


    # Enter a parse tree produced by FSharpParser#new.
    def enterNew(self, ctx:FSharpParser.NewContext):
        pass

    # Exit a parse tree produced by FSharpParser#new.
    def exitNew(self, ctx:FSharpParser.NewContext):
        pass


    # Enter a parse tree produced by FSharpParser#when.
    def enterWhen(self, ctx:FSharpParser.WhenContext):
        pass

    # Exit a parse tree produced by FSharpParser#when.
    def exitWhen(self, ctx:FSharpParser.WhenContext):
        pass


    # Enter a parse tree produced by FSharpParser#seq.
    def enterSeq(self, ctx:FSharpParser.SeqContext):
        pass

    # Exit a parse tree produced by FSharpParser#seq.
    def exitSeq(self, ctx:FSharpParser.SeqContext):
        pass


    # Enter a parse tree produced by FSharpParser#list.
    def enterList(self, ctx:FSharpParser.ListContext):
        pass

    # Exit a parse tree produced by FSharpParser#list.
    def exitList(self, ctx:FSharpParser.ListContext):
        pass


    # Enter a parse tree produced by FSharpParser#array.
    def enterArray(self, ctx:FSharpParser.ArrayContext):
        pass

    # Exit a parse tree produced by FSharpParser#array.
    def exitArray(self, ctx:FSharpParser.ArrayContext):
        pass


    # Enter a parse tree produced by FSharpParser#map.
    def enterMap(self, ctx:FSharpParser.MapContext):
        pass

    # Exit a parse tree produced by FSharpParser#map.
    def exitMap(self, ctx:FSharpParser.MapContext):
        pass


    # Enter a parse tree produced by FSharpParser#generator.
    def enterGenerator(self, ctx:FSharpParser.GeneratorContext):
        pass

    # Exit a parse tree produced by FSharpParser#generator.
    def exitGenerator(self, ctx:FSharpParser.GeneratorContext):
        pass


    # Enter a parse tree produced by FSharpParser#set.
    def enterSet(self, ctx:FSharpParser.SetContext):
        pass

    # Exit a parse tree produced by FSharpParser#set.
    def exitSet(self, ctx:FSharpParser.SetContext):
        pass


    # Enter a parse tree produced by FSharpParser#async_rule.
    def enterAsync_rule(self, ctx:FSharpParser.Async_ruleContext):
        pass

    # Exit a parse tree produced by FSharpParser#async_rule.
    def exitAsync_rule(self, ctx:FSharpParser.Async_ruleContext):
        pass


    # Enter a parse tree produced by FSharpParser#task.
    def enterTask(self, ctx:FSharpParser.TaskContext):
        pass

    # Exit a parse tree produced by FSharpParser#task.
    def exitTask(self, ctx:FSharpParser.TaskContext):
        pass


    # Enter a parse tree produced by FSharpParser#exclamation_mark.
    def enterExclamation_mark(self, ctx:FSharpParser.Exclamation_markContext):
        pass

    # Exit a parse tree produced by FSharpParser#exclamation_mark.
    def exitExclamation_mark(self, ctx:FSharpParser.Exclamation_markContext):
        pass


    # Enter a parse tree produced by FSharpParser#match_with.
    def enterMatch_with(self, ctx:FSharpParser.Match_withContext):
        pass

    # Exit a parse tree produced by FSharpParser#match_with.
    def exitMatch_with(self, ctx:FSharpParser.Match_withContext):
        pass


    # Enter a parse tree produced by FSharpParser#try_with_finally.
    def enterTry_with_finally(self, ctx:FSharpParser.Try_with_finallyContext):
        pass

    # Exit a parse tree produced by FSharpParser#try_with_finally.
    def exitTry_with_finally(self, ctx:FSharpParser.Try_with_finallyContext):
        pass


    # Enter a parse tree produced by FSharpParser#use.
    def enterUse(self, ctx:FSharpParser.UseContext):
        pass

    # Exit a parse tree produced by FSharpParser#use.
    def exitUse(self, ctx:FSharpParser.UseContext):
        pass


    # Enter a parse tree produced by FSharpParser#using.
    def enterUsing(self, ctx:FSharpParser.UsingContext):
        pass

    # Exit a parse tree produced by FSharpParser#using.
    def exitUsing(self, ctx:FSharpParser.UsingContext):
        pass


    # Enter a parse tree produced by FSharpParser#raise.
    def enterRaise(self, ctx:FSharpParser.RaiseContext):
        pass

    # Exit a parse tree produced by FSharpParser#raise.
    def exitRaise(self, ctx:FSharpParser.RaiseContext):
        pass


    # Enter a parse tree produced by FSharpParser#reraise.
    def enterReraise(self, ctx:FSharpParser.ReraiseContext):
        pass

    # Exit a parse tree produced by FSharpParser#reraise.
    def exitReraise(self, ctx:FSharpParser.ReraiseContext):
        pass


    # Enter a parse tree produced by FSharpParser#failwith.
    def enterFailwith(self, ctx:FSharpParser.FailwithContext):
        pass

    # Exit a parse tree produced by FSharpParser#failwith.
    def exitFailwith(self, ctx:FSharpParser.FailwithContext):
        pass


    # Enter a parse tree produced by FSharpParser#invalidArg.
    def enterInvalidArg(self, ctx:FSharpParser.InvalidArgContext):
        pass

    # Exit a parse tree produced by FSharpParser#invalidArg.
    def exitInvalidArg(self, ctx:FSharpParser.InvalidArgContext):
        pass


    # Enter a parse tree produced by FSharpParser#exception_of.
    def enterException_of(self, ctx:FSharpParser.Exception_ofContext):
        pass

    # Exit a parse tree produced by FSharpParser#exception_of.
    def exitException_of(self, ctx:FSharpParser.Exception_ofContext):
        pass


    # Enter a parse tree produced by FSharpParser#member.
    def enterMember(self, ctx:FSharpParser.MemberContext):
        pass

    # Exit a parse tree produced by FSharpParser#member.
    def exitMember(self, ctx:FSharpParser.MemberContext):
        pass


    # Enter a parse tree produced by FSharpParser#val.
    def enterVal(self, ctx:FSharpParser.ValContext):
        pass

    # Exit a parse tree produced by FSharpParser#val.
    def exitVal(self, ctx:FSharpParser.ValContext):
        pass


    # Enter a parse tree produced by FSharpParser#struct.
    def enterStruct(self, ctx:FSharpParser.StructContext):
        pass

    # Exit a parse tree produced by FSharpParser#struct.
    def exitStruct(self, ctx:FSharpParser.StructContext):
        pass


    # Enter a parse tree produced by FSharpParser#with_get_set.
    def enterWith_get_set(self, ctx:FSharpParser.With_get_setContext):
        pass

    # Exit a parse tree produced by FSharpParser#with_get_set.
    def exitWith_get_set(self, ctx:FSharpParser.With_get_setContext):
        pass


    # Enter a parse tree produced by FSharpParser#tuple.
    def enterTuple(self, ctx:FSharpParser.TupleContext):
        pass

    # Exit a parse tree produced by FSharpParser#tuple.
    def exitTuple(self, ctx:FSharpParser.TupleContext):
        pass


    # Enter a parse tree produced by FSharpParser#with.
    def enterWith(self, ctx:FSharpParser.WithContext):
        pass

    # Exit a parse tree produced by FSharpParser#with.
    def exitWith(self, ctx:FSharpParser.WithContext):
        pass


    # Enter a parse tree produced by FSharpParser#record.
    def enterRecord(self, ctx:FSharpParser.RecordContext):
        pass

    # Exit a parse tree produced by FSharpParser#record.
    def exitRecord(self, ctx:FSharpParser.RecordContext):
        pass


    # Enter a parse tree produced by FSharpParser#of.
    def enterOf(self, ctx:FSharpParser.OfContext):
        pass

    # Exit a parse tree produced by FSharpParser#of.
    def exitOf(self, ctx:FSharpParser.OfContext):
        pass


    # Enter a parse tree produced by FSharpParser#enum.
    def enterEnum(self, ctx:FSharpParser.EnumContext):
        pass

    # Exit a parse tree produced by FSharpParser#enum.
    def exitEnum(self, ctx:FSharpParser.EnumContext):
        pass


    # Enter a parse tree produced by FSharpParser#inherit.
    def enterInherit(self, ctx:FSharpParser.InheritContext):
        pass

    # Exit a parse tree produced by FSharpParser#inherit.
    def exitInherit(self, ctx:FSharpParser.InheritContext):
        pass


    # Enter a parse tree produced by FSharpParser#default.
    def enterDefault(self, ctx:FSharpParser.DefaultContext):
        pass

    # Exit a parse tree produced by FSharpParser#default.
    def exitDefault(self, ctx:FSharpParser.DefaultContext):
        pass


    # Enter a parse tree produced by FSharpParser#override.
    def enterOverride(self, ctx:FSharpParser.OverrideContext):
        pass

    # Exit a parse tree produced by FSharpParser#override.
    def exitOverride(self, ctx:FSharpParser.OverrideContext):
        pass


    # Enter a parse tree produced by FSharpParser#abstract.
    def enterAbstract(self, ctx:FSharpParser.AbstractContext):
        pass

    # Exit a parse tree produced by FSharpParser#abstract.
    def exitAbstract(self, ctx:FSharpParser.AbstractContext):
        pass


    # Enter a parse tree produced by FSharpParser#base.
    def enterBase(self, ctx:FSharpParser.BaseContext):
        pass

    # Exit a parse tree produced by FSharpParser#base.
    def exitBase(self, ctx:FSharpParser.BaseContext):
        pass


    # Enter a parse tree produced by FSharpParser#colon_q.
    def enterColon_q(self, ctx:FSharpParser.Colon_qContext):
        pass

    # Exit a parse tree produced by FSharpParser#colon_q.
    def exitColon_q(self, ctx:FSharpParser.Colon_qContext):
        pass


    # Enter a parse tree produced by FSharpParser#interface.
    def enterInterface(self, ctx:FSharpParser.InterfaceContext):
        pass

    # Exit a parse tree produced by FSharpParser#interface.
    def exitInterface(self, ctx:FSharpParser.InterfaceContext):
        pass


    # Enter a parse tree produced by FSharpParser#expression.
    def enterExpression(self, ctx:FSharpParser.ExpressionContext):
        pass

    # Exit a parse tree produced by FSharpParser#expression.
    def exitExpression(self, ctx:FSharpParser.ExpressionContext):
        pass


    # Enter a parse tree produced by FSharpParser#exprs.
    def enterExprs(self, ctx:FSharpParser.ExprsContext):
        pass

    # Exit a parse tree produced by FSharpParser#exprs.
    def exitExprs(self, ctx:FSharpParser.ExprsContext):
        pass



del FSharpParser