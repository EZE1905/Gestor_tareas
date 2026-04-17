from flask import Flask,redirect,render_template,url_for,request,flash
from mgestor_tareas import leer_tareas,agregar_tarea,eliminar_tarea

app = Flask(__name__)
app.secret_key = 'super_secret_key' # Necesario para sesiones

tareas = leer_tareas()

@app.route("/")
def home():
    return render_template("layout.html", tareas = tareas)

@app.route("/agregar_tareas", methods = ["POST"])
def agregar():
    tarea = {
        "tarea":request.form["tarea"],
        "fecha":request.form["fecha"]
    }
    agregar_tarea(tareas,tarea)
    flash('Tarea agregado','success') # Mensaje flash
    return redirect("/") 

@app.route("/eliminar", methods = ["POST"])
def eliminar():
    indice = int(request.form["indice"])
    eliminar_tarea(tareas,indice)
    flash('Tarea eliminado','error') # Mensaje flash
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)