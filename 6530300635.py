from flask import Flask, jsonify, request
from flask_basicauth import BasicAuth

uri = "mongodb+srv://Apichaya:Apichaya@students.doopckz.mongodb.net/?retryWrites=true&w=majority"
uri = "mongodb+srv://viewer:viewer@students.doopckz.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)
db = client["students"]
collection = db["std_info"]

app = Flask(__name__)

#app.config['BASIC_AUTH_USERNAME'] = "username"
#app.config['BASIC_AUTH_PASSWORD'] = "password"
app.config['BASIC_AUTH_USERNAME'] = "vieweruser"
app.config['BASIC_AUTH_PASSWORD'] = "viewerpass"
basic_auth = BasicAuth(app)

@app.route("/")
def Greet():
    return "<p>Welcome to Student Management API</p>"

@app.route("/students", methods = ["GET"])
@basic_auth.required
def get_all_students():
    all_students = collection.find()
    return jsonify({"students":[i for i in all_students]})

@app.route("/students/<int:std_id>", methods = ["GET"])
@basic_auth.required
def get_student(std_id):
    all_students = collection.find()
    student = next( (i for i in all_students if i["_id"] == std_id), None)
@@ -33,6 +35,7 @@ def get_student(std_id):
        return jsonify({"error": "Student not found"}), 404

@app.route("/students", methods = ["POST"])
@basic_auth.required
def create_students():
    try:
        data = request.get_json()
@@ -48,6 +51,7 @@ def create_students():
        return jsonify({"error":"Cannot create new student"}), 500

@app.route("/students/<int:std_id>", methods = ["PUT"])
@basic_auth.required
def update_student(std_id):
    all_students = collection.find()
    student = next( (i for i in all_students if i["_id"] == std_id), None)
@@ -59,6 +63,7 @@ def update_student(std_id):
        return jsonify({"error": "Student not found"}), 404

@app.route("/students/<int:std_id>", methods = ["DELETE"])
@basic_auth.required
def delete_student(std_id):
    all_students = collection.find()
    student = next( (i for i in all_students if i["_id"] == std_id), None)
