from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, origins="*") 

@app.route("/api/users", methods=['GET'])
def users():
    return jsonify({
        "users" : [
            "Sam",
            "Gabby",
            "Jess",
            "James",
            "https://www.youtube.com/watch?v=1qe-4j8H4Me&t=117s",
            "https://www.youtube.com/watch?v=ct1MqpQoM68"
        ],
        "links": [
            "https://www.youtube.com/watch?v=1qe-4j8H4Me&t=117s",
            "https://www.youtube.com/watch?v=ct1MqpQoM68"
        ]
    })

if __name__ == "__main__":
    app.run(debug=True, port=8080)