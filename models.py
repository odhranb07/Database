from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    phone = Column(String(30))

    def __repr__(self):
        return f"<Customer{self.id} {self.name}>"

engine = create_engine("sqlite:///shop.db")
    