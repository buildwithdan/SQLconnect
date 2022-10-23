import psycopg2

try:
    connection = psycopg2.connect(user="dnellpersonal",
                                  password="v2_3uywZ_D7WHHVhxkSCDwhHLvFj9CZ9",
                                  host="db.bit.io",
                                  port="5432",
                                  database="dnellpersonal/test1")
    cursor = connection.cursor()

    postgres_insert_query = """ INSERT INTO mobile VALUES (%s,%s,%s)"""
    record_to_insert = (5, 'One Plus 6', 950)
    cursor.execute(postgres_insert_query, record_to_insert)

    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into mobile table")

except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into mobile table", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")