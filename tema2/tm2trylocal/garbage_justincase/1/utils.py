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

def convertTemperaturesToJSON(temperatures):
    json_list = []
    
    for t in temperatures:
        aux = {'id': t[0], 'valoare': t[1], 'timestamp': t[2].strftime('%Y-%m-%d')}
        #aux = {'id': t[0], 'valoare': t[1], 'timestamp': t[2].date()}
        json_list.append(aux)
    
    print(json_list)
    #return json.dumps(json_list, default=str)
    return jsonify(json_list)

# Delete all temperatures of a city if its in delCityList
def deleteTempByCities(temperatures, delCityList):
    del_temp = []
    for temp in temperatures:
        for city in delCityList:
            # Compare citiy ids
            if temp[3] == city[0]:
                del_temp.append(temp)
    
    remained_temp = [t for t in temperatures if t not in del_temp]
    return remained_temp
                

# def closeDBconnection(connection, cursor):
#     if (connection):
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection is closed")