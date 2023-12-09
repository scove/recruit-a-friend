from unittest import TestCase
from models.friend import Friend
from query_builder import AddFriendQuery


#mock data
jimmy = Friend("jimmy", "jimmy123@jimmymail.com", "1234567", ["baseball", "whatever"]) #do not build twice, will not be fun
jammy = Friend("jammy", "jammy@whatever.com", None, ["soccer", "whatever"])
tammy = Friend("tammy", None, None, ["sales"])

class AddFriendQueryTester(TestCase):
    def test_should_create_query(self):
        assert isinstance(AddFriendQuery(jimmy), AddFriendQuery)
    
    def test_should_interpret_list(self):
        expected_return_value = 'soccer@@@whatever'
        assert AddFriendQuery(jammy).data.interests == expected_return_value
    
    def test_should_build_query(self):
        expected_return_value = "INSERT INTO FRIENDS (name, interests) VALUES (tammy, sales);"
        assert AddFriendQuery(tammy).build_query() == expected_return_value