#!/usr/bin/python3
"""
script that lists all State objects that contain
    the letter a from the database hbtn_0e_6_usa
1. Your script should take 3 arguments:
    mysql username, mysql password and database name
2. You must use the module SQLAlchemy
3. You must import State and Base from model_state
4. Your script should connect to a MySQL
    server running on localhost at port 3306
5. Results must be sorted in ascending order by states.id
6. The results must be displayed as they are in the example below
7. Your code should not be executed when imported
"""


def main():
    """Entry point"""
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.engine import URL
    from sqlalchemy.orm import Session
    from model_state import State, Base
    conn_url = URL.create(
            'mysql+mysqldb',
            host='localhost',
            port=3306,
            username=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3])
    engine = create_engine(conn_url, echo=False)
    with Session(engine) as session:
        states = session.query(
                State).filter(
                        State.name.like('%a%')).order_by(
                                State.id)
        for state in states:
            print('{}: {}'.format(state.id, state.name))


if __name__ == '__main__':
    main()
