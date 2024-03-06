# Generated from Tokenize.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TokenizeParser import TokenizeParser
else:
    from TokenizeParser import TokenizeParser

# This class defines a complete generic visitor for a parse tree produced by TokenizeParser.

class TokenizeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TokenizeParser#dot.
    def visitDot(self, ctx:TokenizeParser.DotContext):
        return self.visitChildren(ctx)


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


    # Visit a parse tree produced by TokenizeParser#fun_type.
    def visitFun_type(self, ctx:TokenizeParser.Fun_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#typezation.
    def visitTypezation(self, ctx:TokenizeParser.TypezationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#if_then_elif_else.
    def visitIf_then_elif_else(self, ctx:TokenizeParser.If_then_elif_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#while_do.
    def visitWhile_do(self, ctx:TokenizeParser.While_doContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#for.
    def visitFor(self, ctx:TokenizeParser.ForContext):
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


    # Visit a parse tree produced by TokenizeParser#not_equal.
    def visitNot_equal(self, ctx:TokenizeParser.Not_equalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#less.
    def visitLess(self, ctx:TokenizeParser.LessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#less_equal.
    def visitLess_equal(self, ctx:TokenizeParser.Less_equalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#greater.
    def visitGreater(self, ctx:TokenizeParser.GreaterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#greater_equal.
    def visitGreater_equal(self, ctx:TokenizeParser.Greater_equalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#equal.
    def visitEqual(self, ctx:TokenizeParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#and.
    def visitAnd(self, ctx:TokenizeParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#or.
    def visitOr(self, ctx:TokenizeParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#lshift.
    def visitLshift(self, ctx:TokenizeParser.LshiftContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#rshift.
    def visitRshift(self, ctx:TokenizeParser.RshiftContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#log_mul.
    def visitLog_mul(self, ctx:TokenizeParser.Log_mulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#log_add.
    def visitLog_add(self, ctx:TokenizeParser.Log_addContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#log_xor.
    def visitLog_xor(self, ctx:TokenizeParser.Log_xorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#log_not.
    def visitLog_not(self, ctx:TokenizeParser.Log_notContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#not.
    def visitNot(self, ctx:TokenizeParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#pipe.
    def visitPipe(self, ctx:TokenizeParser.PipeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#compos.
    def visitCompos(self, ctx:TokenizeParser.ComposContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#assign.
    def visitAssign(self, ctx:TokenizeParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#type.
    def visitType(self, ctx:TokenizeParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#module.
    def visitModule(self, ctx:TokenizeParser.ModuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#open.
    def visitOpen(self, ctx:TokenizeParser.OpenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#namespace.
    def visitNamespace(self, ctx:TokenizeParser.NamespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#class.
    def visitClass(self, ctx:TokenizeParser.ClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#do.
    def visitDo(self, ctx:TokenizeParser.DoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#new.
    def visitNew(self, ctx:TokenizeParser.NewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#then.
    def visitThen(self, ctx:TokenizeParser.ThenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#seq.
    def visitSeq(self, ctx:TokenizeParser.SeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#list.
    def visitList(self, ctx:TokenizeParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#array.
    def visitArray(self, ctx:TokenizeParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#map.
    def visitMap(self, ctx:TokenizeParser.MapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#generator.
    def visitGenerator(self, ctx:TokenizeParser.GeneratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#set.
    def visitSet(self, ctx:TokenizeParser.SetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#async_rule.
    def visitAsync_rule(self, ctx:TokenizeParser.Async_ruleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#task.
    def visitTask(self, ctx:TokenizeParser.TaskContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#exclamation_mark.
    def visitExclamation_mark(self, ctx:TokenizeParser.Exclamation_markContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#match_with.
    def visitMatch_with(self, ctx:TokenizeParser.Match_withContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#try_with_finally.
    def visitTry_with_finally(self, ctx:TokenizeParser.Try_with_finallyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#use.
    def visitUse(self, ctx:TokenizeParser.UseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#using.
    def visitUsing(self, ctx:TokenizeParser.UsingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#raise.
    def visitRaise(self, ctx:TokenizeParser.RaiseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#reraise.
    def visitReraise(self, ctx:TokenizeParser.ReraiseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#failwith.
    def visitFailwith(self, ctx:TokenizeParser.FailwithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#invalidArg.
    def visitInvalidArg(self, ctx:TokenizeParser.InvalidArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#exception_of.
    def visitException_of(self, ctx:TokenizeParser.Exception_ofContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#member.
    def visitMember(self, ctx:TokenizeParser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#val.
    def visitVal(self, ctx:TokenizeParser.ValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#struct.
    def visitStruct(self, ctx:TokenizeParser.StructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#with_get_set.
    def visitWith_get_set(self, ctx:TokenizeParser.With_get_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#tuple.
    def visitTuple(self, ctx:TokenizeParser.TupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#with.
    def visitWith(self, ctx:TokenizeParser.WithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#record.
    def visitRecord(self, ctx:TokenizeParser.RecordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#of.
    def visitOf(self, ctx:TokenizeParser.OfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#enum.
    def visitEnum(self, ctx:TokenizeParser.EnumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#inherit.
    def visitInherit(self, ctx:TokenizeParser.InheritContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#default.
    def visitDefault(self, ctx:TokenizeParser.DefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#override.
    def visitOverride(self, ctx:TokenizeParser.OverrideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#abstract.
    def visitAbstract(self, ctx:TokenizeParser.AbstractContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#base.
    def visitBase(self, ctx:TokenizeParser.BaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#colon_q.
    def visitColon_q(self, ctx:TokenizeParser.Colon_qContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#interface.
    def visitInterface(self, ctx:TokenizeParser.InterfaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#expression.
    def visitExpression(self, ctx:TokenizeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TokenizeParser#exprs.
    def visitExprs(self, ctx:TokenizeParser.ExprsContext):
        return self.visitChildren(ctx)



del TokenizeParser