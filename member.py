from database import Database
from getpass import getpass

def add_member(db:Database):
    print("Welcome to the Online Book Store")
    print("New Member registration")
    fname = input("First name: ")
    lname = input("Last name: ")
    address= input("Address: ")
    city = input("City: ")
    zip = input("Zip: ")
    phone=input("Phone: ")
    email = input("Email: ")
    password = getpass("Password: ")

    try:
        insert_query = f""" INSERT INTO members (fname, lname, address, city, zip, phone, email, password) VALUES ("{fname}", "{lname}", "{address}", "{city}", "{zip}", "{phone}", "{email}", "{password}")"""
        db.execute_with_commit(insert_query)
        print("You have registred successfully!")
        input("Press Enter to go back to Menu")
    except Exception as e:
        print("Registration FAILD!")
        print(e) 

#check the member cridentials
def check_cridentilas(db:Database, email, password):
    query = f""" SELECT * FROM members WHERE email="{email}" AND password="{password}" ; """
    user = db.execute_with_fetchone(query)
    return user is not None