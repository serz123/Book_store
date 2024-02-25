def print_header(title):
    print("***********************************************************")
    print("***                                                     ***")
    print("***          " + title + "           ***")
    print("***                                                     ***")
    print("***********************************************************") 

def print_option(options):
    for i in range(len(options)):
        print(f"{i+1}. {options[i]}") 

def  check_choice(maxOptions):
    selectedOption = None
    while (selectedOption is None):
        choice = input("Enter choice:")
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