#!/usr/bin/python3
"""
script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
1. Your script should take 3 arguments:
    mysql username, mysql password and database name
2. You must use the module SQLAlchemy
3. You must import State and Base from model_state
4. Your script should connect to a MySQL server
    running on localhost at port 3306
5. Print the new states.id after creation
6. Your code should not be executed when imported
"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import Session


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
    with Session(engine) as session:
        state = State(name='Louisiana')
        session.add(state)
        session.commit()
        print(state.id)


if __name__ == '__main__':
    main()
