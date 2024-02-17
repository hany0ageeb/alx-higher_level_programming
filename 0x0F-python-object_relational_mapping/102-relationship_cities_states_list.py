#!/usr/bin/python3
"""
script that lists all City objects from the database hbtn_0e_101_usa
1. Your script should take 3 arguments:
    mysql username, mysql password and database name
2. You must use the module SQLAlchemy
3. Your script should connect to a MySQL server
running on localhost at port 3306
4. You must use only one query to the database
5. You must use the state relationship to access
to the State object linked to the City object
6. Results must be sorted in ascending order by cities.id
7. Results must be displayed as they are in the example below
    <city id>: <city name> -> <state name>
    1: San Francisco -> California
    2: San Jose -> California
8. Your code should not be executed when imported
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import Session, contains_eager, joinedload
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
    with Session(engine) as session:
        cities = session.query(
                City).options(
                        joinedload(
                            City.state,
                            innerjoin=False)).order_by(City.id).all()
        for city in cities:
            print('{}: {} -> {}'.format(city.id, city.name, city.state.name))


if __name__ == '__main__':
    main()
