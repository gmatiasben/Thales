#
# Script to read data from csv file, create a postgreSQL table and write the information into it.
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
        
    cursor.execute("""CREATE TABLE clientes_datos_personales_python(
        ID text,
        RUT text,
        genero text,
        nacimiento text,
        apellido text,
        nombre text,
        direccion text,
        comuna text,
        region text,
        codigo_area text,
        telefono text,
        email text
        )
    """)
        
    with open('C:\\temp\\_data_files\\clientes_datos_personales.csv', 'r') as f:
     
        # Skip the header row.
        next(f)
        cursor.copy_from(f, 'clientes_datos_personales_python', sep=',')

    connection.commit()

    print("Data copy from .csv file to PostgreSQL status: ok")
    
except (Exception, psycopg2.Error) as error:
    print("Error while copying data to PostgreSQL", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")