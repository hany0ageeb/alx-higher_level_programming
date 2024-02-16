#!/usr/bin/python3
"""
script that prints all City objects from the database
1. Your script should take 3 arguments:
    mysql username, mysql password and database name
2. You must use the module SQLAlchemy
3. You must import State and Base from model_state
4. Your script should connect to a MySQL
    server running on localhost at port 3306
5. Results must be sorted in ascending order by cities.id
6. Results must be display as they are in the
   example below (<state name>: (<city id>) <city name>)
7. Your code should not be executed when imported
"""
import sys
from sqlalchemy import create_engine, select
from sqlalchemy.engine import URL
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from model_state import State, Base
from model_city import City


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
        cities = session.query(
                City).options(
                        joinedload(
                            City.state)).order_by(
                                    City.id).all()
        for city in cities:
            print('{}: ({}) {}'.format(city.state.name, city.id, city.name))


if __name__ == '__main__':
    main()
