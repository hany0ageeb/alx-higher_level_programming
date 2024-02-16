#!/usr/bin/python3
"""
script that prints the first State object from the database hbtn_0e_6_usa
1. Your script should take 3 arguments:
    mysql username, mysql password and database name
2. You must use the module SQLAlchemy
3. You must import State and Base from model_state
4. Your script should connect to a MySQL
    server running on localhost at port 3306
5. The state you display must be the first in states.id
6. You are not allowed to fetch all states
    from the database before displaying the result
7. The results must be displayed as they are in the example below
8. if the table states is empty, print Nothing followed by a new line
9. Your code should not be executed when imported
output Exampe:
    1: California
"""


def main():
    """Entry Point"""
    from model_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.engine import URL
    from sqlalchemy.orm import Session
    import sys
    conn_url = URL.create(
            'mysql+mysqldb',
            host='localhost',
            port=3306,
            username=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3])
    engine = create_engine(conn_url)
    with Session(engine) as session:
        result = session.query(State).order_by(State.id).first()
        if result:
            print('{}: {}'.format(result.id, result.name))
        else:
            print('Nothing')


if __name__ == '__main__':
    main()
