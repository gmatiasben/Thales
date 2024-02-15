#
# Script to read data from a postgreSQL table and save it in a csv file.
# Written by Matias Bendel.
#

import psycopg2
import csv
import os

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

    with open('python_input.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(table_col_names)
        # write the data
        for row in table_records:
            writer.writerow(row)    
    f.close()
        
    print("Data copy from PostgreSQL to .csv file status: ok")
    
    cmd = 'C:\\Program\Files\\BDT\\bin\\bdt.bat'
    #-t -c ..\\conf\\bdt.config --central python_csv'
    os.system(cmd)
    
    cmd = ".\\bdt -t -c ..\\conf\\bdt.config --central python_csv"
    os.system(cmd)

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")