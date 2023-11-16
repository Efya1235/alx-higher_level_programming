#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
"""


import MySQLdb
import sys

if __name__ == '__main__':
    """
    Connects to the MySQL database and retrieves a list of states.

    Usage: python script_name.py <username> <password> <database_name>
    """

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    db_connection = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database_name,
        port=3306
    )

    db_cursor = db_connection.cursor()

    db_cursor.execute("SELECT * FROM states ORDER BY states.id")

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)

    db_cursor.close()
    db_connection.close()
