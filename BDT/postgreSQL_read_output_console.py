#
# Script to read data from a postgreSQL table and print it on the console.
# Written by Matias Bendel.
#

import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                  password="XXX",
                                  host="XXX",
                                  port="5432",
                                  database="postgres")
    
    cursor = connection.cursor()
        
    cursor.execute("SELECT * FROM clientes_datos_personales LIMIT 0")
    table_col_names = [desc[0] for desc in cursor.description]
    
    postgreSQL_select_Query = "SELECT * FROM clientes_datos_personales"
    cursor.execute(postgreSQL_select_Query)
    table_records = cursor.fetchall()

    print("")
    for i in table_col_names:
        print(i, end=" ")
    print("")

    for row in table_records:
        for j in row:
            print(j, end=" ")
        print("")
        
    
except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")