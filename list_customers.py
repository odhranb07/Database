from sqlalchemy import Select
from sqlalchemy.orm import Session
from models import Customer, engine
#importing the Select class from sqlalchemy, Session class from sqlalchemy.orm, and Customer and engine from models.py

with Session(engine) as session:
#opening the session
    stmt= Select(Customer). order_by(Customer.name)
#selecting all customers from the database and ordering them by name
    customers= session.scalars(stmt).all()
#send the query to the database and collect the answer into an organised python list of customer objects#

    print(f"{len(customers)}customer(s)")
#print how many customers were found in the database
    for customer in customers:
#go through the list of customers and print their id, name and email
        print(customer.id, customer.name, customer.email)
        
    