from abc import abstractmethod
from dataclasses import fields
from models.friend import RequiredData


class QueryBuilder():
    def __init__(self, input_data: RequiredData):
        self.data = input_data

    @abstractmethod
    def build_query(self):
        pass

class AddFriendQuery(QueryBuilder):
    def __init__(self, input_data: RequiredData):
        super().__init__(input_data)
    
    def build_query(self):
        #"INSERT INTO friends () VALUES ();"
        columns = []
        values = []
        for i in fields(self.data):
            columns.append(i.name)
            if i.name == 'interests':
                processed = '| '.join(getattr(self.data, i.name))
                values.append(processed)
                continue
            values.append(getattr(self.data, i.name))
        columns = ', '.join(columns)
        values = ', '.join(values) #TODO:failing on null
        query_string = f"INSERT INTO FRIENDS ({columns}) VALUES ({values});" #this is insecure rn
        print(query_string)