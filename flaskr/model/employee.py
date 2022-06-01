from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from flaskr.database import Base


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    salary = Column(Integer)
    apartment = Column(String(50))

    def __repr__(self):
        return f'<Employee {self.name!r}>'

class Engineer(Employee):
    __tablename__ = "engineer"
    id = Column(Integer, ForeignKey("employee.id"), primary_key=True)
    engineer_name = Column(String(30))

    __mapper_args__ = {
        "polymorphic_identity": "engineer",
    }

    def __repr__(self):
        return f'<Engineer {self.name!r}>'


class Manager(Employee):
    __tablename__ = "manager"
    id = Column(Integer, ForeignKey("employee.id"), primary_key=True)
    manager_name = Column(String(30))

    company_id = Column(ForeignKey("company.id"))
    company = relationship("Company", back_populates="managers")

    __mapper_args__ = {
        "polymorphic_identity": "manager",
    }

    def __repr__(self):
        return f'<Manager {self.name!r}>'