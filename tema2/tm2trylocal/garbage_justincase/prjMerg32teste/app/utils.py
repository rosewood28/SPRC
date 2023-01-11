from flask import Flask, jsonify, Response, request
import psycopg2
from http import HTTPStatus
import datetime
import json

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

def searchInList(elemId, list):
    for x in list:
        if x[0] == elemId:
            return x
    
    return None

def convertCitiesToJSON(cities_list):
    json_list = []
    for c in cities_list:
        aux = {'id': c[0], 'idTara': c[1], 'nume': c[2], 'lat': c[3], 'lon': c[4]}
        json_list.append(aux)

    return jsonify(json_list)

def convertTempsToJSON(temps):
    json_list = []
    for t in temps:
        aux = {'id': t[0], 'valoare': t[1], 'timestamp': t[2].date().strftime('%y-%m-%d')}
        json_list.append(aux)

    print(json_list)
    return jsonify(json_list)
    #return json.dumps(json_list), 200

# def closeDBconnection(connection, cursor):
#     if (connection):
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection is closed")