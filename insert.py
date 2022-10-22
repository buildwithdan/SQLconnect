#https://www.geeksforgeeks.org/executing-sql-query-with-psycopg2-in-python/


import psycopg2
  
conn = psycopg2.connect(
    database="suppliers", user='r00t', 
  password='thebuckstopshere!!', host='192.168.1.206', port='5432'
)
  
conn.autocommit = True
cursor = conn.cursor()
  
sql = '''CREATE TABLE employees(emp_id int,emp_name varchar, \
salary decimal); '''
  
cursor.execute(sql)
  
conn.commit()
conn.close()