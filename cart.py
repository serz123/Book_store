from database import Database

def add_to_cart(db: Database, user, isbn):  
    userid = user[7]
    try:
        # Check if there is exsisting book in the cart
        check_query = f"""SELECT qty FROM cart WHERE userid='{userid}' AND isbn='{isbn}';"""
        existing_quantity = db.execute_with_fetchone(check_query)
        
        if existing_quantity is not None:
            new_quantity = existing_quantity[0] + get_quantity()
            update_query = f"""UPDATE cart SET qty={new_quantity} WHERE userid='{userid}' AND isbn='{isbn}';"""
            db.execute_with_commit(update_query)
            print("Updating cart was successful!\n")
        else:
            insert_query = f"""INSERT INTO cart VALUES ('{userid}', '{isbn}', '{get_quantity()}');"""
            db.execute_with_commit(insert_query)
            print("Adding book/s to cart was successful!\n")
            
    except Exception as e:
        print("ADDING book/s to cart has FAILED!\n")
        print(e)

def get_quantity():
    desired_quantity = None
    while desired_quantity is None:
        qty = input("Enter qty: ")
        try:
            qty_int = int(qty)
            if 0 < qty_int < 2000:
                desired_quantity = qty_int
            else:
                print("Invalid input: The amount is too big or 0.")
        except Exception:
            print("Invalid input: it should be a number or the amount is too big.")

    return desired_quantity

def get_invoice_info_from_cart(db, user):
    user_id = user[7]
    query = f""" SELECT c.isbn, b.title, b.price, c.qty FROM cart c INNER JOIN books b ON c.isbn = b.isbn WHERE c.userid = {user_id}; """
    invoice_info = db.execute_with_fetchall(query)
    
    return invoice_info
