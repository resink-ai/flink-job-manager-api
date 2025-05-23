from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plan import Plan


T = TypeVar("T", bound="JobPlanInfo")


@_attrs_define
class JobPlanInfo:
    """
    Attributes:
        plan (Union[Unset, Plan]):
    """

    plan: Union[Unset, "Plan"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.plan, Unset):
            plan = self.plan.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if plan is not UNSET:
            field_dict["plan"] = plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.plan import Plan

        d = src_dict.copy()
        _plan = d.pop("plan", UNSET)
        plan: Union[Unset, Plan]
        if isinstance(_plan, Unset):
            plan = UNSET
        else:
            plan = Plan.from_dict(_plan)

        job_plan_info = cls(
            plan=plan,
        )

        job_plan_info.additional_properties = d
        return job_plan_info

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
