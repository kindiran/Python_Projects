import pymssql
from multiprocessing import Pool
from dbutils.pooled_db import PooledDB

# Function to execute SQL queries using a connection from the pool
def execute_query():
    # Acquire a connection from the pool
    with pool.connection() as conn:
        # Create a cursor object to execute SQL queries
        with conn.cursor() as cursor:
            try:
                # Execute the SQL query
                cursor.execute('SELECT * FROM employees.dept')
                rows = cursor.fetchall()
                for row in rows:
                    print(row)

            except pymssql.Error as e:
                print("An error occurred while executing the SQL query:", str(e))
                return None

# Create a connection pool
server = 'localhost'
database = 'tinitiate'
username = 'sa'
password = 'sbroot!23456'

pool = PooledDB(
    creator=pymssql,
    host=server,
    user=username,
    password=password,
    database=database,
    mincached=5,   # Minimum number of idle connections in the pool
    maxcached=10,  # Maximum number of idle connections in the pool
    maxconnections=20  # Maximum number of open connections (including both idle and in-use)
)

print("calling execute query")
execute_query()