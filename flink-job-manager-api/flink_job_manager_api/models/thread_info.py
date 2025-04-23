from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ThreadInfo")


@_attrs_define
class ThreadInfo:
    """
    Attributes:
        stringified_thread_info (Union[Unset, str]):
        thread_name (Union[Unset, str]):
    """

    stringified_thread_info: Union[Unset, str] = UNSET
    thread_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stringified_thread_info = self.stringified_thread_info

        thread_name = self.thread_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stringified_thread_info is not UNSET:
            field_dict["stringifiedThreadInfo"] = stringified_thread_info
        if thread_name is not UNSET:
            field_dict["threadName"] = thread_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        stringified_thread_info = d.pop("stringifiedThreadInfo", UNSET)

        thread_name = d.pop("threadName", UNSET)

        thread_info = cls(
            stringified_thread_info=stringified_thread_info,
            thread_name=thread_name,
        )

        thread_info.additional_properties = d
        return thread_info

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
