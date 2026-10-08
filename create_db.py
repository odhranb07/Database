from sqlalchemy import select
from sqlalchemy.orm import Session
from models import Base, Customer, engine

Base.metadata.create_all(engine)

with Session(engine) as Session:
    first= Session.scalars(select(Customer)).first()
    if first is None:
        Session.add_all([
            Customer(name="John Doe", email="john.doe@example.com", phone="123-456-7890"),
            Customer(name="Jane Smith", email="jane.smith@example.com", phone="098-765-4321"),
            Customer(name="Alice Johnson", email="alice.johnson@example.com"),
        ])
        Session.commit()

        
        print("database created with three customers")
    else:
        print("database already has customers")
