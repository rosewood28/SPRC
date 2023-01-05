from utils import *

app = Flask(__name__)

connection = establishDBconnection()
cursor = connection.cursor()

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
    insert_query = insert + values

    try:
        cursor.execute(insert_query)
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

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)