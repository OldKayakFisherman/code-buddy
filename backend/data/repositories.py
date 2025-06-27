from data.results import PagedDataResult
import math
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func
from sqlmodel import SQLModel
from typing import Type, TypeVar, Generic

T = TypeVar('T', bound=SQLModel)

class BaseRepository(Generic[T]):

    def __init__(self, session: Session, model_class: Type[T]):
        self.__session = session
        self.__model_class = model_class

    @property
    def session(self):
        return self.__session

    @property
    def model(self):
        return self.__model_class
    

    def record_count(self) -> int:
        return self.session.query(self.model).count()
    
    def all(self) -> list[T]:
        return self.session.query(self.model).all()
    
    def paginate(self, page_size: int, page_requested: int) -> PagedDataResult:

        result = PagedDataResult[self.model]

        if page_requested > 1:
            offset = ((page_requested * page_size) - page_size)
            result.results = self.session.query(self.model).order_by(self.model.id).offset(offset).limit(page_size).all()
        else:
            result.results = self.session.query(self.model).order_by(self.model.id).limit(page_size)  

        
        result.total_pages = math.ceil(self.record_count() / page_size )