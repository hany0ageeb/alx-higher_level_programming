#!/usr/bin/python3
"""
script that lists all State objects, and corresponding City
objects, contained in the database hbtn_0e_101_usa
1. Your script should take 3 arguments:
    mysql username, mysql password and database name
2. You must use the module SQLAlchemy
3. The connection to your MySQL server must be to localhost on port 3306
4. You must only use one query to the database
5. You must use the cities relationship for all State objects
6. Results must be sorted in ascending order by states.id and cities.id
7. Results must be displayed as they are in the example below
8. Your code should not be executed when imported
<state id>: <state name>
<tabulation><city id>: <city name>
1: California
    1: San Francisco
    2: San Jose
    3: Los Angeles
    4: Fremont
    5: Livermore
2: Arizona
    6: Page
    7: Phoenix
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import Session, contains_eager, joinedload
from relationship_state import State
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
    engine = create_engine(conn_url, echo=True)
    with Session(engine) as session:
        states = session.query(State).outerjoin(
                City).options(
                        joinedload(
                            State.cities, innerjoin=False)).order_by(
                                    State.id, City.id).all()
        for state in states:
            print("{}: {}".format(state.id, state.name))
            for city in state.cities:
                print("    {}: {}".format(city.id, city.name))


if __name__ == '__main__':
    main()
