#!/usr/bin/env python3
"""
This script lists all states with names starting with 'N' (uppercase)
from the MySQL database `hbtn_0e_0_usa`.

Usage:
    ./script_name.py <mysql_username> <mysql_password> <database_name>

Requirements:
    - MySQL server must be running on localhost at port 3306.
    - The module MySQLdb must be installed (`pip install mysqlclient`).

Functionality:
    - Connects to the specified MySQL database using the provided credentials.
    - Retrieves all entries from the `states` table whose name starts with 'N'.
    - Sorts the results by `id` in ascending order.
    - Prints each row to stdout.

Note:
    - The script will not execute when imported as a module.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Get credentials and DB name from command-line arguments
    user_name = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user_name,
        passwd=pwd,  # 'passwd' is the correct argument for MySQLdb
        db=db_name
    )

    # Create cursor and execute query
    mycursor = db.cursor()
    mycursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    )

    # Fetch and print results
    rows = mycursor.fetchall()
    for row in rows:
        print(row)

    # Close connection
    mycursor.close()
    db.close()
