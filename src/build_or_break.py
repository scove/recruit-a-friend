from query_reader import QueryReader

#TODO: I want this to be in maybe a configuration file, or determined at runtime for now this is good
FRIENDS_TABLE_QUERY_PATH = 'queries/set_up/create_friends_table.sql' 
POSITIONS_TABLE_QUERY_PATH = 'queries/set_up/create_open_positions.sql'
DESTROY_FRIENDS_TABLE_PATH = 'queries/break_down/destroy_friends_table.sql'
DESTROY_POSITIONS_TABLE_PATH = 'queries/break_down/destroy_open_positions.sql'

def set_up(query_runner):
    friends = QueryReader(FRIENDS_TABLE_QUERY_PATH)
    positions = QueryReader(POSITIONS_TABLE_QUERY_PATH)
    query_runner.run_query(friends.content)
    query_runner.run_query(positions.content)

def break_down(query_runner):
    friends = QueryReader(DESTROY_FRIENDS_TABLE_PATH)
    positions = QueryReader(DESTROY_POSITIONS_TABLE_PATH)
    query_runner.run_query(friends.content)
    query_runner.run_query(positions.content)