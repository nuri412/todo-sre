from flask import Flask, request, jsonify

app = Flask(__name__)

# in-memory bd
todos = []

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    todo = {
        'id': len(todos) + 1,
        'task': data.get('task', '')
    }
    todos.append(todo)
    return jsonify(todo), 201

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t['id'] != todo_id]
    return jsonify({'message': 'Deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
