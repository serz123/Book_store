from database import Database

#check the member cridentials
def check_cridentilas(db:Database, email, password):
    query = f""" SELECT * FROM members WHERE email="{email}" AND password="{password}" ; """
    user = db.execute_with_fetchone(query)
    return user is not None