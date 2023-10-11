from flask import Flask, render_template, request, redirect
import json 

app = Flask(__name__)

notes = []

@app.route('/')
def index ():
    load_notes()
    return render_template('index.html', notes=notes)

@app.route('/add_note', methods=['POST'])
def add_note():
    note_text = request.form['note_text']
    note_color = request.form['note_color']
    notes.append({'text': note_text, 'color': note_color})
    save_notes()
    return redirect('/')

@app.route('/delete_note/<int:note_id>', methods=['GET', 'POST'])
def delete_note(note_id):
    if request.method == 'POST':
        del notes[note_id]
        save_notes()
    return index()


@app.route('/clear_all')
def clear_all():
    with open('notes.json', 'w')as file:
        json.dump([], file, indent=4)
    return redirect('/')


@app.route("/search")
def search():
    query = request.args.get('search')
    filtered_notes = []
    for note in notes:
        if note['text'].lower().find(query.lower()) != -1:
            filtered_notes.append(note)
    return render_template("index.html", notes = filtered_notes)


def load_notes():
    global notes
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
            notes = []


def save_notes():
    with open('notes.json', 'w')as file:
        json.dump(notes, file, indent=4)
