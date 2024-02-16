#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
1. Your script should take 4 arguments:
    mysql username, mysql password, database name and state name
2. You must use the module MySQLdb
3. Your script should connect to a MySQL server
 running on localhost at port 3306
4. Results must be sorted in ascending order by cities.id
5. You can use only execute() once
6. Your code should not be executed when imported
"""


def getCitiesByStateName(conn, state_name):
    """
    Returns a list of cities names that belong to state name
    Args:
        conn: connection
        state_name: state name
    Returns:
        list: list of cities names
    """
    cur = conn.cursor()
    cur.execute("""SELECT cities.name
    FROM cities INNER JOIN states
    ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id""", (state_name,))
    cities = []
    rows = cur.fetchmany(100)
    while rows:
        for row in rows:
            cities.append(row[0])
        rows = cur.fetchmany(100)
    cur.close()
    return cities


def main():
    """
    ENTRY POINT
    """
    import sys
    import MySQLdb
    PARAMETERS = {
            'user': sys.argv[1],
            'password': sys.argv[2],
            'database': sys.argv[3],
            'host': 'localhost',
            'port': 3306
    }
    STATE_NAME = sys.argv[4]
    conn = MySQLdb.connect(**PARAMETERS)
    cities = getCitiesByStateName(conn, STATE_NAME)
    print(', '.join(cities))
    conn.close()


if __name__ == '__main__':
    main()
