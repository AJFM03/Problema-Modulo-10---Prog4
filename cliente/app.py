from flask import Flask, render_template, request, redirect, url_for, flash
import requests
from config import API_BASE_URL

app = Flask(__name__)
app.secret_key = "supersecret"

# Listar libros

@app.route("/")
def index():
    try:
        r = requests.get(f"{API_BASE_URL}/books")
        books = r.json()
    except:
        flash("Error al conectar con la API", "danger")
        books = []
    return render_template("index.html", books=books)

# Agregar libro

@app.route("/add", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        data = {
            "title": request.form["title"],
            "author": request.form["author"],
            "genre": request.form["genre"],
            "status": request.form["status"]
        }
        try:
            r = requests.post(f"{API_BASE_URL}/books", json=data)
            if r.status_code == 201:
                flash("Libro agregado correctamente", "success")
                return redirect(url_for("index"))
            else:
                flash("Error al agregar libro", "danger")
        except:
            flash("No se pudo conectar con la API", "danger")
    return render_template("add_book.html")

# Editar libro

@app.route("/edit/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    if request.method == "POST":
        data = {
            "title": request.form["title"],
            "author": request.form["author"],
            "genre": request.form["genre"],
            "status": request.form["status"]
        }
        try:
            r = requests.put(f"{API_BASE_URL}/books/{book_id}", json=data)
            if r.status_code == 200:
                flash("Libro actualizado correctamente", "success")
                return redirect(url_for("index"))
            else:
                flash("Error al actualizar libro", "danger")
        except:
            flash("No se pudo conectar con la API", "danger")
    else:
        try:
            r = requests.get(f"{API_BASE_URL}/books/{book_id}")
            if r.status_code == 200:
                book = r.json()
                return render_template("edit_book.html", book=book)
        except:
            flash("No se pudo conectar con la API", "danger")
    return redirect(url_for("index"))


# Eliminar libro

@app.route("/delete/<book_id>", methods=["POST"])
def delete_book(book_id):
    try:
        r = requests.delete(f"{API_BASE_URL}/books/{book_id}")
        if r.status_code == 200:
            flash("Libro eliminado correctamente", "success")
        else:
            flash("Error al eliminar libro", "danger")
    except:
        flash("No se pudo conectar con la API", "danger")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, port=8000)
