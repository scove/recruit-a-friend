from unittest import TestCase
from models.friend import Friend


#mock data
jimmy = Friend("jimmy", "jimmy123@jimmymail.com", "123456", ['baseball', 'whatever'])
jammy = Friend("jammy", "jammy@whatever.com", None, ["soccer"])

class FriendTester(TestCase):
    def test_should_create_friend_object(self):
        assert isinstance(jimmy, Friend)
    
    def test_should_respect_optional_fields(self):
        assert isinstance(jammy, Friend)
        assert jammy.phone_number == None
    
    def test_should_be_input_agnostic(self):
        tammy_input = {
            "name" : "tammy",
            "email" : None,
            "phone_number" : None,
            "interests" : ["bartender", "waitress"]
        }
        assert isinstance(Friend(**tammy_input), Friend)