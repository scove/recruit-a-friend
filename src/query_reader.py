class QueryReader():
    def __init__(self, query_file_path: str):
        self.location = query_file_path
        self.name = self.extract_query_name()
        self.content = self.read_query()
        self.query_type = self.extract_query_type()
    
    def read_query(self):
        with open(self.location, 'r', encoding='utf-8') as sql_file:
            return sql_file.read()
    
    def extract_query_name(self):
        return self.location.split('/')[-1]
    
    def extract_query_type(self):
        return self.location.split('/')[-2]