from database import Database

def list_all_subjects(db:Database):
    query = f""" SELECT DISTINCT subject FROM books; """
    subjects = db.execute_with_fetchall(query)
    unique_subjects = [subject[0] for subject in subjects]
    
    return unique_subjects

def search_by_subjects(db:Database, subject, limit, offset):
    query = f""" SELECT * FROM books WHERE subject="{subject}" LIMIT {limit} OFFSET {offset}; """
    books = db.execute_with_fetchall(query)

    return books

def search_by_author_sub(db:Database, author):
    query = f""" SELECT * FROM books WHERE author LIKE '%{author}%'; """
    books = db.execute_with_fetchall(query)

    return books