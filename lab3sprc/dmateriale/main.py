from flask import Flask, jsonify, Response, request

app = Flask(__name__)

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

# "nume": "Star Wars 1 - Yoda Version"}
# {
# "nume": "Star Wars 1 - Yoda Version"}
# payload = {}
# payload["id"] = 1

# payload["nume"] = "Star Wars 1 - Yoda Version"

# movies.append(payload)

# print(movies)

@app.route("/movies", methods=["GET"])
def moviesGet():
	print(movies)
	return Response(status=200)

# @app.route("/movies", methods=["POST"])
# def moviesPost():
# 	payload = request.get_json(silent=True)
# 	if not (payload and "nume" in payload and payload["nume"] != ""):
# 		# Error handling
# 		return jsonify({'status': 'Bad Request'}), 400

# 	movies[new_id()] = payload
# 	return jsonify({'status': 'CREATED'}), 201

@app.route("/ruta2")
def salut():
	return "Salut, Lume!"

if __name__ == '__main__':
	app.run('0.0.0.0', debug=True)
