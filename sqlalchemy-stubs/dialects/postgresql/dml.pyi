from ... import Column
from ... import Constraint
from ... import Index
from ... import util as util
from ...orm import Mapped
from ...sql import ColumnCollection
from ...sql.dml import Insert as StandardInsert
from ...sql.elements import ClauseElement
from ...sql.elements import ColumnElement
from ...sql.functions import GenericFunction
from . import ExcludeConstraint

from typing import Any
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union

class Insert(StandardInsert):
    stringify_dialect: str = ...
    # FLARE OVERRIDE
    @util.memoized_property
    def excluded(self) -> ColumnCollection: ...
    def on_conflict_do_update(
        self,
        constraint: Optional[
            Union[str, Index, Constraint, ExcludeConstraint]
        ] = ...,
        index_elements: Sequence[Union[str, Column]] = ...,
        index_where: Optional[ClauseElement] = ...,
        # FLARE OVERRIDE
        set_: (
            Mapping[object, Any]
            | Mapping[Mapped, Union[ColumnElement, GenericFunction]]
            | Mapping[ColumnElement, Union[ColumnElement, GenericFunction]]
        ) = ...,
        where: Optional[ClauseElement] = ...,
    ) -> "Insert": ...
    def on_conflict_do_nothing(
        self,
        constraint: Optional[
            Union[str, Index, Constraint, ExcludeConstraint]
        ] = ...,
        index_elements: Optional[Sequence[Union[str, Column]]] = ...,
        index_where: Optional[Any] = ...,
    ) -> "Insert": ...

insert: Any

class OnConflictClause(ClauseElement):
    stringify_dialect: str = ...
    constraint_target: Any = ...
    inferred_target_elements: Any = ...
    inferred_target_whereclause: Any = ...
    def __init__(
        self,
        constraint: Optional[
            Union[str, Index, Constraint, ExcludeConstraint]
        ] = ...,
        index_elements: Optional[Sequence[Union[str, Column]]] = ...,
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
        constraint: Optional[
            Union[str, Index, Constraint, ExcludeConstraint]
        ] = ...,
        index_elements: Optional[Sequence[Union[str, Column]]] = ...,
        index_where: Optional[Any] = ...,
        # FLARE OVERRIDE
        set_: (
            Mapping[object, Any]
            | Mapping[Mapped, Union[ColumnElement, GenericFunction]]
            | Mapping[ColumnElement, Union[ColumnElement, GenericFunction]]
        ) = ...,
        where: Optional[ClauseElement] = ...,
    ) -> None: ...
