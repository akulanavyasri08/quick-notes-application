from flask import Flask, render_template, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Create database table
def init_db():
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

init_db()

# Home page
@app.route('/')
def home():
  return render_template('index.html')

# Add note API
@app.route('/add_note', methods=['POST'])
def add_note():
    data = request.get_json()
    note = data['note']

    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO notes (content) VALUES (?)", (note,))
    conn.commit()

    conn.close()

    return jsonify({"message": "Note added successfully"})

# Get notes API
@app.route('/get_notes')
def get_notes():
    conn = sqlite3.connect('notes.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM notes ORDER BY id DESC")
    notes = cursor.fetchall()

    conn.close()

    notes_list = []

    for note in notes:
        notes_list.append({
            "id": note[0],
            "content": note[1]
        })

    return jsonify(notes_list)

if __name__ == '__main__':
    app.run(debug=True)