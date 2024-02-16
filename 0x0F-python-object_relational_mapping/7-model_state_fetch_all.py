#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
1. Your script should take 3 arguments:
    mysql username, mysql password and database name
2. You must use the module SQLAlchemy
3. You must import State and Base from model_state
4. Your script should connect to a MySQL server
    running on localhost at port 3306
5. Results must be sorted in ascending order by states.id
6. The results must be displayed as they are in the example below
        1: California
        2: Arizona
7. Your code should not be executed when imported
"""


def main():
    """Entry Point"""
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.engine import URL
    from sqlalchemy.orm import Session
    import sys
    # How to connect using sqlalchemy
    conn_url = URL.create(
            'mysql+mysqldb',
            username=sys.argv[1],
            password=sys.argv[2],
            host='localhost',
            port=3306,
            database=sys.argv[3])
    engine = create_engine(conn_url)
    conn = engine.connect()
    with Session(engine) as session:
        result = session.query(State).order_by(State.id).all()
        for row in result:
            print("{}: {}".format(row.id, row.name))


if __name__ == '__main__':
    main()
