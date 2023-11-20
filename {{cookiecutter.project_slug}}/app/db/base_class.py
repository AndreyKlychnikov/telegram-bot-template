from typing import Any

from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    id: Any

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
