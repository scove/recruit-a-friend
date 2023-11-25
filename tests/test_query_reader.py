from unittest import TestCase, mock
from query_reader import QueryReader

class QueryReaderTester(TestCase):

    def test_should_create_object(self):
        with mock.patch("builtins.open", mock.mock_open(read_data="data")) as mock_file:
            assert isinstance(QueryReader("test/test.sql"), QueryReader)
    
    def test_should_have_expected_attributes(self):
        expected_attributes_and_values = {
            "location" : "queries/test_queries/select_everything.sql",
            "name" : "select_everything.sql",
            "content" : "SELECT * FROM friends;",
            "query_type" : "test_queries"
        }
        with mock.patch("builtins.open", mock.mock_open(read_data="SELECT * FROM friends;")) as mock_file:
            new_reader = QueryReader("queries/test_queries/select_everything.sql")
            assert new_reader.__dict__ == expected_attributes_and_values
    
    @mock.patch('builtins.open')
    def test_should_read_query_file(self, mock_read):
        mock_query_reader = mock.Mock(location="queries/test_queries/select_this.sql")
        QueryReader.read_query(mock_query_reader)
        assert mock_read.call_args == mock.call(
            mock_query_reader.location,
            'r',
            encoding='utf-8'
        )

    def test_should_extract_query_name(self):
        mock_query_reader = mock.Mock(location="queries/test_queries/select_this.sql")
        assert QueryReader.extract_query_name(mock_query_reader) == "select_this.sql"
    
    def test_should_extract_query_type(self):
        mock_query_reader = mock.Mock(location="queries/test_queries/select_this.sql")
        assert QueryReader.extract_query_type(mock_query_reader) == "test_queries"

