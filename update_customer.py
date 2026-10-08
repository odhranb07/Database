from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models import Customer, engine
#importing the select class from sqlalchemy, IntegrityError class from sqlalchemy.orm, and Customer and engine from models.py

customer_id =int(input ("customer id:"))
#asking the user to put the customer id in
with Session(engine) as Session:
#creating the session
    customer= Session.get(Customer, customer_id)
#from customer get the customer id from the inputted id
    if customer is None:
        print(f"customer {customer_id} not found")
#if the customer id is not found in the database then tell the user that the customer doesnt exist
    else:
        print("current email:", customer.email)
#show the user the current email of the customer
        customer.email= input("new email:").strip().lower()
#create the new change to the email and the session then recognises the change
        try:
            Session.commit()
#save the change made to the database
            print(f"customer {customer_id} email updated")
        except IntegrityError:
            Session.rollback()
            print("That email is already registered")
#if the email already belongs to someone explain to the user that the email is already registered and roll back the change



