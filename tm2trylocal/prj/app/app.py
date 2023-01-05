from utils import *

app = Flask(__name__)

connection = establishDBconnection()
cursor = connection.cursor()

# Country methods
@app.route("/api/countries", methods=["POST"])
def countriesPost():
    # Get and verify query
    payload = request.get_json(silent=True)
    print("payload ", payload)
    if not ('nume' in payload and 'lat' in payload and 'lon' in payload):
        return Response(status=HTTPStatus.BAD_REQUEST)
    
    # Construct and execute query
    insert = "INSERT INTO tari (nume_tara, latitudine, longitudine) "
    values = "VALUES ('" + str(payload['nume']) + "', " + str(payload['lat']) + ", " + str(payload['lon']) + ")"
    insertQuery = insert + values

    try:
        cursor.execute(insertQuery)
        connection.commit()
    except psycopg2.errors.UniqueViolation:
        connection.rollback()
        return Response(status=HTTPStatus.CONFLICT)

    print("1 Record inserted successfully")
    # Fetch result
    cursor.execute("SELECT * from tari")
    print("Result ", cursor.fetchall())

    # Get last insert id
    cursor.execute("SELECT currval(pg_get_serial_sequence('tari','id'));") 
    connection.commit()
    last_id = cursor.fetchone()[0]

    return jsonify({'id':last_id}), 201

@app.route("/api/countries", methods=["GET"])
def countriesGet():
    cursor.execute("SELECT * from tari")
    countries_list = cursor.fetchall()

    json_list = []
    for c in countries_list:
        aux = {'id': c[0], 'nume': c[1], 'lat': c[2], 'lon': c[3]}
        json_list.append(aux)
    
    return jsonify(json_list), 200

@app.route("/api/countries/<int:gotId>", methods=["PUT"])
def countriesPutId(gotId):
    # Get and verify query
    payload = request.get_json(silent=True)
    print("payload ", payload)
    if not ('id' in payload and 'nume' in payload and 'lat' in payload and 'lon' in payload):
        return Response(status=HTTPStatus.BAD_REQUEST)

    if gotId != payload['id']:
        return Response(status=HTTPStatus.BAD_REQUEST)

    # Get countries list and search elem by id
    cursor.execute("SELECT * from tari")
    countries_list = cursor.fetchall()

    toModify = searchInList(gotId, countries_list)
    
    if toModify == None:
        return Response(status=HTTPStatus.NOT_FOUND)

    # Construct and execute query
    n = str(payload['nume'])
    la = str(payload['lat'])
    lo = str(payload['lon'])
    updateQuery = "UPDATE tari SET nume_tara = '" + n + "', latitudine = " + la  
    updateQuery += ", longitudine = " + lo + " WHERE id = " + str(gotId)
    
    cursor.execute(updateQuery)
    connection.commit()
    
    return Response(status=HTTPStatus.OK)

@app.route("/api/countries/<int:gotId>", methods=["DELETE"])
def countriesDeleteId(gotId):
    # Get countries list and search elem by id
    cursor.execute("SELECT * from tari")
    countries_list = cursor.fetchall()

    toDelete = searchInList(gotId, countries_list)
    
    if toDelete == None:
        return Response(status=HTTPStatus.NOT_FOUND)

    # Construct and execute query
    deleteQuery = "DELETE FROM tari WHERE id = " + str(gotId)

    cursor.execute(updateQuery)
    connection.commit()

    return Response(status=HTTPStatus.OK)

# City methods
@app.route("/api/cities", methods=["POST"])
def citiesPost():
    # Get and verify query
    payload = request.get_json(silent=True)
    print("payload ", payload)
    if not ('idTara' in payload and 'nume' in payload and 'lat' in payload and 'lon' in payload):
        return Response(status=HTTPStatus.BAD_REQUEST)    

    # Construct and execute query
    insertQuery = "INSERT INTO orase (id_tara, nume_oras, latitudine, longitudine) "
    insertQuery += "VALUES (" + str(payload['idTara']) + ", '" + str(payload['nume']) + "', "
    insertQuery += str(payload['lat']) + ", " + str(payload['lon']) + ")"

    print(insertQuery)

    # Conflict when unique(id_tara, nume_oras) is broken
    try:
        cursor.execute(insertQuery)
        connection.commit()
    except psycopg2.errors.UniqueViolation:
        connection.rollback()
        return Response(status=HTTPStatus.CONFLICT)
    except psycopg2.errors.ForeignKeyViolation:
        connection.rollback()
        return Response(status=HTTPStatus.CONFLICT)

    print("1 Record inserted successfully")
    # Fetch result
    cursor.execute("SELECT * from orase")
    print("Result ", cursor.fetchall())

     # Get last insert id
    cursor.execute("SELECT currval(pg_get_serial_sequence('orase','id'));") 
    connection.commit()
    last_id = cursor.fetchone()[0]

    return jsonify({'id':last_id}), 201

@app.route("/api/cities", methods=["GET"])
def citiesGet():
    cursor.execute("SELECT * from orase")
    cities_list = cursor.fetchall()

    return convertCitiesToJSON(cities_list), 200

@app.route("/api/cities/country/<int:gotId>", methods=["GET"])
def citiesGetById(gotId):
    # Get cities list by country id
    select_query = "SELECT * from orase WHERE id_tara = " + str(gotId)
    cursor.execute(select_query)
    cities_list = cursor.fetchall()
    
    return convertCitiesToJSON(cities_list), 200
    
# Temperatures methods
@app.route("/api/temperatures", methods=["POST"])
def temperaturesPost():
    # Get and verify query
    payload = request.get_json(silent=True)
    print("payload ", payload)
    if not ('idOras' in payload and 'valoare' in payload):
        return Response(status=HTTPStatus.BAD_REQUEST)

    # Construct and execute query
    insertQuery = "INSERT INTO temperaturi (valoare, timestamp, id_oras) VALUES (%s, %s, %s)"
    now = datetime.datetime.now()
    itemTuple = (str(payload['valoare']), now, str(payload['idOras']))

    # Conflict if unicity broken or temperature type is not double 
    try:
        cursor.execute(insertQuery, itemTuple)
        connection.commit()
    except psycopg2.errors.UniqueViolation:
        connection.rollback()
        return Response(status=HTTPStatus.CONFLICT)
    except psycopg2.errors.ForeignKeyViolation:
        connection.rollback()
        return Response(status=HTTPStatus.CONFLICT)
    except psycopg2.errors.InvalidTextRepresentation:
        connection.rollback()
        return Response(status=HTTPStatus.CONFLICT)

    # Get last insert id
    cursor.execute("SELECT currval(pg_get_serial_sequence('orase','id'));") 
    connection.commit()
    last_id = cursor.fetchone()[0]

    return jsonify({'id':last_id}), 201








if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)