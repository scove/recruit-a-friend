from sql_connect import create_connection
from query_runner import QueryRunner
from build_or_break import set_up, break_down
from query_reader import QueryReader

DATABASE_PATH = "/home/sam/Desktop/Projects/recruit-a-friend/raf.sqlite" #TODO: make this configurable

def main():
    c = create_connection(DATABASE_PATH)
    query_runner = QueryRunner(c)
    set_up(query_runner)
    #break_down(query_runner)
    #SetterUpper(query_runner)
    #query_runner.run_query('select 1')
    #run_query(c, "SELECT 1")
    
    #run_query(c, read_query.content)

main()