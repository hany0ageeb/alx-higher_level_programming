#!/usr/bin/python3
"""
script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
1. Your script should take 4 arguments:
mysql username, mysql password, database name
and state name to search (SQL injection free)
2. You must use the module SQLAlchemy
3. You must import State and Base from model_state
4. Your script should connect to a MySQL
    server running on localhost at port 3306
5. You can assume you have one record with the state name to search
6. Results must display the states.id
7. If no state has the name you searched for, display Not found
8. Your code should not be executed when imported
"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import Session


def find_state_by_name(engine, state_name):
    """find sates by name
    Args:
        engine: engine
        state_name(str): state name
    Return:
        [State]: a list of found states
    """
    with Session(engine) as session:
        states = session.query(State).filter(State.name == state_name).all()
        return states


def print_states(states):
    """
    print list of states according to spec
    Args:
        states: a list of states
    """
    if states:
        for state in states:
            print(state.id)
    else:
        print('Not found')


def main():
    """Entry point"""
    conn_url = URL.create(
            'mysql+mysqldb',
            host='localhost',
            port=3306,
            username=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3])
    engine = create_engine(conn_url, echo=False)
    states = find_state_by_name(engine, sys.argv[4])
    print_states(states)


if __name__ == '__main__':
    main()
