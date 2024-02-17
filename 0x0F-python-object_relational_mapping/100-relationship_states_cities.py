#!/usr/bin/python3
"""
script that creates the State “California” with
the City “San Francisco” from the database hbtn_0e_100_usa
1. Your script should take 3 arguments:
    mysql username, mysql password and database name
2. You must use the module SQLAlchemy
3. Your script should connect to a MySQL
    server running on localhost at port 3306
4. You must use the cities relationship for all State objects
5. Your code should not be executed when imported
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import Session
from relationship_state import State, Base
from relationship_city import City


def main():
    """
    Entry Point
    """
    conn_url = URL.create(
            'mysql+mysqldb',
            host='localhost',
            port=3306,
            username=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3])
    engine = create_engine(conn_url, echo=False)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        state = State(name='California', cities=[City(name='San Francisco')])
        session.add(state)
        session.commit()


if __name__ == '__main__':
    main()
