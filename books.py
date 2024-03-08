from database import Database

#Gets all subjects from database
def list_all_subjects(db:Database):
    query = f""" SELECT DISTINCT subject FROM books; """
    subjects = db.execute_with_fetchall(query)
    unique_subjects = [subject[0] for subject in subjects]
    
    return unique_subjects

#Gets books with one subject from database
def search_by_subjects(db:Database, subject, limit, offset):
    query = f""" SELECT * FROM books WHERE subject="{subject}" LIMIT {limit} OFFSET {offset}; """
    books = db.execute_with_fetchall(query)

    return books

#Gets books with one author from database
def search_by_author_sub(db:Database, author):
    query = f""" SELECT * FROM books WHERE author LIKE '%{author}%'; """
    books = db.execute_with_fetchall(query)

    return books

#Gets books with one title from database
def search_by_title_sub(db:Database, title):
    query = f""" SELECT * FROM books WHERE title LIKE '%{title}%'; """
    books = db.execute_with_fetchall(query)

    return books