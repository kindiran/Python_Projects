import pymssql

server = 'localhost'
database = 'tinitiate'
username = 'sa'
password = 'sbroot!23456'
port=1433

try:
    conn = pymssql.connect(server=server, port=port, database=database, user=username, password=password)
except Exception as e:
    print(e)

def db_read(deptid):
    try:
        cursor = conn.cursor()
        query = 'SELECT * FROM employees.dept where deptno = %s'
        data = (deptid)
        cursor.execute(query, data)
   
        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except pymssql.Error as e:
        print(e)
    finally:
        cursor.close()

print("calling db read")
db_read(20)