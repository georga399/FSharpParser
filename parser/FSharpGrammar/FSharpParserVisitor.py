# Generated from FSharpGrammar/FSharpParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .FSharpParser import FSharpParser
else:
    from FSharpParser import FSharpParser

# This class defines a complete generic visitor for a parse tree produced by FSharpParser.

class FSharpParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FSharpParser#dot.
    def visitDot(self, ctx:FSharpParser.DotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#dotIentifier.
    def visitDotIentifier(self, ctx:FSharpParser.DotIentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#int.
    def visitInt(self, ctx:FSharpParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#float.
    def visitFloat(self, ctx:FSharpParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#unit.
    def visitUnit(self, ctx:FSharpParser.UnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#bool.
    def visitBool(self, ctx:FSharpParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#char.
    def visitChar(self, ctx:FSharpParser.CharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#missing_arg.
    def visitMissing_arg(self, ctx:FSharpParser.Missing_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#interpolationSign.
    def visitInterpolationSign(self, ctx:FSharpParser.InterpolationSignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#dollar.
    def visitDollar(self, ctx:FSharpParser.DollarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#string.
    def visitString(self, ctx:FSharpParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#interpolated_string.
    def visitInterpolated_string(self, ctx:FSharpParser.Interpolated_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#attribute.
    def visitAttribute(self, ctx:FSharpParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#round_brackets.
    def visitRound_brackets(self, ctx:FSharpParser.Round_bracketsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#rec.
    def visitRec(self, ctx:FSharpParser.RecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#public.
    def visitPublic(self, ctx:FSharpParser.PublicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#private.
    def visitPrivate(self, ctx:FSharpParser.PrivateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#internal.
    def visitInternal(self, ctx:FSharpParser.InternalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#mutable.
    def visitMutable(self, ctx:FSharpParser.MutableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#let.
    def visitLet(self, ctx:FSharpParser.LetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#fun.
    def visitFun(self, ctx:FSharpParser.FunContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#fun_type.
    def visitFun_type(self, ctx:FSharpParser.Fun_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#typezation.
    def visitTypezation(self, ctx:FSharpParser.TypezationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#if_then_elif_else.
    def visitIf_then_elif_else(self, ctx:FSharpParser.If_then_elif_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#while_do.
    def visitWhile_do(self, ctx:FSharpParser.While_doContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#for.
    def visitFor(self, ctx:FSharpParser.ForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#add.
    def visitAdd(self, ctx:FSharpParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#mul.
    def visitMul(self, ctx:FSharpParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#div.
    def visitDiv(self, ctx:FSharpParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#minus.
    def visitMinus(self, ctx:FSharpParser.MinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#pow.
    def visitPow(self, ctx:FSharpParser.PowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#mod.
    def visitMod(self, ctx:FSharpParser.ModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#not_equal.
    def visitNot_equal(self, ctx:FSharpParser.Not_equalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#less.
    def visitLess(self, ctx:FSharpParser.LessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#less_equal.
    def visitLess_equal(self, ctx:FSharpParser.Less_equalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#greater.
    def visitGreater(self, ctx:FSharpParser.GreaterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#greater_equal.
    def visitGreater_equal(self, ctx:FSharpParser.Greater_equalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#equal.
    def visitEqual(self, ctx:FSharpParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#and.
    def visitAnd(self, ctx:FSharpParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#or.
    def visitOr(self, ctx:FSharpParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#lshift.
    def visitLshift(self, ctx:FSharpParser.LshiftContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#rshift.
    def visitRshift(self, ctx:FSharpParser.RshiftContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#log_mul.
    def visitLog_mul(self, ctx:FSharpParser.Log_mulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#log_add.
    def visitLog_add(self, ctx:FSharpParser.Log_addContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#log_xor.
    def visitLog_xor(self, ctx:FSharpParser.Log_xorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#log_not.
    def visitLog_not(self, ctx:FSharpParser.Log_notContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#not.
    def visitNot(self, ctx:FSharpParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#pipe.
    def visitPipe(self, ctx:FSharpParser.PipeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#compos.
    def visitCompos(self, ctx:FSharpParser.ComposContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#assign.
    def visitAssign(self, ctx:FSharpParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#type.
    def visitType(self, ctx:FSharpParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#module.
    def visitModule(self, ctx:FSharpParser.ModuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#open.
    def visitOpen(self, ctx:FSharpParser.OpenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#namespace.
    def visitNamespace(self, ctx:FSharpParser.NamespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#class.
    def visitClass(self, ctx:FSharpParser.ClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#do.
    def visitDo(self, ctx:FSharpParser.DoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#new.
    def visitNew(self, ctx:FSharpParser.NewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#when.
    def visitWhen(self, ctx:FSharpParser.WhenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#seq.
    def visitSeq(self, ctx:FSharpParser.SeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#list.
    def visitList(self, ctx:FSharpParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#array.
    def visitArray(self, ctx:FSharpParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#map.
    def visitMap(self, ctx:FSharpParser.MapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#generator.
    def visitGenerator(self, ctx:FSharpParser.GeneratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#set.
    def visitSet(self, ctx:FSharpParser.SetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#async_rule.
    def visitAsync_rule(self, ctx:FSharpParser.Async_ruleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#task.
    def visitTask(self, ctx:FSharpParser.TaskContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#exclamation_mark.
    def visitExclamation_mark(self, ctx:FSharpParser.Exclamation_markContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#match_with.
    def visitMatch_with(self, ctx:FSharpParser.Match_withContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#try_with_finally.
    def visitTry_with_finally(self, ctx:FSharpParser.Try_with_finallyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#use.
    def visitUse(self, ctx:FSharpParser.UseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#using.
    def visitUsing(self, ctx:FSharpParser.UsingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#raise.
    def visitRaise(self, ctx:FSharpParser.RaiseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#reraise.
    def visitReraise(self, ctx:FSharpParser.ReraiseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#failwith.
    def visitFailwith(self, ctx:FSharpParser.FailwithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#invalidArg.
    def visitInvalidArg(self, ctx:FSharpParser.InvalidArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#exception_of.
    def visitException_of(self, ctx:FSharpParser.Exception_ofContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#member.
    def visitMember(self, ctx:FSharpParser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#val.
    def visitVal(self, ctx:FSharpParser.ValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#struct.
    def visitStruct(self, ctx:FSharpParser.StructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#with_get_set.
    def visitWith_get_set(self, ctx:FSharpParser.With_get_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#tuple.
    def visitTuple(self, ctx:FSharpParser.TupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#with.
    def visitWith(self, ctx:FSharpParser.WithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#record.
    def visitRecord(self, ctx:FSharpParser.RecordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#of.
    def visitOf(self, ctx:FSharpParser.OfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#enum.
    def visitEnum(self, ctx:FSharpParser.EnumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#inherit.
    def visitInherit(self, ctx:FSharpParser.InheritContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#default.
    def visitDefault(self, ctx:FSharpParser.DefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#override.
    def visitOverride(self, ctx:FSharpParser.OverrideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#abstract.
    def visitAbstract(self, ctx:FSharpParser.AbstractContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#base.
    def visitBase(self, ctx:FSharpParser.BaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#colon_q.
    def visitColon_q(self, ctx:FSharpParser.Colon_qContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#interface.
    def visitInterface(self, ctx:FSharpParser.InterfaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#expression.
    def visitExpression(self, ctx:FSharpParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FSharpParser#exprs.
    def visitExprs(self, ctx:FSharpParser.ExprsContext):
        return self.visitChildren(ctx)



del FSharpParser