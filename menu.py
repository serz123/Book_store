def print_header(title, subtitle):
    print("***********************************************************")
    print("***                                                     ***")
    print("***          " + title + "           ***")
    print("***              " + subtitle + "                            ***")
    print("***********************************************************") 

def print_option(options):
    for i in range(len(options)):
        print(f"{i+1}. {options[i]}") 
    print("q. Quit")
    # Print empty row at the end
    print()

def print_book(book):
    print(f"Author: {book[1]} \nTitle: {book[2]} \nISBN: {book[0]} \nPrice: {book[3]} \nSubject: {book[4]}")
    # Print empty row at the end
    print()

def  check_choice(maxOptions):
    selectedOption = None
    while (selectedOption is None):
        choice = input("Type in your option: ")
        try:
            if choice == 'q':
                quit()
            elif int(choice) in [x for x in range(1,maxOptions+1)]:
                selectedOption = int(choice)
            else:
                print("Invalid input: please select the available options.")
        except Exception:
            selectedOption = None
            print("Invalid input: it should be a number")    
    return  selectedOption  

