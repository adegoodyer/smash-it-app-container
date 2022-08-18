from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# load envars from .env
load_dotenv()

app = Flask(__name__)

# configure sqlite DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# database model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    creation_date = db.Column(db.String(20))
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


@app.route("/")
def home():
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))


def date():
    return datetime.today().strftime("%m-%d-%Y")

if __name__ == "__main__":
    # create db
    db.create_all()

    # create example todo if none exist
    if Todo.query.first() == None:
        todo = Todo(
            creation_date=date(),
            title="Get up and go for a run this morning",
            complete=False,
        )
        db.session.add(todo)
        todo = Todo(
            creation_date=date(),
            title="Brainstorm the next disrupting app",
            complete=True,
        )
        db.session.add(todo)
        todo = Todo(
            creation_date=date(),
            title="Meditate and maintain your balance",
            complete=False,
        )
        db.session.add(todo)
        db.session.commit()

    # run app
    app.run(debug=True)
