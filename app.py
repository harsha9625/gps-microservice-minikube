from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def get_location():

    response = requests.get("https://ipinfo.io/json")
    data = response.json()

    result = {
        "city": data.get("city"),
        "region": data.get("region"),
        "country": data.get("country"),
        "location": data.get("loc")
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
