from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from flaskr.database import Base

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="books")
    name = Column(String(50), nullable=False)
    author = Column(String(50), nullable=False)
    publisher = Column(String(50), nullable=False)
    book_prize = Column(Integer)

    def __repr__(self):
        return f'<Book {self.name!r}>'