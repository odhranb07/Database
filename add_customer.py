from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models import Customer, engine

name=input("name:") .strip()
email=input("email:").strip().lower()


if name =="" or email =="" :
    print("name and email are both required")
else:
    with Session(engine) as session:
        try:
            session.add(Customer(name=name, email=email))
            session.commit()
            print(f"customer added successfully")
        except IntegrityError:
            session.rollback()
            print("That email is already registered")
            

  
