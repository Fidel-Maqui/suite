import psycopg2


def copy_table_data(source_db, destination_db, table_name):
    try:
        # Connect to the source and destination databases
        source_conn = psycopg2.connect(
            database=source_db, user='postgres', password='psw', host='localhost', port='5432')
        dest_conn = psycopg2.connect(
            database=destination_db, user='postgres', password='psw', host='localhost', port='5432')

        # Create a new cursor object
        source_cur = source_conn.cursor()
        dest_cur = dest_conn.cursor()

        # Execute the COPY TO command to copy the data to a file
        with open('temp_file', 'w', encoding='utf-8-sig') as f:
            source_cur.copy_to(f, table_name)

        # Execute the COPY FROM command to copy the data from the file to the destination table
        with open('temp_file', 'r', encoding='utf-8-sig') as f:
            dest_cur.copy_from(f, table_name)

        # Commit the transaction
        dest_conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        # Close the cursor and connection
        if source_conn is not None:
            source_cur.close()
            source_conn.close()

        if dest_conn is not None:
            dest_cur.close()
            dest_conn.close()


# Call the function
copy_table_data('suite', 'suite2', 'salva_strabajador')
