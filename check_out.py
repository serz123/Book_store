from cart import get_invoice_info_from_cart
from order import save_new_order

def get_invoice(db, user):

    info = get_invoice_info_from_cart(db, user)
    if len(info) == 0:
        print("The cart is empty!")
        print()
        #Go back to menu
        return
    print("Current Cart Contents:")
    print()
    print_cart_details(info)
    proceed_to_check_out(db, user, info)

def print_cart_details(info):
    total_price = 0
    print("ISBN         Title                             $   Qty  Total")
    print("-" * 61)
    for book in info:
        print(f"{str(book[0]).ljust(13)}{book[1].ljust(31)}{str(book[2]).ljust(7)}{str(book[3]).ljust(4)}{str(book[2]*book[3]).ljust(6)}")
        total_price += book[2] * book[3]
    print("-" * 61)
    print(f"Total                                                  ${str(total_price).ljust(6)}")
    print("-" * 61)

def proceed_to_check_out(db, user, info):
    selectedOption = None
    while (selectedOption is None):
        choice = input("Proced to check out (Y/N)?: ")
        print()
        if choice == 'q':
            quit()
        elif choice.upper() == 'N':
            return
        elif choice.upper() == "Y":
            order_nmr = save_new_order(db, user, info)
            if order_nmr == 0:
                print("Something went wrong. Please try again later!")
            print(f"          Invoice for Order no.{order_nmr}\n")
            print("Shipping Adress:")
            print(f"Name:    {user[0]} {user[1]}")
            print(f"Address: {user[2]}\n         {user[2]}\n         {user[3]}")
            print_cart_details(info)
            input("Press Enter to go back to Menu")
            return
        else:
            print("Invalid input: please select the available options.")
