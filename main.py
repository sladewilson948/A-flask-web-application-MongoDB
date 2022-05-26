from flask import Flask, render_template, jsonify, request
import pymongo



#connecting to the database localy
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["test-database"]
collection = db["user-details-for-analysis"]


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method=="POST":
        name = request.form["Name"]
        age = request.form["Age"]
        country = request.form["Country"]
        dict1 = {
            "name": name,
            "age": age,
            "country": country,
        }
        #inserting data to the database
        try:
            inseted_id = collection.insert_one(dict1).inserted_id
            return jsonify({"name": name, "age": age, "country": country, "status": f"data added to the database with id {inseted_id}"})
        except Exception:
            return jsonify({"name": name, "age": age, "country": country})
    return render_template("index.html")


if __name__ == '__main__':
    app.run()