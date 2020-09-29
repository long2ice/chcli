# Generated from ClickHouseParser.g4 by ANTLR 4.8
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .ClickHouseParser import ClickHouseParser
else:
    from ClickHouseParser import ClickHouseParser

# This class defines a complete listener for a parse tree produced by ClickHouseParser.
class ClickHouseParserListener(ParseTreeListener):

    # Enter a parse tree produced by ClickHouseParser#parse.
    def enterParse(self, ctx: ClickHouseParser.ParseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#parse.
    def exitParse(self, ctx: ClickHouseParser.ParseContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#query.
    def enterQuery(self, ctx: ClickHouseParser.QueryContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#query.
    def exitQuery(self, ctx: ClickHouseParser.QueryContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#select_query.
    def enterSelect_query(self, ctx: ClickHouseParser.Select_queryContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#select_query.
    def exitSelect_query(self, ctx: ClickHouseParser.Select_queryContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#select_query_main.
    def enterSelect_query_main(self, ctx: ClickHouseParser.Select_query_mainContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#select_query_main.
    def exitSelect_query_main(self, ctx: ClickHouseParser.Select_query_mainContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#select_with_step.
    def enterSelect_with_step(self, ctx: ClickHouseParser.Select_with_stepContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#select_with_step.
    def exitSelect_with_step(self, ctx: ClickHouseParser.Select_with_stepContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#select_select_step.
    def enterSelect_select_step(self, ctx: ClickHouseParser.Select_select_stepContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#select_select_step.
    def exitSelect_select_step(self, ctx: ClickHouseParser.Select_select_stepContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#select_from_step.
    def enterSelect_from_step(self, ctx: ClickHouseParser.Select_from_stepContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#select_from_step.
    def exitSelect_from_step(self, ctx: ClickHouseParser.Select_from_stepContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#select_array_join_step.
    def enterSelect_array_join_step(self, ctx: ClickHouseParser.Select_array_join_stepContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#select_array_join_step.
    def exitSelect_array_join_step(self, ctx: ClickHouseParser.Select_array_join_stepContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#select_sample_step.
    def enterSelect_sample_step(self, ctx: ClickHouseParser.Select_sample_stepContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#select_sample_step.
    def exitSelect_sample_step(self, ctx: ClickHouseParser.Select_sample_stepContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#sample_ratio.
    def enterSample_ratio(self, ctx: ClickHouseParser.Sample_ratioContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#sample_ratio.
    def exitSample_ratio(self, ctx: ClickHouseParser.Sample_ratioContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#select_join_step.
    def enterSelect_join_step(self, ctx: ClickHouseParser.Select_join_stepContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#select_join_step.
    def exitSelect_join_step(self, ctx: ClickHouseParser.Select_join_stepContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#select_join_right_part.
    def enterSelect_join_right_part(self, ctx: ClickHouseParser.Select_join_right_partContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#select_join_right_part.
    def exitSelect_join_right_part(self, ctx: ClickHouseParser.Select_join_right_partContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#select_prewhere_step.
    def enterSelect_prewhere_step(self, ctx: ClickHouseParser.Select_prewhere_stepContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#select_prewhere_step.
    def exitSelect_prewhere_step(self, ctx: ClickHouseParser.Select_prewhere_stepContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#select_where_step.
    def enterSelect_where_step(self, ctx: ClickHouseParser.Select_where_stepContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#select_where_step.
    def exitSelect_where_step(self, ctx: ClickHouseParser.Select_where_stepContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#select_groupby_step.
    def enterSelect_groupby_step(self, ctx: ClickHouseParser.Select_groupby_stepContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#select_groupby_step.
    def exitSelect_groupby_step(self, ctx: ClickHouseParser.Select_groupby_stepContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#select_having_step.
    def enterSelect_having_step(self, ctx: ClickHouseParser.Select_having_stepContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#select_having_step.
    def exitSelect_having_step(self, ctx: ClickHouseParser.Select_having_stepContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#select_orderby_step.
    def enterSelect_orderby_step(self, ctx: ClickHouseParser.Select_orderby_stepContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#select_orderby_step.
    def exitSelect_orderby_step(self, ctx: ClickHouseParser.Select_orderby_stepContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#select_limit_step.
    def enterSelect_limit_step(self, ctx: ClickHouseParser.Select_limit_stepContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#select_limit_step.
    def exitSelect_limit_step(self, ctx: ClickHouseParser.Select_limit_stepContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#select_limitby_step.
    def enterSelect_limitby_step(self, ctx: ClickHouseParser.Select_limitby_stepContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#select_limitby_step.
    def exitSelect_limitby_step(self, ctx: ClickHouseParser.Select_limitby_stepContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#settings_step.
    def enterSettings_step(self, ctx: ClickHouseParser.Settings_stepContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#settings_step.
    def exitSettings_step(self, ctx: ClickHouseParser.Settings_stepContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#select_format_step.
    def enterSelect_format_step(self, ctx: ClickHouseParser.Select_format_stepContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#select_format_step.
    def exitSelect_format_step(self, ctx: ClickHouseParser.Select_format_stepContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#insert_query.
    def enterInsert_query(self, ctx: ClickHouseParser.Insert_queryContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#insert_query.
    def exitInsert_query(self, ctx: ClickHouseParser.Insert_queryContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#create_query.
    def enterCreate_query(self, ctx: ClickHouseParser.Create_queryContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#create_query.
    def exitCreate_query(self, ctx: ClickHouseParser.Create_queryContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#rename_query.
    def enterRename_query(self, ctx: ClickHouseParser.Rename_queryContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#rename_query.
    def exitRename_query(self, ctx: ClickHouseParser.Rename_queryContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#drop_query.
    def enterDrop_query(self, ctx: ClickHouseParser.Drop_queryContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#drop_query.
    def exitDrop_query(self, ctx: ClickHouseParser.Drop_queryContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#alter_query.
    def enterAlter_query(self, ctx: ClickHouseParser.Alter_queryContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#alter_query.
    def exitAlter_query(self, ctx: ClickHouseParser.Alter_queryContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#alter_query_element.
    def enterAlter_query_element(self, ctx: ClickHouseParser.Alter_query_elementContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#alter_query_element.
    def exitAlter_query_element(self, ctx: ClickHouseParser.Alter_query_elementContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#clickhouse_type.
    def enterClickhouse_type(self, ctx: ClickHouseParser.Clickhouse_typeContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#clickhouse_type.
    def exitClickhouse_type(self, ctx: ClickHouseParser.Clickhouse_typeContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#simple_type.
    def enterSimple_type(self, ctx: ClickHouseParser.Simple_typeContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#simple_type.
    def exitSimple_type(self, ctx: ClickHouseParser.Simple_typeContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#enum_entry.
    def enterEnum_entry(self, ctx: ClickHouseParser.Enum_entryContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#enum_entry.
    def exitEnum_entry(self, ctx: ClickHouseParser.Enum_entryContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#use_query.
    def enterUse_query(self, ctx: ClickHouseParser.Use_queryContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#use_query.
    def exitUse_query(self, ctx: ClickHouseParser.Use_queryContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#set_query.
    def enterSet_query(self, ctx: ClickHouseParser.Set_queryContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#set_query.
    def exitSet_query(self, ctx: ClickHouseParser.Set_queryContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#assignment_list.
    def enterAssignment_list(self, ctx: ClickHouseParser.Assignment_listContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#assignment_list.
    def exitAssignment_list(self, ctx: ClickHouseParser.Assignment_listContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#assignment.
    def enterAssignment(self, ctx: ClickHouseParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#assignment.
    def exitAssignment(self, ctx: ClickHouseParser.AssignmentContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#kill_query_query.
    def enterKill_query_query(self, ctx: ClickHouseParser.Kill_query_queryContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#kill_query_query.
    def exitKill_query_query(self, ctx: ClickHouseParser.Kill_query_queryContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#optimize_query.
    def enterOptimize_query(self, ctx: ClickHouseParser.Optimize_queryContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#optimize_query.
    def exitOptimize_query(self, ctx: ClickHouseParser.Optimize_queryContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#table_properties_query.
    def enterTable_properties_query(self, ctx: ClickHouseParser.Table_properties_queryContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#table_properties_query.
    def exitTable_properties_query(self, ctx: ClickHouseParser.Table_properties_queryContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#show_tables_query.
    def enterShow_tables_query(self, ctx: ClickHouseParser.Show_tables_queryContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#show_tables_query.
    def exitShow_tables_query(self, ctx: ClickHouseParser.Show_tables_queryContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#show_processlist_query.
    def enterShow_processlist_query(self, ctx: ClickHouseParser.Show_processlist_queryContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#show_processlist_query.
    def exitShow_processlist_query(self, ctx: ClickHouseParser.Show_processlist_queryContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#check_query.
    def enterCheck_query(self, ctx: ClickHouseParser.Check_queryContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#check_query.
    def exitCheck_query(self, ctx: ClickHouseParser.Check_queryContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#full_table_name.
    def enterFull_table_name(self, ctx: ClickHouseParser.Full_table_nameContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#full_table_name.
    def exitFull_table_name(self, ctx: ClickHouseParser.Full_table_nameContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#partition_name.
    def enterPartition_name(self, ctx: ClickHouseParser.Partition_nameContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#partition_name.
    def exitPartition_name(self, ctx: ClickHouseParser.Partition_nameContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#cluster_name.
    def enterCluster_name(self, ctx: ClickHouseParser.Cluster_nameContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#cluster_name.
    def exitCluster_name(self, ctx: ClickHouseParser.Cluster_nameContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#database_name.
    def enterDatabase_name(self, ctx: ClickHouseParser.Database_nameContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#database_name.
    def exitDatabase_name(self, ctx: ClickHouseParser.Database_nameContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#table_name.
    def enterTable_name(self, ctx: ClickHouseParser.Table_nameContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#table_name.
    def exitTable_name(self, ctx: ClickHouseParser.Table_nameContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#format_name.
    def enterFormat_name(self, ctx: ClickHouseParser.Format_nameContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#format_name.
    def exitFormat_name(self, ctx: ClickHouseParser.Format_nameContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#query_outfile_step.
    def enterQuery_outfile_step(self, ctx: ClickHouseParser.Query_outfile_stepContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#query_outfile_step.
    def exitQuery_outfile_step(self, ctx: ClickHouseParser.Query_outfile_stepContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#engine.
    def enterEngine(self, ctx: ClickHouseParser.EngineContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#engine.
    def exitEngine(self, ctx: ClickHouseParser.EngineContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#identifier_with_optional_parameters.
    def enterIdentifier_with_optional_parameters(
        self, ctx: ClickHouseParser.Identifier_with_optional_parametersContext
    ):
        pass

    # Exit a parse tree produced by ClickHouseParser#identifier_with_optional_parameters.
    def exitIdentifier_with_optional_parameters(
        self, ctx: ClickHouseParser.Identifier_with_optional_parametersContext
    ):
        pass

    # Enter a parse tree produced by ClickHouseParser#identifier_with_parameters.
    def enterIdentifier_with_parameters(
        self, ctx: ClickHouseParser.Identifier_with_parametersContext
    ):
        pass

    # Exit a parse tree produced by ClickHouseParser#identifier_with_parameters.
    def exitIdentifier_with_parameters(
        self, ctx: ClickHouseParser.Identifier_with_parametersContext
    ):
        pass

    # Enter a parse tree produced by ClickHouseParser#order_by_expression_list.
    def enterOrder_by_expression_list(self, ctx: ClickHouseParser.Order_by_expression_listContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#order_by_expression_list.
    def exitOrder_by_expression_list(self, ctx: ClickHouseParser.Order_by_expression_listContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#order_by_element.
    def enterOrder_by_element(self, ctx: ClickHouseParser.Order_by_elementContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#order_by_element.
    def exitOrder_by_element(self, ctx: ClickHouseParser.Order_by_elementContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#table_ttl_list.
    def enterTable_ttl_list(self, ctx: ClickHouseParser.Table_ttl_listContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#table_ttl_list.
    def exitTable_ttl_list(self, ctx: ClickHouseParser.Table_ttl_listContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#table_ttl_declaration.
    def enterTable_ttl_declaration(self, ctx: ClickHouseParser.Table_ttl_declarationContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#table_ttl_declaration.
    def exitTable_ttl_declaration(self, ctx: ClickHouseParser.Table_ttl_declarationContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#nested_table.
    def enterNested_table(self, ctx: ClickHouseParser.Nested_tableContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#nested_table.
    def exitNested_table(self, ctx: ClickHouseParser.Nested_tableContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#name_type_pair_list.
    def enterName_type_pair_list(self, ctx: ClickHouseParser.Name_type_pair_listContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#name_type_pair_list.
    def exitName_type_pair_list(self, ctx: ClickHouseParser.Name_type_pair_listContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#name_type_pair.
    def enterName_type_pair(self, ctx: ClickHouseParser.Name_type_pairContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#name_type_pair.
    def exitName_type_pair(self, ctx: ClickHouseParser.Name_type_pairContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#compound_name_type_pair.
    def enterCompound_name_type_pair(self, ctx: ClickHouseParser.Compound_name_type_pairContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#compound_name_type_pair.
    def exitCompound_name_type_pair(self, ctx: ClickHouseParser.Compound_name_type_pairContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#column_declaration_list.
    def enterColumn_declaration_list(self, ctx: ClickHouseParser.Column_declaration_listContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#column_declaration_list.
    def exitColumn_declaration_list(self, ctx: ClickHouseParser.Column_declaration_listContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#column_declaration.
    def enterColumn_declaration(self, ctx: ClickHouseParser.Column_declarationContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#column_declaration.
    def exitColumn_declaration(self, ctx: ClickHouseParser.Column_declarationContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#column_name.
    def enterColumn_name(self, ctx: ClickHouseParser.Column_nameContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#column_name.
    def exitColumn_name(self, ctx: ClickHouseParser.Column_nameContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#column_type.
    def enterColumn_type(self, ctx: ClickHouseParser.Column_typeContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#column_type.
    def exitColumn_type(self, ctx: ClickHouseParser.Column_typeContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#column_name_list.
    def enterColumn_name_list(self, ctx: ClickHouseParser.Column_name_listContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#column_name_list.
    def exitColumn_name_list(self, ctx: ClickHouseParser.Column_name_listContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#select_expr_list.
    def enterSelect_expr_list(self, ctx: ClickHouseParser.Select_expr_listContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#select_expr_list.
    def exitSelect_expr_list(self, ctx: ClickHouseParser.Select_expr_listContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#select_expr.
    def enterSelect_expr(self, ctx: ClickHouseParser.Select_exprContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#select_expr.
    def exitSelect_expr(self, ctx: ClickHouseParser.Select_exprContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#select_alias.
    def enterSelect_alias(self, ctx: ClickHouseParser.Select_aliasContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#select_alias.
    def exitSelect_alias(self, ctx: ClickHouseParser.Select_aliasContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#alias.
    def enterAlias(self, ctx: ClickHouseParser.AliasContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#alias.
    def exitAlias(self, ctx: ClickHouseParser.AliasContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#alias_name.
    def enterAlias_name(self, ctx: ClickHouseParser.Alias_nameContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#alias_name.
    def exitAlias_name(self, ctx: ClickHouseParser.Alias_nameContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#table_function.
    def enterTable_function(self, ctx: ClickHouseParser.Table_functionContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#table_function.
    def exitTable_function(self, ctx: ClickHouseParser.Table_functionContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#subquery.
    def enterSubquery(self, ctx: ClickHouseParser.SubqueryContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#subquery.
    def exitSubquery(self, ctx: ClickHouseParser.SubqueryContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#expression_with_optional_alias.
    def enterExpression_with_optional_alias(
        self, ctx: ClickHouseParser.Expression_with_optional_aliasContext
    ):
        pass

    # Exit a parse tree produced by ClickHouseParser#expression_with_optional_alias.
    def exitExpression_with_optional_alias(
        self, ctx: ClickHouseParser.Expression_with_optional_aliasContext
    ):
        pass

    # Enter a parse tree produced by ClickHouseParser#ExprConcat.
    def enterExprConcat(self, ctx: ClickHouseParser.ExprConcatContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ExprConcat.
    def exitExprConcat(self, ctx: ClickHouseParser.ExprConcatContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#ExprCase.
    def enterExprCase(self, ctx: ClickHouseParser.ExprCaseContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ExprCase.
    def exitExprCase(self, ctx: ClickHouseParser.ExprCaseContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#ExprTupleElement.
    def enterExprTupleElement(self, ctx: ClickHouseParser.ExprTupleElementContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ExprTupleElement.
    def exitExprTupleElement(self, ctx: ClickHouseParser.ExprTupleElementContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#ExprNot.
    def enterExprNot(self, ctx: ClickHouseParser.ExprNotContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ExprNot.
    def exitExprNot(self, ctx: ClickHouseParser.ExprNotContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#ExprArray.
    def enterExprArray(self, ctx: ClickHouseParser.ExprArrayContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ExprArray.
    def exitExprArray(self, ctx: ClickHouseParser.ExprArrayContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#ExprWithAlias.
    def enterExprWithAlias(self, ctx: ClickHouseParser.ExprWithAliasContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ExprWithAlias.
    def exitExprWithAlias(self, ctx: ClickHouseParser.ExprWithAliasContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#ExprLogical.
    def enterExprLogical(self, ctx: ClickHouseParser.ExprLogicalContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ExprLogical.
    def exitExprLogical(self, ctx: ClickHouseParser.ExprLogicalContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#ExprIn.
    def enterExprIn(self, ctx: ClickHouseParser.ExprInContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ExprIn.
    def exitExprIn(self, ctx: ClickHouseParser.ExprInContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#ExprCast.
    def enterExprCast(self, ctx: ClickHouseParser.ExprCastContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ExprCast.
    def exitExprCast(self, ctx: ClickHouseParser.ExprCastContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#ExprOr.
    def enterExprOr(self, ctx: ClickHouseParser.ExprOrContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ExprOr.
    def exitExprOr(self, ctx: ClickHouseParser.ExprOrContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#ExprFunction.
    def enterExprFunction(self, ctx: ClickHouseParser.ExprFunctionContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ExprFunction.
    def exitExprFunction(self, ctx: ClickHouseParser.ExprFunctionContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#ExprMul.
    def enterExprMul(self, ctx: ClickHouseParser.ExprMulContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ExprMul.
    def exitExprMul(self, ctx: ClickHouseParser.ExprMulContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#ExprId.
    def enterExprId(self, ctx: ClickHouseParser.ExprIdContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ExprId.
    def exitExprId(self, ctx: ClickHouseParser.ExprIdContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#ExprLambda.
    def enterExprLambda(self, ctx: ClickHouseParser.ExprLambdaContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ExprLambda.
    def exitExprLambda(self, ctx: ClickHouseParser.ExprLambdaContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#ExprTernary.
    def enterExprTernary(self, ctx: ClickHouseParser.ExprTernaryContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ExprTernary.
    def exitExprTernary(self, ctx: ClickHouseParser.ExprTernaryContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#ExprParen.
    def enterExprParen(self, ctx: ClickHouseParser.ExprParenContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ExprParen.
    def exitExprParen(self, ctx: ClickHouseParser.ExprParenContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#ExprBetween.
    def enterExprBetween(self, ctx: ClickHouseParser.ExprBetweenContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ExprBetween.
    def exitExprBetween(self, ctx: ClickHouseParser.ExprBetweenContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#ExprSubquery.
    def enterExprSubquery(self, ctx: ClickHouseParser.ExprSubqueryContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ExprSubquery.
    def exitExprSubquery(self, ctx: ClickHouseParser.ExprSubqueryContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#ExprStar.
    def enterExprStar(self, ctx: ClickHouseParser.ExprStarContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ExprStar.
    def exitExprStar(self, ctx: ClickHouseParser.ExprStarContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#ExprInterval.
    def enterExprInterval(self, ctx: ClickHouseParser.ExprIntervalContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ExprInterval.
    def exitExprInterval(self, ctx: ClickHouseParser.ExprIntervalContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#ExprAnd.
    def enterExprAnd(self, ctx: ClickHouseParser.ExprAndContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ExprAnd.
    def exitExprAnd(self, ctx: ClickHouseParser.ExprAndContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#ExprArrayElement.
    def enterExprArrayElement(self, ctx: ClickHouseParser.ExprArrayElementContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ExprArrayElement.
    def exitExprArrayElement(self, ctx: ClickHouseParser.ExprArrayElementContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#ExprIsNull.
    def enterExprIsNull(self, ctx: ClickHouseParser.ExprIsNullContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ExprIsNull.
    def exitExprIsNull(self, ctx: ClickHouseParser.ExprIsNullContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#ExprList.
    def enterExprList(self, ctx: ClickHouseParser.ExprListContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ExprList.
    def exitExprList(self, ctx: ClickHouseParser.ExprListContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#ExprLiteral.
    def enterExprLiteral(self, ctx: ClickHouseParser.ExprLiteralContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ExprLiteral.
    def exitExprLiteral(self, ctx: ClickHouseParser.ExprLiteralContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#ExprUnaryMinus.
    def enterExprUnaryMinus(self, ctx: ClickHouseParser.ExprUnaryMinusContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ExprUnaryMinus.
    def exitExprUnaryMinus(self, ctx: ClickHouseParser.ExprUnaryMinusContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#ExprAdd.
    def enterExprAdd(self, ctx: ClickHouseParser.ExprAddContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#ExprAdd.
    def exitExprAdd(self, ctx: ClickHouseParser.ExprAddContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#interval_unit.
    def enterInterval_unit(self, ctx: ClickHouseParser.Interval_unitContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#interval_unit.
    def exitInterval_unit(self, ctx: ClickHouseParser.Interval_unitContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#expression_list.
    def enterExpression_list(self, ctx: ClickHouseParser.Expression_listContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#expression_list.
    def exitExpression_list(self, ctx: ClickHouseParser.Expression_listContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#not_empty_expression_list.
    def enterNot_empty_expression_list(
        self, ctx: ClickHouseParser.Not_empty_expression_listContext
    ):
        pass

    # Exit a parse tree produced by ClickHouseParser#not_empty_expression_list.
    def exitNot_empty_expression_list(self, ctx: ClickHouseParser.Not_empty_expression_listContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#array.
    def enterArray(self, ctx: ClickHouseParser.ArrayContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#array.
    def exitArray(self, ctx: ClickHouseParser.ArrayContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#function.
    def enterFunction(self, ctx: ClickHouseParser.FunctionContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#function.
    def exitFunction(self, ctx: ClickHouseParser.FunctionContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#function_parameters.
    def enterFunction_parameters(self, ctx: ClickHouseParser.Function_parametersContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#function_parameters.
    def exitFunction_parameters(self, ctx: ClickHouseParser.Function_parametersContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#function_arguments.
    def enterFunction_arguments(self, ctx: ClickHouseParser.Function_argumentsContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#function_arguments.
    def exitFunction_arguments(self, ctx: ClickHouseParser.Function_argumentsContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#function_name.
    def enterFunction_name(self, ctx: ClickHouseParser.Function_nameContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#function_name.
    def exitFunction_name(self, ctx: ClickHouseParser.Function_nameContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#identifier.
    def enterIdentifier(self, ctx: ClickHouseParser.IdentifierContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#identifier.
    def exitIdentifier(self, ctx: ClickHouseParser.IdentifierContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#keyword.
    def enterKeyword(self, ctx: ClickHouseParser.KeywordContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#keyword.
    def exitKeyword(self, ctx: ClickHouseParser.KeywordContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#compound_identifier.
    def enterCompound_identifier(self, ctx: ClickHouseParser.Compound_identifierContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#compound_identifier.
    def exitCompound_identifier(self, ctx: ClickHouseParser.Compound_identifierContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#literal.
    def enterLiteral(self, ctx: ClickHouseParser.LiteralContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#literal.
    def exitLiteral(self, ctx: ClickHouseParser.LiteralContext):
        pass

    # Enter a parse tree produced by ClickHouseParser#err.
    def enterErr(self, ctx: ClickHouseParser.ErrContext):
        pass

    # Exit a parse tree produced by ClickHouseParser#err.
    def exitErr(self, ctx: ClickHouseParser.ErrContext):
        pass


del ClickHouseParser
