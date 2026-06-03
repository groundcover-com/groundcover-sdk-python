from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group import Group
    from ..models.join_defines_a_join_operation_between_two_pipelines import (
        JoinDefinesAJoinOperationBetweenTwoPipelines,
    )
    from ..models.limit_by_defines_per_group_limiting_for_sql_queries_eglimitby import (
        LimitByDefinesPerGroupLimitingForSQLQueriesEGLIMITBY,
    )
    from ..models.math_expression import MathExpression
    from ..models.search_order_by_defines_the_order_for_a_search_pipeline import (
        SearchOrderByDefinesTheOrderForASearchPipeline,
    )
    from ..models.selector import Selector
    from ..models.transform_represents_a_column_transform_that_registers_in_the_alias_registry_transforms_dont_create_subqueries_they_register_handlers_that_resolve_aliases_to_sql_expressions import (
        TransformRepresentsAColumnTransformThatRegistersInTheAliasRegistryTransformsDontCreateSubqueriesTheyRegisterHandlersThatResolveAliasesToSQLExpressions,
    )
    from ..models.union_defines_a_union_operation_between_two_pipelines_unionall import (
        UnionDefinesAUnionOperationBetweenTwoPipelinesUNIONALL,
    )


T = TypeVar("T", bound="SqlPipelineDefinesAPipelineForSearchQueries")


