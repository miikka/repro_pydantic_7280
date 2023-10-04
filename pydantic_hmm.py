from typing import TYPE_CHECKING, Generic, Optional, TypeVar

from pydantic import BaseModel


class Data(BaseModel):
    pass


T = TypeVar("T", bound=Data)


class BaseWrapper(BaseModel, Generic[T]):
    data: Optional[T] = None


class Wrapper(BaseWrapper[Data]):
    pass


def test_vrapped_data_is_none() -> None:
    wrapper = Wrapper()
    if TYPE_CHECKING:
        reveal_type(wrapper.data)
    assert wrapper.data is None and True