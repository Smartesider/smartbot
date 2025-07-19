from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Tenant(Base):
    __tablename__ = 'tenants'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    domain = Column(String, unique=True, nullable=False)
    created_at = Column(String, nullable=False)
    updated_at = Column(String, nullable=False)

    def __repr__(self):
        return f"<Tenant(id={self.id}, name={self.name}, domain={self.domain})>"