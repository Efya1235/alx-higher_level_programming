#!/usr/bin/python3
"""A script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument."""
import sys
import MySQLdb


def main():
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )

    cursor = conn.cursor()
    search = sys.argv[4]
    query = """SELECT * FROM states WHERE name = '{:s}' ORDER BY id ASC""".format(search)
    cursor.execute(query)
    states = cursor.fetchall()
    for h in states:
        if h[1] == search:
            print(h)
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
