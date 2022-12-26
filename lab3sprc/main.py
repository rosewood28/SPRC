from flask import Flask, jsonify, Response, request

app = Flask(__name__)

id = 1
movies = [ 
# {
# "id": 1,
# "nume": "Star Wars 1 - Yoda Version"
# },
# {
# "id": 2,
# "nume": "Star Wars 1 - Another Version"
# }
]

@app.route("/movies", methods=["GET"])
def moviesGet():
	global movies
	return jsonify(movies), 200

@app.route("/movies", methods=["POST"])
def moviesPost():
	payload = request.get_json(silent=True)
	global id, movies
	if not (payload and "nume" in payload and payload["nume"] != ""):
		# Error handling
		return jsonify({'status': 'Bad Request'}), 400

	newMovie = {
		"id": id,
        "nume": payload["nume"]
	}
	movies.append(newMovie)
	id = id + 1

	return jsonify({'status': 'CREATED'}), 201

def searchMovie(id):
	global movies
	for x in movies:
		if x["id"] == id:
			return x

	return None

@app.route("/movie/<int:gotId>", methods=["PUT"])
def putMovieId(gotId):
	payload = request.get_json(silent=True)
	global id, movies
	if not (payload and "nume" in payload and payload["nume"] != ""):
		# Error handling
		return jsonify({'status': 'Bad Request'}), 400

	movie = searchMovie(gotId)
	if movie:
		movie["nume"] = payload["nume"]
		return jsonify({'status': 'UPDATED'}), 200
	
	return jsonify({'status': 'Movie Not Found'}), 404

@app.route("/movie/<int:gotId>", methods=["GET"])
def getMovieId(gotId):
	movie = searchMovie(gotId)
	if movie:
		return movie, 200
	
	return jsonify({'status': 'Movie Not Found'}), 404

@app.route("/movie/<int:gotId>", methods=["DELETE"])
def deleteMovieId(gotId):
	movie = searchMovie(gotId)
	if movie:
		movies.remove(movie)
		return movie, 200
	
	return jsonify({'status': 'Movie Not Found'}), 404

@app.route("/reset", methods=["DELETE"])
def deleteReset():
	global id, movies
	movies = []
	id = 1
	return jsonify({'status' : 'OK'}), 200

if __name__ == '__main__':
	app.run('0.0.0.0', debug=True)
