from flask import Flask, jsonify, Response, request
import psycopg2
from http import HTTPStatus

def establishDBconnection():
    try:
        global connection
        connection = psycopg2.connect(user="postgres",
                                    password="postgres",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="meteoDB")

        # Create a cursor to perform database operations
        global cursor
        cursor = connection.cursor()
        # Print PostgreSQL details
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        # Executing a SQL query
        cursor.execute("SELECT version();")
        # Fetch result
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    return connection

def execute(query):
    try:
        cursor.execute(insert_query)
        connection.commit()
    except:
        return Response(status=HTTPStatus.CONFLICT)

# def closeDBconnection(connection, cursor):
#     if (connection):
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection is closed")