@_attrs_define
class SqlPipelineDefinesAPipelineForSearchQueries:
    """When Join is set, the pipeline acts as a container for the join operation ONLY.
    When Union is set, the pipeline acts as a container for the union operation ONLY.
    In these cases, no other fields should be used.

        Attributes:
            domain (str | Unset): DomainType represents the type of data domain (logs, traces, events, entities, issues,
                apm)
            except_ (list[Selector] | Unset):
            filters (Group | Unset):
            from_ (SqlPipelineDefinesAPipelineForSearchQueries | Unset): When Join is set, the pipeline acts as a container
                for the join operation ONLY.
                When Union is set, the pipeline acts as a container for the union operation ONLY.
                In these cases, no other fields should be used.
            group_by (list[Selector] | Unset):
            having (Group | Unset):
            join (JoinDefinesAJoinOperationBetweenTwoPipelines | Unset):
            limit (int | Unset):
            limit_by (LimitByDefinesPerGroupLimitingForSQLQueriesEGLIMITBY | Unset):
            math_expression (list[MathExpression] | Unset):
            offset (int | Unset):
            order_by (list[SearchOrderByDefinesTheOrderForASearchPipeline] | Unset):
            sample (int | Unset):
            selectors (list[Selector] | Unset):
            transforms (list[TransformRepresentsAColumnTransformThatRegistersInTheAliasRegistryTransformsDontCreateSubquerie
                sTheyRegisterHandlersThatResolveAliasesToSQLExpressions] | Unset):
            union (UnionDefinesAUnionOperationBetweenTwoPipelinesUNIONALL | Unset):
    """

    domain: str | Unset = UNSET
    except_: list[Selector] | Unset = UNSET
    filters: Group | Unset = UNSET
    from_: SqlPipelineDefinesAPipelineForSearchQueries | Unset = UNSET
    group_by: list[Selector] | Unset = UNSET
    having: Group | Unset = UNSET
    join: JoinDefinesAJoinOperationBetweenTwoPipelines | Unset = UNSET
    limit: int | Unset = UNSET
    limit_by: LimitByDefinesPerGroupLimitingForSQLQueriesEGLIMITBY | Unset = UNSET
    math_expression: list[MathExpression] | Unset = UNSET
    offset: int | Unset = UNSET
    order_by: list[SearchOrderByDefinesTheOrderForASearchPipeline] | Unset = UNSET
    sample: int | Unset = UNSET
    selectors: list[Selector] | Unset = UNSET
    transforms: (
        list[
            TransformRepresentsAColumnTransformThatRegistersInTheAliasRegistryTransformsDontCreateSubqueriesTheyRegisterHandlersThatResolveAliasesToSQLExpressions
        ]
        | Unset
    ) = UNSET
    union: UnionDefinesAUnionOperationBetweenTwoPipelinesUNIONALL | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain = self.domain

        except_: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.except_, Unset):
            except_ = []
            for except_item_data in self.except_:
                except_item = except_item_data.to_dict()
                except_.append(except_item)

        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        from_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        group_by: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.group_by, Unset):
            group_by = []
            for group_by_item_data in self.group_by:
                group_by_item = group_by_item_data.to_dict()
                group_by.append(group_by_item)

        having: dict[str, Any] | Unset = UNSET
        if not isinstance(self.having, Unset):
            having = self.having.to_dict()

        join: dict[str, Any] | Unset = UNSET
        if not isinstance(self.join, Unset):
            join = self.join.to_dict()

        limit = self.limit

        limit_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.limit_by, Unset):
            limit_by = self.limit_by.to_dict()

        math_expression: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.math_expression, Unset):
            math_expression = []
            for math_expression_item_data in self.math_expression:
                math_expression_item = math_expression_item_data.to_dict()
                math_expression.append(math_expression_item)

        offset = self.offset

        order_by: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.order_by, Unset):
            order_by = []
            for order_by_item_data in self.order_by:
                order_by_item = order_by_item_data.to_dict()
                order_by.append(order_by_item)

        sample = self.sample

        selectors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.selectors, Unset):
            selectors = []
            for selectors_item_data in self.selectors:
                selectors_item = selectors_item_data.to_dict()
                selectors.append(selectors_item)

        transforms: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.transforms, Unset):
            transforms = []
            for transforms_item_data in self.transforms:
                transforms_item = transforms_item_data.to_dict()
                transforms.append(transforms_item)

        union: dict[str, Any] | Unset = UNSET
        if not isinstance(self.union, Unset):
            union = self.union.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if domain is not UNSET:
            field_dict["domain"] = domain
        if except_ is not UNSET:
            field_dict["except"] = except_
        if filters is not UNSET:
            field_dict["filters"] = filters
        if from_ is not UNSET:
            field_dict["from"] = from_
        if group_by is not UNSET:
            field_dict["groupBy"] = group_by
        if having is not UNSET:
            field_dict["having"] = having
        if join is not UNSET:
            field_dict["join"] = join
        if limit is not UNSET:
            field_dict["limit"] = limit
        if limit_by is not UNSET:
            field_dict["limitBy"] = limit_by
        if math_expression is not UNSET:
            field_dict["mathExpression"] = math_expression
        if offset is not UNSET:
            field_dict["offset"] = offset
        if order_by is not UNSET:
            field_dict["orderBy"] = order_by
        if sample is not UNSET:
            field_dict["sample"] = sample
        if selectors is not UNSET:
            field_dict["selectors"] = selectors
        if transforms is not UNSET:
            field_dict["transforms"] = transforms
        if union is not UNSET:
            field_dict["union"] = union

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group import Group
        from ..models.join_defines_a_join_operation_between_two_pipelines import (
            JoinDefinesAJoinOperationBetweenTwoPipelines,
        )
        from ..models.limit_by_defines_per_group_limiting_for_sql_queries_eglimitby import (
            LimitByDefinesPerGroupLimitingForSQLQueriesEGLIMITBY,
        )
        from ..models.math_expression import MathExpression
        from ..models.search_order_by_defines_the_order_for_a_search_pipeline import (
            SearchOrderByDefinesTheOrderForASearchPipeline,
        )
        from ..models.selector import Selector
        from ..models.transform_represents_a_column_transform_that_registers_in_the_alias_registry_transforms_dont_create_subqueries_they_register_handlers_that_resolve_aliases_to_sql_expressions import (
            TransformRepresentsAColumnTransformThatRegistersInTheAliasRegistryTransformsDontCreateSubqueriesTheyRegisterHandlersThatResolveAliasesToSQLExpressions,
        )
        from ..models.union_defines_a_union_operation_between_two_pipelines_unionall import (
            UnionDefinesAUnionOperationBetweenTwoPipelinesUNIONALL,
        )

        d = dict(src_dict)
        domain = d.pop("domain", UNSET)

        _except_ = d.pop("except", UNSET)
        except_: list[Selector] | Unset = UNSET
        if _except_ is not UNSET:
            except_ = []
            for except_item_data in _except_:
                except_item = Selector.from_dict(except_item_data)

                except_.append(except_item)

        _filters = d.pop("filters", UNSET)
        filters: Group | Unset
        if isinstance(_filters, Unset) or _filters is None:
            filters = UNSET
        else:
            filters = Group.from_dict(_filters)

        _from_ = d.pop("from", UNSET)
        from_: SqlPipelineDefinesAPipelineForSearchQueries | Unset
        if isinstance(_from_, Unset) or _from_ is None:
            from_ = UNSET
        else:
            from_ = SqlPipelineDefinesAPipelineForSearchQueries.from_dict(_from_)

        _group_by = d.pop("groupBy", UNSET)
        group_by: list[Selector] | Unset = UNSET
        if _group_by is not UNSET:
            group_by = []
            for group_by_item_data in _group_by:
                group_by_item = Selector.from_dict(group_by_item_data)

                group_by.append(group_by_item)

        _having = d.pop("having", UNSET)
        having: Group | Unset
        if isinstance(_having, Unset) or _having is None:
            having = UNSET
        else:
            having = Group.from_dict(_having)

        _join = d.pop("join", UNSET)
        join: JoinDefinesAJoinOperationBetweenTwoPipelines | Unset
        if isinstance(_join, Unset) or _join is None:
            join = UNSET
        else:
            join = JoinDefinesAJoinOperationBetweenTwoPipelines.from_dict(_join)

        limit = d.pop("limit", UNSET)

        _limit_by = d.pop("limitBy", UNSET)
        limit_by: LimitByDefinesPerGroupLimitingForSQLQueriesEGLIMITBY | Unset
        if isinstance(_limit_by, Unset) or _limit_by is None:
            limit_by = UNSET
        else:
            limit_by = LimitByDefinesPerGroupLimitingForSQLQueriesEGLIMITBY.from_dict(_limit_by)

        _math_expression = d.pop("mathExpression", UNSET)
        math_expression: list[MathExpression] | Unset = UNSET
        if _math_expression is not UNSET:
            math_expression = []
            for math_expression_item_data in _math_expression:
                math_expression_item = MathExpression.from_dict(math_expression_item_data)

                math_expression.append(math_expression_item)

        offset = d.pop("offset", UNSET)

        _order_by = d.pop("orderBy", UNSET)
        order_by: list[SearchOrderByDefinesTheOrderForASearchPipeline] | Unset = UNSET
        if _order_by is not UNSET:
            order_by = []
            for order_by_item_data in _order_by:
                order_by_item = SearchOrderByDefinesTheOrderForASearchPipeline.from_dict(order_by_item_data)

                order_by.append(order_by_item)

        sample = d.pop("sample", UNSET)

        _selectors = d.pop("selectors", UNSET)
        selectors: list[Selector] | Unset = UNSET
        if _selectors is not UNSET:
            selectors = []
            for selectors_item_data in _selectors:
                selectors_item = Selector.from_dict(selectors_item_data)

                selectors.append(selectors_item)

        _transforms = d.pop("transforms", UNSET)
        transforms: (
            list[
                TransformRepresentsAColumnTransformThatRegistersInTheAliasRegistryTransformsDontCreateSubqueriesTheyRegisterHandlersThatResolveAliasesToSQLExpressions
            ]
            | Unset
        ) = UNSET
        if _transforms is not UNSET:
            transforms = []
            for transforms_item_data in _transforms:
                transforms_item = TransformRepresentsAColumnTransformThatRegistersInTheAliasRegistryTransformsDontCreateSubqueriesTheyRegisterHandlersThatResolveAliasesToSQLExpressions.from_dict(
                    transforms_item_data
                )

                transforms.append(transforms_item)

        _union = d.pop("union", UNSET)
        union: UnionDefinesAUnionOperationBetweenTwoPipelinesUNIONALL | Unset
        if isinstance(_union, Unset) or _union is None:
            union = UNSET
        else:
            union = UnionDefinesAUnionOperationBetweenTwoPipelinesUNIONALL.from_dict(_union)

        sql_pipeline_defines_a_pipeline_for_search_queries = cls(
            domain=domain,
            except_=except_,
            filters=filters,
            from_=from_,
            group_by=group_by,
            having=having,
            join=join,
            limit=limit,
            limit_by=limit_by,
            math_expression=math_expression,
            offset=offset,
            order_by=order_by,
            sample=sample,
            selectors=selectors,
            transforms=transforms,
            union=union,
        )

        sql_pipeline_defines_a_pipeline_for_search_queries.additional_properties = d
        return sql_pipeline_defines_a_pipeline_for_search_queries

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
