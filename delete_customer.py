from sqlalchemy.orm import Session
from models import Customer, engine
#import as as usal
customer_id = int(input("customer id: "))
#as the user for the customer id as an integer
with Session(engine) as session:
    customer = session.get(Customer, customer_id)
#create the session and retrive the customer id

    if customer is None:
        print(f"Customer with id {customer_id} not found.")
#if the customer related to the id inputted let the user know the customer does not exist
    else:
       answer=input(f"Are you sure you want to delete {customer.name}? (y/n): ")
#if the customer does exist then ask the user if they are sure they want to delete the customer
       if answer.lower() == "y":
#user must type the letter y in lowercase to delete the customer
              session.delete(customer)
              session.commit()
              print(f"Customer {customer.name} deleted.")
#if the user is sure of the deletion then the session will delete the customer and save the changes and then lets the customer know that the customer has been deleted
       else:
            print("Deletion cancelled.")
#if the customer says they dont want the customer deleted then the session will acknowledge it and discard the changes