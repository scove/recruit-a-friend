from sqlite3 import Error

class QueryRunner():

    def __init__(self, connection):
        self.connection = connection
    
    def run_query(self, query: str):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"The error '{e}' occurred")
