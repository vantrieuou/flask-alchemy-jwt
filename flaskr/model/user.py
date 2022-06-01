from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from flaskr.database import Base

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    public_id = Column(String(100), unique=True)
    email = Column(String(50), unique=True)
    password = Column(String(120))
    books = relationship("Book", back_populates="user")
    created_date = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'<User {self.email!r}>'