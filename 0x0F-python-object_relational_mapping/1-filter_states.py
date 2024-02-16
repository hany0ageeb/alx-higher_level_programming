#!/usr/bin/python3
"""
script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
1. Your script should take 3 arguments:
    mysql username, mysql password and database name
2. You must use the module MySQLdb
3. Your script should connect to a MySQL server
    running on localhost at port 3306
4. Results must be sorted in ascending order by states.id
5. Results must be displayed as they are in the example below
6. Your code should not be executed when imported
Output Example:
    (4, 'New York')
    (5, 'Nevada')
"""
import MySQLdb
import sys


def main():
    """
    script Entry Point
    """
    conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3])
    cur = conn.cursor()
    cur.execute("""
            SELECT states.id, states.name
            FROM states
            WHERE states.name LIKE BINARY %s
            ORDER BY states.id""", ('%N%',))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == '__main__':
    main()
