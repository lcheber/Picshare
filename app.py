from flask import Flask, g, render_template, request, send_from_directory
import sqlite3
import os
from werkzeug.utils import redirect
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
DATABASE = 'app.db'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.route("/")
def index():
    db = get_db()
    pictures = db.execute("SELECT path FROM pictures")
    return render_template("index.html", all_pictures=pictures)
    # todo_items = ["item1", "item2", "item3"]
    # return render_template("index.html", subtitle="Here are all my lists", list_items=todo_items)

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

@app.route("/", methods=["POST"])
def create ():
    if 'file' not in request.files:
        return redirect("/")
    file = request.files['file']
    if file.filename != '':
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        db = get_db()
        db.execute("INSERT INTO pictures (path) VALUES (?)", [filename])
        db.commit()
    return redirect("/")

if __name__ == '__name__':
    app.run(debug=True)