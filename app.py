from flask import Flask, jsonify, request

app = Flask(__name__)
todos = []

@app.route('/api/todos', methods=['GET'])
def list_todos():
    return jsonify({"todos": todos})

@app.route('/api/todos', methods=['POST'])
def create_todo():
    data = request.json
    todo = {"id": len(todos) + 1, "title": data["title"], "done": False}
    todos.append(todo)
    return jsonify(todo), 201

@app.route('/api/todos/<int:todo_id>', methods=['PATCH'])
def update_todo(todo_id):
    for t in todos:
        if t["id"] == todo_id:
            t["done"] = request.json.get("done", t["done"])
            return jsonify(t)
    return jsonify({"error": "not found"}), 404

if __name__ == '__main__':
    app.run(port=5000)
