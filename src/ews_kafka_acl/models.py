# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

from cloudformation_cli_python_lib.interface import (
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class ResourceHandlerRequest(BaseResourceHandlerRequest):
    # pylint: disable=invalid-name
    desiredResourceState: Optional["ResourceModel"]
    previousResourceState: Optional["ResourceModel"]


@dataclass
class ResourceModel(BaseModel):
    Policies: Optional[Sequence["_Policy"]]
    Id: Optional[str]
    BootstrapServers: Optional[str]
    SecurityProtocol: Optional[str]
    SASLMechanism: Optional[str]
    SASLUsername: Optional[str]
    SASLPassword: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Policies=deserialize_list(json_data.get("Policies"), Policy),
            Id=json_data.get("Id"),
            BootstrapServers=json_data.get("BootstrapServers"),
            SecurityProtocol=json_data.get("SecurityProtocol"),
            SASLMechanism=json_data.get("SASLMechanism"),
            SASLUsername=json_data.get("SASLUsername"),
            SASLPassword=json_data.get("SASLPassword"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Policy(BaseModel):
    Resource: Optional[str]
    PatternType: Optional[str]
    Principal: Optional[str]
    ResourceType: Optional[str]
    Action: Optional[str]
    Effect: Optional[str]
    Host: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Policy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Policy"]:
        if not json_data:
            return None
        return cls(
            Resource=json_data.get("Resource"),
            PatternType=json_data.get("PatternType"),
            Principal=json_data.get("Principal"),
            ResourceType=json_data.get("ResourceType"),
            Action=json_data.get("Action"),
            Effect=json_data.get("Effect"),
            Host=json_data.get("Host"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Policy = Policy
