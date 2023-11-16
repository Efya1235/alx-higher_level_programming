#!/usr/bin/python3
"""
This script displays all values in the states table of
hbtn_0e_0_usa where the name matches the provided argument.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database_name> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    db_connection = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database_name,
        port=3306
    )

    db_cursor = db_connection.cursor()

    # Define the SQL query with string formatting
    sql_query = "SELECT * FROM states WHERE name = %s ORDER BY states.id"

    db_cursor.execute(sql_query, (state_name,))

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)

    db_cursor.close()
    db_connection.close()
