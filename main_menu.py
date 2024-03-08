from menu import print_header, print_option, check_choice, print_book
from getpass import getpass
from member import member_login, add_member
from books import list_all_subjects, search_by_subjects, search_by_author_sub, search_by_title_sub
from cart import add_to_cart
from check_out import get_invoice

user_data = {}
options_main = ["Member Login", "New Member Registration"]
options_member = ["Browse by Subject", "Search by Author/Title", "Check Out", "Logout"]
options_author_or_title = ['Author Search', 'Title Search', 'Go Back To Main Menu']

#Main menu of the application
def main_menu(db):
    global user_data
    #print header
    print_header("Welcome to the Online Book Store", "           ")
    
    while (True):
        # print options
        print_option(options_main)

        #check the user choice
        choice_main = check_choice(len(options_main))

        if choice_main == 1:
            user = member_login(db)
            if(user):
                user_data = user
                member_menu(db)
        elif choice_main == 2: 
            add_member(db)
        else: 
            quit()   

#Menu for memeber that is logged in
def member_menu(db):
    global user_data
       #print header
    print_header("Welcome to the Online Book Store", "Member Menu                            ***\n***                         ")
    
    while (True):
        # print options
        print_option(options_member)

        #check the user choice
        choice_member = check_choice(len(options_member))

        if choice_member == 1:
            browse_by_subject_menu(db)
        elif choice_member == 2: 
            search_by_author_or_title_menu(db)
        elif choice_member == 3: 
            get_invoice(db, user_data)
        elif choice_member == 4: 
            user_data = {}
            main_menu(db)
        else: 
            quit()   

#Menu for browsing books by subject
def browse_by_subject_menu(db):
    options_subjects = list_all_subjects(db)
    # print options
    print_option(options_subjects)
    #check the user choice
    choice_subject = check_choice(len(options_subjects))
    if choice_subject is not None:
        books_displayed_menu(db, 0, options_subjects[choice_subject - 1])
    else: 
        browse_by_subject_menu(db)

#Displaying books and presents options for next step
def books_displayed_menu(db, ofst, subject):
    options_back_and_next = ['Enter ISBN to put in the cart', 'Press ENTER to return to the main menu', 'Press n ENTER to continue browsing']

    # get 2 books
    books = search_by_subjects(db, subject, 2, ofst)

    # Check if there is more books
    ofst = ofst + 2
    next_page_exsist = search_by_subjects(db, subject, 2, ofst)
    if next_page_exsist == []:
        options_back_and_next.pop()

    # print books
    for book in books:
        print_book(book)
 
    #print options
    print_option(options_back_and_next)

    #check the user choice
    selectedOption = None
    books_isbn = [book[0] for book in books]

    while (selectedOption is None):
        choice = input("Type in your option: ")
        print()
        try:
            if choice == 'q':
                quit()

            elif choice == 'n' and next_page_exsist != []:
                books_displayed_menu(db, ofst, subject)
            
            elif choice == '':
                member_menu(db) 

            elif choice in books_isbn:
                selectedOption = choice
                add_to_cart(db, user_data, choice)
    
            else:
                print("Invalid input: please select the available options.")
        except Exception:
            selectedOption = None
            print("Invalid input. Try again!")    

#Menu for searching books by title or author
def search_by_author_or_title_menu(db):
    # print options
    print_option(options_author_or_title)
    #check the user choice
    choice_author_or_title = check_choice(len(options_author_or_title))

    if choice_author_or_title == 1:
        search_by_author_menu(db)
    elif choice_author_or_title == 2: 
        search_by_title_menu(db)
    elif choice_author_or_title == 3: 
        member_menu(db)
    else: 
        quit()  

#Searching books by author
def search_by_author_menu(db):
    options_back_and_next = ['Enter ISBN to put in the cart', 'Press ENTER to return to the main menu', 'Press n ENTER to continue browsing']
    author = input("Enter author name or part of the name: ")
    books = search_by_author_sub(db, author)
    print(f"{len(books)} books found \n")
    #Check if there are books
    if len(books)==0: 
        #Remove enter adding to cart option if there are no book found
        options_back_and_next.pop(0)
    print_books_and_choos_next_action(db, books, options_back_and_next)

#Searching books by title
def search_by_title_menu(db):
    options_back_and_next = ['Enter ISBN to put in the cart', 'Press ENTER to return to the main menu', 'Press n ENTER to continue browsing']
    title = input("Enter title name or part of the name: ")
    books = search_by_title_sub(db, title)
    print(f"{len(books)} books found\n")
     #Check if there are books
    if len(books)==0: 
        #Remove enter adding to cart option if there are no book found
        options_back_and_next.pop(0)
    print_books_and_choos_next_action(db, books, options_back_and_next)
    
#Prit all books and shows nex actions for search menues
def print_books_and_choos_next_action(db, books, options_back_and_next):
    books_to_print = books[:3]
    del books[:3]
    
    next_page_exsist = True
    #Check if there is more books
    if len(books) <= 0: 
        options_back_and_next.pop()
        next_page_exsist = False
    
    for book in books_to_print:
        print_book(book)
  
    print_option(options_back_and_next)

    #check the user choice
    selectedOption = None
    books_isbn = [book[0] for book in books_to_print]

    while (selectedOption is None):
        choice = input("Type in your option: ")
        print()
        try:
            if choice == 'q':
                quit()

            elif choice == 'n' and next_page_exsist == True:
                print_books_and_choos_next_action(db, books, options_back_and_next)
            
            elif choice == '':
                member_menu(db)
                
            elif choice in books_isbn:
                selectedOption = choice
                add_to_cart(db, user_data, choice)

            else:
                print("Invalid input: please select the available options.")
        except Exception:
            selectedOption = None
            print("Invalid input. Try again!")  