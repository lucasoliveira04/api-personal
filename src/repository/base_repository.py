from sqlalchemy.orm import Session 
from typing import TypeVar, Type, List, Generic, Optional

T = TypeVar('T')

class BaseRepository(Generic[T]):
    def __init__(self, session: Session, model_class: Type[T]) -> None:
        self.session = session
        self.model_class = model_class

    def find_by_id(self, id: int | str) -> Optional[T]:
            return self.session.query(self.model_class).filter(self.model_class.id == id).first()

    def find_all(self) -> List[T]:
        return self.session.query(self.model_class).all()
    
    def save(self, obj: T) -> T:
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)
        return obj
    
    def delete(self, obj: T) -> None:
        self.session.delete(obj)
        self.session.commit()

    def delete_by_id(self, id: int | str):
        obj = self.find_by_id(id)
        if obj:
             self.delete(obj)
        else:
            raise ValueError(f"Object with id {id} not found")