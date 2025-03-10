from flask import Flask, jsonify
from flask_cors import CORS
from database import image_collection

app = Flask(__name__)
CORS(app)

@app.route("/images", methods=["GET"])
def get_images():
    """Returnează lista imaginilor salvate"""
    images = list(image_collection.find({}, {"_id": 0}))
    return jsonify(images)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
