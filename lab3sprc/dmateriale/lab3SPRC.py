from flask import Flask, request, Response
from flask.json import jsonify
import json

app = Flask(__name__)

@app.route("/movies", methods=["GET"])
def getMovies():
    global movies
    return jsonify(movies), 200

@app.route("/movie/<int:gotId>", methods=["GET"])
def getSpecificMovie(gotId):
    global movies, movieName
    movieName = ""
    for i in range(0, len(movies)):
        if movies[i]["id"] == gotId:
            movieName = movies[i]
    if movieName:
        return jsonify(movieName), 200

    return jsonify({'status' : 'Not found'}), 404

@app.route("/movie/<int:gotId>", methods=["PUT"])
def modifyMovie(gotId):
    global getMovies
    sentJson = request.json
    hasBeenFound = 0
    if sentJson and sentJson["nume"]:
        for i in range(0, len(movies)):
            if movies[i]["id"] == gotId:
                movies[i]["nume"] = sentJson["nume"]
                hasBeenFound = 1
    else:
        return jsonify({'status' : 'Bad Request'}), 400
    if hasBeenFound == 0:
        return jsonify({'status' : 'Not found'}), 404
    return jsonify({'status' : 'OK'}), 200

@app.route("/movies", methods=["POST"])
def postMovie():
    sentJson = request.json
    global id, movies

    if sentJson and "nume" in sentJson and sentJson["nume"] != "":
        newEntry = {
            "id": id,
            "nume": sentJson["nume"]
        }
        movies.append(newEntry)
        id = id + 1
        return jsonify({'status' : 'CREATED'}), 201
    
    return jsonify({'status' : 'Bad Request'}), 400

@app.route("/reset", methods=["DELETE"])
def resetAll():
    global id, movies
    id = 1
    movies = []
    return jsonify({'status' : 'OK'}), 200

@app.route("/movie/<int:gotId>", methods=["DELETE"])
def delMovie(gotId):
    global id, movies
    foundIndex = -1
    for i in range(0, len(movies)):
        if movies[i]["id"] == gotId:
            foundIndex = i
    if foundIndex == -1:
        return jsonify({'status' : 'Not found'}), 404
    else:
        movies.pop(foundIndex)
        return jsonify({'status' : 'OK'}), 200

if __name__ == '__main__':
    global id
    global movies
    id = 1
    movies = []
    app.run('0.0.0.0', port=7020, debug=True)
