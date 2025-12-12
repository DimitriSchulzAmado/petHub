from sqlalchemy import BIGINT, Column, String

from src.models.sqlite.settings.base import Base


class PetsTable(Base):
    __tablename__ = "pets"

    id = Column(BIGINT, primary_key=True)
    name = Column(String, nullable=True)
    type = Column(String, nullable=True)

    def __repr__(self) -> str:
        return f"Pets [name={self.name}, type={self.type}]"
