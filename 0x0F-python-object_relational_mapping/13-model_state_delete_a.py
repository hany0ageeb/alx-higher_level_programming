#!/usr/bin/python3
"""
script that deletes all State objects with a name
containing the letter a from the database
1. Your script should take 3 arguments:
    mysql username, mysql password and database name
2. You must use the module SQLAlchemy
3. You must import State and Base from model_state
4. Your script should connect to a MySQL server running
    on localhost at port 3306
5. Your code should not be executed when imported
"""
import sys
from sqlalchemy import create_engine, delete
from sqlalchemy.engine import URL
from sqlalchemy.orm import Session
from model_state import State, Base


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
    engine = create_engine(conn_url, echo=False)
    with Session(engine) as session:
        states = session.query(State).filter(State.name.like('%a%')).all()
        for state in states:
            session.delete(state)
        session.commit()


if __name__ == '__main__':
    main()
