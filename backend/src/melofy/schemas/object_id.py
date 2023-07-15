from typing import Any, Callable

from bson import ObjectId
from pydantic_core import core_schema
from pydantic import BaseModel, field_serializer


class PyObjectId(ObjectId):
    @classmethod
    def __get_pydantic_json_schema__(
        cls, core_schema: core_schema.JsonSchema, handler):
        json_schema = handler(core_schema)
        json_schema.update(type="string", format="binary")
        return json_schema
    
    @classmethod
    def validate(
        cls, __input_value: Any, _: core_schema.ValidationInfo
    ) -> ObjectId:
        if not isinstance(__input_value, ObjectId):
            raise ValueError(f"Expected bson.ObjectId, received: {type(__input_value)}")
        return __input_value
    
    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: type[Any], handler: Callable[[Any], core_schema.CoreSchema]
    ) -> core_schema.CoreSchema:
        return core_schema.general_plain_validator_function(cls.validate)


class BaseObjectId(BaseModel):
    mongo_id: PyObjectId


    @field_serializer("mongo_id")
    def serialize_mongo_id(self, mongo_id: PyObjectId, _info) -> str:
        return str(mongo_id)

    # class Config:
    #     populate_by_name=True
    #     arbitarty_types_allowed=True

