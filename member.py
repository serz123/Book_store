from database import Database
from getpass import getpass
from validate_email import validate_email

#Inserts new member to database
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
         # Validate inputs
        if not (fname and lname and address and city and zip and email and password):
            raise ValueError("All fields except phone number are required.")

        # Additional validation for specific fields
        if len(fname) > 50:
            raise ValueError("First name exceeds maximum length (50).")
        if len(lname) > 50:
            raise ValueError("Last name exceeds maximum length (50).")
        if len(address) > 50:
            raise ValueError("Address exceeds maximum length (50).")
        if len(city) > 30:
            raise ValueError("City exceeds maximum length (30).")
        if not validate_email(email) :
            raise ValueError("Email is not valid.")
        if email_used(db, email):
            raise ValueError("Email is already in use.")
        if len(password) > 200:
            raise ValueError("Password exceeds maximum length (200).")
        if not zip.isdigit():
            raise ValueError("Zip code must be a number.")
        insert_query = f""" INSERT INTO members (fname, lname, address, city, zip, phone, email, password) VALUES ("{fname}", "{lname}", "{address}", "{city}", "{zip}", "{phone}", "{email}", "{password}")"""
        db.execute_with_commit(insert_query)
        print()
        print("You have registred successfully!\n")
        input("Press Enter to go back to Menu\n")
        print()
    except Exception as e:
        print("Registration FAILD!")
        print(e) 

#Checks if email is already used for other member
def email_used(db:Database, email):
    query = f""" SELECT * FROM members WHERE email="{email}"; """
    user = db.execute_with_fetchone(query)
    return user is not None

#Member loggs in
def member_login(db: Database):
    valid_cridentials = False
    email,password= (None,None)
    while(not valid_cridentials):
        email = input("Enter email: ")
        password = getpass("Enter password: ")
        user = check_cridentilas(db=db,email=email,password=password)
        if (user):
            valid_cridentials = True
            return user
        else:
            print("Cridentials not true...................")  

#Checks if inputed cridentials are valid
def check_cridentilas(db:Database, email, password):
    query = f""" SELECT * FROM members WHERE email="{email}" AND password="{password}" ; """
    user = db.execute_with_fetchone(query)
    return user