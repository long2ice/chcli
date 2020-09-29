# Generated from ClickHouseParser.g4 by ANTLR 4.8
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .ClickHouseParser import ClickHouseParser
else:
    from ClickHouseParser import ClickHouseParser


# This class defines a complete generic visitor for a parse tree produced by ClickHouseParser.


class ClickHouseParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ClickHouseParser#parse.
    def visitParse(self, ctx: ClickHouseParser.ParseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#query.
    def visitQuery(self, ctx: ClickHouseParser.QueryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#select_query.
    def visitSelect_query(self, ctx: ClickHouseParser.Select_queryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#select_query_main.
    def visitSelect_query_main(self, ctx: ClickHouseParser.Select_query_mainContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#select_with_step.
    def visitSelect_with_step(self, ctx: ClickHouseParser.Select_with_stepContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#select_select_step.
    def visitSelect_select_step(self, ctx: ClickHouseParser.Select_select_stepContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#select_from_step.
    def visitSelect_from_step(self, ctx: ClickHouseParser.Select_from_stepContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#select_array_join_step.
    def visitSelect_array_join_step(self, ctx: ClickHouseParser.Select_array_join_stepContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#select_sample_step.
    def visitSelect_sample_step(self, ctx: ClickHouseParser.Select_sample_stepContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#sample_ratio.
    def visitSample_ratio(self, ctx: ClickHouseParser.Sample_ratioContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#select_join_step.
    def visitSelect_join_step(self, ctx: ClickHouseParser.Select_join_stepContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#select_join_right_part.
    def visitSelect_join_right_part(self, ctx: ClickHouseParser.Select_join_right_partContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#select_prewhere_step.
    def visitSelect_prewhere_step(self, ctx: ClickHouseParser.Select_prewhere_stepContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#select_where_step.
    def visitSelect_where_step(self, ctx: ClickHouseParser.Select_where_stepContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#select_groupby_step.
    def visitSelect_groupby_step(self, ctx: ClickHouseParser.Select_groupby_stepContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#select_having_step.
    def visitSelect_having_step(self, ctx: ClickHouseParser.Select_having_stepContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#select_orderby_step.
    def visitSelect_orderby_step(self, ctx: ClickHouseParser.Select_orderby_stepContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#select_limit_step.
    def visitSelect_limit_step(self, ctx: ClickHouseParser.Select_limit_stepContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#select_limitby_step.
    def visitSelect_limitby_step(self, ctx: ClickHouseParser.Select_limitby_stepContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#settings_step.
    def visitSettings_step(self, ctx: ClickHouseParser.Settings_stepContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#select_format_step.
    def visitSelect_format_step(self, ctx: ClickHouseParser.Select_format_stepContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#insert_query.
    def visitInsert_query(self, ctx: ClickHouseParser.Insert_queryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#create_query.
    def visitCreate_query(self, ctx: ClickHouseParser.Create_queryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#rename_query.
    def visitRename_query(self, ctx: ClickHouseParser.Rename_queryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#drop_query.
    def visitDrop_query(self, ctx: ClickHouseParser.Drop_queryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#alter_query.
    def visitAlter_query(self, ctx: ClickHouseParser.Alter_queryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#alter_query_element.
    def visitAlter_query_element(self, ctx: ClickHouseParser.Alter_query_elementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#clickhouse_type.
    def visitClickhouse_type(self, ctx: ClickHouseParser.Clickhouse_typeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#simple_type.
    def visitSimple_type(self, ctx: ClickHouseParser.Simple_typeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#enum_entry.
    def visitEnum_entry(self, ctx: ClickHouseParser.Enum_entryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#use_query.
    def visitUse_query(self, ctx: ClickHouseParser.Use_queryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#set_query.
    def visitSet_query(self, ctx: ClickHouseParser.Set_queryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#assignment_list.
    def visitAssignment_list(self, ctx: ClickHouseParser.Assignment_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#assignment.
    def visitAssignment(self, ctx: ClickHouseParser.AssignmentContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#kill_query_query.
    def visitKill_query_query(self, ctx: ClickHouseParser.Kill_query_queryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#optimize_query.
    def visitOptimize_query(self, ctx: ClickHouseParser.Optimize_queryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#table_properties_query.
    def visitTable_properties_query(self, ctx: ClickHouseParser.Table_properties_queryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#show_tables_query.
    def visitShow_tables_query(self, ctx: ClickHouseParser.Show_tables_queryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#show_processlist_query.
    def visitShow_processlist_query(self, ctx: ClickHouseParser.Show_processlist_queryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#check_query.
    def visitCheck_query(self, ctx: ClickHouseParser.Check_queryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#full_table_name.
    def visitFull_table_name(self, ctx: ClickHouseParser.Full_table_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#partition_name.
    def visitPartition_name(self, ctx: ClickHouseParser.Partition_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#cluster_name.
    def visitCluster_name(self, ctx: ClickHouseParser.Cluster_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#database_name.
    def visitDatabase_name(self, ctx: ClickHouseParser.Database_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#table_name.
    def visitTable_name(self, ctx: ClickHouseParser.Table_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#format_name.
    def visitFormat_name(self, ctx: ClickHouseParser.Format_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#query_outfile_step.
    def visitQuery_outfile_step(self, ctx: ClickHouseParser.Query_outfile_stepContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#engine.
    def visitEngine(self, ctx: ClickHouseParser.EngineContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#identifier_with_optional_parameters.
    def visitIdentifier_with_optional_parameters(
        self, ctx: ClickHouseParser.Identifier_with_optional_parametersContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#identifier_with_parameters.
    def visitIdentifier_with_parameters(
        self, ctx: ClickHouseParser.Identifier_with_parametersContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#order_by_expression_list.
    def visitOrder_by_expression_list(self, ctx: ClickHouseParser.Order_by_expression_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#order_by_element.
    def visitOrder_by_element(self, ctx: ClickHouseParser.Order_by_elementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#table_ttl_list.
    def visitTable_ttl_list(self, ctx: ClickHouseParser.Table_ttl_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#table_ttl_declaration.
    def visitTable_ttl_declaration(self, ctx: ClickHouseParser.Table_ttl_declarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#nested_table.
    def visitNested_table(self, ctx: ClickHouseParser.Nested_tableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#name_type_pair_list.
    def visitName_type_pair_list(self, ctx: ClickHouseParser.Name_type_pair_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#name_type_pair.
    def visitName_type_pair(self, ctx: ClickHouseParser.Name_type_pairContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#compound_name_type_pair.
    def visitCompound_name_type_pair(self, ctx: ClickHouseParser.Compound_name_type_pairContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#column_declaration_list.
    def visitColumn_declaration_list(self, ctx: ClickHouseParser.Column_declaration_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#column_declaration.
    def visitColumn_declaration(self, ctx: ClickHouseParser.Column_declarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#column_name.
    def visitColumn_name(self, ctx: ClickHouseParser.Column_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#column_type.
    def visitColumn_type(self, ctx: ClickHouseParser.Column_typeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#column_name_list.
    def visitColumn_name_list(self, ctx: ClickHouseParser.Column_name_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#select_expr_list.
    def visitSelect_expr_list(self, ctx: ClickHouseParser.Select_expr_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#select_expr.
    def visitSelect_expr(self, ctx: ClickHouseParser.Select_exprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#select_alias.
    def visitSelect_alias(self, ctx: ClickHouseParser.Select_aliasContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#alias.
    def visitAlias(self, ctx: ClickHouseParser.AliasContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#alias_name.
    def visitAlias_name(self, ctx: ClickHouseParser.Alias_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#table_function.
    def visitTable_function(self, ctx: ClickHouseParser.Table_functionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#subquery.
    def visitSubquery(self, ctx: ClickHouseParser.SubqueryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#expression_with_optional_alias.
    def visitExpression_with_optional_alias(
        self, ctx: ClickHouseParser.Expression_with_optional_aliasContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#ExprConcat.
    def visitExprConcat(self, ctx: ClickHouseParser.ExprConcatContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#ExprCase.
    def visitExprCase(self, ctx: ClickHouseParser.ExprCaseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#ExprTupleElement.
    def visitExprTupleElement(self, ctx: ClickHouseParser.ExprTupleElementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#ExprNot.
    def visitExprNot(self, ctx: ClickHouseParser.ExprNotContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#ExprArray.
    def visitExprArray(self, ctx: ClickHouseParser.ExprArrayContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#ExprWithAlias.
    def visitExprWithAlias(self, ctx: ClickHouseParser.ExprWithAliasContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#ExprLogical.
    def visitExprLogical(self, ctx: ClickHouseParser.ExprLogicalContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#ExprIn.
    def visitExprIn(self, ctx: ClickHouseParser.ExprInContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#ExprCast.
    def visitExprCast(self, ctx: ClickHouseParser.ExprCastContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#ExprOr.
    def visitExprOr(self, ctx: ClickHouseParser.ExprOrContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#ExprFunction.
    def visitExprFunction(self, ctx: ClickHouseParser.ExprFunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#ExprMul.
    def visitExprMul(self, ctx: ClickHouseParser.ExprMulContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#ExprId.
    def visitExprId(self, ctx: ClickHouseParser.ExprIdContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#ExprLambda.
    def visitExprLambda(self, ctx: ClickHouseParser.ExprLambdaContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#ExprTernary.
    def visitExprTernary(self, ctx: ClickHouseParser.ExprTernaryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#ExprParen.
    def visitExprParen(self, ctx: ClickHouseParser.ExprParenContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#ExprBetween.
    def visitExprBetween(self, ctx: ClickHouseParser.ExprBetweenContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#ExprSubquery.
    def visitExprSubquery(self, ctx: ClickHouseParser.ExprSubqueryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#ExprStar.
    def visitExprStar(self, ctx: ClickHouseParser.ExprStarContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#ExprInterval.
    def visitExprInterval(self, ctx: ClickHouseParser.ExprIntervalContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#ExprAnd.
    def visitExprAnd(self, ctx: ClickHouseParser.ExprAndContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#ExprArrayElement.
    def visitExprArrayElement(self, ctx: ClickHouseParser.ExprArrayElementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#ExprIsNull.
    def visitExprIsNull(self, ctx: ClickHouseParser.ExprIsNullContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#ExprList.
    def visitExprList(self, ctx: ClickHouseParser.ExprListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#ExprLiteral.
    def visitExprLiteral(self, ctx: ClickHouseParser.ExprLiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#ExprUnaryMinus.
    def visitExprUnaryMinus(self, ctx: ClickHouseParser.ExprUnaryMinusContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#ExprAdd.
    def visitExprAdd(self, ctx: ClickHouseParser.ExprAddContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#interval_unit.
    def visitInterval_unit(self, ctx: ClickHouseParser.Interval_unitContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#expression_list.
    def visitExpression_list(self, ctx: ClickHouseParser.Expression_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#not_empty_expression_list.
    def visitNot_empty_expression_list(
        self, ctx: ClickHouseParser.Not_empty_expression_listContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#array.
    def visitArray(self, ctx: ClickHouseParser.ArrayContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#function.
    def visitFunction(self, ctx: ClickHouseParser.FunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#function_parameters.
    def visitFunction_parameters(self, ctx: ClickHouseParser.Function_parametersContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#function_arguments.
    def visitFunction_arguments(self, ctx: ClickHouseParser.Function_argumentsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#function_name.
    def visitFunction_name(self, ctx: ClickHouseParser.Function_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#identifier.
    def visitIdentifier(self, ctx: ClickHouseParser.IdentifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#keyword.
    def visitKeyword(self, ctx: ClickHouseParser.KeywordContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#compound_identifier.
    def visitCompound_identifier(self, ctx: ClickHouseParser.Compound_identifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#literal.
    def visitLiteral(self, ctx: ClickHouseParser.LiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ClickHouseParser#err.
    def visitErr(self, ctx: ClickHouseParser.ErrContext):
        return self.visitChildren(ctx)


del ClickHouseParser
