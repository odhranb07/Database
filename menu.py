from sqlalchemy.exc import IntegrityError
from sqlalchemy import Select
from sqlalchemy.orm import Session
from models import Customer, engine
#import as usaul
def list_customers(Session):
    stmt= Select(Customer).order_by(Customer.name)
    for customer in Session.scalars(stmt):
        print(customer.id, customer.name, customer.email)
#creating a function that lists the customers using the session its in
def add_customer(Session):
    name = input("name:").strip()
    email = input("email:").strip().lower()
    if name == "" or email == "":
        print("name and email are both required")
    else:
        try:
            Session.add(Customer(name=name, email=email))
            Session.commit()
            print(f"customer added successfully") 
        except IntegrityError:
            Session.rollback()
            print("That email is already registered")

def update_customer(Session):
    customer_id = int(input("customer id: "))
    stmt = Select(Customer).where(Customer.id == customer_id)
    customer=customer=Session.scalar(stmt)
    if customer is None:
        print(f"customer {customer_id} not found")
    else:
        print(f"customer found: {customer.id} {customer.name} {customer.email}")

def find_customer(Session):
    email = input("email to find:").strip().lower()
    stmt = Select(Customer).where(Customer.email == email)
    customer=Session.scalar(stmt)
    if customer is None:
        print(f"no customer with email {email} found")
    else:
        print(f"customer found: {customer.id} {customer.name} {customer.email}")

with Session(engine) as session:
#create a session for the entire menu
    while True:
#repeat the menu until the user chooses to quit
        print("1. List customers,2= Add customer,3= Update customer,4= find customer, 5=quit")
#show the choices to the user and ask them to choose one
        choice= input("choose:").strip()
        if choice == "1":
          list_customers(session)
#if the user chooses 1, the session will then list all the customers as requested 
        elif choice == "2":
            add_customer(session)
#if the user chooses 2, the program will add a new customer
        elif choice == "3":
            update_customer(session)
#if the user chooses 3, the program will update an existing customer
        elif choice == "4":
            find_customer(session)
#if the user chooses 4, the program will find a customer
        elif choice == "5":
            break
#if the user chooses 5, the program will break out of the loop and end
        else:
            print("you must type either 1, 2,3,4 or 5") 
#any other values that are entered remind the user to put in a valid value