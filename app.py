from flask import Flask, render_template, request, redirect
import json 

app = Flask(__name__)

notes = []

# the home page and render it
@app.route('/')
def index ():
    load_notes()
    return render_template('index.html', notes=notes)

# function for adding a note and pick a color for it then append it
@app.route('/add_note', methods=['POST'])
def add_note():
    note_text = request.form['note_text']
    note_color = request.form['note_color']
    notes.append({'text': note_text, 'color': note_color})
    save_notes()
    return redirect('/')


# function for delete the note that clicked on 
@app.route('/delete_note/<int:note_id>', methods=['GET', 'POST'])
def delete_note(note_id):
    if request.method == 'POST':
        del notes[note_id]
        save_notes()
    return index()

# function for clearing the json file
@app.route('/clear_all')
def clear_all():
    with open('notes.json', 'w') as file:
        json.dump([], file, indent=4)
    return redirect('/')

# rout for searching and it make a loop if the note is lower case or apper reverse it then render the templat
@app.route("/search")
def search():
    query = request.args.get('search')
    filtered_notes = []
    for note in notes:
        if note['text'].lower().find(query.lower()) != -1:
            filtered_notes.append(note)
    return render_template("index.html", notes = filtered_notes)



# loading the notes inside a json file 
def load_notes():
    global notes
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
            notes = []

# saving the notes
def save_notes():
    with open('notes.json', 'w')as file:
        json.dump(notes, file, indent=4)
