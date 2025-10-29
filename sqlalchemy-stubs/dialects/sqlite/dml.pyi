from ... import util as util
from ...orm import Mapped
from ...sql import ColumnCollection
from ...sql.dml import Insert as StandardInsert
from ...sql.elements import ClauseElement
from ...sql.elements import ColumnElement
from ...sql.functions import GenericFunction

from typing import Any
from typing import Mapping
from typing import Optional
from typing import Union

class Insert(StandardInsert):
    stringify_dialect: str = ...
    # FLARE OVERRIDE
    @util.memoized_property
    def excluded(self) -> ColumnCollection: ...
    def on_conflict_do_update(
        self,
        index_elements: Optional[Any] = ...,
        index_where: Optional[Any] = ...,
        # FLARE OVERRIDE
        set_: (
            Mapping[object, Any]
            | Mapping[Mapped, Union[ColumnElement, GenericFunction]]
            | Mapping[ColumnElement, Union[ColumnElement, GenericFunction]]
        ) = ...,
        where: Optional[Any] = ...,
    ) -> None: ...
    def on_conflict_do_nothing(
        self,
        index_elements: Optional[Any] = ...,
        index_where: Optional[Any] = ...,
    ) -> None: ...

insert: Any

class OnConflictClause(ClauseElement):
    stringify_dialect: str = ...
    constraint_target: Any = ...
    inferred_target_elements: Any = ...
    inferred_target_whereclause: Any = ...
    def __init__(
        self,
        index_elements: Optional[Any] = ...,
        index_where: Optional[Any] = ...,
    ) -> None: ...

class OnConflictDoNothing(OnConflictClause):
    __visit_name__: str = ...

class OnConflictDoUpdate(OnConflictClause):
    __visit_name__: str = ...
    update_values_to_set: Any = ...
    update_whereclause: Any = ...
    def __init__(
        self,
        index_elements: Optional[Any] = ...,
        index_where: Optional[Any] = ...,
        # FLARE OVERRIDE
        set_: (
            Mapping[object, Any]
            | Mapping[Mapped, Union[ColumnElement, GenericFunction]]
            | Mapping[ColumnElement, Union[ColumnElement, GenericFunction]]
        ) = ...,
        where: Optional[Any] = ...,
    ) -> None: ...
