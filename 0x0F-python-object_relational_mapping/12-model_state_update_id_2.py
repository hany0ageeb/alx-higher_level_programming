#!/usr/bin/python3
"""
script that changes the name of a State object from the database hbtn_0e_6_usa
1. Your script should take 3 arguments:
    mysql username, mysql password and database name
2. You must use the module SQLAlchemy
3. You must import State and Base from model_state
4. Your script should connect to a
    MySQL server running on localhost at port 3306
5. Change the name of the State where id = 2 to New Mexico
6. Your code should not be executed when imported
"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine, update
from sqlalchemy.engine import URL


def update_state(engine, state_id, state_name):
    """
    update state name
    """
    stmt = update(State).where(State.id == state_id).values(name=state_name)
    with engine.connect() as conn:
        result = conn.execute(stmt)


def main():
    """
    Entry point
    """
    conn_url = URL.create(
            'mysql+mysqldb',
            host='localhost',
            port=3306,
            username=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3])
    engine = create_engine(conn_url)
    update_state(engine, 2, 'New Mexico')


if __name__ == '__main__':
    main()
