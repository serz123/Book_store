from menu import print_header,print_option,check_choice
from getpass import getpass
from mysql.connector import connect
from member import check_cridentilas

options_main = ["Member Login", "New Member Registration"]
options_login = []
def main_menu(db):
    #print header
    print_header("Welcome to the Online Book Store")
    
    while (True):
        # print options
        print_option(options_main)

        #check the user choice
        choice_main = check_choice(len(options_main))

        if choice_main == 1:
            member_login(db)
        elif choice_main == 2: 
            print()
        else: 
            quit()   

valid_cridentials = False
email,password= (None,None)

def member_login(db):
   while(not valid_cridentials):
    email = input("Enter email:")
    password = getpass("Enter password:")
    if (check_cridentilas(db=db,email=email,password=password)):
        valid_conneciton = True
    else:
        print("Cridentials not true...................")  



