from database import Database
from datetime import date as today_date

#Saves new order
def save_new_order(db: Database, user, cart_info):
    try: 
        date = today_date.today().strftime('%Y-%m-%d')
        insert_query_order = f""" INSERT INTO orders (userid, created, shipAddress, shipCity, shipZip) VALUES ("{user[7]}", "{date}", "{user[2]}", "{user[3]}", "{user[4]}");"""
        db.execute_without_commit(insert_query_order)

        order_ono = db.get_last_autoincremented_vallue()
        for book in cart_info:
            insert_query_odetails = f""" INSERT INTO odetails VALUES ("{order_ono}", "{book[0]}", "{book[3]}", "{book[2]*book[3]}");"""
            db.execute_without_commit(insert_query_odetails)

        delete_query = f"""DELETE FROM cart WHERE userid="{user[7]}"; """
        db.execute_with_commit(delete_query)
        return order_ono
    except Exception as e:
        print("Order FAILD!")
        print(e) 
        return 0

