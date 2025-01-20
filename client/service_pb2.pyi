from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CounterRequest(_message.Message):
    __slots__ = ("name", "max_number")
    NAME_FIELD_NUMBER: _ClassVar[int]
    MAX_NUMBER_FIELD_NUMBER: _ClassVar[int]
    name: str
    max_number: int
    def __init__(self, name: _Optional[str] = ..., max_number: _Optional[int] = ...) -> None: ...

class CounterResponse(_message.Message):
    __slots__ = ("number",)
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    number: int
    def __init__(self, number: _Optional[int] = ...) -> None: ...
