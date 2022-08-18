# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401
import typing  # noqa: F401
import functools  # noqa: F401

from frozendict import frozendict  # noqa: F401

import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401

from petstore_api.schemas import (  # noqa: F401
    AnyTypeSchema,
    ComposedSchema,
    DictSchema,
    ListSchema,
    StrSchema,
    IntSchema,
    Int32Schema,
    Int64Schema,
    Float32Schema,
    Float64Schema,
    NumberSchema,
    UUIDSchema,
    DateSchema,
    DateTimeSchema,
    DecimalSchema,
    BoolSchema,
    BinarySchema,
    NoneSchema,
    none_type,
    Configuration,
    Unset,
    unset,
    ComposedBase,
    ListBase,
    DictBase,
    NoneBase,
    StrBase,
    IntBase,
    Int32Base,
    Int64Base,
    Float32Base,
    Float64Base,
    NumberBase,
    UUIDBase,
    DateBase,
    DateTimeBase,
    BoolBase,
    BinaryBase,
    Schema,
    NoneClass,
    BoolClass,
    _SchemaValidator,
    _SchemaTypeChecker,
    _SchemaEnumMaker
)


class FormatTest(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    _required_property_names = {
        "date",
        "number",
        "password",
        "byte",
    }
    
    
    class integer(
        _SchemaValidator(
            inclusive_maximum=100,
            inclusive_minimum=10,
            multiple_of=2,
        ),
        IntSchema
    ):
        pass
    int32 = Int32Schema
    
    
    class int32withValidations(
        _SchemaValidator(
            inclusive_maximum=200,
            inclusive_minimum=20,
        ),
        Int32Schema
    ):
        pass
    int64 = Int64Schema
    
    
    class number(
        _SchemaValidator(
            inclusive_maximum=543.2,
            inclusive_minimum=32.1,
            multiple_of=32.5,
        ),
        NumberSchema
    ):
        pass
    
    
    class _float(
        _SchemaValidator(
            inclusive_maximum=987.6,
            inclusive_minimum=54.3,
        ),
        Float32Schema
    ):
        pass
    locals()["float"] = _float
    del locals()['_float']
    """
    NOTE:
    openapi/json-schema allows properties to have invalid python names
    The above local assignment allows the code to keep those invalid python names
    This allows properties to have names like 'some-name', '1 bad name'
    Properties with these names are omitted from the __new__ + _from_openapi_data signatures
    - __new__ these properties can be passed in as **kwargs
    - _from_openapi_data these are passed in in a dict in the first positional argument *arg
    If the property is required and was not passed in, an exception will be thrown
    """
    float32 = Float32Schema
    
    
    class double(
        _SchemaValidator(
            inclusive_maximum=123.4,
            inclusive_minimum=67.8,
        ),
        Float64Schema
    ):
        pass
    float64 = Float64Schema
    
    
    class arrayWithUniqueItems(
        _SchemaValidator(
            unique_items=True,
        ),
        ListSchema
    ):
        _items = NumberSchema
    
    
    class string(
        _SchemaValidator(
            regex=[{
                'pattern': r'[a-z]',  # noqa: E501
                'flags': (
                    re.IGNORECASE
                )
            }],
        ),
        StrSchema
    ):
        pass
    byte = StrSchema
    binary = BinarySchema
    date = DateSchema
    dateTime = DateTimeSchema
    uuid = UUIDSchema
    uuidNoExample = UUIDSchema
    
    
    class password(
        _SchemaValidator(
            max_length=64,
            min_length=10,
        ),
        StrSchema
    ):
        pass
    
    
    class pattern_with_digits(
        _SchemaValidator(
            regex=[{
                'pattern': r'^\d{10}$',  # noqa: E501
            }],
        ),
        StrSchema
    ):
        pass
    
    
    class pattern_with_digits_and_delimiter(
        _SchemaValidator(
            regex=[{
                'pattern': r'^image_\d{1,3}$',  # noqa: E501
                'flags': (
                    re.IGNORECASE
                )
            }],
        ),
        StrSchema
    ):
        pass
    noneProp = NoneSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        date: date,
        number: number,
        password: password,
        byte: byte,
        integer: typing.Union[integer, Unset] = unset,
        int32: typing.Union[int32, Unset] = unset,
        int32withValidations: typing.Union[int32withValidations, Unset] = unset,
        int64: typing.Union[int64, Unset] = unset,
        float32: typing.Union[float32, Unset] = unset,
        double: typing.Union[double, Unset] = unset,
        float64: typing.Union[float64, Unset] = unset,
        arrayWithUniqueItems: typing.Union[arrayWithUniqueItems, Unset] = unset,
        string: typing.Union[string, Unset] = unset,
        binary: typing.Union[binary, Unset] = unset,
        dateTime: typing.Union[dateTime, Unset] = unset,
        uuid: typing.Union[uuid, Unset] = unset,
        uuidNoExample: typing.Union[uuidNoExample, Unset] = unset,
        pattern_with_digits: typing.Union[pattern_with_digits, Unset] = unset,
        pattern_with_digits_and_delimiter: typing.Union[pattern_with_digits_and_delimiter, Unset] = unset,
        noneProp: typing.Union[noneProp, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'FormatTest':
        return super().__new__(
            cls,
            *args,
            date=date,
            number=number,
            password=password,
            byte=byte,
            integer=integer,
            int32=int32,
            int32withValidations=int32withValidations,
            int64=int64,
            float32=float32,
            double=double,
            float64=float64,
            arrayWithUniqueItems=arrayWithUniqueItems,
            string=string,
            binary=binary,
            dateTime=dateTime,
            uuid=uuid,
            uuidNoExample=uuidNoExample,
            pattern_with_digits=pattern_with_digits,
            pattern_with_digits_and_delimiter=pattern_with_digits_and_delimiter,
            noneProp=noneProp,
            _configuration=_configuration,
            **kwargs,
        )
