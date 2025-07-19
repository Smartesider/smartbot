from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.src.core.database import Base

class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)

    user = relationship("User", back_populates="appointments")

    def __repr__(self):
        return f"<Appointment(id={self.id}, title={self.title}, start_time={self.start_time}, end_time={self.end_time})>"