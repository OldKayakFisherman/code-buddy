from dataclasses import dataclass, Field
from sqlmodel import SQLModel
from typing import Type, TypeVar, Generic

T = TypeVar('T', bound=SQLModel)

@dataclass
class PagedDataResult(Generic[T]):
    results: list[T] = Field(default_factory=list) 
    total_pages: int = 0




