from unittest import TestCase
from models.friend import Friend
from query_builder import AddFriendQuery


#mock data
jimmy = Friend("jimmy", "jimmy123@jimmymail.com", "123456", ['baseball', 'whatever'])
jammy = Friend("jammy", "jammy@whatever.com", None, ["soccer"])

class AddFriendQueryTester(TestCase):
    def test_should_create_query(self):
        assert isinstance(AddFriendQuery(jimmy), AddFriendQuery)
        AddFriendQuery(jammy).build_query()
        assert False