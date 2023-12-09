from abc import abstractmethod
from dataclasses import fields
from models.friend import RequiredData


class QueryBuilder():
    def __init__(self, input_data: RequiredData):
        self.data = input_data

    @abstractmethod
    def build_query(self):
        pass

    @abstractmethod
    def interpret_list(self):
        pass

class AddFriendQuery(QueryBuilder):
    def __init__(self, input_data: RequiredData):
        super().__init__(input_data)
        self.interpret_list()
    
    def interpret_list(self):
        temp = ""
        for i in fields(self.data):
            if i.name == 'interests':
                interest_values = getattr(self.data, i.name)
                temp = ('@@@'.join(interest_values))
                setattr(self.data, i.name, temp)
                break

    def build_query(self):
        columns = []
        values = []
        sql_columns = ""
        sql_values = ""
        #all of this needs to be handled for sql injection
        for i in fields(self.data):
            #check if null
            value_of_column = getattr(self.data, i.name)
            if value_of_column == None:
                continue
            columns.append(i.name)
            values.append(value_of_column)
        
        sql_columns = (', '.join(columns))
        sql_values = (', '.join(values))
        query_string = f"INSERT INTO FRIENDS ({sql_columns}) VALUES ({sql_values});" #this is insecure rn
        return query_string