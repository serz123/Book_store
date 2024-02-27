from menu import print_header,print_option,check_choice
from getpass import getpass
from mysql.connector import connect
from member import check_cridentilas, add_member

options_main = ["Member Login", "New Member Registration"]
options_member = ["Browse by Subject", "Search by Author/Title", "Check Out", "Logout"]
def main_menu(db):
    #print header
    print_header("Welcome to the Online Book Store", "           ")
    
    while (True):
        # print options
        print_option(options_main)

        #check the user choice
        choice_main = check_choice(len(options_main))

        if choice_main == 1:
            valid = member_login(db)
            if(valid):
                member_menu(db)
        elif choice_main == 2: 
            add_member(db)
        else: 
            quit()   

def member_login(db):
    valid_cridentials = False
    email,password= (None,None)
    while(not valid_cridentials):
        email = input("Enter email:")
        password = getpass("Enter password:")
        if (check_cridentilas(db=db,email=email,password=password)):
            valid_cridentials = True
            return valid_cridentials
        else:
            print("Cridentials not true...................")  

def member_menu(db):
       #print header
    print_header("Welcome to the Online Book Store", "Member Menu                            ***\n***                         ")
    
    while (True):
        # print options
        print_option(options_member)

        #check the user choice
        choice_main = check_choice(len(options_member))

        if choice_main == 1:
            valid = member_login(db)
            if(valid):
                member_menu()
        elif choice_main == 2: 
            add_member(db)
        else: 
            quit()   
