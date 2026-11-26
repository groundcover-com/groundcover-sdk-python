from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.explain_source_is_where_the_query_comes_from_exactly_one_of_a_span_or_a_query import (
        ExplainSourceIsWhereTheQueryComesFromExactlyOneOfASpanOrAQuery,
    )


T = TypeVar("T", bound="ExplainRequestNamesADatabaseServerAndTheQueryToExplainOnIt")


@_attrs_define
class ExplainRequestNamesADatabaseServerAndTheQueryToExplainOnIt:
    """
    Attributes:
        cluster (str): The cluster the query came from. Of several integrations on the server, one that runs there is
            preferred.
        server_address (str): The server's host, as its PostgreSQL integration names it.
        source (ExplainSourceIsWhereTheQueryComesFromExactlyOneOfASpanOrAQuery):
        db_name (str | Unset): The database to explain in. Defaults to the span's, when the source is one, then the
            integration's.
        env (str | Unset): The env the query came from. It picks between integrations the cluster does not tell apart.
        server_port (int | Unset): Defaults to 5432.
    """

    cluster: str
    server_address: str
    source: ExplainSourceIsWhereTheQueryComesFromExactlyOneOfASpanOrAQuery
    db_name: str | Unset = UNSET
    env: str | Unset = UNSET
    server_port: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cluster = self.cluster

        server_address = self.server_address

        source = self.source.to_dict()

        db_name = self.db_name

        env = self.env

        server_port = self.server_port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cluster": cluster,
                "server_address": server_address,
                "source": source,
            }
        )
        if db_name is not UNSET:
            field_dict["db_name"] = db_name
        if env is not UNSET:
            field_dict["env"] = env
        if server_port is not UNSET:
            field_dict["server_port"] = server_port

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.explain_source_is_where_the_query_comes_from_exactly_one_of_a_span_or_a_query import (
            ExplainSourceIsWhereTheQueryComesFromExactlyOneOfASpanOrAQuery,
        )

        d = dict(src_dict)
        cluster = d.pop("cluster")

        server_address = d.pop("server_address")

        source = ExplainSourceIsWhereTheQueryComesFromExactlyOneOfASpanOrAQuery.from_dict(d.pop("source"))

        db_name = d.pop("db_name", UNSET)

        env = d.pop("env", UNSET)

        server_port = d.pop("server_port", UNSET)

        explain_request_names_a_database_server_and_the_query_to_explain_on_it = cls(
            cluster=cluster,
            server_address=server_address,
            source=source,
            db_name=db_name,
            env=env,
            server_port=server_port,
        )

        explain_request_names_a_database_server_and_the_query_to_explain_on_it.additional_properties = d
        return explain_request_names_a_database_server_and_the_query_to_explain_on_it

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
