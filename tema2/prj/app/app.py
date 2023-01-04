import psycopg2
from flask import Flask, jsonify, Response, request

app = Flask(__name__)

@app.route("/api/countries", methods=["GET"])
def countriesGet():
    return "WOAAAA"
# try:
#     connection = psycopg2.connect(user="postgres",
#                                 password="postgres",
#                                 host="127.0.0.1",
#                                 port="5432",
#                                 database="database_container")

#     # Create a cursor to perform database operations
#     cursor = connection.cursor()
#     # Print PostgreSQL details
#     print("PostgreSQL server information")
#     print(connection.get_dsn_parameters(), "\n")
#     # Executing a SQL query
#     cursor.execute("SELECT version();")
#     # Fetch result
#     record = cursor.fetchone()
#     print("You are connected to - ", record, "\n")

# except (Exception, Error) as error:
#     print("Error while connecting to PostgreSQL", error)
# finally:
#     if (connection):
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection is closed")

if __name__ == '__main__':
	app.run('0.0.0.0', port=5000, debug=True)