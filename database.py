from mysql.connector import connect


class Database:
    def __init__(self, host, username, password, database) -> None:
        self.connection = connect(
            host=host, user=username, password=password, database=database
        )

#get cursor
    def __get_cursor__(self):
        return self.connection.cursor()
        
    #execute and fetch all reaults
    def execute_with_fetchall(self,query):
        with self.__get_cursor__() as cursor:
            cursor.execute(query)
            return cursor.fetchall()
    
    # execute and fetch one
    def execute_with_fetchone(self, query):
        with self.__get_cursor__() as cursor:
            cursor.execute(query)
            return cursor.fetchone()
    
    #execute with commit
    def execute_with_commit(self,query):
        with self.__get_cursor__() as cursor:
            cursor.execute(query)
            self.connection.commit()

    #execute without commit
    def execute_without_commit(self,query):
        with self.__get_cursor__() as cursor:
            cursor.execute(query)

    #Gets last autoincremented value
    def get_last_autoincremented_vallue(self):
           with self.__get_cursor__() as cursor:
                cursor.execute("SELECT LAST_INSERT_ID();")
                last_insert_id = cursor.fetchone()[0]
                return last_insert_id