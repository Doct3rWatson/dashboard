# app.py - Flask app entry point
from flask import Flask, render_template, request, redirect, jsonify
from calendar_utils import get_combined_calendar_events
import json
from datetime import datetime
import os

app = Flask(__name__)

# Utilities
def read_json(file):
    if os.path.exists(file):
        with open(file, "r") as f:
            return json.load(f)
    return {}

def write_json(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=2)

@app.route("/")
def index():
    events = get_combined_calendar_events()
    meals = read_json("meals.json")
    todos = read_json("todos.json")
    grocery = read_json("grocery.json")
    return render_template("index.html", events=events, meals=meals, todos=todos, grocery=grocery)

@app.route("/update_meals", methods=["POST"])
def update_meals():
    data = request.json
    write_json("meals.json", data)
    return jsonify({"status": "success"})

@app.route("/add_todo", methods=["POST"])
def add_todo():
    todos = read_json("todos.json")
    new_task = request.json.get("task")
    if new_task:
        todos.append({"task": new_task, "done": False})
        write_json("todos.json", todos)
    return jsonify(todos)

@app.route("/toggle_todo", methods=["POST"])
def toggle_todo():
    todos = read_json("todos.json")
    idx = int(request.json.get("index"))
    if 0 <= idx < len(todos):
        todos[idx]["done"] = not todos[idx]["done"]
        write_json("todos.json", todos)
    return jsonify(todos)

@app.route("/delete_todo", methods=["POST"])
def delete_todo():
    todos = read_json("todos.json")
    idx = int(request.json.get("index"))
    if 0 <= idx < len(todos):
        todos.pop(idx)
        write_json("todos.json", todos)
    return jsonify(todos)


@app.route("/add_grocery", methods=["POST"])
def add_grocery():
    grocery = read_json("grocery.json")
    new_task = request.json.get("task")
    if new_task:
        grocery.append({"task": new_task, "done": False})
        write_json("grocery.json", grocery)
    return jsonify(grocery)

@app.route("/toggle_grocery", methods=["POST"])
def toggle_grocery():
    grocery = read_json("grocery.json")
    idx = int(request.json.get("index"))
    if 0 <= idx < len(grocery):
        grocery[idx]["done"] = not grocery[idx]["done"]
        write_json("grocery.json", grocery)
    return jsonify(grocery)

@app.route("/delete_grocery", methods=["POST"])
def delete_grocery():
    grocery = read_json("grocery.json")
    idx = int(request.json.get("index"))
    if 0 <= idx < len(grocery):
        grocery.pop(idx)
        write_json("grocery.json", grocery)
    return jsonify(grocery)

@app.route("/refresh_data")
def refresh_data():
    events = get_combined_calendar_events()
    meals = read_json("meals.json")
    todos = read_json("todos.json")
    grocery = read_json("grocery.json")

    return jsonify({
        "events": events,
        "meals": meals,
        "todos": todos,
        "grocery": grocery
    })


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
