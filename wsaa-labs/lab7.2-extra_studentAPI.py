from flask import Flask, request, jsonify
from studentDAO import studentDAO  # Import StudentDAO

app = Flask(__name__)

# ✅ 1️⃣ GET all students
@app.route("/students", methods=["GET"])
def get_students():
    students = studentDAO.getAll()
    return jsonify(students), 200  # HTTP 200 OK

# ✅ 2️⃣ GET student by ID
@app.route("/students/<int:id>", methods=["GET"])
def get_student_by_id(id):
    student = studentDAO.findByID(id)
    if student:
        return jsonify(student), 200
    return jsonify({"error": "Student not found"}), 404  # HTTP 404 Not Found

# ✅ 3️⃣ POST (Create a new student)
@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()
    if "firstname" not in data or "age" not in data:
        return jsonify({"error": "Missing 'firstname' or 'age' fields"}), 400  # HTTP 400 Bad Request

    new_id = studentDAO.create((data["firstname"], data["age"]))
    return jsonify({"message": "Student created", "id": new_id}), 201  # HTTP 201 Created

# ✅ 4️⃣ PUT (Update student by ID)
@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    data = request.get_json()
    if "firstname" not in data or "age" not in data:
        return jsonify({"error": "Missing 'firstname' or 'age' fields"}), 400

    updated = studentDAO.update((data["firstname"], data["age"], id))
    if updated:
        return jsonify({"message": "Student updated"}), 200
    return jsonify({"error": "Student not found"}), 404

# ✅ 5️⃣ DELETE (Delete student by ID)
@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    deleted = studentDAO.delete(id)
    if deleted:
        return jsonify({"message": "Student deleted"}), 200
    return jsonify({"error": "Student not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)  # Starts the Flask server
