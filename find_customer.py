from sqlalchemy import select
from sqlalchemy.orm import Session
from models import Customer, engine
#importing the select class from sqlalchemy, Session class from sqlalchemy.orm, and Customer and engine from models.py

email= input("email to find:").strip().lower()
#asking for an email to be put in to find a customer in the database
with Session(engine)as Session:
#creating the session
    stmt = select(Customer).where(Customer.email==email)
#creating a select statement to find a customer with the email that was inputted
    customer= Session.scalar(stmt)
#sending the query to the database and printing the answer into an organised python list of customer objects

    if customer is None:
        print(f"no customer with email {email} found")
#if no customer with that emailis found, print that no customer was found with that email
    else:
        print(f"customer found: {customer.id} {customer.name} {customer.email}")
#print the customer with that email and order it in a list by their id,name and email using dots

    