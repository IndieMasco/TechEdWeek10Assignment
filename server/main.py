from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, origins="*") 

@app.route("/")
def index():
    return "Homepage"

@app.route("/users", methods=['GET'])
def users():
    return jsonify({
        "users" : [
            "Sam",
            "Gabby",
            "Jess",
            "James"
        ],
        "links": [
            "https://www.youtube.com/watch?v=6i3e-j3wSf0",
            "https://www.youtube.com/watch?v=AgVqsmz-ZW4",
            "https://www.youtube.com/watch?v=D2cwvpJSBX4",
            "https://www.youtube.com/watch?v=ctQMqqEo4G8"
        ]
    })

if __name__ == "__main__":
    app.run(debug=True, port=8080)