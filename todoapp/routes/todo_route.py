from flask import request, Blueprint, render_template, session, redirect, url_for, flash

from todoapp.database import get_db
from todoapp.todo_repo import read_todo, create_todo, read_todo_by_id, update_todo_by_id

bp = Blueprint("todo", __name__, url_prefix="/todo")


@bp.route("/formulario", methods=("GET", "POST"))
def formulario():
    if request.method == "POST":
        db = get_db()
        title = request.form["todo_title"]
        description = request.form["todo_desc"]

        error = None

        if not title:
            error = "El titulo es requerido."
        if not description:
            error = "La descripción es requerida."

        flash(error)
        if error:
            return render_template("todo/formulario.html")

        user_id = session.get("user_id")
        create_todo(db, title, description, user_id)
        return redirect(url_for("todo.visualizacion"))

    return render_template("todo/formulario.html")


@bp.route("/visualizacion")
def visualizacion():
    db = get_db()
    user_id = session.get("user_id")
    todos = read_todo(db, user_id)

    return render_template("todo/visualizacion.html", todos=todos)


@bp.route("/detalle/<int:todo_id>", methods=("GET", "POST"))
def detalle(todo_id):
    db = get_db()
    user_id = session.get("user_id")

    if request.method == "GET":
        todo = read_todo_by_id(db, todo_id, user_id)
        return render_template("todo/detalle.html", todo=todo)
    elif request.method == "POST":
        state = request.form["state"]
        state = False if state == 'True' else True
        print(type(state))
        print(state)
        update_todo_by_id(db, todo_id, user_id, state)
        return redirect(url_for("todo.visualizacion"))